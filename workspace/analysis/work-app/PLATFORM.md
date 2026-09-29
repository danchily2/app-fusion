# Platform matrix: work-app

What each app relies on from the operating system and its SDKs, from the inventories and the map. `New app` is the default recommendation: **required** means the new app must keep it for existing users (links, push, locales, privacy), and **decide** means a person chooses in `fuse-review`.

| Id | Area | Item | vmm | me-ios | me-android | New app | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PLT-001 | identity | Bundle / application ids | com.visma.vmm, com.visma.vmm.VmmNotificationContent, com.visma.vmm.VmmNotificationService, com.visma.vmm.develop | com.visma.Employee, com.visma.Employee.expense-share-extension, com.visma.vme.payslip, com.visma.vme.payslip.expense-share-extension | com.visma.vme.payslip | decide | drop |
| PLT-002 | identity | Minimum OS | ios 15.1, android 24 | ios 18.0 |  | decide | keep |
| PLT-003 | push | Push notifications | yes | yes | yes | required | - |
| PLT-079 | push | Notification categories and channels | channel:high-priority, category:ANNIVERSARY_CATEGORY, category:DIALOGUE_CATEGORY, category:APPROVAL_INFO_CATEGORY, category:APPROVAL_ACTIONS_APPROVE_REJECT_CATEGORY, category:APPROVAL_ACTIONS_APPROVE_ONLY_CATEGORY, category:APPROVAL_ACTIONS_REJECT_ONLY_CATEGORY, channel:fcm_fallback_notification_channel |  | channel:PAYSLIP_CHANNEL_2, channel:YEAR_END_CHANNEL_2, channel:RECEIPTS_SYNC_CHANNEL_2, channel:OTHER_NOTIFICATIONS_CHANNEL_2 | required | - |
| PLT-004 | links | Universal / app links | applinks:visma-manager.web.app, webcredentials:visma-manager.web.app, visma-manager.web.app | applinks:static.mobileemployee.visma.net, webcredentials:static.mobileemployee.visma.net, applinks:static.mobileemployee.stag.visma.net, webcredentials:static.mobileemployee.stag.visma.net |  | required | - |
| PLT-005 | links | Custom URL schemes | vismamanager | vismame, vismamedev | vismame | required | - |
| PLT-006 | extensions | App extension: notification-content | ios/VmmNotificationContent/Info.plist |  |  | decide | keep |
| PLT-007 | extensions | App extension: notification-service | ios/VmmNotificationService/Info.plist |  |  | decide | keep |
| PLT-008 | extensions | App extension: share |  | ExpenseShareExtension/Info.plist |  | decide | keep |
| PLT-009 | background | Background modes | fetch, processing, remote-notification |  |  | decide | - |
| PLT-010 | permissions | Permission: NSCalendarsFullAccessUsageDescription | yes |  |  | decide | - |
| PLT-011 | permissions | Permission: NSCalendarsUsageDescription | yes |  |  | decide | - |
| PLT-012 | permissions | Permission: NSCameraUsageDescription |  | yes |  | decide | - |
| PLT-013 | permissions | Permission: NSFaceIDUsageDescription |  | yes |  | decide | - |
| PLT-014 | permissions | Permission: NSLocationWhenInUseUsageDescription |  | yes |  | decide | - |
| PLT-015 | permissions | Permission: NSMicrophoneUsageDescription | yes | yes |  | decide | - |
| PLT-016 | permissions | Permission: NSPhotoLibraryAddUsageDescription |  | yes |  | decide | - |
| PLT-017 | permissions | Permission: NSPhotoLibraryUsageDescription | yes | yes |  | decide | - |
| PLT-018 | permissions | Permission: NSSpeechRecognitionUsageDescription | yes | yes |  | decide | - |
| PLT-080 | permissions | Permission: android.permission.ACCESS_COARSE_LOCATION |  |  | yes | decide | - |
| PLT-081 | permissions | Permission: android.permission.ACCESS_FINE_LOCATION |  |  | yes | decide | - |
| PLT-019 | permissions | Permission: android.permission.ACCESS_NETWORK_STATE | yes |  | yes | decide | - |
| PLT-020 | permissions | Permission: android.permission.BROADCAST_CLOSE_SYSTEM_DIALOGS | yes |  |  | decide | - |
| PLT-082 | permissions | Permission: android.permission.CAMERA |  |  | yes | decide | - |
| PLT-083 | permissions | Permission: android.permission.FOREGROUND_SERVICE |  |  | yes | decide | - |
| PLT-021 | permissions | Permission: android.permission.INTERNET | yes |  | yes | decide | - |
| PLT-022 | permissions | Permission: android.permission.NEARBY_WIFI_DEVICES | yes |  |  | decide | - |
| PLT-023 | permissions | Permission: android.permission.POST_NOTIFICATIONS | yes |  | yes | decide | - |
| PLT-024 | permissions | Permission: android.permission.QUERY_ALL_PACKAGES | yes |  |  | decide | - |
| PLT-025 | permissions | Permission: android.permission.READ_CALENDAR | yes |  |  | decide | - |
| PLT-026 | permissions | Permission: android.permission.RECORD_AUDIO | yes |  | yes | decide | - |
| PLT-084 | permissions | Permission: android.permission.USE_BIOMETRIC |  |  | yes | decide | - |
| PLT-027 | permissions | Permission: android.permission.USE_FINGERPRINT | yes |  |  | decide | - |
| PLT-028 | permissions | Permission: android.permission.VIBRATE | yes |  | yes | decide | - |
| PLT-029 | permissions | Permission: android.permission.WAKE_LOCK | yes |  | yes | decide | - |
| PLT-030 | permissions | Permission: android.permission.WRITE_CALENDAR | yes |  |  | decide | - |
| PLT-031 | permissions | Permission: android.permission.WRITE_EXTERNAL_STORAGE | yes |  |  | decide | - |
| PLT-032 | permissions | Permission: com.google.android.c2dm.permission.RECEIVE | yes |  |  | decide | - |
| PLT-085 | permissions | Permission: com.google.android.gms.permission.AD_ID |  |  | yes | decide | - |
| PLT-086 | permissions | Permission: com.visma.employee.permission.SHOW_NOTIFICATION |  |  | yes | decide | - |
| PLT-033 | sharing | App groups | group.com.visma.vmm | group.com.visma.vme.payslip.shared, group.com.visma.Employee.shared |  | decide | drop |
| PLT-034 | security | ATS exceptions / cleartext traffic | NSAllowsLocalNetworking (ios/vmm/Info.plist) |  |  | decide | - |
| PLT-035 | privacy | Privacy manifest | ios/PrivacyInfo.xcprivacy | Employee/PrivacyInfo.xcprivacy, ExpenseShareExtension/PrivacyInfo.xcprivacy |  | required | - |
| PLT-036 | flags | Remote-config flags | 15 keys |  |  | decide | - |
| PLT-037 | analytics | Firebase Analytics | @react-native-firebase/analytics ^25.1.0 |  |  | decide | - |
| PLT-038 | analytics | Snowplow | @snowplow/react-native-tracker ^4.10.0 | snowplow-ios-tracker 6.2.3 |  | decide | - |
| PLT-045 | crash | Sentry | @sentry/react-native ^8.22.0 |  |  | decide | - |
| PLT-046 | crash | Crashlytics | @react-native-firebase/crashlytics ^25.1.0 |  | com.google.firebase:firebase-crashlytics-gradle | decide | - |
| PLT-047 | flags | Firebase Remote Config | @react-native-firebase/remote-config ^25.1.0 |  |  | decide | - |
| PLT-048 | surveys | Survicate | @survicate/react-native-survicate ^8.3.2 | survicate-ios-sdk 8.2.0 |  | decide | - |
| PLT-049 | messaging | Firebase In-App Messaging | @react-native-firebase/in-app-messaging ^25.1.0 |  |  | decide | - |
| PLT-050 | push | Firebase Cloud Messaging | @react-native-firebase/messaging ^25.1.0 |  |  | decide | keep |
| PLT-041 | auth | OAuth (AppAuth) | react-native-app-auth patch:react-native-app-auth@npm%3A8.4.1#~/.yarn/patches/react-native-app-auth-npm-8.4.1-6859698b6b.patch |  |  | decide | - |
| PLT-051 | storage | MMKV | react-native-mmkv ^4 |  |  | decide | decide-later |
| PLT-052 | graphql | Apollo GraphQL | @apollo/client ^3.13.8 |  |  | decide | - |
| PLT-053 | ui | Lottie | lottie-ios 4.5.0, lottie-react-native ^7.3.5 |  |  | decide | - |
| PLT-042 | storage | Local storage | asyncstorage, keychain | keychain, realm-model | room-entity | decide | drop |
| PLT-043 | i18n | Locales | da, en, fi, nl, no, sv | en, da-DK, fi-FI, nb-NO, sv-SE | default | required | - |
| PLT-054 | analytics | Firebase iOS SDK (which products are used is not visible in Package.resolved) |  | firebase-ios-sdk 12.8.0 |  | decide | - |
| PLT-055 | flags | LaunchDarkly |  | ios-client-sdk 11.1.0, swift-eventsource 3.3.0 |  | decide | - |
| PLT-056 | maps | Google Maps |  | ios-maps-sdk 10.7.0, ios-places-sdk 10.6.0 |  | decide | - |
| PLT-057 | storage | Realm |  | realm-core 20.1.5, realm-swift 20.0.5 |  | decide | decide-later |
| PLT-087 | remote config | Firebase Remote Config fetchAndActivate for the Snowplow analytics switch | src/components/uiless/AnalyticsSettingWatcher/AnalyticsSettingWatcher.tsx:27-40 |  |  | decide | - |
| PLT-088 | remote config | Firebase Remote Config user-testing phase JSON with a 13-hour recheck timer | src/components/uiless/UserTestingRecruitmentAccessWatcher/UserTestingRecruitmentAccessWatcher.tsx:16-105 |  |  | decide | - |
| PLT-089 | analytics | Firebase Analytics collection toggle and an integration-roles custom dimension | src/components/uiless/AnalyticsRolesWatcher/AnalyticsRolesWatcher.ts:14-34 |  |  | decide | - |
| PLT-090 | android system UI | Edge-to-edge Android navigation bar icon colour follows the app theme (@zoontek/react-native-navigation-bar) | src/components/uiless/NavigationBarStyleWatcher/NavigationBarStyleWatcher.tsx:7-11 |  |  | decide | - |
| PLT-091 | performance monitoring | Performance monitoring gated on Remote Config readiness | src/components/uiless/PerfMonitoringGate/PerfMonitoringGate.tsx:8-11 |  |  | decide | - |
| PLT-092 | settings persistence | Settings persistence hook host (useSettingsPersistence) | src/components/uiless/SettingsInitializer/SettingsInitializer.tsx:8-14 |  |  | decide | - |
| PLT-093 | app update | App update check overlay host (useUpdateCheck) | src/components/uiless/UpdateCheckWatcher/UpdateCheckWatcher.tsx:15-18 |  |  | decide | - |
| PLT-094 | push | Approval push token registration (APNs/FCM) on foreground, POST Devices | src/components/approval/ApprovalNotificationsReregister/ApprovalNotificationsReregister.tsx:22-90; src/services/queryApi/queryEndpointsHRM/approval/queryEndpointsApproval.ts:688-716 |  |  | decide | - |
| PLT-095 | push | Unregister device token on logout (DELETE Devices/{token}) via logoutUnregisterApprovalNotificationsEpic | src/epics/logoutUnregisterApprovalNotificationsEpic.ts:19; src/services/queryApi/queryEndpointsHRM/approval/queryEndpointsApproval.ts:719-730 |  |  | decide | - |
| PLT-096 | external link | Store rating deep links market:// and itms-apps:// | src/components/approval/AppRateDialog/AppRateDialog.tsx:157-169 |  |  | decide | - |
| PLT-097 | share | System share sheet for task documents with image-to-PDF generation | src/components/approval/ApprovalDocumentShare/ApprovalDocumentShare.tsx:8-9,26-117 |  |  | decide | - |
| PLT-098 | file system | Attachment download/cache and TIFF conversion via react-native-blob-util | src/utils/attachments.ts:4,229-270 |  |  | decide | - |
| PLT-099 | haptics | Vibration on multiselect of a task (respects vibration setting) | src/components/approval/ApprovalList/ApprovalListItem/ApprovalListItem.tsx:152-156 |  |  | decide | - |
| PLT-100 | accessibility | Swipe actions hidden when screen reader is enabled | src/components/approval/ApprovalListSwipeItemRight/ApprovalListSwipeItemRight.tsx:34-38 |  |  | decide | - |
| PLT-101 | storage | Encrypted MMKV persistence of approval, approvalRecentSearches, appRate, settings, collapsed groups slices (RTK Query c… | src/configs/reduxState.ts:107-128 |  |  | decide | - |
| PLT-102 | webview / external app handoff | BankID / bank 2FA WebView that opens custom URL schemes (bankid://) through Linking.openURL, with a scheme blocklist | src/components/autopay/AutopayApproveTransaction/webViewUrlPolicy.ts:16-34; src/components/autopay/AutopayApproveTransaction/AutopayApproveTransaction.tsx:101-126 |  |  | decide | - |
| PLT-103 | webview | Approval completion detected by redirect-URL sniffing (firebaseapp.com = ok, web.app = cancel) | src/components/autopay/AutopayApproveTransaction/AutopayApproveTransaction.tsx:132-156; src/services/apiAutopay/apiAutopay.ts:119-124 |  |  | decide | - |
| PLT-104 | debug | Dev-only HTML dump script injected into the approve WebView (__DEV__ guard) | src/components/autopay/AutopayApproveTransaction/approveWebViewDebug.ts:15-28; AutopayApproveTransaction.tsx:293-297 |  |  | decide | - |
| PLT-105 | haptics | Vibration on payment selection (android.permission.VIBRATE) | src/components/autopay/TransactionListItem/TransactionListItem.tsx:72-74; android/app/src/main/AndroidManifest.xml:10 |  |  | decide | - |
| PLT-106 | file system | Invoice PDF saved to a local file from an arraybuffer response | src/services/apiAutopay/apiAutopay.ts:287-300 |  |  | decide | - |
| PLT-107 | feature flag | features.showAutopayOverviewTab gates the Overview tab | src/components/autopay/AutopayTopBar/AutopayTopBar.tsx:30,57-59 |  |  | decide | - |
| PLT-108 | calendar | Device calendar sync of birthdays/anniversaries via react-native-calendar-events | src/hooks/useSyncCalendar.ts:41-60 |  |  | decide | - |
| PLT-109 | notifications | App icon badge reset on forced logout | src/components/common/ModalDialog/ModalDialog.tsx:37 |  |  | decide | - |
| PLT-110 | debug | Hidden environment switcher (prod/stage/sandbox) unlocked by 6 taps | src/components/common/EnvPicker/EnvPicker.tsx:59-65 |  |  | decide | - |
| PLT-111 | webview | Accessibility statement rendered in WebviewModal with embedded fonts | src/components/common/LangAccPicker/LangAccPicker.tsx:81-88 |  |  | decide | - |
| PLT-112 | navigation | Android hardware back handler that closes the document selector, then the fullscreen document viewer, then clears the a… | src/components/common/ThemedBackButtonWithDocViewer/ThemedBackButtonWithDocViewer.tsx:26-53 |  |  | decide | - |
| PLT-113 | external links | Opens the store listing with market:// on Android and itms-apps:// on iOS | src/components/common/UpdateDialog/UpdateDialog.tsx:23-29 |  |  | decide | - |
| PLT-114 | storage | redux-persist whitelist includes settings, npsSurvey, features and whatsNew, which hold dontShowNpsSurvey, sandboxColor… | src/configs/reduxState.ts:107-128 |  |  | decide | - |
| PLT-115 | accessibility | What's New media honours the reduce-motion and screen-reader settings | src/components/common/WhatsNewMedia/WhatsNewMedia.tsx:32-33 |  |  | decide | - |
| PLT-116 | network | Sandbox status is fetched from a hardcoded external Azure dashboard URL, outside the app's apiBase | src/consts/constants.ts:18 |  |  | decide | - |
| PLT-117 | device integration | Open phone dialer, SMS and mail apps via Linking (tel:, sms:, mailto:) with canOpenURL check | src/components/hrm/HrmEmployeeDetailHead/HrmEmployeeDetailHead.tsx:125-155 |  |  | decide | - |
| PLT-118 | device integration | Native Share sheet for contact values | src/components/hrm/HrmEmployeeDetailAccordeon/ReadOnlyField/ReadOnlyField.tsx:50-54 |  |  | decide | - |
| PLT-119 | device integration | Clipboard write of employee post address (@react-native-clipboard/clipboard) | src/components/hrm/HrmEmployeeDetailAccordeon/HrmEmployeeDetailAccordion.tsx:1,261 |  |  | decide | - |
| PLT-120 | storage | Redux slices hrmEmployeeList, hrmAnniversary, hrmDialogue, hrmDialogueCollapsedGroups, features persisted via custom en… | src/configs/reduxState.ts:107-128 |  |  | decide | - |
| PLT-121 | network | Authenticated image loading for Dottie profile photos (Bearer header on Image source) | src/hooks/useDottieProfileImageSource.ts:20-22 |  |  | decide | - |
| PLT-122 | push notification | Notification payload normalizer (integration, attributes, taskId, action button, RemoteInput userText, Gaia threadId; a… | src/components/modals/ChatModal/utils.ts:162-218 |  |  | decide | - |
| PLT-123 | speech | Speech-to-text dictation via @react-native-voice/voice with Android microphone permission | src/hooks/useSpeech.ts:1-15 |  |  | decide | - |
| PLT-124 | keyboard | Android soft input mode switched to adjustResize while the Gaia chat is focused | src/components/modals/GaiaChatModal/GaiaChatModal.tsx:268-279 |  |  | decide | - |
| PLT-125 | webview | In-app WebView showing sanitized HTML with an external-link allowlist for W3C WAI | src/components/modals/WebviewModal/WebviewModal.tsx:30-76 |  |  | decide | - |
| PLT-126 | external links | Linking.openURL for Gaia citation sources and task-card browser fallback | src/components/modals/GaiaChatModal/GaiaChatItem.tsx:85-95 |  |  | decide | - |
| PLT-127 | feature flags | Gaia capabilities catalog and frontend navigation tools gated by dev flags | src/components/modals/GaiaChatModal/useGaiaFrontendToolExecutor.ts:70 |  |  | decide | - |
| PLT-128 | credentials | OpenAI base URL and API key constants in code (both empty strings, '' preview) | src/hooks/useAi.tsx:6-7 |  |  | decide | - |
| PLT-129 | storage | Encrypted MMKV redux store (id redux-state, AES-256, key from persistent random seed) | src/configs/persistEngine.ts:70-75 |  |  | decide | - |
| PLT-130 | storage | One-time legacy AsyncStorage persist:root import with keychain key, then cleanup | src/configs/legacyPersistImport.ts:56-188 |  |  | decide | - |
| PLT-131 | monitoring | Firebase Performance HTTP metrics on every axios request (react-native-firebase/perf) | src/configs/axiosInterceptors.ts:85-134 |  |  | decide | - |
| PLT-132 | monitoring | Sentry crash, session, stall, failed-request and navigation tracing with dev/prod DSNs | src/configs/sentryConfig.ts:100-123 |  |  | decide | - |
| PLT-133 | notifications | Notification open consumer and reminder sync mounted in the logged-in tab navigator | src/configs/navConfig/navConfig.tsx:61-63 |  |  | decide | - |
| PLT-134 | notifications | Common stacks register employee detail and birthday-bot screens so notification taps push onto the focused tab | src/configs/navConfig/common/CommonScreensNavConfig.tsx:375-405 |  |  | decide | - |
| PLT-135 | navigation | No linking config on NavigationContainer (no React Navigation deep-link paths in this area) | src/configs/navConfig/navConfig.tsx:177-189 |  |  | decide | - |
| PLT-136 | device | Shake gesture watcher and network logger screen (dev tools) | src/configs/navConfig/navConfig.tsx:185; src/configs/navConfig/common/CommonScreensNavConfig.tsx:308-312 |  |  | decide | - |
| PLT-137 | startup | BootSplash hidden on navigation ready | src/configs/navConfig/navConfig.tsx:151-161 |  |  | decide | - |
| PLT-138 | analytics | Screen view event on every route change (SCREEN_VIEW) | src/configs/navConfig/navConfig.tsx:124-126 |  |  | decide | - |
| PLT-139 | secrets | Hardcoded Sentry DSNs (masked 'b5d7…', 'b5bb…') | src/configs/sentryConfig.ts:114; src/configs/sentryConfig.ts:120 |  |  | decide | - |
| PLT-140 | secrets | Hardcoded legacy encryption key prefix constant (masked 'nIH…') | src/configs/legacyPersistImport.ts:17 |  |  | decide | - |
| PLT-141 | auth | Visma Connect OAuth via react-native-app-auth with universal-link redirect https://visma-manager.web.app/connect-login | src/screens/common/LoginSelectScreen/LoginSelectScreen.tsx:93; src/services/apiManagerConnect/apiManagerConnect.ts:55 |  |  | decide | - |
| PLT-142 | auth | Web logout via Linking.openURL endsession and universal-link callback connect-logout (10s fallback) | src/services/apiManagerConnect/apiManagerConnect.ts:468-501 |  |  | decide | - |
| PLT-143 | notifications | App icon badge reset on logout | src/screens/common/SettingsScreen/SettingsScreen.tsx:194 |  |  | decide | - |
| PLT-144 | notifications | Notifee local/trigger notifications with approve/reject/forward action categories (dev tools) | src/screens/common/SettingsDevToolsScreen/SettingsDevToolsScreen.tsx:663-745 |  |  | decide | - |
| PLT-145 | notifications | Push device registration POST/DELETE Devices (RTK Query) | src/services/queryApi/queryEndpointsHRM/approval/queryEndpointsApproval.ts:688-735 |  |  | decide | - |
| PLT-146 | media | Photo library picker with crop (react-native-image-crop-picker) | src/screens/common/ProfilePictureScreen/ProfilePictureScreen.tsx:11-19 |  |  | decide | - |
| PLT-147 | system | Android hardware back blocked during login and pending ToS | src/screens/common/LoginSelectScreen/LoginSelectScreen.tsx:156-171; src/screens/common/SettingsTosScreen/SettingsTosScreen.tsx:32-42 |  |  | decide | - |
| PLT-148 | system | Share sheet for error reports; clipboard in dev tools | src/screens/common/RequestErrorLogsScreen/RequestErrorLogsScreen.tsx:36 |  |  | decide | - |
| PLT-149 | browser | In-app browser for legal/license links | src/screens/common/SettingsLicensesScreen/SettingsLicensesScreen.tsx:34 |  |  | decide | - |
| PLT-150 | push | Dialogue detail opened from push notification (fromNotification param) with custom back navigation | src/screens/hrm/DialogueDetailsScreen/DialogueDetailsScreen.tsx:71-77,156-203 |  |  | decide | - |
| PLT-151 | push | Birthday bot flow can be cold-started from a notification | src/screens/hrm/HrmBirthdayBot/HrmBotGenerateMessageScreen/HrmBotGenerateMessageScreen.tsx:58-64 |  |  | decide | - |
| PLT-152 | lifecycle | AppState foreground refetch of open dialogue | src/screens/hrm/DialogueDetailsScreen/DialogueDetailsScreen.tsx:208-225 |  |  | decide | - |
| PLT-153 | share | react-native-share system share sheet | src/screens/hrm/HrmBirthdayBot/HrmBotGeneratingFinishedScreen/HrmBotGeneratingFinishedScreen.tsx:29,200 |  |  | decide | - |
| PLT-154 | deep link out | sms: URL opened via Linking | src/screens/hrm/HrmBirthdayBot/HrmBotGeneratingFinishedScreen/HrmBotGeneratingFinishedScreen.tsx:226-228 |  |  | decide | - |
| PLT-155 | android | Hardware back button handling | src/screens/hrm/DialogueSplitsScreen/DialogueSplitsScreen.tsx:98-110 |  |  | decide | - |
| PLT-156 | android | Keyboard soft input adjustResize via react-native-keyboard-controller | src/screens/hrm/DialogueDetailsScreen/DialogueDetailsScreen.tsx:128-140 |  |  | decide | - |
| PLT-157 | storage | Encrypted MMKV redux persistence whitelist includes hrmEmployeeList, hrmAnniversary, hrmDialogue, hrmDialogueCollapsedG… | src/configs/reduxState.ts:107-128 |  |  | decide | - |
| PLT-158 | notifications | App icon badge count set to number of pending approval tasks | src/screens/manager/ApprovalScreen/components/TabPresent/TabPresent.tsx:108-114 |  |  | decide | - |
| PLT-159 | remote config | Firebase Remote Config fetch for user-testing recruitment phase | src/screens/manager/ApprovalScreen/components/TabPresent/TabPresent.tsx:156-169 |  |  | decide | - |
| PLT-160 | surveys | Survicate survey triggered on approval list after a task is closed (feature flag useSurvicate) | src/screens/manager/ApprovalScreen/ApprovalScreen.tsx:71-84 |  |  | decide | - |
| PLT-161 | navigation | Android hardware back handling on approval list, task detail (fullscreen document), Compello and order field overlays | src/screens/manager/ApprovalScreen/ApprovalScreen.tsx:125-156 |  |  | decide | - |
| PLT-162 | navigation | beforeRemove unsaved-changes guard on BXN order edit | src/screens/manager/BnxtOrderDetailScreen/BnxtOrderDetailScreen.tsx:211-224 |  |  | decide | - |
| PLT-163 | linking | tel: and mailto: links from BXN associate card | src/screens/manager/BnxtAssociateCardScreen/BnxtAssociateCardScreen.tsx:144-166 |  |  | decide | - |
| PLT-164 | files | Base64 attachment written to cache and rendered with react-native-pdf | src/screens/manager/BnxtAttachmentViewerScreen/BnxtAttachmentViewerScreen.tsx:19-42 |  |  | decide | - |
| PLT-165 | device info | react-native-device-info used for feedback payload | src/screens/manager/ApprovalTaskBXNLineEditFeedbackScreen/ApprovalTaskBXNLineEditFeedbackScreen.tsx:56-65 |  |  | decide | - |
| PLT-166 | feature flag | BXN tabbed hub (getBnxtTabbedHubEnabled) swaps BnxtHubScreen for BnxtWorkspaceScreen | src/configs/navConfig/bnxtOrders/BnxtOrdersNavConfig.tsx:63-80 |  |  | decide | - |
| PLT-167 | api | Business NXT GraphQL via Apollo at business.visma.net / business.stag.visma.net /api/graphql | src/services/apiBaseStateless.ts:37-44 |  |  | decide | - |
| PLT-168 | navigation | beforeRemove guard blocks Android hardware back and iOS swipe-back while there are unsaved line edits or open overlays | src/screens/manager/ApprovalTaskBXNLineEditScreen/ApprovalTaskBXNLineEditScreen.tsx:434-459 |  |  | decide | - |
| PLT-169 | navigation | Route 'ApprovalTaskBXNLineEditScreen' registered in the Approval stack and opened from DocumentEditorButton via TAB_ROU… | src/configs/navConfig/approval/ApprovalNavConfig.tsx:135 |  |  | decide | - |
| PLT-170 | network | Apollo GraphQL client with endpoint {PRODUCTION/STAGING}_URI_BASE/api/graphql | src/services/apolloClient.ts:204-206; src/services/apiBaseStateless.ts:41-45 |  |  | decide | - |
| PLT-171 | storage | Custom mode and selected fields are kept in the persisted settings slice (redux persist whitelist) | src/configs/reduxState.ts:107-108 |  |  | decide | - |
| PLT-172 | navigation | beforeRemove guard blocks leaving the line editor with unsaved changes (Android hardware back, iOS swipe-back) | src/screens/manager/ApprovalTaskEditFinancialsLinesScreen/ApprovalTaskEditFinancialsLinesScreen.tsx:299-325 |  |  | decide | - |
| PLT-173 | navigation | Edit overlay back handler closes the field edit overlay before popping the screen | src/screens/manager/ApprovalTaskEditFinancialsLinesScreen/context/FieldEditOverlayContext.tsx:118-150 |  |  | decide | - |
| PLT-174 | storage | The settings slice (custom mode and selected financial line fields) is persisted through the redux whitelist | src/configs/reduxState.ts:107-108 |  |  | decide | - |
| PLT-175 | navigation | Stack route ApprovalTaskVoucherlinesEditorScreen registered in the approval stack, with params { index: number } | src/configs/navConfig/approval/ApprovalNavConfig.tsx:165-172 |  |  | decide | - |
| PLT-176 | remote config | What's New spotlight payload from Firebase Remote Config key feature_whats_new_v1 | src/services/whatsNew/whatsNewConfig.ts:114-123; src/consts/firebase.ts:19 |  |  | decide | - |
| PLT-177 | feature flag | Start tab dark-shipped behind loginManager.toggledStartPageDevFlag | src/configs/navConfig/navConfig.tsx:61; src/configs/TabBar.tsx:94 |  |  | decide | - |
| PLT-178 | feature flag | Home search overlay behind features.showHomeSearch (dev tools) | src/hooks/useHomeSearchEnabled.ts |  |  | decide | - |
| PLT-179 | dev tools | 'Empty on shake' debug empty mode honoured by Home, cleared by pull-to-refresh | src/screens/StartScreen/hooks/useStartScreenData.ts:144,646 |  |  | decide | - |
| PLT-180 | navigation | Start stack registers StartScreen, ApprovalTaskScreen and common screens; mounts ApprovalTaskActionsDrawer | src/configs/navConfig/startScreen/StartScreenNavConfig.tsx:18-77 |  |  | decide | - |
| PLT-181 | persistence | redux-persist whitelist includes features, hrmAnniversary, whatsNew, autopay; RTK Query cache not persisted | src/configs/reduxState.ts:107-126 |  |  | decide | - |
| PLT-182 | remote config | Firebase Remote Config gates user-testing recruitment banner in AutoPay list | src/screens/autopay/AutopayHomeTabPaymentsScreen/AutopayHomeTabPaymentsScreen.tsx:340-353 |  |  | decide | - |
| PLT-183 | remote config | Firebase Remote Config supplies localized user-test description HTML (prod/stage keys) | src/screens/UserTestingRecruitment/UserTestingTestDescriptionScreen/UserTestingTestDescriptionScreen.tsx:34-54 |  |  | decide | - |
| PLT-184 | app lifecycle | AppState listener reloads AutoPay payments when app returns from background | src/screens/autopay/AutopayHomeTabPaymentsScreen/AutopayHomeTabPaymentsScreen.tsx:296-313 |  |  | decide | - |
| PLT-185 | android | Hardware back button clears AutoPay multiselect instead of navigating | src/screens/autopay/AutopayHomeScreen/AutopayListMultiselectBar/AutopayListMultiselectBar.tsx:45-59 |  |  | decide | - |
| PLT-186 | device info | react-native-device-info used for OS/model/version in feedback and user-testing payloads | src/screens/FeedbackScreen/FeedbackScreen.tsx:60-69 |  |  | decide | - |
| PLT-187 | web | Expo web build registers a service worker (/expo-service-worker.js) | web-build/register-service-worker.js:3-14 |  |  | decide | - |
| PLT-188 | performance | Screen performance tracing and React Profiler on AutoPay screens | src/screens/autopay/AutopayHomeTabPaymentsScreen/AutopayHomeTabPaymentsScreen.tsx:402 |  |  | decide | - |
| PLT-189 | feature flags | Business NXT integration, order edit and tabbed hub flags (dev-tools gated) | src/selectors/bnxtOrders/bnxtOrdersSelectors.ts:9-20 |  |  | decide | - |
| PLT-190 | persistence | Persisted redux slices include settings, osr, autopay, features, gaiaChat, gaiaRuns, hrmDialogueCollapsedGroups | src/configs/reduxState.ts:108-127 |  |  | decide | - |
| PLT-191 | navigation | Coordinator actions showCalendarFeed(initialDate) / showCalendarMonthView / appWillEnterForeground routed to calendar |  | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarCoordinator.swift:77-94 |  | decide | - |
| PLT-192 | in-app survey | Survicate survey with thank-you toast after saving absence/checkout or leaving balances |  | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrationCoordinator/CreateAbsenceRegistrationCoordinator.swift:86 |  | decide | - |
| PLT-193 | app messaging | NotificationCenter AppMessage.reloadStartPage posted after registration/confirm |  | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AddAbsenceCoordinator/AddAbsenceCoordinator.swift:240 |  | decide | - |
| PLT-194 | app events | TCA AppEventsFeature/AppEventPublisher bus for calendar, chatbot and absence-registration events (e.g. absenceViewAppea… |  | Modules/CalendarFeature/Sources/CalendarFeature/AppEvents/AppEventPublisher.swift:14-60 |  | decide | - |
| PLT-195 | chatbot entry | EditAbsenceRegistrationCoordinator initializers for editing from chatbot links and predictions |  | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrationCoordinator/EditAbsenceRegistrationCoordinator.swift:58-80 |  | decide | - |
| PLT-196 | permissions | Microphone and speech recognition usage descriptions used by chatbot voice input |  | Employee/Info.plist:50, Employee/Info.plist:56 |  | decide | - |
| PLT-197 | deep link / system URL | Opens UIApplication.openSettingsURLString when speech permission is denied |  | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotView.swift:40-42 |  | decide | - |
| PLT-198 | in-app messaging | NotificationCenter AppMessage.resetCalendar / resetCalendarBackground observers reload calendar; chatbot close posts re… |  | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarViewController.swift:138-139; Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Coordinator/CalendarChatBotCoordinator.… |  | decide | - |
| PLT-199 | connectivity | Reachability status change toggles offline placeholder and disables calendar buttons |  | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarViewController.swift:913-960 |  | decide | - |
| PLT-200 | analytics | Snowplow structured events in category CalendarBot for chatbot actions |  | Modules/SnowplowAnalytics/Sources/SnowplowAnalytics/Events/Events.swift:112-115, 370-385 |  | decide | - |
| PLT-201 | dead code | EditAbsenceRegistrationFeature/EditAbsenceRegistrationView are defined but never presented (chat uses EditPredictedAbse… |  | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/EditAbsenceRegistration/EditAbsenceRegistrationView.swift:43; no references found outside its own files |  | decide | - |
| PLT-202 | external URL | Hardcoded chatbot feedback form URL (Google Forms) |  | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/LearnMore/LearnMoreConstants.swift:4 (https://forms.gle/****) |  | decide | - |
| PLT-203 | camera / photo library | UIImagePickerController with camera or photo library source for the profile picture (needs NSCameraUsageDescription / p… |  | Modules/DottieFeature/Sources/DottieFeature/Features/EmployeeInfo/Sheets/ProfileImageSheet/ImagePickerView.swift:8-18 |  | decide | - |
| PLT-204 | file preview | Quick Look preview of downloaded documents stored as temporary files that are deleted on dismiss |  | Modules/DottieFeature/Sources/DottieFeature/Features/DocumentsAndBenefits/DocumentsAndBenefitsView.swift:59-62 |  | decide | - |
| PLT-205 | in-app browser | openURLInApp for external document links and benefit links; dismissing it triggers the mark-as-read prompt |  | Modules/DottieFeature/Sources/DottieFeature/Features/OrgDocumentPreview/OrgDocumentPreviewView.swift:17-23 |  | decide | - |
| PLT-206 | inbox integration | Dottie notifications plugged into the shared InboxMessages inbox as InboxContentProvider id 'dottie-notifications' |  | Modules/DottieFeature/Sources/DottieFeature/Features/Notifications/DottieNotificationsInboxProvider.swift:9-33 |  | decide | - |
| PLT-207 | session / cache | In-memory profile cache keyed by userId_tenantId and shared profile image; refreshed when stale (15 min) from Start pag… |  | Modules/DottieFeature/Sources/DottieFeature/Repository/DottieEmployeeRepository.Live.swift:7-58 |  | decide | - |
| PLT-208 | push | APNs registration with multi-account token register/deregister on change |  | Employee/AppDelegate.swift:115-129 |  | decide | - |
| PLT-209 | push | Badge count cleared when scene becomes active |  | Employee/SceneDelegate.swift:79-81 |  | decide | - |
| PLT-210 | security | Passcode/biometric lock presented on launch and after background timeout when a session is active |  | Employee/SceneDelegate.swift:67-73,134-138 |  | decide | - |
| PLT-211 | security | Blur overlay hides sensitive content in app switcher |  | Employee/SceneDelegate.swift:83-92,150-156 |  | decide | - |
| PLT-212 | storage | KeychainBiometricStorage for biometric token (service Constants.Security.biometricKeychainService) |  | Employee/AppDependencies.swift:244-252 |  | decide | - |
| PLT-213 | storage | UserDefaultsPasscodeRepository for passcode configuration |  | Employee/AppDependencies.swift:452 |  | decide | - |
| PLT-214 | deep link | URLRouterCoordinator started at launch; scene openURLContexts is empty |  | Employee/SceneDelegate.swift:94-95,115-117 |  | decide | - |
| PLT-215 | app group | App group group.com.visma.vme.payslip.shared (AppStore) / group.com.visma.Employee.shared |  | Employee/EmployeeAppConstants.swift:13-19 |  | decide | - |
| PLT-216 | analytics | Snowplow analytics and Survicate surveys configured |  | Employee/AppDependencies.swift:156-170,491-494 |  | decide | - |
| PLT-217 | tips | TipKit configured with immediate display frequency |  | Employee/AppDelegate.swift:100-108 |  | decide | - |
| PLT-218 | third-party | Google Maps / Google Places SDK and ThirdPartyKeyProvisioner initialized from storage |  | Employee/AppDelegate.swift:25-26,95 |  | decide | - |
| PLT-219 | push | Push permission request and APNs registration on app entry; deregisters stored token if denied |  | Employee/MainCoordinator/MainCoordinator.swift:409-427 |  | decide | - |
| PLT-220 | push | UNUserNotificationCenter delegate: foreground banner+sound and tap routing by eventId |  | Employee/PushNotifications/PushNotificationHandlingService.UserNotificationsCenter.swift:11-29 |  | decide | - |
| PLT-221 | push | Multi-account push registration: device token registered for every authenticated account |  | Employee/PushNotifications/MultiAccountPushManager.live.swift:37-73 |  | decide | - |
| PLT-222 | storage | APNs device token kept in UserDefaults key <bundleID>.deviceToken |  | Employee/PushNotifications/PushTokenStorage.userDefaults.swift:14-25 |  | decide | - |
| PLT-223 | auth | OAuth login via ASWebAuthenticationSession, ephemeral session, universal-link callback (AllowedAppLinks.hostname/callba… |  | Employee/Accounts/Feature/Login/OAuthLogin.live.swift:35-44 |  | decide | - |
| PLT-224 | biometrics | Biometric app lock using Keychain item with .userPresence and kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly, optional… |  | Employee/Security/Biometric/BiometricSecureStorage.swift:28-55 |  | decide | - |
| PLT-225 | biometrics | LocalAuthentication capability checks (Face ID / Touch ID / Optic ID mapped to Face ID) |  | Employee/Security/DeviceSecurityService.swift:12-32 |  | decide | - |
| PLT-226 | security | App lock window presented on launch/resume above main window when PIN or biometric token exists |  | Employee/Security/Passcode/PasscodePresenter.swift:39-63 |  | decide | - |
| PLT-227 | security | Legacy UserDefaults PIN repository (plain string array) used only by UserDataMigrationService |  | Employee/Security/Passcode/UserDefaultsPasscodeRepository.swift:40-50 |  | decide | - |
| PLT-228 | developer | developerForcePincode AppStorage flag disables biometrics |  | Employee/Security/DeveloperForcePincodeKey.swift:6-8 |  | decide | - |
| PLT-229 | developer | Hidden 5-tap environment switcher on login screen (staging/production), not DEBUG-gated |  | Employee/Accounts/Feature/Login/SelectAccountView.swift:48-50 |  | decide | - |
| PLT-230 | extension | Share extension can change current company; main app reloads context on foreground |  | Employee/MainCoordinator/MainCoordinator.swift:371-377 |  | decide | - |
| PLT-231 | app update | Forced/optional app update gate (AppUpdateCoordinator via RemoteControl) before entering app |  | Employee/MainCoordinator/MainCoordinator.swift:75-81 |  | decide | - |
| PLT-232 | navigation | Start tab root: StartPageCoordinator shows StartPageViewController from the StartPage storyboard in a TabNavigationCont… |  | Employee/StartPage/Coordinator/StartPageCoordinator.swift:28-62 |  | decide | - |
| PLT-233 | in-app messaging | NotificationCenter AppMessage.reloadStartPage triggers a start page reload; AppMessage.resetCalendar is posted after ch… |  | Employee/StartPage/StartPageViewController.swift:418-420; Employee/StartPage/ViewControllerCheckinWrapper.swift:158-160 |  | decide | - |
| PLT-234 | connectivity | Reachability listener reloads the start page on online/offline change; offline disables quick actions and adds an offli… |  | Employee/StartPage/StartPageViewController.swift:1054-1075 |  | decide | - |
| PLT-235 | biometrics | First-run biometrics setup gate before the start page loads |  | Employee/StartPage/StartPageViewController.swift:222-234 |  | decide | - |
| PLT-236 | web | Survey form opens in Safari (SafariCoordinator); information-message links open externally via MEURLHandler |  | Employee/StartPage/Cards/DetailProviders/SurveyCardDetailsProvider.swift:30-31; Employee/StartPage/Cards/DetailProviders/InformationCardDetailsProvider.swift:31-34 |  | decide | - |
| PLT-237 | UI / OS version | iOS 26 Liquid Glass branches: company selector moves to a nav-bar UIMenu, large titles are turned off, and bar button b… |  | Employee/StartPage/StartPageViewController.swift:634-660,778-781 |  | decide | - |
| PLT-238 | sync | SyncService.sync() runs before every start page data load |  | Employee/StartPage/StartPageViewController.swift:407-413,430-434 |  | decide | - |
| PLT-239 | security | Auto-lock after 15 seconds in background (securityLockTimer pause/resume, lockTimeout 15.0) |  | Employee/Services/SecurityService.swift:129-139 |  | decide | - |
| PLT-240 | security | Security state sanitizer on launch (align login type with biometric token/PIN presence) |  | Employee/Services/SecurityService.swift:149-164 |  | decide | - |
| PLT-241 | migration | Biometric migration: legacy PIN replaced by biometric token when device owner auth is available |  | Employee/Services/Migration/BiometricMigrationService.swift:21-57 |  | decide | - |
| PLT-242 | migration | Multi-user migration of single-user storage, login type and passcode |  | Employee/Services/Migration/MultiuserMigrationService.swift:28-33 |  | decide | - |
| PLT-243 | migration | Realm and user data migrations |  | Employee/Services/Migration/RealmMigrationService.swift:1 |  | decide | - |
| PLT-244 | app group | Shared app-group container with per-user Realm db_<sha256(userId)>.realm and shared UserDefaults (used by extensions) |  | Modules/EmployeeAppCore/Sources/EmployeeAppCore/SharedContainer/SharedContainer.swift:21-40 |  | decide | - |
| PLT-245 | deep link | Universal link hosts static.mobileemployee(.stag).visma.net with /auth/callback (OAuth) and /close (registered but not… |  | EmployeeServices/EmployeeAPIInterface/Sources/EmployeeAPIInterface/APIInterfaceConstants.swift:67-96; Employee/Shared/URLRouter/URLRouterCoordinator.swift:22-42 |  | decide | - |
| PLT-246 | push | Push registration on login and unregistration on logout |  | Employee/Services/AppStateService.swift:59-64,73-83 |  | decide | - |
| PLT-247 | speech | Speech recognition service (SFSpeechRecognizer + AVAudioEngine) with mic/speech permission checks |  | Modules/EmployeeAppCore/Sources/EmployeeAppCore/Services/SpeechRecognition/SpeechRecognizerService.speechFramework.swift:16-176 |  | decide | - |
| PLT-248 | photos | Save photo to Photo Library |  | Modules/EmployeeAppCore/Sources/EmployeeAppCore/Photos/PhotoLibrary.swift:15 |  | decide | - |
| PLT-249 | telemetry | Client error logging POST /employee/api/v1/logging/clienterror (202 empty allowed) |  | EmployeeServices/EmployeeAPIInterface/Sources/EmployeeAPIInterface/Request/PostClientError.swift:11-28 |  | decide | - |
| PLT-250 | config | Third-party keys (Firebase, Google Maps, Google Places, LaunchDarkly, Survicate) fetched from backend, cached and appli… |  | Employee/Services/ThirdPartyKeys/ThirdPartyKeyProvisioner.swift:25-56; Employee/Services/ThirdPartyKeys/FirebaseKeyInitializer.swift:25 |  | decide | - |
| PLT-251 | network | API base URLs https://mobileemployee.visma.net (prod) / mobileemployee.stag.visma.net; Visma Connect authorize/token/re… |  | EmployeeServices/EmployeeAPIInterface/Sources/EmployeeAPIInterface/APIInterfaceConstants.swift:33-50; EmployeeServices/EmployeeAPI/Sources/EmployeeAPI/APIConstants.swift:12-60 |  | decide | - |
| PLT-252 | maps | MapKit hotel/POI search (MKLocalSearchCompleter) for allowance lodging |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Allowance/Repository/HotelSearch/MapKitSearchService.swift:11-21 |  | decide | - |
| PLT-253 | photos | Save attachment image to photo library (needs NSPhotoLibraryAddUsageDescription), falls back to opening Settings |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Attachments/AttachmentsFeature.swift:274-341 |  | decide | - |
| PLT-254 | camera | Receipt scanner (camera/library/file sources) for adding attachments |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Attachments/ReceiptScannerView.swift:8-20 |  | decide | - |
| PLT-255 | quicklook | QuickLook preview of attachments |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Attachments/AttachmentsView.swift:7-21 |  | decide | - |
| PLT-256 | files | Export attachment file through the Files document picker |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Attachments/MediaPickerExportView.swift:1-61 |  | decide | - |
| PLT-257 | sync | Sync plus calendar/start-page reload after an allowance is saved or deleted (NotificationCenter AppMessage.resetCalenda… |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Allowance/Coordinator/AddAllowanceCoordinator.swift:167-180 |  | decide | - |
| PLT-258 | feature flag | rollBackToDraft flag sent with direct send-for-approval |  | EmployeeServices/Expense/Sources/Expense/Service/ExpenseService.swift:237-246 |  | decide | - |
| PLT-259 | camera | Camera permission requested before receipt scanner (AVCaptureDevice.requestAccess for .video) |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Coordinators/AddNewReceiptCoordinator.swift:58-65 |  | decide | - |
| PLT-260 | in-app browser | Emission methodology links (cornell.edu, ducky.eco) opened in-app |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/ClimateReports/Views/EmissionReports/HowDoWeCalculateEmissionsView.swift:26-33; Modules/EmployeeExpenses/Sources/EmployeeExpenses/ClimateReports/View… |  | decide | - |
| PLT-261 | in-app survey | Survicate thank-you survey requested after a receipt is saved or edited in a claim |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Coordinators/AddNewReceiptCoordinator.swift:268-272; Modules/EmployeeExpenses/Sources/EmployeeExpenses/Coordinators/EditReceiptInClaimCoordinator.swi… |  | decide | - |
| PLT-262 | cross-screen refresh | NotificationCenter AppMessage.reloadStartPage/resetCalendar/reloadReceiptScreen after claim changes |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Claims/ClaimsTableViewController.swift:282-284; Modules/EmployeeExpenses/Sources/EmployeeExpenses/Coordinators/PresentExpenseCoordinator.swift:62-66 |  | decide | - |
| PLT-263 | sync | Receipt/draft sync triggered after claim save (syncService.syncReceipts / sync) |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Claims/Create/CreateClaimViewController.swift:243; Modules/EmployeeExpenses/Sources/EmployeeExpenses/Coordinators/EditReceiptInClaimCoordinator.swift… |  | decide | - |
| PLT-264 | permissions | When-in-use location for adding mileage (current location as start or destination) |  | Employee/Info.plist:48; Modules/EmployeeExpenses/Sources/EmployeeExpenses/Location/LocationService.swift |  | decide | - |
| PLT-265 | third-party SDK | Google Maps and Places SDK with an API key initializer (key value not reproduced) |  | Employee/Services/ThirdPartyKeys/GoogleMapsKeyInitializer.swift:14 |  | decide | - |
| PLT-266 | sync | Offline mileage drafts are saved locally and uploaded later by SyncService; a reachability listener blocks online-only… |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Mileage/Repository/DraftRepository.mileageDatabase.swift; Modules/EmployeeExpenses/Sources/EmployeeExpenses/Mileage/ViewModels/ExpenseMileageViewMode… |  | decide | - |
| PLT-267 | in-app messaging | NotificationCenter AppMessage reloadReceiptScreen, reloadStartPage, resetCalendar and reloadExpenseScreen refresh other… |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Mileage/Coordinators/EditMileageInClaimCoordinator.swift:131-140 |  | decide | - |
| PLT-268 | extension | Receipt detail reused by the Expense share extension (saveFromExtension config, resource release) |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/ReceiptDetailViewController.swift:142-147,255-270 |  | decide | - |
| PLT-269 | quicklook | PDF receipt preview via QLPreviewController with temp file |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/ReceiptDetailViewController.swift:1533-1560 |  | decide | - |
| PLT-270 | connectivity | Reachability listener toggles offline banner and disables send/merge actions |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/ReceiptDetailViewController.swift:2561-2580,2674 |  | decide | - |
| PLT-271 | background sync | Receipt upload/sync triggered on inbox open and after merge; sync events drive list reload |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/Features/ReceiptsList/ReceiptsListFeature.swift:493-545 |  | decide | - |
| PLT-272 | maps | Server-proxied directions (POST /employee/api/v1/maps/directions) and Google Places search for distance |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/Models/ReceiptDetailViewModel.swift:1401-1441 |  | decide | - |
| PLT-273 | storage | UserDefaults: submit-for-approval don't-show-again flag and distance suggestions |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/ReceiptDetailViewController.swift:684-738,2459-2472 |  | decide | - |
| PLT-274 | camera | Camera capture with permission gate and open-Settings fallback (WeScan) |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Wescan/CameraViewController.swift:112-196 |  | decide | - |
| PLT-275 | photos | Photo library picker (UIImagePickerController .photoLibrary) |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Wescan/MediaPickerCoordinator.swift:54-95 |  | decide | - |
| PLT-276 | files | Document picker import (pdf, image), security-scoped URL, and export to Files |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Wescan/MediaPickerCoordinator.swift:97-197 |  | decide | - |
| PLT-277 | background sync | Reachability-triggered expense sync on background-QoS OperationQueues |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Services/SyncService.swift:80-82,324-330 |  | decide | - |
| PLT-278 | extension | Share extension uses Smartscan for shared receipts (ExpenseShareExtension/ShareReceiptCoordinator) |  | ExpenseShareExtension/ShareReceiptCoordinator.swift:288 |  | decide | - |
| PLT-279 | third-party SDK | Google Places autocomplete (placeProvider) with Powered-by-Google attribution |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/Repository/SearchList.Places/SearchListRepository.places.swift:54-97 |  | decide | - |
| PLT-280 | third-party SDK | Survicate survey thank-you toast after saving or adding expenses to a claim |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/ReceiptsCoordinator.swift:276,297 |  | decide | - |
| PLT-281 | notifications (in-app) | NotificationCenter AppMessage.reloadReceiptScreen reloads the expenses list |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/Repository/ReceiptsRepositoryClient.Live.swift:491-501 |  | decide | - |
| PLT-282 | orientation | Camera scanner locked to portrait |  | Modules/EmployeeExpenses/Sources/EmployeeExpenses/Wescan/CameraViewController.swift:228-230 |  | decide | - |
| PLT-283 | permissions | Speech recognition / microphone for voice-to-text in the assistant prompt bar |  | Modules/EmployeeAppCoreInterface/Sources/EmployeeAppCoreInterface/Services/SpeechRecognizerService.swift:13-38; Modules/EmployeeChatBot/Sources/EmployeeChatBot/View/PromptBar.swift:30-67 |  | decide | - |
| PLT-284 | storage/security | Realm encryption key in the keychain (generic password, AfterFirstUnlock, optional access group) |  | EmployeeServices/EmployeeCore/Sources/EmployeeCore/Services/CryptoService/CryptoService.swift:21-110; EmployeeServices/EmployeeCore/Sources/EmployeeCore/Dependencies/CoreDependencyFactory.swift:16-21 |  | decide | - |
| PLT-285 | app group | Shared container for the shared/per-user Realm files and shared UserDefaults (used by extensions) |  | Modules/EmployeeAppCoreInterface/Sources/EmployeeAppCoreInterface/SharedContainer/SharedContainer.swift:11-17 |  | decide | - |
| PLT-286 | storage | Versioned encrypted Realm schema with migrations; the DB file is deleted when it cannot be opened |  | EmployeeServices/EmployeeDatabase/Sources/EmployeeDatabase/RealmService.swift:64-128; EmployeeServices/EmployeeDatabase/Sources/EmployeeDatabase/DatabaseConstants.swift:84 |  | decide | - |
| PLT-287 | storage | UserDefaults preference keys (receipt hint, company selector, review prompt timing, survey dont-show-again, submit-for-… |  | Modules/EmployeeAppCoreInterface/Sources/EmployeeAppCoreInterface/Preferences/UserPreferencesKeys.swift:3-22 |  | decide | - |
| PLT-288 | connectivity | Network reachability monitor shared as the in-memory 'isConnected' state |  | Modules/EmployeeAppCoreInterface/Sources/EmployeeAppCoreInterface/NetworkMonitor/NetworkMonitorReducer.swift:24-60 |  | decide | - |
| PLT-289 | photos | Save photo to the photo library (interface only) |  | Modules/EmployeeAppCoreInterface/Sources/EmployeeAppCoreInterface/Photos/PhotoLibrary.swift:10-12 |  | decide | - |
| PLT-290 | appearance | User-selectable appearance (light/dark) manager interface |  | Modules/EmployeeAppCoreInterface/Sources/EmployeeAppCoreInterface/Appearance/AppearanceManager.swift:12-23 |  | decide | - |
| PLT-291 | navigation | Coordinator presenters (push, modal, sheet, tab bar, window) and URLHandler for opening external URLs |  | Modules/EmployeeAppCoreInterface/Sources/EmployeeAppCoreInterface/Coordinator/Coordinator.swift; Modules/EmployeeAppCoreInterface/Sources/EmployeeAppCoreInterface/URLHandler/URLHandler.swift:10-12 |  | decide | - |
| PLT-292 | clipboard | Copy to system pasteboard via PasteboardHandler TCA dependency (UIPasteboard.general) |  | Modules/EmployeeUIComponents/Sources/EmployeeUIComponents/PasteboardHandler.Dependencies.swift:5-22 |  | decide | - |
| PLT-293 | analytics | Free-text AnalyticsService.log breadcrumbs in form cells and item selector (e.g. 'Date cell tapped', 'Flight duration s… |  | Modules/EmployeeUIComponents/Sources/EmployeeUIComponents/FormCells/FormDateTableViewCell.swift:119-147 |  | decide | - |
| PLT-294 | permissions | Microphone and speech-recognition usage descriptions for voice input to the employee agent |  | Employee/Info.plist:50-57 |  | decide | - |
| PLT-295 | in-app browser | SFSafariView / openURLInApp modifier opens web links inside the app with SFSafariViewController (used by the Calendar c… |  | Modules/EmployeeUIComponents/Sources/EmployeeUIComponents/SwiftUI/SFSafariView/SafariViewControllerViewModifier.swift:30-51 |  | decide | - |
| PLT-296 | push notifications | New payslip push opens payslip detail modal |  | Employee/PushNotifications/Events/NewPayslipNotificationPayload.swift:29; Employee/Payslips/Coordinator/ShowPayslipCoordinator.swift:36-77 |  | decide | - |
| PLT-297 | push notifications | Year-end report push opens report modal |  | Employee/PushNotifications/Events/YearEndNotificationPayload.swift:29; Employee/Payslips/Coordinator/ShowEndYearCoordinator.swift:62 |  | decide | - |
| PLT-298 | document preview | QuickLook preview of payslip / export / year-end PDFs |  | Modules/PayslipsFeature/Sources/PayslipFeature/Features/Main/MainPayslipView.swift:401; Modules/PayslipsFeature/Sources/PayslipFeature/Features/PayslipDetail/PayslipDetailView.swift:77; Modules/Paysl… |  | decide | - |
| PLT-299 | app review | App rating prompt triggered after viewing a payslip |  | Modules/PayslipsFeature/Sources/PayslipFeature/Features/AppRating/AppRatingFeature.swift:24-40; Employee/Payslips/Service/AppRatingService.RatingService.swift:13-17 |  | decide | - |
| PLT-300 | in-app survey | Survicate survey after leaving payslip detail when no review prompt is shown |  | Modules/PayslipsFeature/Sources/PayslipFeature/Features/Main/MainPayslipFeature.swift:301-305; Modules/PayslipsFeature/Sources/PayslipFeature/Features/Main/PayslipDetail/MainPayslipDetailFeature.swif… |  | decide | - |
| PLT-301 | app lifecycle | Payslips reset and reload when app enters foreground |  | Employee/Payslips/Coordinator/PayslipsListCoordinator.swift:101-102 |  | decide | - |
| PLT-302 | connectivity | Network monitor drives offline overlay and disables year-end PDF |  | Modules/PayslipsFeature/Sources/PayslipFeature/Features/Main/MainPayslipView.swift:451-456; Modules/PayslipsFeature/Sources/PayslipFeature/Features/YearEndReport/YearEndReportDetailView.swift:36 |  | decide | - |
| PLT-303 | entry point | Start-page payslip card presents payslip detail |  | Employee/StartPage/Cards/DetailProviders/PayslipCardDetailsProvider.swift:86 |  | decide | - |
| PLT-304 | navigation | Personal Information pushed from Start page |  | Employee/StartPage/StartPageViewController.swift:834-836 |  | decide | - |
| PLT-305 | navigation | Personal Information presented modally from User Profile |  | Employee/Accounts/Feature/UserProfile/UserProfileCoordinator.swift:118-125 |  | decide | - |
| PLT-306 | navigation | Interactive pop / sheet dismiss blocked when unsaved changes (UIGestureRecognizerDelegate, UIAdaptivePresentationContro… |  | Modules/PersonalInformation/Sources/PersonalInformation/Coordinator/PersonalInformationCoordinator.swift:106-133 |  | decide | - |
| PLT-307 | feature flag | changeBankAccount company feature access gates bank account editing |  | Modules/PersonalInformation/Sources/PersonalInformation/UserPersonalInformationToUIModelMapper.swift:37 |  | decide | - |
| PLT-308 | analytics | Snowplow event names Save changes success / failed / polling timeout |  | Modules/SnowplowAnalytics/Sources/SnowplowAnalytics/Events/Events.swift:386-390 |  | decide | - |
| PLT-309 | push notification | New inbox message push opens the inbox coordinator |  | Employee/PushNotifications/Events/NewInboxMessageNotificationPayload.swift:30-34 |  | decide | - |
| PLT-310 | remote config | LaunchDarkly feature flags with an anonymous 'me-ios' context (app_version, os_version, os_name); the mobile key comes… |  | Modules/FeatureKit/Sources/FeatureKit/Core/RemoteConfigClient/RemoteConfigClient.LaunchDarkly.swift:66-86 |  | decide | - |
| PLT-311 | secure storage | Third-party SDK keys (LaunchDarkly, Firebase, GoogleMaps, GooglePlaces, Survicate) are fetched from the server and cach… |  | EmployeeServices/ThirdPartyKeys/Sources/ThirdPartyKeys/Service/ThirdPartyKeysService.Live.swift:3-36; EmployeeServices/ThirdPartyKeys/Sources/ThirdPartyKeys/Storage/ThirdPartyKeysStore.swift:11-43 (G… |  | decide | - |
| PLT-312 | secure storage | User session, logged-in users and the per-user current company context are persisted in SecureStorage |  | EmployeeServices/UserService/Sources/UserService/Service/UserService.swift:98-99,254-256,329-331 |  | decide | - |
| PLT-313 | maps | Google Maps / Places provider (map view, path geometry, place autocomplete) used by mileage |  | Modules/GoogleMapsProvider/Sources/GoogleMapsProvider/GoogleMapsProviderRegistration.swift:13-17 |  | decide | - |
| PLT-314 | analytics | Snowplow tracker with structured, unstructured and timing events and custom contexts (meal_count, sequence) |  | Modules/SnowplowAnalytics/Sources/SnowplowAnalytics/Events/Events.swift:13-148; Modules/SnowplowAnalytics/Sources/SnowplowAnalytics/Service/SnowplowService.swift |  | decide | - |
| PLT-315 | app lifecycle | Remote-control forced or suggested update gate at launch, which replaces window.rootViewController |  | Modules/RemoteControl/Sources/RemoteControl/UI/AppUpdateCoordinator.swift:33-53; Employee/MainCoordinator/MainCoordinator.swift:75-81 |  | decide | - |
| PLT-316 | reachability | NetworkMonitorReducer in the inbox reloads when connectivity returns |  | Modules/InboxMessages/Sources/InboxMessages/InboxMessagesFeature.swift:156-157 |  | decide | - |
| PLT-317 | permissions | RECORD_AUDIO runtime permission for voice input in the calendar assistant chat |  |  | absence/src/main/java/com/visma/employee/calendar/calendar_bot/presentation/chat/CalendarBotChatScreen.kt:121-127 | decide | - |
| PLT-318 | speech | Speech-to-text voice input handler feeding the chat input bar |  |  | absence/src/main/java/com/visma/employee/calendar/calendar_bot/presentation/chat/CalendarBotChatViewModel.kt:106-130 | decide | - |
| PLT-319 | navigation | Navigation3 NavKey entries for absence feed, event selection, add/edit event, details, summary, calendar bot chat and l… |  |  | absence/src/main/java/com/visma/employee/navigation/entries/AbsenceEntries.kt:107-190 | decide | - |
| PLT-320 | surveys | Survicate NPS survey trigger after registration save and time confirmation |  |  | absence/src/main/java/com/visma/employee/absence/add_event/AddEventViewModel.kt:287-299 | decide | - |
| PLT-321 | gestures | Drag-to-select date range and swipe month navigation on calendar grid |  |  | absence/src/main/java/com/visma/employee/absence/feed/calendar_view/components/calendar/CalendarView.kt:186-210 | decide | - |
| PLT-322 | camera | CameraX receipt scanner with ML object detection and auto-crop |  |  | app/src/main/java/com/visma/employee/camera/CameraCoordinator.kt:97-160 | decide | - |
| PLT-323 | file picker | ACTION_GET_CONTENT chooser for image/PDF |  |  | app/src/main/java/com/visma/employee/camera/CameraCoordinator.kt:199-214 | decide | - |
| PLT-324 | store | Google Play In-App Review flow |  |  | app/src/main/java/com/visma/employee/core/analytics/AppReviewManagerImpl.kt:24-58 | decide | - |
| PLT-325 | remote config | RemoteControl config force/suggested update gate |  |  | absence/src/main/java/com/visma/employee/absence/data/important_info/ImportantInfoServiceImpl.kt:37-78 | decide | - |
| PLT-326 | survey | Survicate NPS trigger on leaving balances |  |  | absence/src/main/java/com/visma/employee/absence/summary/AbsenceSummaryViewModel.kt:72-74 | decide | - |
| PLT-327 | external link | Calendar bot feedback opens Google Form in browser |  |  | absence/src/main/java/com/visma/employee/calendar/calendar_bot/presentation/learn_more/CalendarBotLearnMoreViewModel.kt:62-70 | decide | - |
| PLT-328 | navigation | Navigation3 absence entries (feed, selection, summary, details, bot chat/learn more, add/edit) |  |  | absence/src/main/java/com/visma/employee/navigation/entries/AbsenceEntries.kt:107-198 | decide | - |
| PLT-329 | connectivity | Auto reload balances on connection restored |  |  | absence/src/main/java/com/visma/employee/absence/summary/AbsenceSummaryViewModel.kt:50-60 | decide | - |
| PLT-330 | push | Notification channels and channel groups created at startup |  |  | app/src/main/java/com/visma/employee/home/NotificationHandler.kt:22-35 | decide | - |
| PLT-331 | push | Notification tap router (account/company switch + redirectTo deep link) |  |  | app/src/main/java/com/visma/employee/home/NotificationHandler.kt:37-90 | decide | - |
| PLT-332 | permissions | POST_NOTIFICATIONS runtime request on Android 13+ with snackbar to settings on denial |  |  | app/src/main/java/com/visma/employee/home/MainActivity.kt:203-215,748-759 | decide | - |
| PLT-333 | deep link | Gated root deep-link handler (lock/welcome deferral) |  |  | app/src/main/java/com/visma/employee/home/MainActivity.kt:572-614 | decide | - |
| PLT-334 | auth | OAuth auth-callback intent capture and login re-host |  |  | app/src/main/java/com/visma/employee/home/MainActivity.kt:256-259,616-636,761-782 | decide | - |
| PLT-335 | share extension | ACTION_SEND share target handling |  |  | app/src/main/java/com/visma/employee/home/MainActivity.kt:465-570 | decide | - |
| PLT-336 | security | App lock shown on resume when locked; timestamp on pause |  |  | app/src/main/java/com/visma/employee/home/MainActivity.kt:317-335 | decide | - |
| PLT-337 | startup | Splash screen with remote update gate and push device registration + analytics init |  |  | app/src/main/java/com/visma/employee/home/MainActivity.kt:217-221,337-459 | decide | - |
| PLT-338 | storage | Corrupted storage event clears auth data |  |  | app/src/main/java/com/visma/employee/home/MainActivity.kt:338-345 | decide | - |
| PLT-339 | security | App lock with biometrics / device credential / PIN after 180 s in background |  |  | app/src/main/java/com/visma/employee/navigation/entries/LockEntries.kt:111-140; app/src/main/java/com/visma/employee/core/SecurityServiceImpl.kt:61-78 | decide | - |
| PLT-340 | security | Automatic security-type migration on lock (upgrade PIN to biometrics, downgrade when device lock removed) |  |  | app/src/main/java/com/visma/employee/core/SecurityMigrationHandlerImpl.kt:15-55 | decide | - |
| PLT-341 | security | Screenshot allow/block preference |  |  | app/src/main/java/com/visma/employee/core/SecurityServiceImpl.kt:53-59 | decide | - |
| PLT-342 | background | WorkManager with HiltWorkerFactory configured in Application |  |  | app/src/main/java/com/visma/employee/Application.kt:41-45 | decide | - |
| PLT-343 | storage | DataStore-to-Room migration at app start |  |  | app/src/main/java/com/visma/employee/Application.kt:34 | decide | - |
| PLT-344 | remote config | RemoteConfigService closed on terminate |  |  | app/src/main/java/com/visma/employee/Application.kt:22-50 | decide | - |
| PLT-345 | camera | Camera permission request and ML prominent-object detection for receipts |  |  | app/src/main/java/com/visma/employee/navigation/entries/CameraEntry.kt:140-165 | decide | - |
| PLT-346 | share | Inbound share (shareUri) routed to receipt camera flow with employer picker |  |  | app/src/main/java/com/visma/employee/navigation/entries/CameraEntry.kt:263-271; app/src/main/java/com/visma/employee/home/dialogs/MainActivityDialogs.kt:41-51 | decide | - |
| PLT-347 | auth | OAuth auth-callback consumption on login screen |  |  | app/src/main/java/com/visma/employee/navigation/entries/LoginEntries.kt:123-129 | decide | - |
| PLT-348 | system | Clipboard copy of colleague details |  |  | app/src/main/java/com/visma/employee/navigation/entries/DottieEntries.kt:109-113 | decide | - |
| PLT-349 | system | Vibration on wrong PIN |  |  | app/src/main/java/com/visma/employee/navigation/entries/LockEntries.kt:146-150 | decide | - |
| PLT-350 | navigation | Navigation3 NavKeys for all app destinations |  |  | app/src/main/java/com/visma/employee/navigation/keys/AppNavKeys.kt:11-71 | decide | - |
| PLT-351 | push | DefaultFirebaseMessagingService (FCM messages and token refresh) |  |  | app/src/main/java/com/visma/employee/core/notification/DefaultFirebaseMessagingService.kt:23-75 | decide | - |
| PLT-352 | deep link | https app links /app/* (autoVerify) on static.mobileemployee(.stag).visma.net |  |  | app/src/main/AndroidManifest.xml:87-97 | decide | - |
| PLT-353 | deep link | OAuth callback https /auth/callback (autoVerify) and vismame://auth/callback |  |  | app/src/main/java/com/visma/employee/navigation/RootDeepLinks.kt:161-170 | decide | - |
| PLT-354 | share extension | ACTION_SEND intent filter for images and PDFs |  |  | app/src/main/AndroidManifest.xml:99-105 | decide | - |
| PLT-355 | biometrics | BiometricPrompt lock and setup (BIOMETRIC_STRONG / DEVICE_CREDENTIAL) |  |  | app/src/main/java/com/visma/employee/navigation/RootHostBiometricActions.kt:13-81 | decide | - |
| PLT-356 | security | Lock re-push policy and screenshot blocking (FLAG_SECURE) |  |  | app/src/main/java/com/visma/employee/navigation/LockRepushPolicy.kt:11-18 | decide | - |
| PLT-357 | camera/ML | ML Kit prominent-object detection for the receipt camera |  |  | app/src/main/java/com/visma/employee/camera/objectdetection/ProminentObjectProcessor.kt:18-40 | decide | - |
| PLT-358 | storage | Room api_keys.db with an encrypted keys column |  |  | core/src/main/java/com/visma/employee/core/storage/persistance/apikey/ApiKeyDatabase.kt:10-38 | decide | - |
| PLT-359 | file sharing | FileProvider for opening reports and exported payslips |  |  | app/src/main/java/com/visma/employee/navigation/RootHostFileActions.kt:90-138 | decide | - |
| PLT-360 | browser | Chrome Custom Tabs for Visma Connect login |  |  | app/src/main/java/com/visma/employee/navigation/RootHostFileActions.kt:29-45 | decide | - |
| PLT-361 | in-app review | AppReviewManager review prompt after payslip views |  |  | app/src/main/java/com/visma/employee/navigation/RootHostActionsFactory.kt:78-81 | decide | - |
| PLT-362 | security | Screenshot blocking via FLAG_SECURE unless allowed by security service or debug/testing |  |  | core/src/main/java/com/visma/employee/core/BaseActivity.kt:100-107 | decide | - |
| PLT-363 | auth | Forced logout relaunch on corrupted storage, unauthorized user, no-features user, or token failure |  |  | core/src/main/java/com/visma/employee/core/BaseActivity.kt:120-166 | decide | - |
| PLT-364 | i18n | Per-app language applied via LanguageContextWrapper in attachBaseContext |  |  | core/src/main/java/com/visma/employee/core/BaseActivity.kt:83-98 | decide | - |
| PLT-365 | storage | AndroidKeyStore AES key (alias constant) for encrypting stored strings (EncryptedStringConverter) |  |  | core/src/main/java/com/visma/employee/core/storage/crypto/Crypto.kt:12-40 | decide | - |
| PLT-366 | notifications | Notification channel groups/channels mapped to event ids; default channel DEFAULT_CHANNEL |  |  | core/src/main/java/com/visma/employee/core/notification/channels/ChannelGroupDescription.kt:11-20 | decide | - |
| PLT-367 | review | Google Play in-app review flow |  |  | app/src/main/java/com/visma/employee/core/analytics/AppReviewManagerImpl.kt:23-64 | decide | - |
| PLT-368 | speech | On-device SpeechRecognizer voice input |  |  | core/src/main/java/com/visma/employee/core/employee_assistant/data/SpeechRecognitionHelperImpl.kt:68-96 | decide | - |
| PLT-369 | files | FileProvider + ACTION_VIEW chooser for file preview |  |  | core/src/main/java/com/visma/employee/core/PdfUtils.kt:22-44 | decide | - |
| PLT-370 | navigation | Activity-level bottom modal sheet events (add/delete expense, account manager, calendar day details, highlight feature… |  |  | core/src/main/java/com/visma/employee/core/compose_activity_bottom_modal_sheet/ComposeActivityBottomModalSheetEvent.kt:9-51 | decide | - |
| PLT-371 | push | FCM device registration and unregistration with retry |  |  | core/src/main/java/com/visma/employee/core/notification/RetryingSubscriptionService.kt:15-65 | decide | - |
| PLT-372 | push | Notification channels: Salary group (payslip, year-end, receipt sync) and Other |  |  | core/src/main/java/com/visma/employee/core/notification/ChannelConfigurationsProvider.kt:18-108 | decide | - |
| PLT-373 | permissions | Runtime permission helper that opens app and notification settings |  |  | core/src/main/java/com/visma/employee/camera/helpers/PermissionHelper.kt:17-52 | decide | - |
| PLT-374 | security | App lock by biometrics, device credential or PIN, 180 s timeout, screenshot flag |  |  | core/src/main/java/com/visma/employee/core/settings/SecurityService.kt:10-25 | decide | - |
| PLT-375 | analytics | Snowplow tracker with lifecycle, screen-view, exception and install autotracking |  |  | core/src/main/java/com/visma/employee/core/analytics/snowplow/SnowplowLogger.kt:57-85 | decide | - |
| PLT-376 | remote config | LaunchDarkly feature flags keyed by a remotely fetched key |  |  | core/src/main/java/com/visma/employee/core/remote/RemoteConfigServiceImpl.kt:32-113 | decide | - |
| PLT-377 | remote keys | Third-party keys (Survicate, LaunchDarkly, GooglePlaces) fetched and cached from the backend |  |  | core/src/main/java/com/visma/employee/core/remotekeys/RemoteKeysRepositoryImpl.kt:25-72 | decide | - |
| PLT-378 | storage | Room CacheDatabase (receipts, attachments, currencies, mileage, templates, preferences) with a DataStore-to-Room migrat… |  |  | core/src/main/java/com/visma/employee/core/storage/migration/DataStoreToRoomMigration.kt | decide | - |
| PLT-379 | storage | FileProvider paths for sharing files |  |  | core/src/main/java/com/visma/employee/core/storage/FileProviderPaths.kt | decide | - |
| PLT-380 | permissions | RECORD_AUDIO runtime permission request with rationale and open-settings fallback for voice input |  |  | core/src/main/java/com/visma/employee/core/employee_assistant/presentation/util/voice_input/VoiceInputPermissionHandlers.kt:34-52 | decide | - |
| PLT-381 | lifecycle | Speech recognizer torn down on pause or dispose |  |  | core/src/main/java/com/visma/employee/core/employee_assistant/presentation/util/voice_input/VoiceInputLifecycleEffect.kt:9-26 | decide | - |
| PLT-382 | storage | Room UserDatabase with user accounts, app and user preferences, mileage preferences, highlight dismissals and frequentl… |  |  | core/src/main/java/com/visma/employee/core/storage/persistance/user/UserDatabase.kt:18-169 | decide | - |
| PLT-383 | file-cache | Dottie document download cache: sanitized file names in cacheDir, cleared on screen load, deleted after preview |  |  | dottie/src/main/java/com/visma/employee/dottie/data/DottieServiceImpl.kt:128-145 | decide | - |
| PLT-384 | clipboard | Copy profile field values to the clipboard |  |  | dottie/src/main/java/com/visma/employee/dottie/presentation/employee_info/form/ClipboardCopier.kt:7-9 | decide | - |
| PLT-385 | navigation | Back handler blocks leaving the profile with unsaved changes and shows a discard dialog |  |  | dottie/src/main/java/com/visma/employee/dottie/presentation/employee_info/components/EmployeeInfoScreen.kt:74 | decide | - |
| PLT-386 | app-update | UpdateInfoState model: suggested, mandatory and OS updates (the logic lives outside this shard) |  |  | core/src/main/java/com/visma/employee/core/data/update/UpdateInfoState.kt:6-10 | decide | - |
| PLT-387 | network | HATEOAS POST and GET by URL plus Dottie notifications and new-count; used by the app-module inbox and home badge, outsi… |  |  | dottie/src/main/java/com/visma/employee/dottie/data/DottieServiceImpl.kt:169-214 | decide | - |
| PLT-388 | camera | Camera capture with runtime CAMERA permission for the profile photo |  |  | dottie/src/main/java/com/visma/employee/dottie/presentation/image/rememberImagePickerLaunchers.kt:40-118 | decide | - |
| PLT-389 | media picker | Photo picker (PickVisualMedia ImageOnly) |  |  | dottie/src/main/java/com/visma/employee/dottie/presentation/image/rememberImagePickerLaunchers.kt:35 | decide | - |
| PLT-390 | push | FCM device unregister on sign-out |  |  | dottie/src/main/java/com/visma/employee/dottie/presentation/user_menu/UserMenuViewModel.kt:125-133 | decide | - |
| PLT-391 | offline | Mileage saved to a local offline draft when there is no network |  |  | expense/src/main/java/com/visma/employee/expense/api/MileagesServiceImpl.kt:191-198 | decide | - |
| PLT-392 | config | Google Maps API key read from manifest meta-data (com.google.android.geo.API_KEY) |  |  | expense/src/main/java/com/visma/employee/expense/api/Constants.kt:8 | decide | - |
| PLT-393 | background task | WorkManager-driven offline draft sync observed by inbox (SyncManagerImpl.draftsState) |  |  | expense/src/main/java/com/visma/employee/expense/inbox/compose/ExpenseDraftsScreen.kt:583-648 | decide | - |
| PLT-394 | navigation | Navigation3 NavDisplay internal mileage back stack (MileageHomeKey, MileageMapKey, MileageDestinationKey, MileageMapDes… |  |  | expense/src/main/java/com/visma/employee/expense/mileage/compose/MileageContent.kt:199-305 | decide | - |
| PLT-395 | permissions | Location permission settings opened from map destination picker |  |  | expense/src/main/java/com/visma/employee/expense/mileage/compose/MileageContent.kt:300 | decide | - |
| PLT-396 | window | Soft input mode switched per mileage screen (adjust resize/pan) |  |  | expense/src/main/java/com/visma/employee/expense/mileage/compose/MileageContent.kt:211-229 | decide | - |
| PLT-397 | connectivity | ConnectionManager offline banner and offline-disabled actions |  |  | expense/src/main/java/com/visma/employee/expense/inbox/compose/ExpenseDraftsScreen.kt:163-165 | decide | - |
| PLT-398 | camera | Add receipt opens camera (onOpenCamera) when templates cached |  |  | expense/src/main/java/com/visma/employee/expense/inbox/compose/ExpenseDraftsScreen.kt:758-767 | decide | - |
| PLT-399 | storage | Receipt attachment saved to the public Downloads folder via MediaStore |  |  | expense/src/main/java/com/visma/employee/expense/inbox/details/ExpenseDraftDetailsViewModel.kt:1643-1671 | decide | - |
| PLT-400 | camera | Camera opened to add a receipt attachment |  |  | expense/src/main/java/com/visma/employee/expense/inbox/details/DraftDetailsCoordinator.kt:459-461 | decide | - |
| PLT-401 | survey | Survicate NPS survey triggered after a receipt is saved |  |  | expense/src/main/java/com/visma/employee/expense/inbox/details/ExpenseDraftDetailsViewModel.kt:1738-1740 | decide | - |
| PLT-402 | connectivity | Claim details reload when the connection comes back; offline banner on the receipt screen |  |  | expense/src/main/java/com/visma/employee/expense/details/ExpenseRowsViewModel.kt:270-280 | decide | - |
| PLT-403 | offline | Receipt draft saved offline when upsert fails with UnknownHostException |  |  | expense/src/main/java/com/visma/employee/expense/inbox/data/ExpenseDraftsServiceImpl.kt:95-100 | decide | - |
| PLT-404 | share extension | Camera/share-to-app mode: saving shows a 'receipt saved' dialog and then leaves share mode |  |  | expense/src/main/java/com/visma/employee/expense/inbox/details/DraftDetailsCoordinator.kt:271-286 | decide | - |
| PLT-405 | navigation | Navigation3 keys ExpenseDraftDetailsKey, CostUnitSelectionKey and ProjectAccountingSelectionKey |  |  | expense/src/main/java/com/visma/employee/expense/inbox/details/DraftDetailsCoordinator.kt:323-454 | decide | - |
| PLT-406 | permissions | ACCESS_FINE_LOCATION runtime request for current location in mileage map |  |  | expense/src/main/java/com/visma/employee/expense/destination/screens/MileageMapDestinationScreen.kt:112-130 | decide | - |
| PLT-407 | maps | Google Maps map picker and Places autocomplete for mileage destinations |  |  | expense/src/main/java/com/visma/employee/expense/destination/screens/MileageMapDestinationScreen.kt:333-450 | decide | - |
| PLT-408 | storage | Room cache of recent mileage locations (max 4) |  |  | expense/src/main/java/com/visma/employee/expense/viewmodel/destination/CachingRepository.kt:14-125 | decide | - |
| PLT-409 | navigation | Navigation3 entry provider for expense destinations (inbox, claim selection, rows, cost unit, project, draft details, c… |  |  | expense/src/main/java/com/visma/employee/navigation/entries/ExpenseEntries.kt:103-389 | decide | - |
| PLT-410 | dead code | Unused DirectionsApi GET api/directions/json (takes a key query param; no implementation found) |  |  | expense/src/main/java/com/visma/employee/expense/api/directions/DirectionsApi.kt:8-17 | decide | - |
| PLT-411 | maps | Google Maps compose map with route polylines and full-screen mode |  |  | expense/src/main/java/com/visma/employee/expense/compose/map/Components.kt:65-110 | decide | - |
| PLT-412 | maps | Google Places SDK set up with a remote-provided API key (new Places API) |  |  | expense/src/main/java/com/visma/employee/expense/autocomplete/places/PlacesInitializerImpl.kt:10-12 | decide | - |
| PLT-413 | navigation | Navigation3 NavKeys for expense inbox, claims, draft details and mileage |  |  | expense/src/main/java/com/visma/employee/navigation/keys/ExpenseNavKeys.kt:6-45 | decide | - |
| PLT-414 | camera | Camera claim and attachment results passed between screens through ExpenseResultHolder |  |  | expense/src/main/java/com/visma/employee/navigation/result/ExpenseResultHolder.kt:266-280 | decide | - |
| PLT-415 | storage | SharedPreferences key for the send-for-approval 'don't show again' choice |  |  | expense/src/main/java/com/visma/employee/expense/preferences/SendApprovalPreferences.kt:15 | decide | - |
| PLT-416 | persistence | Room cache of frequently used hotels (table frequently_used_hotels) |  |  | core/src/main/java/com/visma/employee/core/storage/persistance/user/FrequentlyUsedHotelDbModel.kt:7-37 | decide | - |
| PLT-417 | persistence | Per-user 'don't show send-for-approval confirmation again' preference |  |  | core/src/main/java/com/visma/employee/core/storage/preferences/UserPreferencesRepositoryImpl.kt:118 | decide | - |
| PLT-418 | background task | ExpenseUploadWorker (Hilt CoroutineWorker) uploads offline drafts via WorkManager OneTimeWorkRequest |  |  | expense/src/main/java/com/visma/employee/core/storage/sync/SyncManagerImpl.kt:61-68 | decide | - |
| PLT-419 | location | Current GPS location lookup for mileage waypoint, GPS-disabled handling |  |  | expense/src/main/java/com/visma/employee/expense/viewmodel/DestinationViewModel.kt:232-256 | decide | - |
| PLT-420 | maps | Google Places client and directions route manager for mileage |  |  | expense/src/main/java/com/visma/employee/expense/viewmodel/ExpenseMileageRouteViewModel.kt:17-34 | decide | - |
| PLT-421 | auth | Visma Connect OAuth2 PKCE browser sign-in with redirect callback handling (code/state verification) |  |  | login/src/main/java/com/visma/employee/login/LoginViewModel.kt:154-285 | decide | - |
| PLT-422 | auth | Token revocation on account removal or logout (connect/revocation) |  |  | login/src/main/java/com/visma/employee/account_manager/data/AccountManagerServiceImpl.kt:207-258 | decide | - |
| PLT-423 | background task | Coroutine refresh of tokens for inactive saved accounts at startup |  |  | login/src/main/java/com/visma/employee/account_manager/data/AccountManagerServiceImpl.kt:60-63,127-175 | decide | - |
| PLT-424 | persistence | Room user-accounts table (UserDatabaseDao) behind AccountManagerDbService |  |  | login/src/main/java/com/visma/employee/account_manager/data/database/AccountManagerDbServiceImpl.kt:15-30 | decide | - |
| PLT-425 | persistence | Per-user preference cleanup (user, mileage, highlight dismissal, app prefs, appearance cache) |  |  | login/src/main/java/com/visma/employee/account_manager/domain/PreferencesCleanupService.kt:11-35 | decide | - |
| PLT-426 | navigation | Navigation3 NavKeys and entries for FAQ (FaqKey with PreselectedFaqContext, FaqContextKey, FaqSendFeedbackKey) |  |  | faq/src/main/java/com/visma/employee/navigation/keys/FaqNavKeys.kt:7-21 | decide | - |
| PLT-427 | navigation | Navigation3 NavKeys for Payslip (SalaryFeedKey, PayslipDetailsKey with payslipId/companyId, ReportDetailsKey, PayslipBo… |  |  | payslip/src/main/java/com/visma/employee/navigation/keys/PayslipNavKeys.kt:6-24 | decide | - |
| PLT-428 | in-app review | Review request when the salary feed resumes |  |  | payslip/src/main/java/com/visma/employee/navigation/entries/PayslipEntries.kt:58-63 | decide | - |
| PLT-429 | voice input | Speech-recognition voice input with runtime microphone permission in the payslip bot |  |  | payslip/src/main/java/com/visma/employee/payslip/payslip_bot/presentation/chat_screen/PayslipBotChatScreen.kt:156-178 | decide | - |
| PLT-430 | clipboard | Copy a bot message to the clipboard |  |  | payslip/src/main/java/com/visma/employee/payslip/payslip_bot/presentation/chat_screen/PayslipBotChatScreen.kt:256 | decide | - |
| PLT-431 | file handling | Open downloaded payslip, report or exported PDFs in an external app, with a 'no suitable app' fallback |  |  | payslip/src/main/java/com/visma/employee/navigation/entries/PayslipEntries.kt:146-152 | decide | - |
| PLT-432 | analytics | Snowplow structured events via AnalyticsLogger (FAQ, Payslip, Auth categories) |  |  | core/src/main/java/com/visma/employee/core/analytics/AnalyticsEvents.kt:107-115,287-302 | decide | - |
| PLT-433 | ml | On-device expense-type prediction model trained when a draft is saved |  |  | expense/src/main/java/com/visma/employee/expense/inbox/claimselection/viewmodels/ClaimSummaryViewModel.kt:450-463 | decide | - |
