#!/usr/bin/env bash
# Shared fixture: two tiny source apps (React Native "mgr", native iOS "emp") as git repositories in ./src-*.
set -euo pipefail
mk() { mkdir -p "$(dirname "$1")"; cat > "$1"; }
mk src-mgr/package.json <<'J'
{"name":"mgr","dependencies":{"react-native":"0.80.0","@react-navigation/native":"7.0.0"}}
J
mk src-mgr/src/consts/screens.ts <<'J'
export const SCREEN_APPROVALS = 'ApprovalsScreen';
J
mk src-mgr/src/nav/Nav.tsx <<'J'
import ApprovalsScreen from '../screens/ApprovalsScreen';
import { SCREEN_APPROVALS } from '../consts/screens';
export const Nav = () => <Stack.Navigator><Stack.Screen name={SCREEN_APPROVALS} component={ApprovalsScreen} /></Stack.Navigator>;
J
mk src-mgr/src/screens/ApprovalsScreen.tsx <<'J'
export default function ApprovalsScreen() { return null }
J
mk src-mgr/README.md <<'J'
Teh manager app.
J
mk src-emp/Emp.xcodeproj/project.pbxproj <<'J'
// !$*UTF8*$!
{
		0123456789ABCDEF01234567 /* Emp */ = {
			isa = PBXNativeTarget;
			name = Emp;
			productType = "com.apple.product-type.application";
		};
}
J
mk src-emp/Emp/Payslips.swift <<'J'
struct GetPayslips: APIClientRequest { var resourceName: String { "/employee/api/v1/payslips" } }
J
for d in src-mgr src-emp; do
  git -C "$d" init -q -b main
  git -C "$d" -c user.name=t -c user.email=t@t add -A
  git -C "$d" -c user.name=t -c user.email=t@t commit -qm init
done
