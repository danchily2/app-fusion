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
| PLT-058 | calendar | Device calendar write access (react-native-calendar-events) to create or remove the birthday and anniversary calendars;… | src/hooks/useSyncCalendar.ts:41-77; ios/vmm/Info.plist:61-64; android/app/src/main/AndroidManifest.xml:11-12 |  |  | decide | - |
| PLT-059 | feature flag | Calendar sync gated on dev flag VMM-7635-calendar-sync-dev-flag (isCalendarSyncEnabled), mentioned only in a comment | src/screens/common/SettingsScreen/SettingsScreen.tsx:404-405 |  |  | decide | - |
| PLT-060 | navigation | EmployeeCalendarScreen registered in the HRM and Approval stacks, with CalendarOptionsMenu as headerRight; opened from… | src/configs/navConfig/hrm/HrmNavConfig.tsx:139-147; src/configs/navConfig/approval/ApprovalNavConfig.tsx:113-121; src/components/hrm/HrmEmployeeDetailAccordeon/HrmEmployeeDetailAccordion.tsx:272 |  |  | decide | - |
| PLT-061 | persistence | Calendar display preferences and calendarSync live in the settings slice, which is on the redux-persist whitelist | src/configs/reduxState.ts:107-108; src/reducers/common/settingsReducer/settingsReducer.ts:73,111 |  |  | decide | - |
| PLT-062 | navigation | Root coordinator actions showCalendarFeed(initialDate) / showCalendarMonthView / appWillEnterForeground routed into the… |  | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarCoordinator.swift:77-94 |  | decide | - |
| PLT-063 | lifecycle | Month grid reloads the current month when the app returns to the foreground |  | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarContainerViewController.swift:444-448 |  | decide | - |
| PLT-064 | in-app messaging | NotificationCenter AppMessage.reloadStartPage posted after a registration or time confirmation |  | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AddAbsenceCoordinator/AddAbsenceCoordinator.swift:240 |  | decide | - |
| PLT-065 | third-party SDK | Survicate survey (requestSurveyShowingThankYouToast) after saving a registration |  | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrationCoordinator/CreateAbsenceRegistrationCoordinator.swift:86 |  | decide | - |
| PLT-066 | local storage | UserDefaults-backed calendar preferences (view mode, filter toggles, balances control options) |  | Modules/EmployeeAppCoreInterface/Sources/EmployeeAppCoreInterface/Preferences/UserPreferencesKeys.swift:13-21 |  | decide | - |
| PLT-067 | permissions | Microphone and speech recognition for agent voice input (SFSpeechRecognizer) |  | Employee/Info.plist:50-57; Employee/AppDependencies.swift:1182-1184 |  | decide | - |
| PLT-068 | deep link / system URL | Opens the app Settings page when speech permission is denied |  | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotView.swift:40-44 |  | decide | - |
| PLT-069 | external URL | Agent feedback Google Form URL, hard-coded |  | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/LearnMore/LearnMoreConstants.swift:12 |  | decide | - |
| PLT-070 | app messaging | Closing the agent posts AppMessage.reloadStartPage and AppMessage.resetCalendar |  | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Coordinator/CalendarChatBotCoordinator.swift:79-82 |  | decide | - |
| PLT-071 | lifecycle | Calendar list resets after the app returns from background (AppMessage.resetCalendarBackground) |  | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarViewController.swift:138-139 |  | decide | - |
| PLT-072 | navigation entry | Employee Agent opened from a calendar navigation bar button, presented modally |  | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarContainerViewController.swift:125-135,417-421 |  | decide | - |
| PLT-073 | dead code | EditAbsenceRegistrationView and EditAbsenceRegistrationFeature are declared but never instantiated or scoped (not in Ca… |  | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/EditAbsenceRegistration/EditAbsenceRegistrationView.swift:43 |  | decide | - |
| PLT-074 | dead code | AbsenceRegistrationEventsFeature logs nothing itself. Only the parent CalendarEventsFeature logs calendarBotEditRegistr… |  | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Events/CalendarEventsFeature.swift:43-51 |  | decide | - |
| PLT-075 | dead code | GetAbsenceRegistration, GetDimensionValues and TimeService.getTimeTemplates are never called by production code (only m… |  | EmployeeServices/Calendar/Sources/Calendar/Request/Absence/GetAbsenceRegistration.swift:19; EmployeeServices/Calendar/Sources/Calendar/Request/Absence/GetDimensionValues.swift:20; EmployeeServices/Ca… |  | decide | - |
| PLT-076 | networking | HATEOAS-driven endpoints: update/delete/checkout/confirm/dimension URLs come from server links, not constants |  | EmployeeServices/Calendar/Sources/Calendar/Service/TimeService.swift:113-126 |  | decide | - |
| PLT-077 | analytics | Snowplow structured calendar events built in SnowplowEventFactory |  | Modules/SnowplowAnalytics/Sources/SnowplowAnalytics/Events/Factory/SnowplowEventFactory.swift:38-59 |  | decide | - |
| PLT-078 | dead code | CalendarViewModelPayslip.getCellInstance asserts; migrated to PayslipsFeature |  | Employee/CalendarLeftover/CalendarViewModelPayslip.swift:33-36 |  | decide | - |
