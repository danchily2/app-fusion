"""Fixture builders for the App Fusion script tests: tiny React Native, iOS and Android apps, and a workspace."""

import json
import os
import subprocess
import sys
import tempfile
import textwrap

SCRIPTS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, SCRIPTS)


def write(root, rel, text):
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(textwrap.dedent(text).lstrip("\n"))
    return path


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def git_init(root):
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}
    subprocess.run(["git", "init", "-q", "-b", "main", root], check=True, env=env)
    subprocess.run(["git", "-C", root, "add", "-A"], check=True, env=env)
    subprocess.run(["git", "-C", root, "commit", "-qm", "init"], check=True, env=env)


def rn_app(root):
    write(root, "package.json", json.dumps({
        "name": "mgr", "dependencies": {"react-native": "0.80.0", "@react-navigation/native": "7.0.0",
                                         "@react-native-firebase/messaging": "20.0.0", "react-native-keychain": "9.0.0",
                                         "@react-native-firebase/analytics": "20.0.0"},
        "devDependencies": {"jest": "29.0.0", "@testing-library/react-native": "13.0.0"}}))
    write(root, "src/consts/screens.ts", """
        export const SCREEN_APPROVALS = 'ApprovalsScreen';
        export const SCREEN_APPROVAL_DETAIL = 'ApprovalDetailScreen';
        export const FEEDBACK_PATH = 'api/v1/feedback';
    """)
    write(root, "src/configs/navConfig/ApprovalNav.tsx", """
        import React from 'react';
        import ApprovalsScreen from '../../screens/approvals/ApprovalsScreen';
        import { ApprovalDetailScreen } from '../../screens/approvals/ApprovalDetailScreen';
        import { SCREEN_APPROVALS, SCREEN_APPROVAL_DETAIL } from '../../consts/screens';
        export const ApprovalStack = () => (
          <Stack.Navigator>
            <Stack.Screen name={SCREEN_APPROVALS} component={ApprovalsScreen} options={{ title: 'x' }} />
            <Stack.Screen
              name={SCREEN_APPROVAL_DETAIL}
              component={ApprovalDetailScreen}
            />
            {routes.map(route => <Stack.Screen key={route.name} name={route.name} component={route.c} />)}
          </Stack.Navigator>
        );
    """)
    write(root, "src/screens/approvals/ApprovalsScreen.tsx", "export default function ApprovalsScreen() { return null }\n")
    write(root, "src/screens/approvals/ApprovalDetailScreen.tsx", "export function ApprovalDetailScreen() { return null }\n")
    write(root, "src/services/api.ts", """
        import { FEEDBACK_PATH } from '../consts/screens';
        export const api = createApi({ endpoints: builder => ({
          getTasks: builder.query({ query: () => ({ url: `approval/rest/tasks/${id}` }) }),
          approve: builder.mutation({ query: body => ({ url: 'approval/rest/tasks/approve', method: 'POST', body }) }),
          feedback: builder.mutation({ query: body => ({ url: `${base}${FEEDBACK_PATH}`, method: 'POST' }) }),
        }) });
        axios.get('https://api.example.net/api/v1/bootstrap');
        searchParams.get('Status');
        const license = { url: 'https://github.com/axios/axios/blob/HEAD/LICENSE' };
    """)
    write(root, "src/services/apiAutopay.ts", """
        export const list = () => { const method = 'GET'; const url = `${apiBase.getBaseUrl()}autopay/transaction/list?rows=${2000}`; return makeRequest({ method, url }) }
        export const approve = () => {
          const method = 'POST';
          const url = `${apiBase.getBaseUrl()}autopay/transactions/approve`;
          return makeRequest({ method, url })
        }
    """)
    write(root, "src/services/mswHandlers.ts", "http.get('https://mock.example/api/mocked', () => {})\n")
    write(root, "src/utils/eventLogging/events/approvalEvents.ts", """
        export const APPROVAL_EVENTS = {
          APPROVE: 'approval_approve',
          REJECT: 'approval_reject',
          NESTED: { INNER: 'not_top_level' },
        };
    """)
    write(root, "src/utils/storage.ts", """
        import AsyncStorage from '@react-native-async-storage/async-storage';
        const TOKEN_KEY = 'session_token';
        await AsyncStorage.setItem(TOKEN_KEY, 'x');
        await AsyncStorage.getItem('last_seen');
    """)
    write(root, "src/assets/i18n/en.json", json.dumps({"approve": "Approve", "reject": "Reject", "nested": {"title": "Approvals"}}))
    write(root, "src/assets/i18n/da.json", json.dumps({"approve": "Godkend"}))
    write(root, "src/screens/approvals/__tests__/ApprovalsScreen.test.tsx", "it('works', () => {})\n")
    write(root, ".maestro/approve.yaml", "appId: com.x.mgr\n---\n- launchApp\n- tapOn: Approve\n")
    write(root, "ios/Mgr/Info.plist", """
        <?xml version="1.0" encoding="UTF-8"?>
        <plist version="1.0"><dict>
          <key>CFBundleIdentifier</key><string>com.x.mgr</string>
          <key>NSCameraUsageDescription</key><string>scan</string>
          <key>CFBundleURLTypes</key><array><dict><key>CFBundleURLSchemes</key><array><string>mgrapp</string></array></dict></array>
          <key>UIBackgroundModes</key><array><string>remote-notification</string></array>
        </dict></plist>
    """)
    write(root, "ios/Mgr/Mgr.entitlements", """
        <?xml version="1.0" encoding="UTF-8"?>
        <plist version="1.0"><dict>
          <key>aps-environment</key><string>development</string>
          <key>com.apple.developer.associated-domains</key><array><string>applinks:mgr.example.net</string></array>
        </dict></plist>
    """)
    write(root, "android/app/build.gradle", "android { defaultConfig { applicationId \"com.x.mgr\"\n minSdkVersion 24 } }\n")
    write(root, "android/app/src/main/AndroidManifest.xml", """
        <manifest xmlns:android="http://schemas.android.com/apk/res/android" package="com.x.mgr">
          <uses-permission android:name="android.permission.CAMERA" />
          <application>
            <activity android:name=".MainActivity" android:exported="true">
              <intent-filter android:autoVerify="true">
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data android:scheme="https" android:host="mgr.example.net" />
              </intent-filter>
            </activity>
          </application>
        </manifest>
    """)
    return root


def ios_app(root):
    write(root, "Emp.xcodeproj/project.pbxproj", """
        // !$*UTF8*$!
        {
        /* Begin PBXNativeTarget section */
        		0123456789ABCDEF01234567 /* Emp */ = {
        			isa = PBXNativeTarget;
        			name = Emp;
        			productType = "com.apple.product-type.application";
        		};
        		0123456789ABCDEF01234568 /* Share */ = {
        			isa = PBXNativeTarget;
        			name = Share;
        			productType = "com.apple.product-type.app-extension";
        		};
        /* End PBXNativeTarget section */
        				PRODUCT_BUNDLE_IDENTIFIER = com.x.emp;
        				IPHONEOS_DEPLOYMENT_TARGET = 17.0;
        				OAUTH_SCHEME = empauth;
        }
    """)
    write(root, "Emp/Info.plist", """
        <?xml version="1.0" encoding="UTF-8"?>
        <plist version="1.0"><dict>
          <key>CFBundleIdentifier</key><string>$(PRODUCT_BUNDLE_IDENTIFIER)</string>
          <key>NSFaceIDUsageDescription</key><string>unlock</string>
          <key>CFBundleURLTypes</key><array><dict><key>CFBundleURLSchemes</key><array><string>$(OAUTH_SCHEME)</string></array></dict></array>
        </dict></plist>
    """)
    write(root, "Share/Info.plist", """
        <?xml version="1.0" encoding="UTF-8"?>
        <plist version="1.0"><dict>
          <key>NSExtension</key><dict><key>NSExtensionPointIdentifier</key><string>com.apple.share-services</string></dict>
        </dict></plist>
    """)
    write(root, "Emp/Emp.entitlements", """
        <?xml version="1.0" encoding="UTF-8"?>
        <plist version="1.0"><dict>
          <key>com.apple.security.application-groups</key><array><string>group.com.x.emp</string></array>
        </dict></plist>
    """)
    write(root, "Emp/PrivacyInfo.xcprivacy", "<plist><dict/></plist>\n")
    write(root, "Services/API/Sources/API/Constants.swift", """
        public enum APIConstants { public enum URL { public static let v1 = "/employee/api/v1" } }
        let odpUserId = "odpUserId"
    """)
    write(root, "Services/API/Sources/API/APIClientRequest.swift", """
        public protocol APIClientRequest { var resourceName: String { get }; var method: String { get } }
        public extension APIClientRequest {
            var method: String { return HTTPMethod.GET.rawValue }
        }
    """)
    write(root, "Services/Expense/Sources/Expense/GetReceipts.swift", """
        public struct GetReceipts: APIClientRequest {
            let odpUserId: Int
            public var resourceName: String {
                return "\\(APIConstants.URL.v1)/employees/\\(odpUserId)/expense/inbox"
            }
        }
        public struct PostClaim: APIClientRequest {
            public var resourceName: String { "\\(APIConstants.URL.v1)/expense/claims" }
            var method: String {
                return HTTPMethod.POST.rawValue
            }
        }
    """)
    write(root, "Services/Expense/Package.swift", 'let package = Package(\n    name: "Expense",\n    targets: []\n)\n')
    write(root, "Modules/Payslips/Sources/Payslips/PayslipsFeature.swift", """
        import ComposableArchitecture
        @Reducer
        public struct PayslipsFeature { }
        struct PayslipRow: View { var body: some View { Text("x") } }
        final class LegacyViewController: UIViewController { }
        final class MainCoordinator { }
        protocol Coordinator { }
        public enum Event: Equatable { case payslipOpen, exportAll
            case addAbsence(String) }
        func help() { let u = URL(string: "https://www.example.com/help") }
        func save() { UserDefaults.standard.set(true, forKey: "onboarded") }
    """)
    write(root, "Emp/Localizable.xcstrings", json.dumps({"sourceLanguage": "en", "version": "1.0", "strings": {
        "payslip.title": {"localizations": {"en": {"stringUnit": {"state": "translated", "value": "Payslips"}},
                                            "nb-NO": {"stringUnit": {"state": "translated", "value": "Lønnsslipper"}}}},
        "Export all": {}}}))
    write(root, "EmpTests/PayslipsTests.swift", "import Testing\n@Test func x() {}\n")
    return root


def android_app(root):
    write(root, "settings.gradle", "include ':app', ':feature:expense'\n")
    write(root, "app/build.gradle.kts", 'android { defaultConfig { applicationId = "com.x.emp"\n minSdk = 26 } }\ndependencies { implementation("com.squareup.retrofit2:retrofit:2.11.0") }\n')
    write(root, "app/src/main/AndroidManifest.xml", """
        <manifest xmlns:android="http://schemas.android.com/apk/res/android">
          <uses-permission android:name="android.permission.INTERNET" />
          <application>
            <activity android:name=".MainActivity" android:exported="true" />
            <service android:name=".Push" android:exported="false">
              <intent-filter><action android:name="com.google.firebase.MESSAGING_EVENT" /></intent-filter>
            </service>
          </application>
        </manifest>
    """)
    write(root, "feature/expense/src/main/java/com/x/expense/ExpenseService.kt", """
        const val V1 = "employee/api/v1"
        interface ExpenseService {
            @GET("$V1/expense/claims")
            suspend fun claims(): List<Claim>
            @POST("employee/api/v1/expense/claims/{id}/submit")
            suspend fun submit(@Path("id") id: String)
        }
        @Composable fun ExpenseScreen() {}
        class ExpenseFragment : Fragment()
    """)
    write(root, "app/src/main/res/values/strings.xml", '<resources><string name="expense_title">Expenses</string></resources>\n')
    write(root, "app/src/main/res/values-da/strings.xml", '<resources><string name="expense_title">Udgifter</string></resources>\n')
    write(root, "app/src/main/res/values-night/strings.xml", '<resources><string name="expense_title">x</string></resources>\n')
    write(root, "feature/expense/src/test/java/com/x/expense/ExpenseTest.kt", "import org.junit.Test\nclass ExpenseTest { @Test fun a() {} }\n")
    return root


class Workspace:
    """A temp workspace with two linked apps (a React Native manager app and a native iOS employee app)."""

    def __init__(self, git=True):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = os.path.realpath(self.tmp.name)
        self.ws = os.path.join(self.root, "ws")
        os.makedirs(self.ws)
        self.rn = rn_app(os.path.join(self.root, "src-mgr"))
        self.ios = ios_app(os.path.join(self.root, "src-emp"))
        if git:
            git_init(self.rn)
            git_init(self.ios)

    def run(self, script, *args, check=True, env=None, stdin=None):
        argv = [sys.executable, os.path.join(SCRIPTS, script), *args]
        if script not in ("guard.py",):  # --workspace goes before a `--`: what follows it is the test command itself
            at = argv.index("--") if "--" in argv else len(argv)
            argv[at:at] = ["--workspace", self.ws]
        out = subprocess.run(argv, capture_output=True, text=True, cwd=self.ws, env={**os.environ, **(env or {})}, input=stdin)
        if check and out.returncode != 0:
            raise AssertionError(f"{script} {' '.join(args)} failed ({out.returncode}):\n{out.stdout}\n{out.stderr}")
        return out

    def init(self):
        self.run("workspace.py", "init", "p", "--source", f"mgr={self.rn}", "--source", f"emp={self.ios}",
                 "--product", "mgr=Manager", "--product", "emp=Employee")
        return self

    def path(self, *parts):
        return os.path.join(self.ws, *parts)

    def text(self, *parts):
        with open(self.path(*parts), encoding="utf-8") as fh:
            return fh.read()

    def json(self, *parts):
        with open(self.path(*parts), encoding="utf-8") as fh:
            return json.load(fh)

    def put_json(self, rel, data):
        path = self.path(rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(data, fh)
        return path

    def close(self):
        self.tmp.cleanup()
