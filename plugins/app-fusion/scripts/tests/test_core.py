import json
import os
import tempfile
import unittest

import helpers  # noqa: F401  (puts scripts/ on sys.path)
from fusionlib import android, ios, rn
from fusionlib import strings as strcat
from fusionlib.common import endpoints_match, looks_like_path, mask, normalize_endpoint, sanitize_url
from fusionlib.detect import detect


class Endpoints(unittest.TestCase):
    def test_normalize(self):
        cases = {
            "https://api.x.net/api/v1/items?x=1": "/api/v1/items",
            "\\(APIConstants.URL.v1)/employees/\\(id)/inbox": "/employees/{}/inbox",
            "users/${a.b(c)}/settings": "/users/{}/settings",
            "compello/tenants/${t}/invoices/${i}/lines${buildQuery({ a: b(c) })}": "/compello/tenants/{}/invoices/{}/lines",
            "/items/:id/": "/items/{}",
            "/Items/{itemId}": "/items/{}",
            "${baseUrl}${PATH}": None,
            "": None,
        }
        for raw, want in cases.items():
            self.assertEqual(normalize_endpoint(raw), want, raw)

    def test_match(self):
        self.assertTrue(endpoints_match("/employee/api/v1/feedback", "/api/v1/feedback"))
        self.assertTrue(endpoints_match("/users/{}/settings", "/api/users/{}/settings"))
        self.assertTrue(endpoints_match("/items", "/items"))
        self.assertFalse(endpoints_match("/financials/{}/{}", "/employee/api/v1/employees/{}/calendar/checkin"))
        self.assertFalse(endpoints_match("/v1/items", "/v2/items"))
        self.assertFalse(endpoints_match("/a/b", "/c/b"))
        self.assertFalse(endpoints_match("/{}/{}", "/x/{}"))

    def test_path_shape(self):
        for yes in ("hrm/anniversary", "/api/v1/x", "https://x.net/api/y"):
            self.assertTrue(looks_like_path(yes), yes)
        for no in ("application/json", "dd/MM/yyyy", "icons/logo.png", "./local/file", "Status", "^\\d+/\\d+$"):
            self.assertFalse(looks_like_path(no), no)

    def test_secrets(self):
        self.assertEqual(mask("AKIA1234567"), "AKI****")
        self.assertEqual(sanitize_url("https://user:pw@github.com/org/r.git"), "https://github.com/org/r.git")
        self.assertIn("token=****", sanitize_url("https://x.net/a?token=abc&b=1"))


class Strings(unittest.TestCase):
    def test_i18n_json_and_locales(self):
        with tempfile.TemporaryDirectory() as root:
            helpers.write(root, "src/i18n/en.json", json.dumps({"a": "A", "n": {"b": "B"}}))
            helpers.write(root, "src/i18n/nb-NO.json", json.dumps({"a": "Å"}))
            cat = strcat.find_i18n_json(root, include=["src"])
            self.assertEqual(sorted(cat["keys"]), ["a", "n.b"])
            self.assertEqual(cat["source"], "en")
            self.assertEqual(cat["values"]["n.b"], "B")
            self.assertEqual(strcat.summary(cat)["missingPerLocale"]["nb-NO"], 1)
        self.assertEqual(strcat.base_locale("no"), strcat.base_locale("nb-NO"))

    def test_android_ignores_non_locale_qualifiers(self):
        with tempfile.TemporaryDirectory() as root:
            android_root = helpers.android_app(root)
            files = [f"app/src/main/res/{d}/strings.xml" for d in ("values", "values-da", "values-night")]
            cat = strcat.parse_android_strings(android_root, files)
            self.assertEqual(sorted(cat["locales"]), ["da", "default"])


class Extractors(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = self.tmp.name

    def tearDown(self):
        self.tmp.cleanup()

    def test_react_native(self):
        root = helpers.rn_app(os.path.join(self.root, "rn"))
        self.assertEqual(detect(root)["stack"], "react-native")
        inv = rn.extract(root)
        c = inv["counts"]
        self.assertEqual(c["routes"], 2, "constants only; route.name is a dynamic site")
        self.assertEqual(c["dynamicRouteSites"], 1)
        self.assertEqual(c["screens"], 2)
        self.assertEqual({r["value"] for r in inv["routes"]}, {"ApprovalsScreen", "ApprovalDetailScreen"})
        paths = {(e["method"], e["path"]) for e in inv["endpoints"]}
        self.assertIn(("GET", "/approval/rest/tasks/{}"), paths)
        self.assertIn(("POST", "/approval/rest/tasks/approve"), paths)
        self.assertIn(("POST", "/api/v1/feedback"), paths, "the ${PATH} constant is resolved")
        self.assertIn(("GET", "/api/v1/bootstrap"), paths)
        self.assertFalse(any("mocked" in p for _, p in paths), "msw mock handlers are not the app")
        self.assertFalse(any("license" in p for _, p in paths))
        self.assertEqual(c["events"], 2, "top-level catalog members only")
        self.assertEqual(c["stringKeys"], 3)
        self.assertEqual({(s["kind"], s["key"]) for s in inv["storage"] if s["kind"] == "asyncstorage"},
                         {("asyncstorage", "session_token"), ("asyncstorage", "last_seen")})
        self.assertEqual(c["maestroFlows"], 1)
        p = inv["platform"]
        self.assertTrue(p["push"])
        self.assertIn("mgrapp", p["urlSchemes"])
        self.assertIn("applinks:mgr.example.net", p["associatedDomains"])
        self.assertIn("mgr.example.net", p["appLinkHosts"])
        self.assertEqual(p["minOS"].get("android"), 24)

    def test_native_ios(self):
        root = helpers.ios_app(os.path.join(self.root, "ios"))
        self.assertEqual(detect(root)["stack"], "ios-native")
        inv = ios.extract(root)
        c = inv["counts"]
        eps = {(e["method"], e["path"]) for e in inv["endpoints"]}
        self.assertIn(("GET", "/employee/api/v1/employees/{}/expense/inbox"), eps,
                      "qualified constant resolved, bare \\(odpUserId) stays a parameter, protocol default GET")
        self.assertIn(("POST", "/employee/api/v1/expense/claims"), eps)
        self.assertEqual(c["tcaFeatures"], 1)
        self.assertEqual(c["uikitControllers"], 1)
        self.assertEqual(c["coordinators"], 2, "includes the unprefixed base protocol")
        self.assertEqual({e["name"] for e in inv["events"] if e["family"] == "Event"}, {"payslipOpen", "exportAll", "addAbsence"})
        self.assertEqual(inv["webLinks"][0]["url"], "https://www.example.com/help")
        self.assertIn(("userdefaults", "onboarded"), {(s["kind"], s["key"]) for s in inv["storage"]})
        self.assertEqual(c["stringKeys"], 2)
        self.assertIn("nb-NO", inv["strings"]["locales"])
        p = inv["platform"]
        self.assertEqual(p["minOS"], {"ios": "17.0"})
        self.assertIn("empauth", p["urlSchemes"], "$(OAUTH_SCHEME) expanded from build settings")
        self.assertEqual([x["type"] for x in p["extensions"]], ["share"])
        self.assertIn("group.com.x.emp", p["appGroups"])
        self.assertEqual({t["kind"] for t in p["targets"]}, {"app", "extension"})
        self.assertEqual(len(p["privacyManifest"]), 1)

    def test_native_android(self):
        root = helpers.android_app(os.path.join(self.root, "and"))
        self.assertEqual(detect(root)["stack"], "android-native")
        inv = android.extract(root)
        eps = {(e["method"], e["path"]) for e in inv["endpoints"]}
        self.assertIn(("GET", "/employee/api/v1/expense/claims"), eps, "const val template resolved")
        self.assertIn(("POST", "/employee/api/v1/expense/claims/{}/submit"), eps)
        self.assertEqual({s["kind"] for s in inv["screens"]}, {"composable", "fragment"})
        self.assertTrue(inv["platform"]["push"])
        self.assertEqual(inv["platform"]["bundleIds"], ["com.x.emp"])
        self.assertEqual(inv["counts"]["packages"], 2)
        self.assertEqual(inv["tests"]["unitTestFiles"], 1)


if __name__ == "__main__":
    unittest.main()
