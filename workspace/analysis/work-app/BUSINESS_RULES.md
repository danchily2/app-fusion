# Business rules: work-app

153 rules mined from the source apps, generated 2026-09-28T19:32:43+00:00. Each card cites the code it comes from (`file:line` under `legacy/<app>`), and a second agent checked every citation. 7 candidates were rejected by that check.

| Id | Rule | App | Capability | Category | Priority | Confidence | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RULE-001 | Definite-time registrations combine date and clock time in UTC | me-ios | CAP-012 | Calculation | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:613-657 |
| RULE-002 | Balances cover the whole calendar month | me-ios | CAP-010 | Calculation | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/BalancesOverview/UseCase/LoadBalancesOverviewUseCase.repository.swift:22-28 |
| RULE-003 | Days on or before the confirmation date are marked confirmed or approved | me-ios | CAP-020 | Calculation | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Utils/CalendarViewUtils.swift:107-121 |
| RULE-004 | List calendar groups by UTC month, newest first, without duplicates | me-ios | CAP-002 | Calculation | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarUtils.swift:142-193 |
| RULE-005 | Each team member gets one yearly all-day birthday event with a reminder the day before | vmm | CAP-007 | Calculation | P1 | Medium | src/hooks/useSyncCalendar.ts:95-147 |
| RULE-006 | Sickness summaries default to today's date in UTC | vmm | CAP-009 | Calculation | P1 | Medium | src/services/apiCalendar/apiCalendar.ts:327-336 |
| RULE-007 | Balance group total shown as expandable row | me-ios | CAP-010 | Calculation | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/BalancesOverview/Mapper/BalancesOverview.Mapper.swift:116-139 |
| RULE-008 | Confirmed-time entry is added to a month even when the feed had none | me-ios | CAP-020 | Calculation | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Repository/CalendarFeedRepositoryAdapter.swift:81-114 |
| RULE-009 | Weekend is always Saturday and Sunday | me-ios | CAP-005 | Calculation | P2 | Medium | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Utils/CalendarViewUtils.swift:103-104 |
| RULE-010 | Month grid starts on the locale's first weekday and has just enough rows | me-ios | CAP-001 | Calculation | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Utils/CalendarViewUtils.swift:22-58 |
| RULE-011 | Multi-day absences are detected in GMT | me-ios | CAP-002 | Calculation | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarUtils.swift:46-90 |
| RULE-012 | Hour-based absence duration falls back to end minus start | me-ios | CAP-002 | Calculation | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarUtils.swift:98-106 |
| RULE-013 | Confirmed-time row joins the list only inside the loaded date range | me-ios | CAP-020 | Calculation | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/ViewControllerModels/CalendarFeedViewModel.swift:180-265 |
| RULE-014 | Each team member gets one yearly all-day work anniversary event with a reminder the day before | vmm | CAP-007 | Calculation | P2 | High | src/hooks/useSyncCalendar.ts:152-226 |
| RULE-015 | Claims status filter applies to both past and future pages, split at today | me-ios | CAP-028 | Validation | P1 | High | Employee/CalendarLeftover/ClaimsCalendarViewModel.swift:150-170 |
| RULE-016 | Duplicate claims are removed by claim id | me-ios | CAP-028 | Validation | P1 | High | Employee/CalendarLeftover/ClaimsCalendarViewModel.swift:240-272 |
| RULE-017 | Registration templates, time templates and dimension values fail when the server status is Error | me-ios | CAP-012 | Validation | P1 | High | EmployeeServices/Calendar/Sources/Calendar/Service/AbsenceRegistrationService.swift:41-52 |
| RULE-018 | Calendar feed keeps only Absence-type items | me-ios | CAP-001 | Validation | P1 | High | EmployeeServices/Calendar/Sources/Calendar/Service/CalendarService.swift:28-41 |
| RULE-019 | Empty option values are sent as null | me-ios | CAP-012 | Validation | P1 | High | EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/AbsenceField.swift:263-270 |
| RULE-020 | Absence from and to dates accept date-only or date-time | me-ios | CAP-012 | Validation | P1 | Medium | EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/AbsenceType.swift:96-110 |
| RULE-021 | Confirm-time date validations: the rule name says when the date fails | me-ios | CAP-020 | Validation | P1 | Medium | EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/ConfirmTimeTemplate.swift:176-259 |
| RULE-022 | Confirm-time: first failing validation at a given level | me-ios | CAP-020 | Validation | P1 | High | EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/ConfirmTimeTemplate.swift:274-281 |
| RULE-023 | Medical certificate percentage 0-100 in 5% steps, default 100% | me-ios | CAP-012 | Validation | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/Cells/CertificatePercentageTableViewCellViewModel.swift:20-60 |
| RULE-024 | Hours/percent number entry capped at 999 | me-ios | CAP-012 | Validation | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/Cells/NumberFieldTableViewCell.swift:65-76 |
| RULE-025 | Comment text is cleared when the user starts editing | me-ios | CAP-015 | Validation | P1 | Medium | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/Cells/TextTableViewCell.swift:49-66 |
| RULE-026 | Unrecognised date in template falls back to today | me-ios | CAP-012 | Validation | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/SectionViewModels/FormFieldCellViewModels/DateFieldCellViewModel.swift:38-47 |
| RULE-027 | To-date follows from-date and cannot be earlier | me-ios | CAP-012 | Validation | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/SectionViewModels/FormFieldCellViewModels/DateFieldCellViewModel.swift:49-76 (plus ViewModel/AbsenceRegistrationViewModel.swift:565… |
| RULE-028 | Definite-time adds required start and end time fields prefilled from the dates | me-ios | CAP-012 | Validation | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:372-407 |
| RULE-029 | Save is disabled until every required field has a value | me-ios | CAP-012 | Validation | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:428-431 (applied to the button at Modules/CalendarFeature/Sources/CalendarFeature/Abse… |
| RULE-030 | Certificate fields stripped on submit when no certificate | me-ios | CAP-012 | Validation | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:672-682 |
| RULE-031 | Child field defaults to the first child | me-ios | CAP-012 | Validation | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:888-896 |
| RULE-032 | Medical certificate section applies only to sickness and is cleared when switched off | me-ios | CAP-012 | Validation | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:938-991 |
| RULE-033 | Tapping the selected dimension value clears it | me-ios | CAP-013 | Validation | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/DimensionValueItemSelectorViewModel.swift:301-329 |
| RULE-034 | Confirming time from the day sheet: errors block, warnings need user approval | me-ios | CAP-020 | Validation | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/UseCase/ConfirmTimeUseCase.timeService.swift:31-59 |
| RULE-035 | Sick leave missing a required medical certificate date cannot be confirmed directly | me-ios | CAP-024 | Validation | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Extensions/AbsenceType+MedicalCertificate.swift:14-52 |
| RULE-036 | Employee Agent confirms the timesheet without checking template validations | me-ios | CAP-022 | Validation | P1 | Medium | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Message/QuickResponseAction/QuickResponseAction.confirmPredictedConfirmTimeEvent.swift:33-50 |
| RULE-037 | Device calendar permission is required before syncing | vmm | CAP-007 | Validation | P1 | High | src/hooks/useSyncCalendar.ts:40-61 |
| RULE-038 | Employee calendar requires the employee's company tenant | vmm | CAP-001 | Validation | P1 | High | src/screens/EmployeeCalendarScreen/EmployeeCalendarScreen.tsx:116-119 |
| RULE-039 | Workshift company setting defaults to time mode, and shifts without a parseable start are dropped | me-ios | CAP-001 | Validation | P2 | High | EmployeeServices/Calendar/Sources/Calendar/Mapper/WorkshiftMapper.swift:6-28 (plus Service/CalendarService.swift:87 for the default) |
| RULE-040 | Dimension (cost unit) search sends the search term as query 'q' | me-ios | CAP-013 | Validation | P2 | High | EmployeeServices/Calendar/Sources/Calendar/Service/AbsenceRegistrationService.swift:136-139 (helper: EmployeeServices/EmployeeAPIInterface/Sources/EmployeeAPIInterface/Model/ResponseModel.swift:130-1… |
| RULE-041 | Special days: unparseable dates dropped, public-holiday flag ignored | me-ios | CAP-001 | Validation | P2 | High | EmployeeServices/Calendar/Sources/Calendar/Service/CalendarService.swift:91-101 |
| RULE-042 | Employee Agent rejects an empty prompt | me-ios | CAP-021 | Validation | P2 | High | EmployeeServices/Calendar/Sources/Calendar/Service/EmployeeCalendarBotService.swift:26-42 |
| RULE-043 | Checkout template date range is set only when the link supports it | me-ios | CAP-019 | Validation | P2 | High | EmployeeServices/Calendar/Sources/Calendar/Service/TimeService.swift:148-167 |
| RULE-044 | Template lookup by event type short code | me-ios | CAP-006 | Validation | P2 | High | EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/CalendarTemplates.swift:36-42 |
| RULE-045 | Month/year picker spans 20 years back and forward | me-ios | CAP-001 | Validation | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/Components/CalendarMonthYearNavigationFeature.swift:29-97 |
| RULE-046 | Blank or overlapping agent prompts are ignored | me-ios | CAP-021 | Validation | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:231-245 |
| RULE-047 | Month/year picker offers 2 years back and 5 years forward | vmm | CAP-001 | Validation | P2 | Medium | src/screens/EmployeeCalendarScreen/components/CalendarMonthYearPicker/CalendarMonthYearPicker.tsx:20-101 |
| RULE-048 | Claims tab and its filter bar appear only when the claims data source is enabled | me-ios | CAP-028 | Eligibility | P1 | Medium | Employee/CalendarLeftover/ClaimsCalendarViewModel.swift:33-72 |
| RULE-049 | Payslips list filtered by selected employers (tenants) | me-ios | CAP-029 | Eligibility | P1 | High | Employee/Payslips/PayslipsCalendarViewModel.swift:62-81 |
| RULE-050 | Start-page absence cards: which vacation and parental leave items become cards | me-ios | CAP-017 | Eligibility | P1 | High | Employee/StartPage/Tasks/GetCalendarItemsTask.swift:19-20,47-76 |
| RULE-051 | Absences are edited or deleted only through server-provided links | me-ios | CAP-015 | Eligibility | P1 | High | EmployeeServices/Calendar/Sources/Calendar/Service/AbsenceRegistrationService.swift:82-103 |
| RULE-052 | Deleting a check-in uses the server's link and HTTP method | me-ios | CAP-019 | Eligibility | P1 | High | EmployeeServices/Calendar/Sources/Calendar/Service/TimeService.swift:204-229 |
| RULE-053 | Time confirmation and its template: HTTP 403 means the feature is off | me-ios | CAP-020 | Eligibility | P1 | High | EmployeeServices/Calendar/Sources/Calendar/Service/TimeService.swift:28-77 |
| RULE-054 | Editing a checkout should require both update and delete links (unused check) | me-ios | CAP-019 | Eligibility | P1 | Medium | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrationCoordinator/EditCheckoutRegistrationCoordinator.swift:57-68 |
| RULE-055 | Check-in edit and delete need server links | me-ios | CAP-019 | Eligibility | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/CalendarEventEditing/CheckinEventEditor.swift:26-41 |
| RULE-056 | Absence types reload only with calendar write permission | me-ios | CAP-012 | Eligibility | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:272-291 |
| RULE-057 | Changing check-out dates requires time permissions | me-ios | CAP-019 | Eligibility | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:293-314 |
| RULE-058 | Input type selector only shown when more than one option exists | me-ios | CAP-012 | Eligibility | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:857-886 (hiding applied at 589-591; field toggling at 409-424) |
| RULE-059 | Confirm-time entry offered only with confirm-time permission | me-ios | CAP-020 | Eligibility | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/RegisterAbsenceTypeItemSelectorViewModel.swift:44-61 |
| RULE-060 | Edit button shown only when server provides edit links; edit needs write permission | me-ios | CAP-015 | Eligibility | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Absence/AbsenceViewTableViewController.swift:98-146 (plus 266-268 for the showEditButton gate) |
| RULE-061 | Tapping a calendar day: register on empty day, details otherwise | me-ios | CAP-006 | Eligibility | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/CalendarGridFeature.swift:210-231 |
| RULE-062 | Long-press and drag registers a period | me-ios | CAP-006 | Eligibility | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/CalendarGridFeature.swift:238-273 |
| RULE-063 | Roster shifts cannot be opened as registrations | me-ios | CAP-004 | Eligibility | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/CalendarGridFeature.swift:318-328 |
| RULE-064 | Day detail sheet: which actions appear and how events are listed | me-ios | CAP-004 | Eligibility | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/DayDetailView.swift:18-133 |
| RULE-065 | Confirm-time button needs the confirmTime permission | me-ios | CAP-020 | Eligibility | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarViewController.swift:508-524 |
| RULE-066 | Register-event button needs a write permission | me-ios | CAP-006 | Eligibility | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarViewController.swift:526-542 |
| RULE-067 | Calendar is available only to users with an absence or time permission | me-ios | CAP-001 | Eligibility | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Extensions/ArrayExtensions.swift:13-17 |
| RULE-068 | Calendar tab titled 'Claims' for expense-only users | me-ios | CAP-001 | Eligibility | P2 | Medium | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarContainerViewController.swift:325-370 |
| RULE-069 | Only days of the displayed month show events and respond to taps | me-ios | CAP-004 | Eligibility | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/Components/CalendarWeekDaysRow.swift:36-45 |
| RULE-070 | Month cells show only absence and roster events, filtered by type | me-ios | CAP-005 | Eligibility | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Utils/CalendarViewUtils.swift:138-147 |
| RULE-071 | Agent offers Edit only when exactly one registration was predicted | me-ios | CAP-024 | Eligibility | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:287-325 |
| RULE-072 | Absences created in the chat can be opened only if they have a retrieval link | me-ios | CAP-025 | Eligibility | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:592-604 |
| RULE-073 | Calendar hides entry types the user filtered out | vmm | CAP-005 | Eligibility | P2 | High | src/screens/EmployeeCalendarScreen/EmployeeCalendarScreen.tsx:137-149 |
| RULE-074 | Empty (draft) claims are fetched once per reset, filtered by the selected statuses | me-ios | CAP-028 | Lifecycle | P1 | High | Employee/CalendarLeftover/ClaimsCalendarViewModel.swift:91-106 |
| RULE-075 | Check-in and check-out send the device's local time with time zone | me-ios | CAP-018 | Lifecycle | P1 | High | EmployeeServices/Calendar/Sources/Calendar/Service/TimeService.swift:169-202 (plus 113-126 for status mapping; timestamp format at EmployeeServices/EmployeeCore/Sources/EmployeeCore/CoreFormatStyle.s… |
| RULE-076 | Delete is available only in edit mode and must be confirmed | me-ios | CAP-016 | Lifecycle | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrationTableViewController.swift:423-429 |
| RULE-077 | Absence save response lifecycle: Success, ValidationError, Error, ConfirmationRequired | me-ios | CAP-012 | Lifecycle | P1 | Medium | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/CalendarEventEditing/AbsenceEventEditor.swift:34-90 |
| RULE-078 | Only input type, comment and sickness percentage survive a type change | me-ios | CAP-012 | Lifecycle | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:223-248 |
| RULE-079 | Month grid: confirmed and approved timesheet entries are built separately | me-ios | CAP-020 | Lifecycle | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Model/Domain/CalendarGridItem.swift:114-164 |
| RULE-080 | Month grid knows only approved, rejected and pending request statuses | me-ios | CAP-004 | Lifecycle | P1 | Medium | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Model/Domain/CalendarGridItem.swift:95-95 (enum at 46-51) |
| RULE-081 | List view: timesheet counts as approved when the approval date is on or after the confirmation date | me-ios | CAP-020 | Lifecycle | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarUtils.swift:92-96 |
| RULE-082 | Agent answer order: registrations first, then timesheet confirmation, then balances | me-ios | CAP-021 | Lifecycle | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:275-285 |
| RULE-083 | How the agent reports registration results and failures | me-ios | CAP-021 | Lifecycle | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:419-494 |
| RULE-084 | A future absence needs explicit confirmation before it is registered again | me-ios | CAP-021 | Lifecycle | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:538-564 |
| RULE-085 | Turning sync on saves the setting only if the sync run succeeds; turning it off always saves Off | vmm | CAP-007 | Lifecycle | P1 | High | src/components/common/CalendarSyncPicker/CalendarSyncPicker.tsx:37-56 (with src/hooks/useSyncCalendar.ts:47-60,255) |
| RULE-086 | Turning sync on deletes events that already exist for an employee instead of keeping them | vmm | CAP-007 | Lifecycle | P1 | Medium | src/hooks/useSyncCalendar.ts:139-146 |
| RULE-087 | Turning sync off removes both Manager App calendars and clears the synced list | vmm | CAP-007 | Lifecycle | P1 | High | src/hooks/useSyncCalendar.ts:229-239 |
| RULE-088 | Synced events live in two dedicated device calendars | vmm | CAP-007 | Lifecycle | P1 | High | src/hooks/useSyncCalendar.ts:63-93 and 152-169 |
| RULE-089 | Balance group categories: vacation, attendance, sickness, sick child | me-ios | CAP-011 | Lifecycle | P2 | High | EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/Balances/EmployeeBalanceGroup.swift:14-22 |
| RULE-090 | A deleted absence is shown as struck through in the earlier success message | me-ios | CAP-025 | Lifecycle | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:567-589 |
| RULE-091 | Switching from list to month view keeps the month last seen in the list | vmm | CAP-003 | Lifecycle | P2 | High | src/screens/EmployeeCalendarScreen/EmployeeCalendarScreen.tsx:151-158 |
| RULE-092 | Only pending requests show a status tag in the day sheet | vmm | CAP-004 | Lifecycle | P2 | High | src/screens/EmployeeCalendarScreen/components/EmployeeCalendarDayDetail.tsx:76-102 |
| RULE-093 | Server-requested confirmation before saving (future registration) | me-ios | CAP-012 | Policy | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/CalendarEventEditing/AbsenceEventEditor.swift:34-90 |
| RULE-094 | Month data loading stops after 50 page requests or at the first error | me-ios | CAP-001 | Policy | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Repository/CalendarFeedRepositoryAdapter.swift:59-79 |
| RULE-095 | Offline calendar hides the list and blocks registration and confirmation | me-ios | CAP-002 | Policy | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarViewController.swift:913-967 |
| RULE-096 | Closing the Employee Agent refreshes the start page and calendar | me-ios | CAP-021 | Policy | P1 | Medium | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Coordinator/CalendarChatBotCoordinator.swift:71-82 |
| RULE-097 | Agent registers each predicted absence separately and in parallel | me-ios | CAP-021 | Policy | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/UseCase/RegisterAbsenceEventsUseCase.swift:51-72 |
| RULE-098 | Several agent events needing attention are sent back for one-by-one registration | me-ios | CAP-021 | Policy | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:361-376 |
| RULE-099 | Confirm actions are locked while a submission is running | me-ios | CAP-022 | Policy | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:744-753 |
| RULE-100 | Team absence feed returns 'no absences' on any failure | vmm | CAP-008 | Policy | P1 | High | src/services/queryApi/queryEndpointsCalendar/queryEndpointsCalendar.ts:35-67 |
| RULE-101 | Employee calendar month grid shows mock data instead of the employee's real calendar | vmm | CAP-001 | Policy | P1 | High | src/services/queryApi/queryEndpointsCalendar/queryEndpointsCalendar.ts:71-75 |
| RULE-102 | Start-page absence cards look from 7 days back to 1 month ahead | me-ios | CAP-017 | Policy | P2 | High | Employee/StartPage/Tasks/GetCalendarItemsTask.swift:19-20 |
| RULE-103 | Satisfaction survey offered after save, not after delete | me-ios | CAP-015 | Policy | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrationCoordinator/EditAbsenceRegistrationCoordinator.swift:122-130 |
| RULE-104 | Type picker error messages | me-ios | CAP-012 | Policy | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/RegisterAbsenceTypeItemSelectorViewModel.swift:84-108 |
| RULE-105 | Balances load once and can be retried | me-ios | CAP-010 | Policy | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/BalancesOverview/Features/BalancesOverviewFeature.swift:60-105 |
| RULE-106 | Balances toggle choice is remembered per section | me-ios | CAP-010 | Policy | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/BalancesOverview/UseCase/ResolveBalancesControlsUseCase.preferences.swift:6-16 |
| RULE-107 | Month view reloads when the app returns to foreground | me-ios | CAP-001 | Policy | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarContainerViewController.swift:444-448 |
| RULE-108 | Calendar view mode remembered | me-ios | CAP-003 | Policy | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarContainerViewController.swift:70-76 (restore; default at 52; save at 164-165) |
| RULE-109 | Calendar filters are saved on the device | me-ios | CAP-005 | Policy | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/CalendarFilterPreferences.swift:4-63 |
| RULE-110 | Calendar display filter defaults | me-ios | CAP-005 | Policy | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/Components/CalendarViewFilterFeature.swift:89-179 |
| RULE-111 | Returning from background jumps the calendar back to today | me-ios | CAP-002 | Policy | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarViewController.swift:482-488 |
| RULE-112 | Calendar load errors are combined into one alert; some errors are silent | me-ios | CAP-002 | Policy | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarViewController.swift:715-747 |
| RULE-113 | Example prompts load once per session and fail silently | me-ios | CAP-026 | Policy | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/LearnMore/LearnMoreReducer.swift:37-57 |
| RULE-114 | Agent feedback goes to an external Google Form | me-ios | CAP-027 | Policy | P2 | Medium | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/LearnMore/LearnMoreReducer.swift:58-59 |
| RULE-115 | Sync result message is shown 2 seconds later, only for On and Off | vmm | CAP-007 | Policy | P2 | Medium | src/hooks/useSyncCalendar.ts:240-254 |
| RULE-116 | Calendar list stops loading more months after a page fails | vmm | CAP-002 | Policy | P2 | High | src/screens/EmployeeCalendarScreen/EmployeeCalendarScreen.tsx:207-212 |
| RULE-117 | Period aggregation always sends a 'today' parameter, empty when not given | vmm | CAP-009 | Policy | P2 | Low | src/services/apiCalendar/apiCalendar.ts:269-306 |
| RULE-118 | End-of-year balance request defaults to full expansion with balance sums | vmm | CAP-009 | Policy | P2 | High | src/services/apiCalendar/apiCalendar.ts:86-100 |
| RULE-119 | Calendar list scrolls back at most 24 months, newest first | vmm | CAP-002 | Policy | P2 | High | src/services/queryApi/queryEndpointsCalendar/queryEndpointsCalendar.ts:147-167 (cap constant at line 17) |
| RULE-120 | Input-type display: hours rounded to whole numbers, percent divided by 100, quantity as 'Name: value' | me-ios | CAP-024 | Formatting | P1 | High | EmployeeServices/CalendarInterface/Sources/CalendarInterface/FormatStyles/AbsenceType/AbsenceTypeFormatStyle.swift:448-511 (helpers at 422-445) |
| RULE-121 | Registration dates shown and picked in the absence time zone | me-ios | CAP-012 | Formatting | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/Cells/DateTableViewCell.swift:45-113 |
| RULE-122 | Hours/percent values converted between local and JSON decimal format | me-ios | CAP-012 | Formatting | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/SectionViewModels/FormFieldCellViewModels/NumberFieldCellViewModel.swift:27-39 (formatters: EmployeeServices/EmployeeCore/Sources/E… |
| RULE-123 | Balances summary hours and amounts formatting | me-ios | CAP-010 | Formatting | P1 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/BalancesOverview/Mapper/BalancesOverviewUIModel.Mapper.swift:148-173 |
| RULE-124 | Claim list row: date as day plus upper-case short month, amount with 2 decimals, status text | me-ios | CAP-028 | Formatting | P2 | Medium | Employee/CalendarLeftover/CalendarViewModelClaim.swift:62-87 |
| RULE-125 | Expense claims list is grouped by year, newest first, with undated claims in their own section | me-ios | CAP-028 | Formatting | P2 | High | Employee/CalendarLeftover/ClaimsCalendarViewModel.swift:240-259 |
| RULE-126 | Several cards of the same vacation kind are grouped | me-ios | CAP-017 | Formatting | P2 | Medium | Employee/StartPage/Tasks/GetCalendarItemsTask.swift:28-45 |
| RULE-127 | Balance durations shown as hours and minutes, zero units hidden | me-ios | CAP-010 | Formatting | P2 | High | EmployeeServices/CalendarInterface/Sources/CalendarInterface/DomainModel/Balances/BalanceDurationFormatStyle.swift:3-18 |
| RULE-128 | Registration summary text (chatbot style): name, date range, input type | me-ios | CAP-024 | Formatting | P2 | High | EmployeeServices/CalendarInterface/Sources/CalendarInterface/FormatStyles/AbsenceType/AbsenceTypeFormatStyle.swift:144-168 |
| RULE-129 | Changing the number-input locale on the input-type style has no effect | me-ios | CAP-024 | Formatting | P2 | High | EmployeeServices/CalendarInterface/Sources/CalendarInterface/FormatStyles/AbsenceType/AbsenceTypeFormatStyle.swift:269-273 |
| RULE-130 | Dimension option display as 'id - name' | me-ios | CAP-013 | Formatting | P2 | High | EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/AbsenceField.swift:280-287 |
| RULE-131 | Absence type colours | me-ios | CAP-001 | Formatting | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrationUtils.swift:146-174 |
| RULE-132 | Dimension value shown as 'id - name' | me-ios | CAP-013 | Formatting | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/SectionViewModels/DimensionFieldsSectionViewModel.swift:36-54,83-87 |
| RULE-133 | Required text fields labelled '(required)' in the placeholder | me-ios | CAP-012 | Formatting | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/SectionViewModels/FormFieldCellViewModels/StringFieldCellViewModel.swift:51-59 |
| RULE-134 | Remaining vacation days message | me-ios | CAP-012 | Formatting | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:433-448 |
| RULE-135 | Absence type search is case-insensitive across groups | me-ios | CAP-012 | Formatting | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceTypeSelectorViewModel.swift:19-31 |
| RULE-136 | Absence details hide empty and full-day fields and show approval status | me-ios | CAP-014 | Formatting | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Absence/AbsenceViewTableViewController.swift:232-263 |
| RULE-137 | Definite-time and hours shown in the details | me-ios | CAP-014 | Formatting | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Absence/AbsenceViewTableViewController.swift:418-426 |
| RULE-138 | Time confirmation marker on calendar days | me-ios | CAP-001 | Formatting | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/Components/CalendarDayView.swift:103-115 |
| RULE-139 | Day sheet title shows the numeric date in the calendar's locale | me-ios | CAP-004 | Formatting | P2 | Medium | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/DayDetailFeature.swift:30-33 |
| RULE-140 | Approval status colour and emphasis | me-ios | CAP-002 | Formatting | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarUtils.swift:298-316 |
| RULE-141 | Approval status labels | me-ios | CAP-002 | Formatting | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarUtils.swift:322-346 |
| RULE-142 | Absence description text depends on the input type | me-ios | CAP-002 | Formatting | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarUtils.swift:37-106 |
| RULE-143 | Month headings and the jump-to-date picker use GMT | me-ios | CAP-002 | Formatting | P2 | High | Modules/CalendarFeature/Sources/CalendarFeature/Calendar/ViewControllerModels/SectionsSingleSourceCalendarViewModel.swift:119-130 |
| RULE-144 | Register-time options: confirm-time first, absence types in a fixed order | me-ios | CAP-012 | Formatting | P2 | Medium | Modules/CalendarFeature/Sources/CalendarFeature/Service/AbsenceService.swift:80-127 |
| RULE-145 | Synced event titles read 'label Lastname Firstname' with forced capitalisation | vmm | CAP-007 | Formatting | P2 | High | src/hooks/useSyncCalendar.ts:106-108 |
| RULE-146 | Week numbers are ISO weeks shown on the Monday cell | vmm | CAP-005 | Formatting | P2 | High | src/screens/EmployeeCalendarScreen/EmployeeCalendarScreen.tsx:276-277 |
| RULE-147 | Month grid weeks start on Monday and move one month per arrow tap | vmm | CAP-001 | Formatting | P2 | High | src/screens/EmployeeCalendarScreen/EmployeeCalendarScreen.tsx:428-430 (arrows: 199-205, wired at 230-235) |
| RULE-148 | Entry type decides icon and colour | vmm | CAP-001 | Formatting | P2 | High | src/screens/EmployeeCalendarScreen/calendarEventStyles.ts:17-69 |
| RULE-149 | List view subtitle shows hours, quantity or time range | vmm | CAP-002 | Formatting | P2 | High | src/screens/EmployeeCalendarScreen/components/EmployeeCalendarAgendaView/EmployeeCalendarAgendaView.tsx:38-50 |
| RULE-150 | Calendar date headings are capitalised in the app language | vmm | CAP-002 | Formatting | P2 | High | src/screens/EmployeeCalendarScreen/components/EmployeeCalendarAgendaView/EmployeeCalendarAgendaView.tsx:62-77 |
| RULE-151 | A day cell shows at most two entries plus a '+N' count | vmm | CAP-001 | Formatting | P2 | High | src/screens/EmployeeCalendarScreen/components/EmployeeCalendarDayCell.tsx:39-105 |
| RULE-152 | Day sheet time label: 'Full day' or a 24-hour time range | vmm | CAP-004 | Formatting | P2 | High | src/screens/EmployeeCalendarScreen/components/EmployeeCalendarDayDetail.tsx:38-91 |
| RULE-153 | Hide-weekends grid shows Monday to Friday rows only | vmm | CAP-005 | Formatting | P2 | Medium | src/screens/EmployeeCalendarScreen/components/WeekdayCalendarGrid/WeekdayCalendarGrid.tsx:33-81 (tap blocking: src/screens/EmployeeCalendarScreen/components/EmployeeCalendarDayCell.tsx:54-61) |

## Cross-app conflicts

The same decision is made differently by two apps. A person picks the behavior the new app keeps (`/app-fusion:fuse-review`).

| Question | Capability | Rules | Difference |
| --- | --- | --- | --- |
| CAP-001:RULE-045+RULE-047 | CAP-001 | RULE-047, RULE-045 | The year ranges differ. vmm offers 2 years back and 5 forward (September 2026 gives 2024-2031). me-ios offers 20 years each way (March 2025 gives 2005-2045). |
| CAP-001:RULE-010+RULE-147 | CAP-001 | RULE-147, RULE-010 | The first day of the week differs. vmm always starts weeks on Monday (firstDay=1), whatever the locale. me-ios uses the locale's first weekday, so a Sunday-first locale starts the grid on Sunday. |
| CAP-001:RULE-045+RULE-147 | CAP-001 | RULE-147, RULE-045 | Changing month works differently. In vmm swiping is turned off (enableSwipeMonths=false), so the user can only change month with the arrow buttons. In me-ios a swipe of at least 50 pt changes the month. |
| CAP-001:RULE-038+RULE-067 | CAP-001 | RULE-038, RULE-067 | The access check differs. vmm shows the calendar only when it can find the employee's company tenant in the cached employee list; if not, it shows 'employee_calendar_load_error' and makes no permission check. me-ios requires one of addAbsence, addTime, absenceReadOnly, timeReadOnly, absenceWrite or timeWrite; an [expenseClaims]-only user gets the empty state. |
| CAP-001:RULE-018+RULE-101 | CAP-001 | RULE-101, RULE-018 | The data in the grid differs. vmm shows fixed sample entries from mockData.ts (for example 'Sickness' on 7 October 2026 and a pending 'Vacation' on 8 October) for every employee. me-ios shows the real feed and drops any item whose type is not 'Absence' (for example 'Payslip'). The vmm behaviour looks like a defect. |
| CAP-002:RULE-012+RULE-149 | CAP-002 | RULE-149, RULE-012 | How hours are shown: vmm prints the raw Hours property plus 'h' (Hours='7.5' gives '7.5h') and has no fallback. me-ios parses hours in the device locale, shows a compact duration ('7,5' gives '7 h 30 min'), and when there is no hours property it uses end minus start (09:00-11:30 gives '2 h 30 min'). |
| CAP-002:RULE-142+RULE-149 | CAP-002 | RULE-149, RULE-142 | Which properties drive the list description: vmm matches 'Hours' and 'Quantity' with exact case and has no percent case. me-ios matches 'hours', 'percent' and 'quantity' in any case, shows Percent absences as '50% <period>', formats time ranges in UTC ('08:00 - 12:00'), and gives a single-day Full Day absence no description. |
| CAP-005:RULE-110+RULE-146 | CAP-005 | RULE-146, RULE-110 | Week numbers are on by default in vmm (calendarShowWeekNumbers=true) but off by default in me-ios (showWeekNumbers=false), so a new user sees week 40 on 2026-09-28 in vmm and no week number in me-ios. |
| CAP-005:RULE-070+RULE-073 | CAP-005 | RULE-073, RULE-070 | The calendar shows different things. vmm shows every entry type that is not filtered out (attendance, absence, supplement) in the day cell and in the detail sheet. me-ios month cells show only absence and roster events and always leave out confirmed-time entries. |
| CAP-005:RULE-073+RULE-110 | CAP-005 | RULE-073, RULE-110 | The filters differ. vmm has three filters (attendance, absence, supplement). me-ios also has a roster filter (showRoster=true), treats 'unknown' as a filterable type, and has a showLabels toggle (default false). vmm has no roster filter, no 'unknown' type and no labels toggle. |
| CAP-005:RULE-070+RULE-073 | CAP-005 | RULE-073, RULE-070 | The apps may group the same entry under different filters. In me-ios an absence event can have the filterable type 'attendance', so hiding attendance hides it. In vmm the 'absence' entry type is controlled only by the Show absence filter. This needs checking: the same absence may disappear under a different toggle in each app. |
| CAP-003:RULE-091+RULE-108 | CAP-003 | RULE-091, RULE-108 | The default calendar view differs: vmm opens in 'grid' (month) view (settingsReducer.ts:119), but me-ios opens in list view (UserPreferences.calendarViewMode default .list, CalendarContainerViewController.swift:52). So a first-time user sees the month grid in vmm and the list in me-ios. |
| CAP-004:RULE-080+RULE-092 | CAP-004 | RULE-092, RULE-080 | Which request statuses get a tag in the calendar day view: vmm knows only 'none' and 'pending' and tags only pending, while me-ios also tags approved (green) and rejected (red). So an approved or rejected absence has a tag in me-ios and none in vmm. |
| CAP-004:RULE-080+RULE-092 | CAP-004 | RULE-092, RULE-080 | The colour of the pending tag: orange in vmm, blue in me-ios. |

## Calculation

### RULE-001: Definite-time registrations combine date and clock time in UTC
**App:** me-ios
**Capability:** CAP-012
**Category:** Calculation
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:613-657`
**Plain English:** When the input type is 'definite time', on submit the app merges the From/To date with the Start/End time fields into full UTC date-times before sending.
**Specification:**
  Given InputType = DefiniteTime, FromDate '2025-03-10T00:00:00', ToDate '2025-03-10T00:00:00', Start time 08:30:00, End time 12:00:00
  When  The user taps Save
  Then  FromDate is sent as '2025-03-10T08:30:00' and ToDate as '2025-03-10T12:00:00'
**Parameters:** UTC calendar, locale-invariant date-time and HH:mm:ss formatters
**Edge cases handled:** End time earlier than start time on the same day is not rejected on the client. Parsing failure of any of the four values sends empty strings.
**Suspected defect:** If any of the four values fails to parse, FromDate and ToDate are overwritten with empty strings and submitted, silently wiping the dates instead of blocking the save.
**Confidence:** High

### RULE-002: Balances cover the whole calendar month
**App:** me-ios
**Capability:** CAP-010
**Category:** Calculation
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/BalancesOverview/UseCase/LoadBalancesOverviewUseCase.repository.swift:22-28`
**Plain English:** The balances overview is requested from the first to the last day of the month being viewed.
**Specification:**
  Given The calendar shows February 2024
  When  The user opens the summary
  Then  Balances are requested for 2024-02-01 to 2024-02-29
**Parameters:** UTC calendar with device locale
**Edge cases handled:** The month is the one currently displayed in list or month view, else the current month (CalendarContainerViewController 401-408).
**Confidence:** High

### RULE-003: Days on or before the confirmation date are marked confirmed or approved
**App:** me-ios
**Capability:** CAP-020
**Category:** Calculation
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Utils/CalendarViewUtils.swift:107-121`
**Plain English:** In the month grid, a day is marked time-confirmed when it is on or before the confirmed entry's date, and time-approved when it is on or before the approved entry's date.
**Specification:**
  Given A confirmed entry dated 2026-09-15 and an approved entry dated 2026-09-10
  When  The September grid is drawn
  Then  1-15 September are marked confirmed and 1-10 September are also marked approved. 16 September has no mark.
**Parameters:** Comparison: date <= eventDate, or the same calendar day
**Confidence:** High

### RULE-004: List calendar groups by UTC month, newest first, without duplicates
**App:** me-ios
**Capability:** CAP-002
**Category:** Calculation
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarUtils.swift:142-193`
**Plain English:** List items are placed into sections by their start date's UTC year and month. An absence whose id is already in its section is skipped. Items in each section are sorted newest first, and sections are ordered newest month first (SectionsSingleSourceCalendarViewModel.swift:64-66).
**Specification:**
  Given Absence id 'A1' dated 2026-09-01T00:30+02:00 arriving twice in two pages
  When  Both pages are merged
  Then  A1 appears once, in the August 2026 section, because the start date is 2026-08-31 in UTC.
**Parameters:** Month key: getUTCYearMonth(). Items without a date go under distantPast.
**Confidence:** High

### RULE-005: Each team member gets one yearly all-day birthday event with a reminder the day before
**App:** vmm
**Capability:** CAP-007
**Category:** Calculation
**Priority:** P1
**Source:** `src/hooks/useSyncCalendar.ts:95-147`
**Plain English:** For every employee in the manager's employee list without an existing birthday event (matched by employee id stored in the event URL, looking 10 years ahead), the app creates a yearly repeating all-day event on the date of birth in the current year, with an alarm 1440 minutes (1 day) before.
**Specification:**
  Given Employee id E1 born 1990-03-15, no event with url E1 in the next 10 years, today 2026-09-28
  When  sync_all runs
  Then  An all-day yearly event starting 2026-03-15 is saved with an alarm 1 day before, and E1 is added to the synced list
**Parameters:** Lookahead 10 years; recurrence yearly, interval 1; alarm -1440 minutes; allDay true
**Suspected defect:** Start date uses moment.utc(dateOfBirth).set('year', currentYear) then UTC start of day: Feb 29 births clamp to Feb 28 permanently; UTC midnight on an all-day event may shift the day in negative-offset time zones. Also employees added later are only synced when the switch is toggled again.
**Confidence:** Medium: Is it intended that a 29 February birthday is stored on 28 February (moment clamps the date in non-leap 2026) and then repeats on 28 Feb every year, and that dates are computed in UTC, which can show the event one day early in time zones west of UTC?

### RULE-006: Sickness summaries default to today's date in UTC
**App:** vmm
**Capability:** CAP-009
**Category:** Calculation
**Priority:** P1
**Source:** `src/services/apiCalendar/apiCalendar.ts:327-336`
**Plain English:** The sick-child current-year summary (and the self-certification 12-month summary at lines 357-366) uses today's UTC date as the target date when none is given.
**Specification:**
  Given A device in Oslo (UTC+2) at 2026-09-29 01:00 local time and no target date
  When  The sick-child summary is requested
  Then  targetisodate=2026-09-28 (the previous day) is sent
**Parameters:** expand=constrain.to.range,items; details=sickness12months for both summaries
**Suspected defect:** new Date().toISOString() gives the UTC date, so between local midnight and the UTC offset the counts are for yesterday; the sick-child call reuses details=sickness12months, which looks copy-pasted.
**Confidence:** Medium: Should the target date be the user's local date? And is details=sickness12months also correct for the sick-child current-year summary?

### RULE-007: Balance group total shown as expandable row
**App:** me-ios
**Capability:** CAP-010
**Category:** Calculation
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/BalancesOverview/Mapper/BalancesOverview.Mapper.swift:116-139`
**Plain English:** When a balance group has a total, it is shown as one row with the total and unit that expands to the individual balances; without a total, balances are listed directly.
**Specification:**
  Given A vacation group total 25 days with balances 'Earned 20' and 'Transferred 5'
  When  The overview is shown
  Then  One row '25 days' expands to 'Earned 20 days' and 'Transferred 5 days'
**Edge cases handled:** The total is shown as given by the server; the app does not recompute it.
**Confidence:** High

### RULE-008: Confirmed-time entry is added to a month even when the feed had none
**App:** me-ios
**Capability:** CAP-020
**Category:** Calculation
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Repository/CalendarFeedRepositoryAdapter.swift:81-114`
**Plain English:** If the month's feed items include no confirmed-time entry, the app fetches the confirmation details and puts their entries at the front of the month's items. The grid can then mark confirmed days.
**Specification:**
  Given A September 2026 feed with 3 absences and no confirm-time entry, and confirmation details with confirmer date 2026-08-31
  When  The month grid is built
  Then  A 'Timesheet confirmed' entry dated 2026-08-31 is added to the grid items.
**Parameters:** none
**Confidence:** High

### RULE-009: Weekend is always Saturday and Sunday
**App:** me-ios
**Capability:** CAP-005
**Category:** Calculation
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Utils/CalendarViewUtils.swift:103-104`
**Plain English:** The grid treats weekday 1 (Sunday) and weekday 7 (Saturday) as weekend days in every locale. Hide-weekends removes the Saturday and Sunday column names (lines 156-161).
**Specification:**
  Given A user whose locale has a Friday-Saturday weekend
  When  The user turns on 'Hide weekends'
  Then  Saturday and Sunday are hidden. Friday stays visible.
**Parameters:** Weekend weekdays: 1 and 7 (Gregorian)
**Confidence:** Medium: Should weekends come from the company's work calendar or the locale rather than a fixed Saturday and Sunday?

### RULE-010: Month grid starts on the locale's first weekday and has just enough rows
**App:** me-ios
**Capability:** CAP-001
**Category:** Calculation
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Utils/CalendarViewUtils.swift:22-58`
**Plain English:** The grid starts on the calendar's first weekday on or before the 1st of the month. The number of weeks is the offset plus the days in the month, divided by 7 and rounded up.
**Specification:**
  Given September 2026 (1 September is a Tuesday) in a locale where weeks start on Monday
  When  The grid is built
  Then  It starts on Monday 31 August and has (1 + 30 + 6) / 7 = 5 rows, ending Sunday 4 October.
**Parameters:** Fallbacks: 6 weeks if the month interval is unknown; 30 days if the month length is unknown
**Confidence:** High

### RULE-011: Multi-day absences are detected in GMT
**App:** me-ios
**Capability:** CAP-002
**Category:** Calculation
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarUtils.swift:46-90`
**Plain English:** An absence counts as multi-day when its start and end fall on different calendar days in GMT, whatever the user's time zone.
**Specification:**
  Given An absence from 2026-09-01T23:00Z to 2026-09-02T01:00Z
  When  The app checks whether it spans several days
  Then  It counts as multi-day, and the short date period is added to its description.
**Parameters:** timeZone = .gmt
**Confidence:** High

### RULE-012: Hour-based absence duration falls back to end minus start
**App:** me-ios
**Capability:** CAP-002
**Category:** Calculation
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarUtils.swift:98-106`
**Plain English:** For hour-based absences, the duration comes from the 'hours' property, parsed as a localized number and multiplied by 3600 seconds. If the property is missing or not a number, the app uses the time between start and end. The result is formatted as a compact duration in the device locale.
**Specification:**
  Given An Hours absence with hours='7,5' in a nb-NO locale, and another with no hours property running 09:00-11:30
  When  The durations are shown
  Then  The first shows a compact 7 h 30 min. The second shows a compact 2 h 30 min.
**Parameters:** 1 hour = 3600 s; format .workshiftCompactDuration(locale: .autoupdatingCurrent)
**Confidence:** High

### RULE-013: Confirmed-time row joins the list only inside the loaded date range
**App:** me-ios
**Capability:** CAP-020
**Category:** Calculation
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/ViewControllerModels/CalendarFeedViewModel.swift:180-265`
**Plain English:** The confirmed-time row is added to the list once, when its date falls between the loaded minimum and maximum dates, or when no more pages remain in the direction that covers it.
**Specification:**
  Given Loaded range 2026-06-01..2026-09-30 and a confirmation dated 2026-09-15
  When  A page arrives
  Then  The 'Timesheet confirmed' row is added under September 2026 and is not added again later.
**Parameters:** none
**Confidence:** High

### RULE-014: Each team member gets one yearly all-day work anniversary event with a reminder the day before
**App:** vmm
**Capability:** CAP-007
**Category:** Calculation
**Priority:** P2
**Source:** `src/hooks/useSyncCalendar.ts:152-226`
**Plain English:** Same as birthdays but based on the employment date, stored in the anniversaries calendar.
**Specification:**
  Given Employee id E2 with employmentDate 2015-06-01 and no existing anniversary event
  When  sync_all runs
  Then  An all-day yearly event starting 2026-06-01 with a 1-day-before alarm is saved in 'Manager App - Anniversaries'
**Parameters:** Lookahead 10 years; recurrence yearly; alarm -1440 minutes
**Suspected defect:** Same Feb 29 / UTC start-of-day issue as birthdays.
**Confidence:** High

## Validation

### RULE-015: Claims status filter applies to both past and future pages, split at today
**App:** me-ios
**Capability:** CAP-028
**Category:** Validation
**Priority:** P1
**Source:** `Employee/CalendarLeftover/ClaimsCalendarViewModel.swift:150-170`
**Plain English:** When one or more claim statuses are selected, the past feed starts from today and the future feed from tomorrow, both limited to the selected statuses. When no status is selected, the default feed URLs are kept.
**Specification:**
  Given Today is 2026-09-28 and the user selects the 'approved' quick filter
  When  the list resets
  Then  past claims load from 2026-09-28 backwards and future claims from 2026-09-29 forwards, both with status 'approved'
**Parameters:** past anchor = today; future anchor = today + 1 day
**Edge cases handled:** An empty selection skips the URL rewrite, so all statuses are shown.
**Confidence:** High

### RULE-016: Duplicate claims are removed by claim id
**App:** me-ios
**Capability:** CAP-028
**Category:** Validation
**Priority:** P1
**Source:** `Employee/CalendarLeftover/ClaimsCalendarViewModel.swift:240-272`
**Plain English:** A claim that arrives again (for example from both the empty-claims fetch and the paged fetch) is shown once, matched by id. Claims without an id are never treated as duplicates.
**Specification:**
  Given Claim id 'C-100' has already been listed in 2026, and the next page returns 'C-100' again
  When  the page is merged
  Then  'C-100' appears only once
**Parameters:** Match key: expenseItem.data.id
**Edge cases handled:** If both ids are nil, the claims count as different, so id-less claims can repeat.
**Confidence:** High

### RULE-017: Registration templates, time templates and dimension values fail when the server status is Error
**App:** me-ios
**Capability:** CAP-012
**Category:** Validation
**Priority:** P1
**Source:** `EmployeeServices/Calendar/Sources/Calendar/Service/AbsenceRegistrationService.swift:41-52`
**Plain English:** Calendar templates are accepted only when the server status exists, is not Error, and data is present. Otherwise the server's status text is shown as a validation error, or a generic error when there is no text.
**Specification:**
  Given The templates endpoint returns status Error with description 'No employment in period'
  When  the user opens registration for 2026-10-01 to 2026-10-31
  Then  the user sees the validation error 'No employment in period'
**Parameters:** statusCode != .error and data != nil
**Edge cases handled:** A missing status object also counts as failure. getTimeTemplates (TimeService.swift:79-101) and getDimensionsValues (lines 115-134) use the same pattern.
**Confidence:** High

### RULE-018: Calendar feed keeps only Absence-type items
**App:** me-ios
**Capability:** CAP-001
**Category:** Validation
**Priority:** P1
**Source:** `EmployeeServices/Calendar/Sources/Calendar/Service/CalendarService.swift:28-41`
**Plain English:** When loading calendar items for a date range, only items of type 'Absence' are kept (this type also carries attendance and supplement item types). Any other item type is dropped. The end date defaults to today.
**Specification:**
  Given The calendar endpoint returns an 'Absence' item and an item of type 'Payslip' for September 2026
  When  getCalendarItems is called
  Then  only the Absence item is returned
**Parameters:** CalendarItemFamily discriminator 'type': Absence → CalendarItemAbsence; anything else is unknown and dropped
**Edge cases handled:** A paged feed (getCalendarItems(url:), lines 43-55) fails unless the first status is Success.
**Confidence:** High

### RULE-019: Empty option values are sent as null
**App:** me-ios
**Capability:** CAP-012
**Category:** Validation
**Priority:** P1
**Source:** `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/AbsenceField.swift:263-270`
**Plain English:** When a registration is saved, an option value left as an empty string is sent to the server as null.
**Specification:**
  Given An Hours option whose value field is ''
  When  the registration is posted
  Then  the JSON contains value: null
**Parameters:** emptyStringToNilTransformer
**Confidence:** High

### RULE-020: Absence from and to dates accept date-only or date-time
**App:** me-ios
**Capability:** CAP-012
**Category:** Validation
**Priority:** P1
**Source:** `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/AbsenceType.swift:96-110`
**Plain English:** The FromDate and ToDate fields of an absence are read as a UTC date, falling back to a UTC date-time. The summary formatter instead uses only 'yyyy-MM-ddTHH:mm:ss' in GMT.
**Specification:**
  Given FromDate value '2026-10-05'
  When  dateFrom / the summary formatter's fromDate is read
  Then  dateFrom is 2026-10-05, but the summary formatter's fromDate is nil, so no date is shown
**Parameters:** field ids FromDate, ToDate; the formatter parse lives at AbsenceTypeFormatStyle.swift:514-524
**Suspected defect:** Two different parsers for the same field: a date-only value is shown by one path and silently dropped by the other.
**Confidence:** Medium: Does the server ever send FromDate/ToDate as date-only for predicted registrations?

### RULE-021: Confirm-time date validations: the rule name says when the date fails
**App:** me-ios
**Capability:** CAP-020
**Category:** Validation
**Priority:** P1
**Source:** `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/ConfirmTimeTemplate.swift:176-259`
**Plain English:** The date chosen for confirming time is checked against server rules. GreaterThan X is valid only on or before X, GreaterThanOrEqual X only before X, LessThan X only on or after X, LessThanOrEqual X only after X. Required uses a regex.
**Specification:**
  Given The server sends a GreaterThan validation with value '2026-09-30' at level Error
  When  the user picks 2026-10-01 / 2026-09-30
  Then  2026-10-01 fails with the server's displayText, and 2026-09-30 is valid
**Parameters:** validation types RegEx/Required, Object/GreaterThan, GreaterThanOrEqual, LessThan, LessThanOrEqual; levels Error and Warning; dates in Constants.dateFormatter format
**Edge cases handled:** An unparseable date or a missing value counts as invalid. Unknown type and name pairs decode to nil and are ignored. The base validation always passes.
**Suspected defect:** The names describe the failing condition (inverted from the usual meaning). Rebuilders may implement it the other way round. Confirming time beyond the allowed date affects payroll.
**Confidence:** Medium: Does the server define 'GreaterThan X' as 'error when the date is greater than X'? The client assumes so.

### RULE-022: Confirm-time: first failing validation at a given level
**App:** me-ios
**Capability:** CAP-020
**Category:** Validation
**Priority:** P1
**Source:** `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/ConfirmTimeTemplate.swift:274-281`
**Plain English:** For the chosen date, the app finds the first validation on the 'Date' field that fails at the requested level (Error or Warning), so Error and Warning can be handled separately.
**Specification:**
  Given The Date field has a Warning LessThan '2026-09-01' and an Error GreaterThan '2026-09-30'
  When  the user picks 2026-08-15 and the Error level is checked
  Then  there is no Error failure; checking the Warning level returns the LessThan warning
**Parameters:** field id "Date" (line 34-36)
**Confidence:** High

### RULE-023: Medical certificate percentage 0-100 in 5% steps, default 100%
**App:** me-ios
**Capability:** CAP-012
**Category:** Validation
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/Cells/CertificatePercentageTableViewCellViewModel.swift:20-60`
**Plain English:** The certificate percentage stepper ranges from 0 to 100 in steps of 5, starts at 100 and is displayed with a percent sign.
**Specification:**
  Given A certificate percentage of 100
  When  The user taps minus three times
  Then  It reads '85%' and the value 85 is stored
**Parameters:** min 0, max 100, step 5, default 100
**Edge cases handled:** A stored value outside 0-100 is ignored and 100 is shown. Fractions are truncated with Int().
**Confidence:** High

### RULE-024: Hours/percent number entry capped at 999
**App:** me-ios
**Capability:** CAP-012
**Category:** Validation
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/Cells/NumberFieldTableViewCell.swift:65-76`
**Plain English:** The hours or percent entry field accepts only numeric input whose value does not exceed 999, and clears its content when the user starts editing.
**Specification:**
  Given An empty Hours field
  When  The user types '1','0','0','0'
  Then  The field shows '100'; the 4th digit is rejected because 1000 > 999
**Parameters:** max = 999; device-locale NumberFormatter
**Edge cases handled:** Percent is not capped at 100 here. Deletions are always allowed.
**Suspected defect:** The check appends the typed character to the end of the text rather than applying it at the cursor range, so edits in the middle are validated against the wrong number; also a percent above 100 (e.g. 250) is accepted client-side.
**Confidence:** High

### RULE-025: Comment text is cleared when the user starts editing
**App:** me-ios
**Capability:** CAP-015
**Category:** Validation
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/Cells/TextTableViewCell.swift:49-66`
**Plain English:** The text field is meant to clear only its placeholder when focused, but because placeholder and real text share the same colour, any existing text is cleared on focus.
**Specification:**
  Given An existing absence with comment 'Dentist 10:00'
  When  The user taps into the comment field to edit
  Then  The field is emptied; if they type 'x' the saved comment becomes 'x'
**Parameters:** placeholder detection by textColor == Gaia.Text.body
**Edge cases handled:** If the user leaves without typing, the model keeps the old value.
**Suspected defect:** Placeholder check compares against the normal text colour, so real comments are wiped on focus (data loss risk).
**Confidence:** Medium: Is clearing an existing comment on focus intended, or should only the placeholder be cleared?

### RULE-026: Unrecognised date in template falls back to today
**App:** me-ios
**Capability:** CAP-012
**Category:** Validation
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/SectionViewModels/FormFieldCellViewModels/DateFieldCellViewModel.swift:38-47`
**Plain English:** Date fields accept 'yyyy-MM-dd' or a date-time string; if neither parses, the picker shows today and an error is logged, but the stored value is not changed.
**Specification:**
  Given A template FromDate value '10/03/2025'
  When  The form is displayed
  Then  The date row shows today's date while the model still holds '10/03/2025'
**Parameters:** AbsenceRegistrationUtils.parseDate (93-101)
**Suspected defect:** Displayed date and submitted value can differ.
**Confidence:** High

### RULE-027: To-date follows from-date and cannot be earlier
**App:** me-ios
**Capability:** CAP-012
**Category:** Validation
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/SectionViewModels/FormFieldCellViewModels/DateFieldCellViewModel.swift:49-76 (plus ViewModel/AbsenceRegistrationViewModel.swift:565…`
**Plain English:** When the user picks a new from-date, the to-date is reset to the same day, its picker minimum becomes the from-date, the available absence types are reloaded for the new period and all chosen cost-unit dimension values are cleared.
**Specification:**
  Given A registration with FromDate 2025-03-10, ToDate 2025-03-14 and Project dimension '1001'
  When  The user changes FromDate to 2025-03-17
  Then  ToDate becomes 2025-03-17, dates before 2025-03-17 cannot be picked for ToDate, templates are re-fetched for 17-17 March and the Project dimension is emptied
**Parameters:** minimumDate = FromDate; reset handled in AbsenceRegistrationViewModel.updateToDateToMatchFromDate (565-578)
**Edge cases handled:** Picking the same date again does not trigger (DateTableViewCell only fires when value changes). If the new period returns zero templates, the old type list is kept.
**Confidence:** High

### RULE-028: Definite-time adds required start and end time fields prefilled from the dates
**App:** me-ios
**Capability:** CAP-012
**Category:** Validation
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:372-407`
**Plain English:** Selecting the 'definite time' input type relabels the from-date as 'Date' and adds required Start time and End time fields, prefilled from the time part of the from/to values (or the last value the user entered).
**Specification:**
  Given FromDate '2025-03-10T09:00:00' and ToDate '2025-03-10T15:00:00' and no cached times
  When  The input type DefiniteTime is shown
  Then  Start time shows 09:00 and End time 15:00, both required
**Parameters:** field ids FromTime/ToTime, required=true
**Edge cases handled:** If dates are date-only strings, parsing fails and current device time is used as default.
**Confidence:** High

### RULE-029: Save is disabled until every required field has a value
**App:** me-ios
**Capability:** CAP-012
**Category:** Validation
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:428-431 (applied to the button at Modules/CalendarFeature/Sources/CalendarFeature/Abse…`
**Plain English:** The Save button on the absence/time registration form is enabled only when no field marked required by the server template is empty.
**Specification:**
  Given A Vacation template whose fields FromDate (required, '2025-03-10') and Comment (required, empty)
  When  The form re-evaluates after any field change
  Then  Save is disabled; once Comment is 'Family trip' Save becomes enabled
**Parameters:** required flag comes from server template fieldInfo; check is value.isEmpty
**Edge cases handled:** Only top-level fieldInfo is checked; the client-added Start/End time fields and dimension sub-fields are not validated. A whitespace-only value counts as filled.
**Suspected defect:** Required dimension sub-items (Dimensions.items) are never checked, so a required cost unit can be left empty on the client.
**Confidence:** High

### RULE-030: Certificate fields stripped on submit when no certificate
**App:** me-ios
**Capability:** CAP-012
**Category:** Validation
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:672-682`
**Plain English:** When creating a registration with the medical certificate switch off, certificate date and percentage are blanked before sending.
**Specification:**
  Given A Sickness registration where the certificate percentage was set to 50 and then the switch turned off
  When  The user saves a new registration
  Then  Certificate date and percentage are sent empty
**Parameters:** hasSicknessCertificate flag
**Edge cases handled:** The same stripping is not done on update (submitUpdatedEvent), relying on the switch handler having cleared them.
**Suspected defect:** Update path does not re-clear certificate fields; values restored by the section cache could be sent on edit.
**Confidence:** High

### RULE-031: Child field defaults to the first child
**App:** me-ios
**Capability:** CAP-012
**Category:** Validation
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:888-896`
**Plain English:** For absence types with a Child field (e.g. sick child), an empty child value is preset to the first child in the list.
**Specification:**
  Given A Sick child template with children ['Emma', 'Liam'] and no selection
  When  The form is built
  Then  Child is set to 'Emma'
**Parameters:** first item of selection list
**Edge cases handled:** A user who does not notice may register for the wrong child.
**Confidence:** High

### RULE-032: Medical certificate section applies only to sickness and is cleared when switched off
**App:** me-ios
**Capability:** CAP-012
**Category:** Validation
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:938-991`
**Plain English:** For Sickness only, a 'medical certificate' switch controls the certificate date and percentage: on restores the last entered values (date defaults to the from-date, percentage to 100), off clears both.
**Specification:**
  Given A Sickness registration from 2025-03-10 with no cached certificate values
  When  The user turns the medical certificate switch on
  Then  Certificate date is 2025-03-10 and certificate percentage is 100; turning it off empties both
**Parameters:** defaultCertificatePercentage = "100"; date fallback = today
**Edge cases handled:** Ignored for any event type other than Sickness. When the switch is off only the toggle row is shown.
**Confidence:** High

### RULE-033: Tapping the selected dimension value clears it
**App:** me-ios
**Capability:** CAP-013
**Category:** Validation
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/DimensionValueItemSelectorViewModel.swift:301-329`
**Plain English:** Selecting a dimension value sets it; selecting the already-selected value deselects it and empties the dimension.
**Specification:**
  Given Project dimension currently '1001 - Internal'
  When  The user taps '1001 - Internal' again
  Then  The Project dimension becomes empty
**Parameters:** recently used values sorted by id (71-87)
**Edge cases handled:** Recently used list is sorted by id string, not by recency.
**Confidence:** High

### RULE-034: Confirming time from the day sheet: errors block, warnings need user approval
**App:** me-ios
**Capability:** CAP-020
**Category:** Validation
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/UseCase/ConfirmTimeUseCase.timeService.swift:31-59`
**Plain English:** Before confirming time up to a date, the app fetches the confirm-time template for that date. A failing validation at Error level stops the confirmation and shows its message. A failing Warning-level validation asks the user; if they press OK, the app confirms without re-checking any validation.
**Specification:**
  Given The user taps Confirm time on 2026-09-15 and the template returns a failing Warning 'You have 2 unregistered days'
  When  The user presses OK in the warning alert
  Then  The time confirmation is registered for 2026-09-15 through the template's update link (DayDetailFeature.swift:109-118). With an Error-level failure, an Error alert shows its text and nothing is registered.
**Parameters:** Validation levels: Error, then Warning. Fallback message: 'unexpectedError'. The update link rel is .update.
**Suspected defect:** If the template has no update link, registerTimeConfirmation is called with url=nil, and the app does not check for that first.
**Confidence:** High

### RULE-035: Sick leave missing a required medical certificate date cannot be confirmed directly
**App:** me-ios
**Capability:** CAP-024
**Category:** Validation
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Extensions/AbsenceType+MedicalCertificate.swift:14-52`
**Plain English:** A predicted Sickness absence is not ready to confirm when its 'Certificate.Date' field is required and empty. The user must edit it first. All other predictions are ready (EventDataType.swift:79-94).
**Specification:**
  Given The agent predicts sickness from 2026-09-14, with Certificate.Date required and empty
  When  The prediction is shown
  Then  No Confirm button is offered for it. The bot says a medical certificate is required for the absence from 14.09.2026, with buttons 'Edit registration' and 'Cancel'.
**Parameters:** Field id 'Certificate.Date'; event type Sickness; the date is formatted numeric in the current locale.
**Confidence:** High

### RULE-036: Employee Agent confirms the timesheet without checking template validations
**App:** me-ios
**Capability:** CAP-022
**Category:** Validation
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Message/QuickResponseAction/QuickResponseAction.confirmPredictedConfirmTimeEvent.swift:33-50`
**Plain English:** When the user confirms a timesheet predicted by the agent, the app reads the date from the template's Date field and registers the confirmation through the template's update link. It does not evaluate any Error or Warning validations first.
**Specification:**
  Given The agent predicts 'confirm time up to 2026-09-15', and the template carries a failing Warning validation
  When  The user taps Confirm
  Then  The confirmation is sent at once, with no warning shown. On success the chat reads 'timesheet sent for approval'. On failure an error message appears.
**Parameters:** The date is parsed with Constants.dateFormatter. Missing data gives unexpectedError id 04e45a6c-268e-41bc-8be9-53a13354c907.
**Suspected defect:** This path skips the validation gate that the day-sheet path enforces. It also parses the date with Constants.dateFormatter, while the event description (CalendarBotEventDescription.swift:28) parses the same field with utcDateFormatter, so the date shown and the date submitted can differ across time zones.
**Confidence:** Medium: Should confirming through the agent apply the same Error and Warning checks as the calendar's Confirm time, or does the prediction service already check them?

### RULE-037: Device calendar permission is required before syncing
**App:** vmm
**Capability:** CAP-007
**Category:** Validation
**Priority:** P1
**Source:** `src/hooks/useSyncCalendar.ts:40-61`
**Plain English:** If the app does not have calendar permission, it asks for it; if the user refuses, it shows a 'missing calendar permissions' error and stops without changing anything.
**Specification:**
  Given Calendar permission status is 'denied'
  When  A sync is started and the user refuses the permission prompt
  Then  An error toast 'missing-calendar-permissions' is shown and the sync is aborted (returns false)
**Parameters:** Required status: 'authorized'
**Confidence:** High

### RULE-038: Employee calendar requires the employee's company tenant
**App:** vmm
**Capability:** CAP-001
**Category:** Validation
**Priority:** P1
**Source:** `src/screens/EmployeeCalendarScreen/EmployeeCalendarScreen.tsx:116-119`
**Plain English:** The calendar can load only when the employee is found in the cached employee list with a company tenant id; otherwise, once loading is done, it shows the load error message.
**Specification:**
  Given Employee id E9 is not in the cached employee list and the list has finished loading
  When  The manager opens E9's calendar
  Then  The screen shows 'employee_calendar_load_error' and no feed is requested
**Parameters:** companyTenantId from useGetAllEmployeesNewQuery listByIds
**Confidence:** High

### RULE-039: Workshift company setting defaults to time mode, and shifts without a parseable start are dropped
**App:** me-ios
**Capability:** CAP-001
**Category:** Validation
**Priority:** P2
**Source:** `EmployeeServices/Calendar/Sources/Calendar/Mapper/WorkshiftMapper.swift:6-28 (plus Service/CalendarService.swift:87 for the default)`
**Plain English:** A roster shift is kept only if its local start time parses. Its id is 'roster-' plus the start time. If the server sends no data, the app assumes no shifts and time (not hours) mode.
**Specification:**
  Given A shift with startLocal '2026-01-02T08:00:00' and one with no startLocal
  When  workshifts are mapped
  Then  one shift with id 'roster-2026-01-02T08:00:00' is kept and the other is dropped
**Parameters:** default WorkshiftResponse(useWorkshiftsInHours: false, workshifts: []) at CalendarService.swift:87
**Edge cases handled:** Local times are parsed with a UTC formatter, so they display correctly only if the display also uses UTC. Two shifts with the same start get the same id.
**Confidence:** High: Can two roster shifts start at the same time (split shifts)? The id would collide.

### RULE-040: Dimension (cost unit) search sends the search term as query 'q'
**App:** me-ios
**Capability:** CAP-013
**Category:** Validation
**Priority:** P2
**Source:** `EmployeeServices/Calendar/Sources/Calendar/Service/AbsenceRegistrationService.swift:136-139 (helper: EmployeeServices/EmployeeAPIInterface/Sources/EmployeeAPIInterface/Model/ResponseModel.swift:130-1…`
**Plain English:** Searching cost-unit dimension values adds the typed term to the server-provided link as the query parameter 'q'.
**Specification:**
  Given A dimension values link and the search term 'Oslo'
  When  the user searches
  Then  the link is called with q=Oslo
**Parameters:** searchParam = "q"; DimensionValueDefaults count = 50 and offset = 0 are declared but not used in this service
**Suspected defect:** DimensionValueDefaults (50/0) is dead code, so the page size is whatever the server link contains.
**Confidence:** High

### RULE-041: Special days: unparseable dates dropped, public-holiday flag ignored
**App:** me-ios
**Capability:** CAP-001
**Category:** Validation
**Priority:** P2
**Source:** `EmployeeServices/Calendar/Sources/Calendar/Service/CalendarService.swift:91-101`
**Plain English:** Special days are shown by date and name. Entries whose date is not an ISO date are dropped, and the server's isPublicHoliday flag is not passed on.
**Specification:**
  Given The server returns {date:'2026-12-25', displayName:'Christmas Day', isPublicHoliday:true} and {date:'25/12', displayName:'X'}
  When  special days load
  Then  one special day, 25 Dec 2026 'Christmas Day', is kept, with no holiday flag
**Parameters:** ISO date parse strategy
**Confidence:** High: Should public holidays be shown differently from other special days? The client currently discards isPublicHoliday.

### RULE-042: Employee Agent rejects an empty prompt
**App:** me-ios
**Capability:** CAP-021
**Category:** Validation
**Priority:** P2
**Source:** `EmployeeServices/Calendar/Sources/Calendar/Service/EmployeeCalendarBotService.swift:26-42`
**Plain English:** A prompt to the Employee Agent must not be empty. The prompt is sent with the device's current local time and time zone offset, so the server can resolve words like 'tomorrow'.
**Specification:**
  Given The user sends '' / 'Vacation tomorrow' at 2026-09-28 10:00 in UTC+2
  When  prediction is requested
  Then  '' fails with 'Invalid input. Input cannot be empty'; 'Vacation tomorrow' is posted with localTime '2026-09-28T10:00:00+02:00'
**Parameters:** ISO-8601 with current time zone
**Edge cases handled:** A prompt of only spaces passes the check. The error text is hard-coded in English (CalendarBotService.swift:66-68).
**Suspected defect:** No whitespace trim, so ' ' is sent to the server. The error message is not localized.
**Confidence:** High

### RULE-043: Checkout template date range is set only when the link supports it
**App:** me-ios
**Capability:** CAP-019
**Category:** Validation
**Priority:** P2
**Source:** `EmployeeServices/Calendar/Sources/Calendar/Service/TimeService.swift:148-167`
**Plain English:** When opening the checkout template for a date range, the from and to dates are written into the link only if it already has both fromDate and toDate parameters (matched case-insensitively). Otherwise the link is used unchanged.
**Specification:**
  Given A checkout template link with FromDate and ToDate parameters, and a range from 2026-09-28 to 2026-09-28
  When  the template is requested
  Then  FromDate=2026-09-28&ToDate=2026-09-28 is set on the link
**Parameters:** date format Constants.dateFormatter
**Confidence:** High

### RULE-044: Template lookup by event type short code
**App:** me-ios
**Capability:** CAP-006
**Category:** Validation
**Priority:** P2
**Source:** `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/CalendarTemplates.swift:36-42`
**Plain English:** To start a registration of a given type, the app takes the first template across all groups whose short code matches.
**Specification:**
  Given Groups 'Absence' and 'Time', both holding a template with short code 'FER'
  When  template(with: 'FER') is called
  Then  the template from the first group is used
**Parameters:** match on data.eventTypeShortCode
**Confidence:** High

### RULE-045: Month/year picker spans 20 years back and forward
**App:** me-ios
**Capability:** CAP-001
**Category:** Validation
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/Components/CalendarMonthYearNavigationFeature.swift:29-97`
**Plain English:** The month/year picker offers years from 20 before to 20 after the shown year and jumps to the 1st of the chosen month; arrows and swipes move one month.
**Specification:**
  Given The calendar shows March 2025
  When  The picker opens
  Then  Years 2005-2045 are offered; choosing June 2030 shows 1 June 2030
**Parameters:** datePickerYearRange = 20; swipe minimumDistance 50 pt (CalendarGridView 126)
**Edge cases handled:** Header reads abbreviated month and year, e.g. 'Mar 2025'.
**Confidence:** High

### RULE-046: Blank or overlapping agent prompts are ignored
**App:** me-ios
**Capability:** CAP-021
**Category:** Validation
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:231-245`
**Plain English:** A prompt is sent to the agent only if it still has text after trimming whitespace and no other agent task is running. Sending also stops voice recording and clears any quick-response buttons still on screen.
**Specification:**
  Given The prompt field holds ' ', or a previous prediction is still loading
  When  The user presses send or the return key
  Then  Nothing is sent. The prompt ' sick today ' would be sent as 'sick today'.
**Parameters:** Trim: whitespace and newlines
**Confidence:** High

### RULE-047: Month/year picker offers 2 years back and 5 years forward
**App:** vmm
**Capability:** CAP-001
**Category:** Validation
**Priority:** P2
**Source:** `src/screens/EmployeeCalendarScreen/components/CalendarMonthYearPicker/CalendarMonthYearPicker.tsx:20-101`
**Plain English:** The year dropdown lists from 2 years before to 5 years after the year shown; month names come from the app language, capitalised; a pick jumps to the first of that month.
**Specification:**
  Given The grid shows September 2026
  When  The user opens the year dropdown
  Then  Years 2024 to 2031 are listed
**Parameters:** YEAR_RANGE_BEFORE = 2; YEAR_RANGE_AFTER = 5
**Suspected defect:** The range is relative to the displayed year, not today's year, so it does not really limit navigation.
**Confidence:** Medium: Should the year range be fixed to today's year? It is based on the year shown, so repeated picks (and the arrows) can reach any year, while the list view is capped at 24 months back.

## Eligibility

### RULE-048: Claims tab and its filter bar appear only when the claims data source is enabled
**App:** me-ios
**Capability:** CAP-028
**Category:** Eligibility
**Priority:** P1
**Source:** `Employee/CalendarLeftover/ClaimsCalendarViewModel.swift:33-72`
**Plain English:** Claims are fetched, and the quick filter bar is shown, only when the claims data source reports that it is enabled.
**Specification:**
  Given claimsPagingController.dataSource.isEnabled is false for this user
  When  the claims screen opens
  Then  no claims are fetched and no status filter bar is shown
**Parameters:** isEnabled comes from ClaimsPagingControllerDataSource (flag defined outside this area)
**Edge cases handled:** The filter bar gate is in ClaimsCalendarViewModel+UIKit.swift:13-14.
**Confidence:** Medium: What decides dataSource.isEnabled (a company setting, role or feature flag)? The target app has to reproduce it.

### RULE-049: Payslips list filtered by selected employers (tenants)
**App:** me-ios
**Capability:** CAP-029
**Category:** Eligibility
**Priority:** P1
**Source:** `Employee/Payslips/PayslipsCalendarViewModel.swift:62-81`
**Plain English:** When the user picks employers, the payslip list is cleared and reloaded with only those tenant ids. Past payslips load from today and future ones from tomorrow.
**Specification:**
  Given The user has payslips from tenants 'T1' and 'T2' and selects only 'T1', today being 2026-09-28
  When  the filter is applied
  Then  the list resets and loads only T1 payslips, past ones from 2026-09-28 backwards and future ones from 2026-09-29
**Parameters:** past anchor = today; future anchor = today + 1 day
**Confidence:** High

### RULE-050: Start-page absence cards: which vacation and parental leave items become cards
**App:** me-ios
**Capability:** CAP-017
**Category:** Eligibility
**Priority:** P1
**Source:** `Employee/StartPage/Tasks/GetCalendarItemsTask.swift:19-20,47-76`
**Plain English:** Only vacation and parental leave items that have both a start and end date become start-page cards: declined vacation starting today or later, approved parental leave that is upcoming or ongoing, and approved vacation that is ongoing, upcoming within 14 days, or approved further ahead.
**Specification:**
  Given Today is 2026-09-28 and the calendar returns an approved Vacation from 2026-10-05 to 2026-10-09, an approved Vacation from 2026-11-02 to 2026-11-06, a denied Vacation from 2026-09-28, and an approved Sickness item
  When  the start page builds its absence cards
  Then  the 5 Oct vacation shows as an Upcoming Vacation card, the 2 Nov vacation as an Approved Vacation card, the 28 Sep denied vacation as a Declined Vacation card, and the sickness item gets no card
**Parameters:** twoWeeksInFuture = today + 14 days; statuses 'approved', 'denied'; item types Vacation, ParentalLeave; comparisons at day granularity
**Edge cases handled:** An approved vacation starting exactly on day today+14 matches neither the 'before today+14' nor the 'after today+14' branch, so it gets no card. Items without dateFrom or dateTo are dropped. Pending vacations never get a card.
**Suspected defect:** Gap at the 14-day boundary: a vacation starting exactly 14 days ahead gets no card. AppConstants.CardExpiration values are static lets, so they are computed once, the first time they are used. If the app stays running past midnight, the window stays anchored to the launch day.
**Confidence:** High

### RULE-051: Absences are edited or deleted only through server-provided links
**App:** me-ios
**Capability:** CAP-015
**Category:** Eligibility
**Priority:** P1
**Source:** `EmployeeServices/Calendar/Sources/Calendar/Service/AbsenceRegistrationService.swift:82-103`
**Plain English:** An absence can be updated only if the server sent an 'update' link, and deleted only if it sent a 'delete' link. Without the link, the action fails with an unexpected error.
**Specification:**
  Given An approved vacation whose detail response has only a 'self' link
  When  the user tries to edit or delete it
  Then  no request is sent and an unexpected error is raised
**Parameters:** link rels .update and .delete
**Edge cases handled:** This also covers CAP-016 (delete). Edit permission depends entirely on the server links; the client has no status check of its own.
**Confidence:** High

### RULE-052: Deleting a check-in uses the server's link and HTTP method
**App:** me-ios
**Capability:** CAP-019
**Category:** Eligibility
**Priority:** P1
**Source:** `EmployeeServices/Calendar/Sources/Calendar/Service/TimeService.swift:204-229`
**Plain English:** A check-in can be deleted or updated only through a server-provided action with a non-empty link. Delete also needs a valid HTTP method.
**Specification:**
  Given A check-in action with href '' / a valid href and method 'delete'
  When  the user deletes it
  Then  an empty href raises an error and no call is made; a valid href is called with DELETE
**Parameters:** method is upper-cased and mapped to HTTPMethod
**Confidence:** High

### RULE-053: Time confirmation and its template: HTTP 403 means the feature is off
**App:** me-ios
**Capability:** CAP-020
**Category:** Eligibility
**Priority:** P1
**Source:** `EmployeeServices/Calendar/Sources/Calendar/Service/TimeService.swift:28-77`
**Plain English:** If the server answers 403 to the confirm-time details or template request, the app treats time confirmation as disabled for this user rather than as an error. Any status other than Success returns the server's message.
**Specification:**
  Given The user's company has not enabled time confirmation
  When  GET calendar/confirm returns HTTP 403
  Then  the result is featureDisabled (CalendarError / AbsenceRegistrationError) and no error message is shown
**Parameters:** statusCode 403
**Confidence:** High

### RULE-054: Editing a checkout should require both update and delete links (unused check)
**App:** me-ios
**Capability:** CAP-019
**Category:** Eligibility
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrationCoordinator/EditCheckoutRegistrationCoordinator.swift:57-68`
**Plain English:** A validation that a checkout has both update and delete links exists but is never called, so the edit screen opens regardless.
**Specification:**
  Given A checkout template with no update or delete links
  When  The edit checkout flow starts
  Then  The edit screen opens anyway; errors only appear when saving or deleting
**Parameters:** verifyInputData() -> invalidInputData
**Suspected defect:** verifyInputData is dead code; start() never calls it.
**Confidence:** Medium: Should the edit check-in screen refuse to open (invalidInputData) when the update or delete link is missing, as verifyInputData intends?

### RULE-055: Check-in edit and delete need server links
**App:** me-ios
**Capability:** CAP-019
**Category:** Eligibility
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/CalendarEventEditing/CheckinEventEditor.swift:26-41`
**Plain English:** A check-in/check-out registration can be updated only if the server supplied an 'update' link and deleted only if it supplied a 'delete' link; otherwise an unexpected error is shown.
**Specification:**
  Given A checkout template whose links contain update but not delete
  When  The user taps Delete
  Then  An unexpected error is shown and nothing is deleted
**Parameters:** rel .update / .delete
**Edge cases handled:** The Delete button is still displayed because edit mode is set regardless of links.
**Confidence:** High

### RULE-056: Absence types reload only with calendar write permission
**App:** me-ios
**Capability:** CAP-012
**Category:** Eligibility
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:272-291`
**Plain English:** Absence/time templates for a new period are fetched only if the user has calendar write permissions; without them an empty list is used and the current type is kept.
**Specification:**
  Given A user without calendar write permission
  When  The from-date changes to 2025-04-01
  Then  No templates are requested and the form stays unchanged
**Parameters:** hasCalendarWritePermissions()
**Edge cases handled:** Missing company features throws unexpected error F3E6C9B3-7284-4F9B-8BAA-E5859750CC57.
**Confidence:** High

### RULE-057: Changing check-out dates requires time permissions
**App:** me-ios
**Capability:** CAP-019
**Category:** Eligibility
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:293-314`
**Plain English:** When the date of a check-out edit changes, a fresh check-out template is fetched only if the company grants the user Add time or Time write; otherwise nothing is reloaded.
**Specification:**
  Given A user whose company features are [absenceRead] editing a check-out
  When  They change the from-date
  Then  No new template is fetched and the form keeps the old template
**Parameters:** UserPermission.addTime or .timeWrite
**Edge cases handled:** A server error with no data shows the status description or 'Unexpected error' and pops the screen.
**Confidence:** High

### RULE-058: Input type selector only shown when more than one option exists
**App:** me-ios
**Capability:** CAP-012
**Category:** Eligibility
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:857-886 (hiding applied at 589-591; field toggling at 409-424)`
**Plain English:** The day/hours/percent segmented selector appears only if the template offers several input types; the stored choice is used if still offered, otherwise the first option is selected, and choosing Hours or Percent adds a numeric field for that option.
**Specification:**
  Given A template with input type options FullDay, Hours, Percent and a stored value 'Hours'
  When  The form is built
  Then  The selector shows three segments with Hours selected and an hours number field is added
**Parameters:** option dataType decimal or percent adds a field
**Edge cases handled:** A single-option input type is hidden entirely; a stored value no longer offered is replaced by option 1 and written back to the model.
**Confidence:** High

### RULE-059: Confirm-time entry offered only with confirm-time permission
**App:** me-ios
**Capability:** CAP-020
**Category:** Eligibility
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/RegisterAbsenceTypeItemSelectorViewModel.swift:44-61`
**Plain English:** The type picker for a new registration includes the 'confirm timesheet' item only when the company grants confirm-time permission.
**Specification:**
  Given A user whose company lacks the confirmTime feature
  When  They open 'Select type' from the calendar
  Then  Only absence/time templates are listed, no timesheet confirmation
**Parameters:** hasConfirmTimePermission()
**Edge cases handled:** Templates are fetched for the initial date range (default today-today).
**Confidence:** High

### RULE-060: Edit button shown only when server provides edit links; edit needs write permission
**App:** me-ios
**Capability:** CAP-015
**Category:** Eligibility
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Absence/AbsenceViewTableViewController.swift:98-146 (plus 266-268 for the showEditButton gate)`
**Plain English:** On an absence's detail screen, Edit appears only if the server returned edit links, and tapping it opens the editor only if calendar templates can be loaded (requires calendar write permission and at least one template).
**Specification:**
  Given An approved vacation whose detail response has links, viewed by a user without calendar write permission
  When  The user taps Edit
  Then  The spinner closes and the editor does not open
**Parameters:** hasCalendarWritePermissions(); showEditButton when !linksForEdit.isEmpty (266-268)
**Edge cases handled:** No message explains why editing did nothing.
**Suspected defect:** Silent no-op when templates are empty; the user gets no feedback.
**Confidence:** High

### RULE-061: Tapping a calendar day: register on empty day, details otherwise
**App:** me-ios
**Capability:** CAP-006
**Category:** Eligibility
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/CalendarGridFeature.swift:210-231`
**Plain English:** In month view, tapping a day with no entries starts a new registration for that day only if the user has calendar write permission; a day with entries opens the day detail sheet.
**Specification:**
  Given A user without calendar write permission and an empty 12 March
  When  They tap 12 March
  Then  Nothing opens; tapping 13 March with a vacation opens day details
**Parameters:** isWriteAvailable = hasCalendarWritePermissions()
**Edge cases handled:** Taps while dragging are ignored.
**Confidence:** High

### RULE-062: Long-press and drag registers a period
**App:** me-ios
**Capability:** CAP-006
**Category:** Eligibility
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/CalendarGridFeature.swift:238-273`
**Plain English:** Long-pressing and dragging across days selects a date range (in either direction) and on release starts a registration for that period if the user has write permission; only days in the displayed month can be selected.
**Specification:**
  Given A user with write permission in March 2025
  When  They long-press 14 March and drag back to 10 March
  Then  A new registration opens from 10 to 14 March
**Parameters:** only isCurrentMonth days (CalendarGridView 213-215)
**Edge cases handled:** The range can include weekends even when weekends are hidden.
**Confidence:** High

### RULE-063: Roster shifts cannot be opened as registrations
**App:** me-ios
**Capability:** CAP-004
**Category:** Eligibility
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/CalendarGridFeature.swift:318-328`
**Plain English:** In day details, tapping a roster shift does nothing; other entries open their registration; 'Register' in day details requires write permission.
**Specification:**
  Given Day details for 12 March with a roster shift 08:00-15:00
  When  The user taps the shift
  Then  Nothing opens
**Parameters:** eventType.isRosterType
**Confidence:** High

### RULE-064: Day detail sheet: which actions appear and how events are listed
**App:** me-ios
**Capability:** CAP-004
**Category:** Eligibility
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/DayDetailView.swift:18-133`
**Plain English:** The day sheet shows a special day as a red header (named 'Special day' when it has no name). Roster shifts appear as non-tappable 'Scheduled hours' rows. Other events are tappable and carry a status tag. 'Register time or absence' appears only when writing is allowed, and 'Confirm time' only when confirmation is allowed.
**Specification:**
  Given A read-only user opens 9 September, which holds a public holiday named '' and one attendance event
  When  The sheet appears
  Then  It shows a red 'Special day' header and the attendance row with its tag, and neither the Register nor the Confirm time button.
**Parameters:** Flags isWriteAvailable and isConfirmTimeAvailable are set by the caller (DayDetailFeature.swift:29-37). Empty day text: 'noActivityCalendar'.
**Confidence:** High

### RULE-065: Confirm-time button needs the confirmTime permission
**App:** me-ios
**Capability:** CAP-020
**Category:** Eligibility
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarViewController.swift:508-524`
**Plain English:** The list calendar shows the 'Confirm time' secondary button only when the user's permissions include confirmTime. A tap does nothing while the calendar buttons are disabled, for example when offline.
**Specification:**
  Given A user with permissions [addTime, confirmTime] who is online
  When  The user taps 'Confirm time'
  Then  The confirmation alert of the add-absence coordinator opens. A user without confirmTime sees no button at all.
**Parameters:** Permission: confirmTime
**Confidence:** High

### RULE-066: Register-event button needs a write permission
**App:** me-ios
**Capability:** CAP-006
**Category:** Eligibility
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarViewController.swift:526-542`
**Plain English:** The list calendar shows the 'register event' button only to users who have addAbsence, addTime, absenceWrite or timeWrite. Read-only users do not see the button, and the button bar is removed.
**Specification:**
  Given User A with [absenceReadOnly, timeReadOnly] and user B with [absenceWrite]
  When  The list calendar opens
  Then  User A sees no register button and the button container is removed (lines 568-575). User B sees the 'Register event' primary button.
**Parameters:** Write permissions: addAbsence, addTime, absenceWrite, timeWrite (ArrayExtensions.swift:19-21)
**Confidence:** High

### RULE-067: Calendar is available only to users with an absence or time permission
**App:** me-ios
**Capability:** CAP-001
**Category:** Eligibility
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Extensions/ArrayExtensions.swift:13-17`
**Plain English:** The calendar feed loads only if the current user has at least one of six permissions: addAbsence, addTime, absenceReadOnly, timeReadOnly, absenceWrite or timeWrite.
**Specification:**
  Given A user whose permissions are [expenseClaims] only
  When  The calendar feed tries to load
  Then  The feed is disabled (the data source's isEnabled is false), nothing is fetched and the empty state appears. A user with [timeReadOnly] would get the feed.
**Parameters:** Calendar permissions: addAbsence, addTime, absenceReadOnly, timeReadOnly, absenceWrite, timeWrite. Enforced via CalendarFeedPagingControllerDataSource.isEnabled (DataSource/CalendarFeedPagingControllerDataSource.swift:23-25).
**Confidence:** High

### RULE-068: Calendar tab titled 'Claims' for expense-only users
**App:** me-ios
**Capability:** CAP-001
**Category:** Eligibility
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarContainerViewController.swift:325-370`
**Plain English:** The tab is titled Calendar when the user has both absence and time permissions; otherwise Claims if they have expense claims; otherwise Calendar if they have absence or time.
**Specification:**
  Given A user with absence permission and expense claims but no time permission
  When  The tab bar is built
  Then  The tab reads 'Claims' with the expense icon
**Confidence:** Medium: Should a user with absence permissions and expense claims really see the tab as 'Claims' rather than 'Calendar'?

### RULE-069: Only days of the displayed month show events and respond to taps
**App:** me-ios
**Capability:** CAP-004
**Category:** Eligibility
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/Components/CalendarWeekDaysRow.swift:36-45`
**Plain English:** Leading or trailing days from the previous or next month appear in the grid but carry no events (CalendarViewUtils.swift:100), and tapping or long-pressing them does nothing.
**Specification:**
  Given The September 2026 grid, which shows 31 August in its first row
  When  The user taps 31 August
  Then  Nothing happens, and 31 August shows no events.
**Parameters:** none
**Confidence:** High

### RULE-070: Month cells show only absence and roster events, filtered by type
**App:** me-ios
**Capability:** CAP-005
**Category:** Eligibility
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Utils/CalendarViewUtils.swift:138-147`
**Plain English:** A day cell shows only absence-type and roster events. Confirmed-time and special-day entries never appear as cell events. An event without a filterable type is always shown, and one with a filterable type is hidden when the user has hidden that type.
**Specification:**
  Given A day with an absence (filterable type 'attendance'), a roster shift and a confirmed-time entry, and the user has hidden attendance
  When  The day cell is drawn
  Then  The cell shows only the roster shift.
**Parameters:** Filterable types: absence, attendance, supplement, unknown
**Confidence:** High

### RULE-071: Agent offers Edit only when exactly one registration was predicted
**App:** me-ios
**Capability:** CAP-024
**Category:** Eligibility
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:287-325`
**Plain English:** After a prediction, the bot offers Confirm when at least one event is ready, Edit when exactly one event was predicted, and always Cancel. If no event is ready, the bot sends the follow-up messages for events that need editing instead of a summary.
**Specification:**
  Given The agent predicts 2 vacations, both ready
  When  The summary appears
  Then  The buttons are Confirm and Cancel, with no Edit. With a single predicted vacation, the buttons would be Confirm, Edit and Cancel.
**Parameters:** none
**Confidence:** High

### RULE-072: Absences created in the chat can be opened only if they have a retrieval link
**App:** me-ios
**Capability:** CAP-025
**Category:** Eligibility
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:592-604`
**Plain English:** Tapping an event in the chat opens its detail only if it is a registered absence that has a retrieval link. Predicted, deleted and confirm-time events do nothing when tapped.
**Specification:**
  Given A success summary with a registered vacation that has a retrieval link
  When  The user taps it
  Then  The absence detail view opens.
**Parameters:** none
**Confidence:** High

### RULE-073: Calendar hides entry types the user filtered out
**App:** vmm
**Capability:** CAP-005
**Category:** Eligibility
**Priority:** P2
**Source:** `src/screens/EmployeeCalendarScreen/EmployeeCalendarScreen.tsx:137-149`
**Plain English:** Entries of type attendance, absence or supplement are hidden when the matching filter is off; entries of any other type are always shown.
**Specification:**
  Given Show absence = off and a day with one 'absence' entry and one 'attendance' entry
  When  The month grid is shown
  Then  Only the attendance entry appears on that day and in its detail sheet
**Parameters:** Filters calendarShowAttendance / calendarShowAbsence / calendarShowSupplement, all default true (settingsReducer.ts:121-123)
**Suspected defect:** Filters apply to the grid and day sheet only; the list view (agendaItems, line 177-179) ignores them.
**Confidence:** High

## Lifecycle

### RULE-074: Empty (draft) claims are fetched once per reset, filtered by the selected statuses
**App:** me-ios
**Capability:** CAP-028
**Category:** Lifecycle
**Priority:** P1
**Source:** `Employee/CalendarLeftover/ClaimsCalendarViewModel.swift:91-106`
**Plain English:** Before loading paged claims, the app fetches the claims with status 'empty' once per list reset, using the selected status filter, and adds them to the list.
**Specification:**
  Given The claims list has just been reset with filter statuses ['open']
  When  data is fetched twice while scrolling
  Then  the 'empty' claims request runs only on the first fetch, and the paged claims request runs on both
**Parameters:** AppConstants.ClaimStatus.empty = "empty"; the flag emptyClaimsShouldBeFetched is set back to true on reset()
**Edge cases handled:** If the empty-claims request fails, the error is recorded and it is not retried until the next reset.
**Confidence:** High

### RULE-075: Check-in and check-out send the device's local time with time zone
**App:** me-ios
**Capability:** CAP-018
**Category:** Lifecycle
**Priority:** P1
**Source:** `EmployeeServices/Calendar/Sources/Calendar/Service/TimeService.swift:169-202 (plus 113-126 for status mapping; timestamp format at EmployeeServices/EmployeeCore/Sources/EmployeeCore/CoreFormatStyle.s…`
**Plain English:** Check-in uses PUT with the device's current time as ISO-8601 with its time zone offset. Check-out uses PUT to the server-provided checkout link with the same kind of timestamp. Each returns the new status: Idle, CheckedIn, Error or Conflict.
**Specification:**
  Given The user taps Check in at 2026-09-28 08:02:10 in UTC+2
  When  the request is sent
  Then  the body is {localTime:'2026-09-28T08:02:10+02:00'} and the response status is 'CheckedIn'
**Parameters:** CheckinStatus values Idle, CheckedIn, Error, Conflict, unknown (Checkin.swift:11-19)
**Edge cases handled:** The timestamp comes from the device clock, so a wrong clock records wrong worked time. A response without data throws an unexpected error.
**Confidence:** High: Should the server stamp check-in time instead of trusting the device clock?

### RULE-076: Delete is available only in edit mode and must be confirmed
**App:** me-ios
**Capability:** CAP-016
**Category:** Lifecycle
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrationTableViewController.swift:423-429`
**Plain English:** The Delete button appears only when editing an existing registration; tapping it opens a warning dialog and the registration is deleted only if the user confirms.
**Specification:**
  Given An existing vacation registration opened for editing
  When  The user taps Delete and then Delete in the warning dialog
  Then  The registration is removed via the server's delete link and the 'deleted' post screen is shown
**Parameters:** warning text S.Calendar.deleteRegistrationEventWarning
**Edge cases handled:** New registrations never show Delete. Cancel leaves the record untouched.
**Confidence:** High

### RULE-077: Absence save response lifecycle: Success, ValidationError, Error, ConfirmationRequired
**App:** me-ios
**Capability:** CAP-012
**Category:** Lifecycle
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/CalendarEventEditing/AbsenceEventEditor.swift:34-90`
**Plain English:** Registering or updating an absence returns one of four outcomes: Success, ValidationError, Error or ConfirmationRequired. ConfirmationRequired returns a template that the user must confirm, using the server's save-button text, before it is saved.
**Specification:**
  Given A vacation registration that would exceed the remaining balance
  When  the server answers statusCode 'ConfirmationRequired' with a template
  Then  the app treats it as needing user confirmation (AbsenceRegistrationError.createAbsenceConfirmationRequired) rather than as saved
**Parameters:** statusCode values Error, Success, ValidationError, ConfirmationRequired; a response without a statusCode key fails to decode
**Edge cases handled:** An unknown statusCode maps to .unknown. The same lifecycle applies to AbsenceUpdateResponse (lines 221-237).
**Confidence:** Medium: Is ConfirmationRequired only for balance overdraft, or also for other policy warnings? The server decides, and the merged app needs the same confirm step.

### RULE-078: Only input type, comment and sickness percentage survive a type change
**App:** me-ios
**Capability:** CAP-012
**Category:** Lifecycle
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:223-248`
**Plain English:** When the user switches to another absence type, the entered input type and comment are carried over (plus certificate percentage if the new type is Sickness); all other entered values are discarded.
**Specification:**
  Given A Vacation draft with comment 'Doctor' and project dimension '1001'
  When  The user switches the type to Sickness
  Then  Comment 'Doctor' is kept, the dimension value is cleared
**Parameters:** fieldsToRestore = InputType, Comment, (+CertificatePercentage if Sickness)
**Edge cases handled:** For predictions from the Employee Agent the whole cache is cleared and saved values merged into the schema instead.
**Confidence:** High

### RULE-079: Month grid: confirmed and approved timesheet entries are built separately
**App:** me-ios
**Capability:** CAP-020
**Category:** Lifecycle
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Model/Domain/CalendarGridItem.swift:114-164`
**Plain English:** In the month grid, identical approver and confirmer dates produce one approved entry. Otherwise the grid shows an approved entry at the approver date (if any) and a separate pending 'confirmed' entry at the confirmer date (if any).
**Specification:**
  Given Confirmer date 2026-09-15 and approver date 2026-09-30
  When  The month grid is built
  Then  Two 'Timesheet confirmed' entries appear: approved on 2026-09-30 and pending on 2026-09-15. The list view would show one approved row.
**Parameters:** Entry ids: confirmTime_approved, confirmTime_confirmed
**Suspected defect:** Equality uses exact Date values, so dates differing by seconds produce two entries. The list view compares with >= instead, so the two views can show different statuses for the same timesheet.
**Confidence:** High

### RULE-080: Month grid knows only approved, rejected and pending request statuses
**App:** me-ios
**Capability:** CAP-004
**Category:** Lifecycle
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Model/Domain/CalendarGridItem.swift:95-95 (enum at 46-51)`
**Plain English:** When an absence becomes a grid entry, its request status must exactly match 'approved', 'rejected' or 'pending'. Any other value becomes 'none', and the day-detail sheet then shows no status tag (DayDetailView.swift:18-34).
**Specification:**
  Given An absence with requestStatus 'sent'
  When  The user opens its day in the month grid
  Then  The event shows no status tag, while the list view labels the same absence 'Awaiting approval'.
**Parameters:** Grid statuses: approved (green tag), rejected (red tag), pending (blue tag), none (no tag)
**Suspected defect:** The match is case-sensitive and ignores statuses the list view handles, so the same absence can look 'Awaiting approval' in the list and unlabelled in the grid.
**Confidence:** Medium: Should the grid map sent, denied, notApproved, awaitingClearance, open, paid and canceled the way the list does? Right now they show no status in the day detail.

### RULE-081: List view: timesheet counts as approved when the approval date is on or after the confirmation date
**App:** me-ios
**Capability:** CAP-020
**Category:** Lifecycle
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarUtils.swift:92-96`
**Plain English:** In the list calendar, a confirmed timesheet shows as approved only when both dates exist and the approver's date is the same as or later than the confirmer's date. In every other case it shows as pending.
**Specification:**
  Given Confirmer date 2026-09-15 and approver date 2026-09-10
  When  The confirmed-time row is shown in the list
  Then  The status is pending. With approver date 2026-09-15 or later it is approved. With no approver date it is pending.
**Parameters:** Comparison: approvalDate >= confirmationDate
**Confidence:** High

### RULE-082: Agent answer order: registrations first, then timesheet confirmation, then balances
**App:** me-ios
**Capability:** CAP-021
**Category:** Lifecycle
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:275-285`
**Plain English:** If the agent's response contains registration predictions, only those are handled. Otherwise a confirm-time template is handled. Otherwise the balances text is shown.
**Specification:**
  Given A response with 1 predicted vacation and a balances text
  When  The response is processed
  Then  Only the vacation prediction is offered for confirmation, and the balances text is not shown.
**Parameters:** none
**Confidence:** High

### RULE-083: How the agent reports registration results and failures
**App:** me-ios
**Capability:** CAP-021
**Category:** Lifecycle
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:419-494`
**Plain English:** Successful registrations are listed in a success summary. A failed registration that needs confirmation (for example a future absence) becomes a confirm/cancel prompt. Other failures show the event description plus the error. If more than one failure would need buttons, the bot asks the user to register one by one. Once no buttons remain, the bot asks 'anything else?'.
**Specification:**
  Given 3 predicted absences: 2 succeed, 1 fails with 'Overlaps existing absence'
  When  The results come back
  Then  The chat shows a success summary listing the 2 absences, then an error message '<event description>\nOverlaps existing absence', then 'Anything else?'.
**Parameters:** none
**Confidence:** High

### RULE-084: A future absence needs explicit confirmation before it is registered again
**App:** me-ios
**Capability:** CAP-021
**Category:** Lifecycle
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:538-564`
**Plain English:** When the server answers a registration with 'confirmation required' and a message, the bot shows that message as a warning with Confirm and Cancel. Confirm registers the template again (QuickResponseAction.confirmFutureAbsenceRegistration.swift:18-34). Without a message, the bot shows it as an error.
**Specification:**
  Given Registering vacation for 2027-01-10 returns createAbsenceConfirmationRequired with the message 'This absence is far in the future. Continue?'
  When  The user taps Confirm
  Then  The absence is submitted again and the result appears as a success or error message. Cancel discards it.
**Parameters:** none
**Confidence:** High

### RULE-085: Turning sync on saves the setting only if the sync run succeeds; turning it off always saves Off
**App:** vmm
**Capability:** CAP-007
**Category:** Lifecycle
**Priority:** P1
**Source:** `src/components/common/CalendarSyncPicker/CalendarSyncPicker.tsx:37-56 (with src/hooks/useSyncCalendar.ts:47-60,255)`
**Plain English:** Tapping the switch runs a full sync (birthdays and anniversaries) when it is not already on, and runs removal when it is on; a second tap is ignored until 2 seconds after the run finishes.
**Specification:**
  Given calendarSync = sync_off
  When  The manager taps the switch and calendar permission is denied
  Then  runSync returns false and the setting stays sync_off; had permission been granted, the setting becomes sync_all. From sync_all a tap always sets sync_off, even if removal fails
**Parameters:** Modes sync_off / sync_all (sync_birthdays and sync_anniversaries exist but the switch never uses them); lockout 2000 ms
**Suspected defect:** runSync returns true even when calendar creation or event saves fail (success flag is only used for the toast), so the setting can say 'On' when no events were written.
**Confidence:** High

### RULE-086: Turning sync on deletes events that already exist for an employee instead of keeping them
**App:** vmm
**Capability:** CAP-007
**Category:** Lifecycle
**Priority:** P1
**Source:** `src/hooks/useSyncCalendar.ts:139-146`
**Plain English:** When an employee already has a synced event, the code removes it rather than skipping it, even in sync_all mode.
**Specification:**
  Given The 'Manager App - Birthdays' calendar still holds an event for employee E1 (for example after a reinstall reset the setting to Off)
  When  The manager turns sync on (sync_all)
  Then  E1's existing birthday event is removed and no new one is created, so E1 ends up without a birthday event
**Parameters:** Same logic in anniversaries branch (lines 218-225)
**Suspected defect:** The else-if branch fires for foundEvents.length > 0 regardless of mode, so a re-sync with existing events removes them.
**Confidence:** Medium: Should turning sync on keep (or recreate) events that already exist for an employee, instead of deleting them?

### RULE-087: Turning sync off removes both Manager App calendars and clears the synced list
**App:** vmm
**Capability:** CAP-007
**Category:** Lifecycle
**Priority:** P1
**Source:** `src/hooks/useSyncCalendar.ts:229-239`
**Plain English:** Mode Off (or no mode) deletes both 'Manager App' calendars from the device; birthdays-only deletes the anniversaries calendar and anniversaries-only deletes the birthdays calendar.
**Specification:**
  Given Both 'Manager App - Birthdays' and 'Manager App - Anniversaries' exist
  When  sync_off runs
  Then  Both calendars are removed from the device and the HRM synced-employee list is cleared
**Parameters:** sync_birthdays removes anniversaries calendar; sync_anniversaries removes birthdays calendar
**Confidence:** High

### RULE-088: Synced events live in two dedicated device calendars
**App:** vmm
**Capability:** CAP-007
**Category:** Lifecycle
**Priority:** P1
**Source:** `src/hooks/useSyncCalendar.ts:63-93 and 152-169`
**Plain English:** Birthdays go into a device calendar titled 'Manager App - Birthdays' and anniversaries into 'Manager App - Anniversaries'; each is created only if a calendar with that exact title does not already exist.
**Specification:**
  Given No device calendar titled 'Manager App - Birthdays' exists
  When  Sync mode sync_all runs
  Then  A calendar 'Manager App - Birthdays' (owner 'VMM', source 'Manager', primary blue colour) is created; an existing calendar with that title is reused
**Parameters:** MANAGER_BIRTHDAYS_CALENDAR='Manager App - Birthdays'; MANAGER_ANNIVERSARIES_CALENDAR='Manager App - Anniversaries' (consts/constants.ts:119-120)
**Confidence:** High

### RULE-089: Balance group categories: vacation, attendance, sickness, sick child
**App:** me-ios
**Capability:** CAP-011
**Category:** Lifecycle
**Priority:** P2
**Source:** `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/Balances/EmployeeBalanceGroup.swift:14-22`
**Plain English:** Balance groups belong to one of the categories vacation, attendance, sickness or sickchild. Any other value is treated as 'none'.
**Specification:**
  Given The server sends a balance group with category 'overtime'
  When  it is decoded
  Then  its category is 'none'
**Parameters:** raw values vacation, attendance, sickness, sickchild, none; the unit id 'Hours' is recognised (EmployeeBalanceUnit.swift:21-23)
**Confidence:** High

### RULE-090: A deleted absence is shown as struck through in the earlier success message
**App:** me-ios
**Capability:** CAP-025
**Category:** Lifecycle
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:567-589`
**Plain English:** After the user deletes an absence created in the chat, the bot posts an 'event has been deleted' message. The earlier success summary is rewritten so that event shows struck through and can no longer be tapped, and the summary loses its buttons.
**Specification:**
  Given A chat summary listing vacation 2026-10-05 that was created in the chat
  When  The user deletes that vacation from its detail view
  Then  A new bot message says it was deleted, and the vacation line in the old summary appears struck through with no chevron.
**Parameters:** none
**Confidence:** High

### RULE-091: Switching from list to month view keeps the month last seen in the list
**App:** vmm
**Capability:** CAP-003
**Category:** Lifecycle
**Priority:** P2
**Source:** `src/screens/EmployeeCalendarScreen/EmployeeCalendarScreen.tsx:151-158`
**Plain English:** When the user switches from list to grid, the grid opens on the month at the top of the list.
**Specification:**
  Given The list is scrolled to entries in June 2026
  When  The user switches to grid view
  Then  The grid shows June 2026
**Parameters:** Default view mode 'grid' (settingsReducer.ts:119)
**Confidence:** High

### RULE-092: Only pending requests show a status tag in the day sheet
**App:** vmm
**Capability:** CAP-004
**Category:** Lifecycle
**Priority:** P2
**Source:** `src/screens/EmployeeCalendarScreen/components/EmployeeCalendarDayDetail.tsx:76-102`
**Plain English:** In the day details sheet, an entry whose request status is 'pending' gets an orange status tag; entries with status 'none' get no tag.
**Specification:**
  Given A Vacation entry with requestStatus 'pending' and a Sickness entry with requestStatus 'none'
  When  The user opens the day sheet
  Then  Vacation shows an orange 'pending' tag and Sickness shows no tag
**Parameters:** Feed request statuses: 'none' / 'pending' only
**Suspected defect:** getApprovalStatusColors defines green for 'none', but it is never used; the feed has no approved or rejected status, unlike AbsenceRegistrationResource (Pending/Approved/Rejected/Cancelled).
**Confidence:** High

## Policy

### RULE-093: Server-requested confirmation before saving (future registration)
**App:** me-ios
**Capability:** CAP-012
**Category:** Policy
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/CalendarEventEditing/AbsenceEventEditor.swift:34-90`
**Plain English:** If the server answers a create or update with 'confirmation required' and a warning notification, the app shows the server's warning with its save-button text (default 'Confirm'); confirming resubmits the server-returned template, cancelling discards the pending confirmation.
**Specification:**
  Given A vacation starting 2026-07-01 that the server flags with warning 'This is far in the future'
  When  The user taps Save
  Then  A 'Future registration' alert shows the warning; tapping the server's button re-sends, Cancel returns to the form
**Parameters:** statusCode .confirmationRequired; style warning; update uses PUT to response.updateUrl
**Edge cases handled:** If no warning notification is present nothing is thrown and the save is treated as successful. For updates a missing updateUrl also skips the confirmation.
**Suspected defect:** A confirmationRequired response without a warning notification is treated as success and the post-registration screen is shown although nothing was saved.
**Confidence:** High

### RULE-094: Month data loading stops after 50 page requests or at the first error
**App:** me-ios
**Capability:** CAP-001
**Category:** Policy
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Repository/CalendarFeedRepositoryAdapter.swift:59-79`
**Plain English:** To fill a month grid, the app keeps requesting past and future pages until the loaded range covers the month, no more pages exist, an error occurs, or 50 rounds have run. If the month lies wholly outside the loaded range, the app first restarts the feed at the month's start date.
**Specification:**
  Given A month grid for 2026-09-01..2026-10-04 with a loaded feed range of 2026-09-10..2026-09-20
  When  The month is fetched
  Then  The app requests past and future pages repeatedly until the range covers 2026-09-01 and 2026-10-04, stopping after at most 50 rounds or at the first error.
**Parameters:** maxIterations = 50
**Confidence:** High

### RULE-095: Offline calendar hides the list and blocks registration and confirmation
**App:** me-ios
**Capability:** CAP-002
**Category:** Policy
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarViewController.swift:913-967`
**Plain English:** When the device goes offline, the calendar hides the list and the register/confirm buttons, disables their actions and shows an offline placeholder. When the connection returns, the calendar restores them and reloads itself if it is visible.
**Specification:**
  Given A user viewing the calendar list with the device online
  When  Connectivity is lost, then comes back
  Then  On loss: the list is hidden, the offline text shows, and taps on Register or Confirm time are ignored. On return: the placeholder is removed, the buttons work again and the feed resets and reloads (lines 960-967). There is no offline queue of registrations.
**Parameters:** The offline text depends on permissions: expenseClaims gives the claims offline text; addAbsence or addTime gives the calendar offline text with 117 pt top padding (lines 54-75).
**Suspected defect:** In calendarViewModelDidFetchData (lines 234-242), the branch `else if isOffline && !isEmpty`, which would show 'cannot load more content', can never run because the `if isOffline` above it already caught that case.
**Confidence:** High

### RULE-096: Closing the Employee Agent refreshes the start page and calendar
**App:** me-ios
**Capability:** CAP-021
**Category:** Policy
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Coordinator/CalendarChatBotCoordinator.swift:71-82`
**Plain English:** When the agent chat is closed, the app asks the start page and the calendar to reload so registrations made in the chat appear. The chat cannot be dismissed by swiping (line 61), and the conversation is kept only in memory, so it is lost on close.
**Specification:**
  Given A user registered 2 absences in the agent chat
  When  The user closes the chat
  Then  The start page and calendar reload and show the 2 absences. Reopening the chat starts with only the introduction messages.
**Parameters:** Notifications: reloadStartPage, resetCalendar
**Confidence:** Medium: Is losing the chat history on close intended, or should the conversation be kept for the session?

### RULE-097: Agent registers each predicted absence separately and in parallel
**App:** me-ios
**Capability:** CAP-021
**Category:** Policy
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/UseCase/RegisterAbsenceEventsUseCase.swift:51-72`
**Plain English:** Confirming several predicted absences sends one create request per absence, all at once. Each succeeds or fails on its own, with no rollback of the others. An empty list sends nothing.
**Specification:**
  Given The user confirms 3 predicted absences and the 2nd is rejected by the server
  When  Registration runs
  Then  Absences 1 and 3 are saved and 2 is reported as failed.
**Parameters:** none
**Suspected defect:** The result handler force-unwraps registrationResponse.retrievalLink (CalendarChatBotViewModel.swift:509). A successful create that returns no retrieval link would crash the app after the absence was already saved.
**Confidence:** High

### RULE-098: Several agent events needing attention are sent back for one-by-one registration
**App:** me-ios
**Capability:** CAP-021
**Category:** Policy
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:361-376`
**Plain English:** If exactly one predicted event needs editing, the bot shows the medical-certificate prompt for it. If more than one needs editing, the bot asks the user to register the events one by one.
**Specification:**
  Given The agent predicts 2 sickness absences, both missing a required certificate date
  When  The predictions are processed
  Then  The bot replies with the 'register events one by one' message and offers no per-event edit.
**Parameters:** Threshold: more than 1 event
**Confidence:** High

### RULE-099: Confirm actions are locked while a submission is running
**App:** me-ios
**Capability:** CAP-022
**Category:** Policy
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:744-753`
**Plain English:** While a confirm action runs in the agent chat, the chat is marked busy and shows a loading message, so new prompts are refused. The day sheet likewise disables Confirm time while a confirmation is running (DayDetailView.swift:122-128). Sending any new chat message removes the previous quick-response buttons (lines 168-172).
**Specification:**
  Given The user taps Confirm on 2 predicted absences
  When  The user tries to send another prompt before the result arrives
  Then  The prompt is not sent, and the earlier Confirm button is gone, so the absences cannot be submitted twice.
**Parameters:** Busy for: confirmCalendarEventPrediction, confirmConfirmTimePrediction, confirmFutureAbsenceRegistration
**Confidence:** High

### RULE-100: Team absence feed returns 'no absences' on any failure
**App:** vmm
**Capability:** CAP-008
**Category:** Policy
**Priority:** P1
**Source:** `src/services/queryApi/queryEndpointsCalendar/queryEndpointsCalendar.ts:35-67`
**Plain English:** The Start screen's 'who is absent' feed fetches 100 days forward from the month start for all managed employees across companies; any error (403, network, unknown environment, bad payload) is treated as an empty list, not an error.
**Specification:**
  Given The feed endpoint returns 403 'User not allowed to do this operation'
  When  The Start screen loads the absence summary for from=2026-09-01
  Then  The feed returns employees = [] and the absence signal is simply not shown, with no error message
**Parameters:** Offset=100, Direction=1, X-Visma-Employee-Version 12.0, default env 'production'
**Suspected defect:** A real outage looks the same as 'nobody is absent'; managers cannot tell the data is missing.
**Confidence:** High

### RULE-101: Employee calendar month grid shows mock data instead of the employee's real calendar
**App:** vmm
**Capability:** CAP-001
**Category:** Policy
**Priority:** P1
**Source:** `src/services/queryApi/queryEndpointsCalendar/queryEndpointsCalendar.ts:71-75`
**Plain English:** The employee calendar feed currently ignores the employee and returns a fixed April 2026 sample (sickness, vacation, overtime, etc.) copied into whatever month is shown.
**Specification:**
  Given A manager opens the calendar of any employee and navigates to October 2026
  When  The grid loads
  Then  Sample entries appear, for example 'Sickness' on 7 October and a pending 'Vacation' on 8 October, whatever that employee actually registered
**Parameters:** Fixture from mockData.ts (April 2026, days past month length dropped)
**Suspected defect:** Marked TEMPORARY; managers could act on fictitious absence and sickness data for named employees.
**Confidence:** High: Is it acceptable for a production build to show fabricated sickness and vacation entries for real employees, or should the screen be hidden until the live feed (commented out at lines 77-139) is enabled?

### RULE-102: Start-page absence cards look from 7 days back to 1 month ahead
**App:** me-ios
**Capability:** CAP-017
**Category:** Policy
**Priority:** P2
**Source:** `Employee/StartPage/Tasks/GetCalendarItemsTask.swift:19-20`
**Plain English:** The start page loads calendar items from 7 days in the past to 1 month in the future to build its vacation and leave cards.
**Specification:**
  Given The app was launched on 2026-09-28
  When  the start-page absence task runs
  Then  it requests calendar items from 2026-09-21 to 2026-10-28
**Parameters:** oneWeekInPast = -7 days; oneMonthInFuture = +1 month (AppConstants.CardExpiration)
**Edge cases handled:** The window uses values computed once per process (static lets), so it does not move forward while the app keeps running.
**Suspected defect:** The window is not recalculated after midnight while the app keeps running.
**Confidence:** High

### RULE-103: Satisfaction survey offered after save, not after delete
**App:** me-ios
**Capability:** CAP-015
**Category:** Policy
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrationCoordinator/EditAbsenceRegistrationCoordinator.swift:122-130`
**Plain English:** After editing an absence, the in-app survey is requested only when the action was a save; after new registrations and check-out edits it is requested on any non-cancelled finish.
**Specification:**
  Given A user deletes an absence
  When  The post screen closes
  Then  No survey is requested
**Parameters:** SurvicateService.requestSurveyShowingThankYouToast
**Confidence:** High

### RULE-104: Type picker error messages
**App:** me-ios
**Capability:** CAP-012
**Category:** Policy
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/RegisterAbsenceTypeItemSelectorViewModel.swift:84-108`
**Plain English:** Load errors in the type picker show provider/validation reasons and 4xx server reasons; 'feature disabled' errors are silently ignored; duplicate messages are shown once.
**Specification:**
  Given The templates call returns HTTP 403 'Absence module not active' and confirm-time returns featureDisabled
  When  The picker loads
  Then  An error banner shows 'Absence module not active' only
**Parameters:** 400..<500 with non-empty reason
**Edge cases handled:** Set-based de-duplication loses message order.
**Confidence:** High

### RULE-105: Balances load once and can be retried
**App:** me-ios
**Capability:** CAP-010
**Category:** Policy
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/BalancesOverview/Features/BalancesOverviewFeature.swift:60-105`
**Plain English:** The overview loads on first appearance only; on failure the user can retry; offline shows a 'connect and retry' message; a new load cancels one in flight.
**Specification:**
  Given The device is offline
  When  The summary opens
  Then  The 'connect and retry' message appears with a retry option
**Parameters:** cancelInFlight = true
**Confidence:** High

### RULE-106: Balances toggle choice is remembered per section
**App:** me-ios
**Capability:** CAP-010
**Category:** Policy
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/BalancesOverview/UseCase/ResolveBalancesControlsUseCase.preferences.swift:6-16`
**Plain English:** A balance section's toggle starts at the user's saved choice if still offered, otherwise at the server default; changing it is saved on the device. The first option means off, the last means on.
**Specification:**
  Given A vacation toggle with options ['earned','available'], default 'earned', saved choice 'available'
  When  The overview loads
  Then  The toggle is on and values for 'available' are shown
**Parameters:** persisted in UserPreferences.calendarBalancesControlOption; off = options.first, on = options.last
**Edge cases handled:** A saved option no longer offered falls back to the default. Controls whose type is not 'toggle' are not shown.
**Confidence:** High

### RULE-107: Month view reloads when the app returns to foreground
**App:** me-ios
**Capability:** CAP-001
**Category:** Policy
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarContainerViewController.swift:444-448`
**Plain English:** When the app comes back to the foreground in month view, the displayed month is reloaded from the server; offline shows an offline empty view.
**Specification:**
  Given Month view showing April 2025
  When  The app returns from background
  Then  April 2025 is fetched again
**Parameters:** offline view in CalendarGridView 51-56
**Edge cases handled:** List view is not reloaded here.
**Confidence:** High

### RULE-108: Calendar view mode remembered
**App:** me-ios
**Capability:** CAP-003
**Category:** Policy
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarContainerViewController.swift:70-76 (restore; default at 52; save at 164-165)`
**Plain English:** The last chosen list/month view is saved and restored on next launch, only for users with calendar permissions; default is list.
**Specification:**
  Given A user with calendar permissions who last used month view
  When  They open the calendar
  Then  Month view opens
**Parameters:** UserPreferences.calendarViewMode; default .list
**Edge cases handled:** Summary, Employee Agent and view switch buttons also require calendar permissions (111-136).
**Confidence:** High

### RULE-109: Calendar filters are saved on the device
**App:** me-ios
**Capability:** CAP-005
**Category:** Policy
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/CalendarFilterPreferences.swift:4-63`
**Plain English:** The month view can hide weekends (5-day grid), absences, attendance, supplements and roster shifts, and show week numbers and labels; all default off and persist between sessions.
**Specification:**
  Given Hide weekends and Hide attendance on
  When  March 2025 is shown
  Then  The grid shows Monday-Friday only and attendance entries are hidden
**Parameters:** daysPerWeek 7, weekendDaysCount 2 (CalendarGridConfiguration 15-16)
**Edge cases handled:** Hiding weekends also removes other-month week rows.
**Confidence:** High

### RULE-110: Calendar display filter defaults
**App:** me-ios
**Capability:** CAP-005
**Category:** Policy
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/Components/CalendarViewFilterFeature.swift:89-179`
**Plain English:** By default, week numbers are off, events show as icons rather than text, attendance, absence and supplement are all shown, and the roster is shown. Hide-weekends takes the value passed in. The attendance, absence and supplement checkboxes mean 'show', so ticking one sends hide=false.
**Specification:**
  Given Default filter settings
  When  The user unticks 'Absence'
  Then  The calendar receives hideAbsenceChanged(true), and absence-type events disappear from the cells.
**Parameters:** showWeekNumbers=false, showLabels=false, hideAbsence=false, hideAttendance=false, hideSupplement=false, showRoster=true
**Confidence:** High

### RULE-111: Returning from background jumps the calendar back to today
**App:** me-ios
**Capability:** CAP-002
**Category:** Policy
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarViewController.swift:482-488`
**Plain English:** When the app sends the reset-after-background message, a visible calendar sets its jump target to today and reloads at once. A hidden calendar reloads the next time it appears.
**Specification:**
  Given A user left the calendar scrolled to March 2024 and the app comes back from background on 2026-09-28
  When  The resetCalendarBackground notification fires while the calendar is visible
  Then  The feed resets and scrolls to 2026-09-28.
**Parameters:** Notifications: AppMessage.resetCalendarBackground, AppMessage.resetCalendar
**Confidence:** High

### RULE-112: Calendar load errors are combined into one alert; some errors are silent
**App:** me-ios
**Capability:** CAP-002
**Category:** Policy
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarViewController.swift:715-747`
**Plain English:** When the feed fails, the app joins all error messages into one alert. Provider and validation reasons are shown as returned. Feature-disabled, no-internet and cancelled errors are dropped. Any other error shows the generic 'unexpected error' text.
**Specification:**
  Given A fetch returns CalendarError.providerError("Service unavailable") and AppNetError.noInternet
  When  The fetch finishes while online
  Then  One alert titled 'Error' appears with the message 'Service unavailable'. The no-internet error is not shown. The alert appears once and is then cleared.
**Parameters:** Silent errors: CalendarError.featureDisabled, AbsenceRegistrationError.featureDisabled, AppNetError.noInternet, AppNetError.canceled. Separator: a single space.
**Confidence:** High

### RULE-113: Example prompts load once per session and fail silently
**App:** me-ios
**Capability:** CAP-026
**Category:** Policy
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/LearnMore/LearnMoreReducer.swift:37-57`
**Plain English:** Learn More fetches example prompts the first time it opens and reuses them afterwards. A failed fetch shows no examples and no error. Picking an example puts it in the prompt field without sending it (CalendarChatBotView.swift:142-147).
**Specification:**
  Given The prompts service is unreachable
  When  The user opens Learn More
  Then  The loading indicator stops and no examples are listed. No error is shown.
**Parameters:** none
**Confidence:** High

### RULE-114: Agent feedback goes to an external Google Form
**App:** me-ios
**Capability:** CAP-027
**Category:** Policy
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/LearnMore/LearnMoreReducer.swift:58-59`
**Plain English:** The 'give feedback' action opens a fixed, third-party Google Forms address inside the app.
**Specification:**
  Given A user in Learn More
  When  The user taps feedback
  Then  https://forms.gle/hD3FxxN4igj7R47k6 opens.
**Parameters:** chatBotFeedbackFormURL = https://forms.gle/hD3FxxN4igj7R47k6 (not a credential)
**Confidence:** Medium: Is a hard-coded third-party Google Form approved for collecting employee feedback, or should the address come from configuration or an internal channel?

### RULE-115: Sync result message is shown 2 seconds later, only for On and Off
**App:** vmm
**Capability:** CAP-007
**Category:** Policy
**Priority:** P2
**Source:** `src/hooks/useSyncCalendar.ts:240-254`
**Plain English:** Two seconds after a sync, the app shows '<Sync all> successful' or '<Sync all> failed' (or the Off equivalents); birthdays-only and anniversaries-only modes show no message.
**Specification:**
  Given sync_all run where one saveEvent call fails
  When  2000 ms have passed
  Then  An error toast '<sync_all> failed' is shown, but only if the failure has already been reported by then
**Parameters:** Delay 2000 ms
**Suspected defect:** Events are saved inside an un-awaited async forEach, so the success flag can still be true when the toast fires, and the message may report success when saves later fail.
**Confidence:** Medium: Is a fixed 2-second wait an acceptable way to decide success, given that event saves are not awaited?

### RULE-116: Calendar list stops loading more months after a page fails
**App:** vmm
**Capability:** CAP-002
**Category:** Policy
**Priority:** P2
**Source:** `src/screens/EmployeeCalendarScreen/EmployeeCalendarScreen.tsx:207-212`
**Plain English:** While a page load is in error, reaching the list end does not request further months; months already loaded stay on screen.
**Specification:**
  Given The page for July 2026 failed to load
  When  The user scrolls to the end again
  Then  No new request is made and the already loaded Aug and Sep 2026 entries remain visible
**Parameters:** none
**Confidence:** High

### RULE-117: Period aggregation always sends a 'today' parameter, empty when not given
**App:** vmm
**Capability:** CAP-009
**Category:** Policy
**Priority:** P2
**Source:** `src/services/apiCalendar/apiCalendar.ts:269-306`
**Plain English:** The balance period aggregation request always includes employee and 'today' (empty if not supplied), plus optional start/end date, legacy date and includeFutureRegistrations.
**Specification:**
  Given A request for employee E1 with no query options
  When  It is sent
  Then  The query is '?employee=E1&today='
**Parameters:** today='' default; includeFutureRegistrations passed through as given
**Confidence:** Low: What does the server do with an empty 'today' value: use its own current date, or ignore future registrations?

### RULE-118: End-of-year balance request defaults to full expansion with balance sums
**App:** vmm
**Capability:** CAP-009
**Category:** Policy
**Priority:** P2
**Source:** `src/services/apiCalendar/apiCalendar.ts:86-100`
**Plain English:** When no options are given, the end-of-year balance request asks for expand=all and details=balanceSum.
**Specification:**
  Given A request for employee E1 end-of-year balances from 2026-01-01 with no query options
  When  It is sent
  Then  The URL ends with /endofyear/2026-01-01?expand=all&details=balanceSum
**Parameters:** expand default 'all'; details default 'balanceSum'
**Confidence:** High

### RULE-119: Calendar list scrolls back at most 24 months, newest first
**App:** vmm
**Capability:** CAP-002
**Category:** Policy
**Priority:** P2
**Source:** `src/services/queryApi/queryEndpointsCalendar/queryEndpointsCalendar.ts:147-167 (cap constant at line 17)`
**Plain English:** The list view starts at the current month and loads one earlier month per page as the user scrolls, stopping after 24 months; days in each month are listed newest first.
**Specification:**
  Given Today is 2026-09-28 and 24 monthly pages are already loaded (Sep 2026 back to Oct 2024)
  When  The user reaches the end of the list
  Then  No further month is requested
**Parameters:** AGENDA_MONTHS_CAP = 24; page key = month start YYYY-MM-DD; currently mock data (line 161-164)
**Suspected defect:** Also served from mock data, like the grid.
**Confidence:** High

## Formatting

### RULE-120: Input-type display: hours rounded to whole numbers, percent divided by 100, quantity as 'Name: value'
**App:** me-ios
**Capability:** CAP-024
**Category:** Formatting
**Priority:** P1
**Source:** `EmployeeServices/CalendarInterface/Sources/CalendarInterface/FormatStyles/AbsenceType/AbsenceTypeFormatStyle.swift:448-511 (helpers at 422-445)`
**Plain English:** The input type of a registration is shown by kind. DefiniteTime shows a time interval. FullDay shows the option name. Hours shows the hour value rounded to 0 decimals plus the unit. Percent shows value/100 as a locale percent. Quantity shows 'Name: value'.
**Specification:**
  Given An Hours option with value '7.5' and name 'hours'; a Percent option with value '50'; a Quantity option 'Km' with value '42'
  When  formatted in en_US
  Then  it reads '8 hours', '50%', 'Km: 42'
**Parameters:** hours precision fractionLength(0); percent input parsed in base locale and divided by 100
**Edge cases handled:** An unknown input type shows the raw value. A DefiniteTime without both dates shows ''.
**Suspected defect:** Hours are rounded to whole numbers, so 7.5 hours reads as '8 hours'. The user may confirm a registration showing a different value from the one that will be saved.
**Confidence:** High: Should partial hours (e.g. 7.5) be shown with decimals in the registration summary?

### RULE-121: Registration dates shown and picked in the absence time zone
**App:** me-ios
**Capability:** CAP-012
**Category:** Formatting
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/Cells/DateTableViewCell.swift:45-113`
**Plain English:** Dates are displayed with the app-locale UTC date format and picked in the absence time zone, requiring explicit confirmation in the picker.
**Specification:**
  Given A FromDate stored as 2025-03-10 UTC and a user in UTC-5
  When  The date row is shown
  Then  It shows 10 March 2025 (not 9 March)
**Parameters:** Constants.utcAppLocaleDateFormatter; Constants.absenceTimeZone; requiresConfirmation = true
**Confidence:** High

### RULE-122: Hours/percent values converted between local and JSON decimal format
**App:** me-ios
**Capability:** CAP-012
**Category:** Formatting
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/SectionViewModels/FormFieldCellViewModels/NumberFieldCellViewModel.swift:27-39 (formatters: EmployeeServices/EmployeeCore/Sources/E…`
**Plain English:** Numbers are shown in the user's regional format and stored in JSON (dot-decimal) format; a stored value of '0' is shown as an empty field; percent fields show a % sign.
**Specification:**
  Given A Norwegian-locale user and a stored Hours value '7.5'
  When  The field is displayed and the user retypes '3,25'
  Then  It shows '7,5' and stores '3.25'
**Parameters:** StringUtils.convertToLocalRegion / convertFromLocalRegion / convertToJSON
**Edge cases handled:** Unparseable input is stored as '0'.
**Confidence:** High

### RULE-123: Balances summary hours and amounts formatting
**App:** me-ios
**Capability:** CAP-010
**Category:** Formatting
**Priority:** P1
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/BalancesOverview/Mapper/BalancesOverviewUIModel.Mapper.swift:148-173`
**Plain English:** Balance durations are shown with the balance duration format and amounts in the user's locale with up to two decimals followed by the unit.
**Specification:**
  Given A vacation balance of 12.345 with unit 'days' for a Norwegian locale, and a summary item of 7.5 hours
  When  The balances overview is shown
  Then  The balance reads '12,35 days' and the summary item is a 7 h 30 min duration
**Parameters:** fractionLength 0...2; duration = hours * 3600 s (BalancesOverview.Mapper 169-173)
**Edge cases handled:** Option-valued balances with no matching option show blank.
**Confidence:** High

### RULE-124: Claim list row: date as day plus upper-case short month, amount with 2 decimals, status text
**App:** me-ios
**Capability:** CAP-028
**Category:** Formatting
**Priority:** P2
**Source:** `Employee/CalendarLeftover/CalendarViewModelClaim.swift:62-87`
**Plain English:** Each claim row shows the title, the amount in the device locale with exactly 2 decimals and no currency symbol, the approval status text, and the start date as day plus upper-case short month.
**Specification:**
  Given A claim 'Taxi' of 1234.5 dated 2026-01-11 with status 'sent', and a device locale of en_US
  When  the row is shown
  Then  it reads 'Taxi', '1,234.50', 'Awaiting approval', '11 JAN'
**Parameters:** min and max fraction digits = 2; status mapping approved→Approved, open→Not sent, paid→Paid, canceled→Cancelled, rejected/denied→Declined, sent/pending/notApproved→Awaiting approval, awaitingClearance→Awaiting clearance (CalendarUtils.getApprovalText)
**Edge cases handled:** A missing amount shows an empty string. An unknown status shows empty text. No currency code is shown.
**Confidence:** Medium: Claims can be in foreign currencies. Is showing the amount without a currency intended?

### RULE-125: Expense claims list is grouped by year, newest first, with undated claims in their own section
**App:** me-ios
**Capability:** CAP-028
**Category:** Formatting
**Priority:** P2
**Source:** `Employee/CalendarLeftover/ClaimsCalendarViewModel.swift:240-259`
**Plain English:** Claims are put into one section per start-date year. Sections run from newest year to oldest, and claims within a section from newest to oldest. Claims without a date go into a 'Claims without date' section.
**Specification:**
  Given Claims dated 2026-03-10, 2025-12-01 and one claim without a date
  When  the claims list is shown
  Then  sections read 'Claims without date' (1 claim), '2026' (1 claim) and '2025' (1 claim)
**Parameters:** Section key = start of year of dateFrom, or Date.distantFuture when there is no date; sort descending
**Edge cases handled:** Undated claims use distantFuture as their key, so their section sorts first. The year title uses the locale year formatter (lines 203-209).
**Confidence:** High

### RULE-126: Several cards of the same vacation kind are grouped
**App:** me-ios
**Capability:** CAP-017
**Category:** Formatting
**Priority:** P2
**Source:** `Employee/StartPage/Tasks/GetCalendarItemsTask.swift:28-45`
**Plain English:** When more than one Approved, Declined or Upcoming vacation card exists, the cards are combined into one grouped card. Ongoing vacation and parental leave cards show only the first item of their kind.
**Specification:**
  Given Two approved vacations both start more than 14 days ahead, and two approved parental leaves are ongoing today
  When  the start page shows cards
  Then  one grouped card holds the two approved vacations, and only one Ongoing Parental Leave card is shown
**Parameters:** Grouping applies to ApprovedVacation, DeclinedVacation and UpcomingVacation when count > 1
**Edge cases handled:** Grouping uses the type name. For Ongoing Vacation, Ongoing Parental Leave and Upcoming Parental Leave, only items.first is kept and the other items are silently hidden.
**Suspected defect:** A second overlapping ongoing or upcoming parental leave, or a second ongoing vacation, is dropped from the start page.
**Confidence:** Medium: Should overlapping ongoing vacations or parental leaves each get a card, or be grouped, instead of showing only the first one?

### RULE-127: Balance durations shown as hours and minutes, zero units hidden
**App:** me-ios
**Capability:** CAP-010
**Category:** Formatting
**Priority:** P2
**Source:** `EmployeeServices/CalendarInterface/Sources/CalendarInterface/DomainModel/Balances/BalanceDurationFormatStyle.swift:3-18`
**Plain English:** Time balances are shown in narrow hours and minutes, zero units are left out, and commas are removed.
**Specification:**
  Given A balance of 37 hours 30 minutes / 8 hours 0 minutes, en_US locale
  When  shown
  Then  it reads '37h 30m' / '8h'
**Parameters:** allowed units hours and minutes; width narrow; zeroValueUnits hide
**Edge cases handled:** Days are never used, so 300 hours shows as '300h'. The sign of negative balances follows the platform format.
**Confidence:** High

### RULE-128: Registration summary text (chatbot style): name, date range, input type
**App:** me-ios
**Capability:** CAP-024
**Category:** Formatting
**Priority:** P2
**Source:** `EmployeeServices/CalendarInterface/Sources/CalendarInterface/FormatStyles/AbsenceType/AbsenceTypeFormatStyle.swift:144-168`
**Plain English:** A predicted registration is summarized as display name, day-and-month date or interval, and input type, joined with ', ' and skipping empty parts. Dates are read in GMT, and numbers from the server are parsed in the base (invariant) locale.
**Specification:**
  Given Vacation from 2026-10-05T00:00:00 to 2026-10-09T00:00:00, input type FullDay 'Full day', en_US
  When  the summary is shown
  Then  it reads roughly 'Vacation, 10/5 – 10/9, Full day'
**Parameters:** separator ', '; time zone GMT; numberInputLocale = Constants.Locales.Base; the input time style is shortened
**Confidence:** High

### RULE-129: Changing the number-input locale on the input-type style has no effect
**App:** me-ios
**Capability:** CAP-024
**Category:** Formatting
**Priority:** P2
**Source:** `EmployeeServices/CalendarInterface/Sources/CalendarInterface/FormatStyles/AbsenceType/AbsenceTypeFormatStyle.swift:269-273`
**Plain English:** Setting a number-input locale should change how server numbers are parsed, but the input-type style assigns its own old value back.
**Specification:**
  Given A style built with numberInputLocale Base, then .numberInputLocale(nb_NO)
  When  an Hours value '7,5' is formatted
  Then  it is still parsed with the Base locale, fails, and shows ''
**Parameters:** none
**Suspected defect:** `style.numberInputLocale = numberInputLocale` ignores the `locale` parameter.
**Confidence:** High

### RULE-130: Dimension option display as 'id - name'
**App:** me-ios
**Capability:** CAP-013
**Category:** Formatting
**Priority:** P2
**Source:** `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/AbsenceField.swift:280-287`
**Plain English:** A selectable option is shown as its id and name joined with ' - ', leaving out empty parts.
**Specification:**
  Given An option with id '4010' and name 'Sales Oslo' / only name 'Sales'
  When  shown
  Then  it reads '4010 - Sales Oslo' / 'Sales'
**Parameters:** separator ' - '
**Confidence:** High

### RULE-131: Absence type colours
**App:** me-ios
**Capability:** CAP-001
**Category:** Formatting
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrationUtils.swift:146-174`
**Plain English:** Parental leave is shown in warning colour, sickness/sick child/absence in error colour, vacation in success colour and attendance/supplement in information colour.
**Specification:**
  Given A vacation and a sick-child entry on the same day
  When  The month grid is shown
  Then  Vacation is green (success) and sick child red (error)
**Edge cases handled:** Unknown type uses success icon colour with page background.
**Confidence:** High

### RULE-132: Dimension value shown as 'id - name'
**App:** me-ios
**Capability:** CAP-013
**Category:** Formatting
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/SectionViewModels/DimensionFieldsSectionViewModel.swift:36-54,83-87`
**Plain English:** A selected dimension value is displayed as its id and name separated by ' - ', and a saved value missing from the recent list is added to it.
**Specification:**
  Given Project value id '1001' named 'Internal'
  When  The dimension row is shown
  Then  It reads '1001 - Internal'
**Parameters:** separator ' - '
**Edge cases handled:** Empty parts are omitted.
**Confidence:** High

### RULE-133: Required text fields labelled '(required)' in the placeholder
**App:** me-ios
**Capability:** CAP-012
**Category:** Formatting
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/SectionViewModels/FormFieldCellViewModels/StringFieldCellViewModel.swift:51-59`
**Plain English:** Free-text fields show their name, '(required)' if required, and the server hint text below.
**Specification:**
  Given A required Comment field with hint 'Describe the reason'
  When  The field is empty
  Then  Placeholder reads 'Comment (required)' followed by the hint
**Parameters:** S.fieldRequiredText
**Confidence:** High

### RULE-134: Remaining vacation days message
**App:** me-ios
**Capability:** CAP-012
**Category:** Formatting
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:433-448`
**Plain English:** If the template returns a remaining-vacation balance, the form shows it with singular/plural wording, and in red when zero.
**Specification:**
  Given A Vacation template with remainingVacationDays 0, 1 and 12.5
  When  The footer of the dates section is shown
  Then  0 shows the zero message in red, 1 the singular message, 12.5 the plural message with '12.5'
**Parameters:** keys ABSENCE_VACATION_DAYS_REMAINING(_ZERO/_PLURAL); cleanValue drops '.0'
**Edge cases handled:** Negative balances use the plural wording without red. Shown only under section index 1.
**Confidence:** High

### RULE-135: Absence type search is case-insensitive across groups
**App:** me-ios
**Capability:** CAP-012
**Category:** Formatting
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceTypeSelectorViewModel.swift:19-31`
**Plain English:** Searching the absence type list matches any type whose name contains the search text, ignoring case, across all groups.
**Specification:**
  Given Groups containing 'Vacation' and 'Vacation - advance'
  When  The user searches 'vac'
  Then  Both types are listed in a flat list
**Parameters:** lowercased contains
**Edge cases handled:** Group headers themselves only match if they have no children.
**Confidence:** High

### RULE-136: Absence details hide empty and full-day fields and show approval status
**App:** me-ios
**Capability:** CAP-014
**Category:** Formatting
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Absence/AbsenceViewTableViewController.swift:232-263`
**Plain English:** The absence detail screen omits the input type when it is Full day, hides fields with empty values, shows an approval status section only when there is status text (with the approver's comment on a new line), and shows the comment only if filled.
**Specification:**
  Given A vacation with InputType FullDay, empty Child, status 'Rejected' and approver comment 'Busy week'
  When  The detail screen loads
  Then  It shows status 'Rejected' with 'Busy week' below, no input type row and no child row
**Parameters:** FieldOptionItem.Name.fullDay; approversComment appended (464-478)
**Confidence:** High

### RULE-137: Definite-time and hours shown in the details
**App:** me-ios
**Capability:** CAP-014
**Category:** Formatting
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Absence/AbsenceViewTableViewController.swift:418-426`
**Plain English:** In details, a definite-time absence shows 'start - end' in UTC time, and an hours absence shows a compact hours duration.
**Specification:**
  Given A definite-time absence 2025-03-10 08:30 to 12:00 UTC
  When  The input type row is shown
  Then  It reads '08:30 - 12:00'
**Parameters:** Constants.utcTimeFormatter; CalendarUtils.compactHoursDuration
**Confidence:** High

### RULE-138: Time confirmation marker on calendar days
**App:** me-ios
**Capability:** CAP-001
**Category:** Formatting
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/Components/CalendarDayView.swift:103-115`
**Plain English:** Days of the shown month get a green marker when time is approved and a secondary-colour marker when confirmed but awaiting approval; other-month days get none.
**Specification:**
  Given 10 March approved, 11 March confirmed
  When  March is shown
  Then  10 March has a green bar, 11 March a secondary bar
**Parameters:** texts: approved -> 'Timesheet approved', pending -> 'Awaiting approval' (AbsenceRegistrationUtils 80-87)
**Edge cases handled:** Approved wins over confirmed.
**Confidence:** High

### RULE-139: Day sheet title shows the numeric date in the calendar's locale
**App:** me-ios
**Capability:** CAP-004
**Category:** Formatting
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/DayDetailFeature.swift:30-33`
**Plain English:** The day sheet title is the tapped date in numeric format, using the calendar's locale and time zone. Roster events are meant to be listed first.
**Specification:**
  Given A tap on 15 September 2026 with locale nb-NO
  When  The sheet opens
  Then  The title reads '15.09.2026'.
**Parameters:** Date.FormatStyle(date: .numeric, time: .omitted)
**Suspected defect:** `day.events.sorted { lhs, _ in lhs.isRosterType }` is not a valid ordering (it returns true for roster-vs-roster), so the order of events is undefined and roster-first is not guaranteed.
**Confidence:** Medium: Should roster shifts always be listed first in the day sheet, with the other events keeping their original order?

### RULE-140: Approval status colour and emphasis
**App:** me-ios
**Capability:** CAP-002
**Category:** Formatting
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarUtils.swift:298-316`
**Plain English:** Approved shows in the success colour. Paid, sent, pending, open and notApproved show in the information colour. Rejected, denied and canceled show in the error colour. Awaiting clearance shows in purple. Statuses that need the user's attention are shown in bold (lines 266-280).
**Specification:**
  Given An absence with status 'rejected'
  When  Its row is drawn
  Then  'Declined' appears in the error colour, in bold footnote.
**Parameters:** Bold statuses: sent, rejected, denied, pending, notApproved, awaitingClearance
**Confidence:** High

### RULE-141: Approval status labels
**App:** me-ios
**Capability:** CAP-002
**Category:** Formatting
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarUtils.swift:322-346`
**Plain English:** The request status from the server is mapped to a user-facing label, ignoring case. Unknown statuses show no label.
**Specification:**
  Given Absence rows with statuses 'OPEN', 'denied', 'sent' and 'awaitingClearance'
  When  The list rows are shown
  Then  The labels read 'Not sent', 'Declined', 'Awaiting approval' and 'Awaiting clearance'. 'approved' gives 'Approved', 'paid' gives 'Paid', 'canceled' gives 'Cancelled', and 'foo' gives an empty label.
**Parameters:** approved→Approved; open→Not sent; paid→Paid; canceled→Cancelled; rejected, denied→Declined; sent, pending, notApproved→Awaiting approval; awaitingClearance→Awaiting clearance
**Confidence:** High

### RULE-142: Absence description text depends on the input type
**App:** me-ios
**Capability:** CAP-002
**Category:** Formatting
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarUtils.swift:37-106`
**Plain English:** Each absence gets a subtitle built from its input type. Hours shows a compact duration. Percent shows 'N%'. Quantity shows 'N <quantity>'. Definite time shows the UTC 'HH:mm - HH:mm' range. Full day shows nothing on a single day. Multi-day absences also get the short date period.
**Specification:**
  Given A Percent absence with property percent=50 from 2026-09-01 to 2026-09-03, and a single-day Definite Time absence from 08:00 to 12:00 UTC
  When  Their descriptions are built
  Then  The first reads '50% <short period 1-3 Sep>'. The second reads '08:00 - 12:00'. A single-day Full Day absence has no description.
**Parameters:** Property names are matched case-insensitively: 'hours', 'percent', 'quantity'. Times are formatted in UTC.
**Suspected defect:** A Percent or Quantity absence with the property missing returns no description at all, which also drops the multi-day date period.
**Confidence:** High

### RULE-143: Month headings and the jump-to-date picker use GMT
**App:** me-ios
**Capability:** CAP-002
**Category:** Formatting
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/ViewControllerModels/SectionsSingleSourceCalendarViewModel.swift:119-130`
**Plain English:** Section headings show the month name computed in GMT. The navigation bar shows the abbreviated month and year in the app's language (FormatStyles.swift:13). The jump-to-date picker works in GMT and needs Done to apply (CalendarHeaderView.swift:70-83).
**Specification:**
  Given A section keyed 2026-09-01 UTC and the app language Norwegian
  When  The list shows it
  Then  The heading shows the September month name, and the navigation bar reads 'sep. 2026'.
**Parameters:** timeZone .gmt; format .month(.abbreviated).year() in the app locale
**Confidence:** High

### RULE-144: Register-time options: confirm-time first, absence types in a fixed order
**App:** me-ios
**Capability:** CAP-012
**Category:** Formatting
**Priority:** P2
**Source:** `Modules/CalendarFeature/Sources/CalendarFeature/Service/AbsenceService.swift:80-127`
**Plain English:** In the registration type picker, 'Confirm time to' appears first when the confirm-time template has at least one field item, followed by the server's template groups. The helper that would order templates as Attendance, Sickness, SickChild, Vacation, Absence, ParentalLeave, Supplement (lines 24-32, 76-78) is only called from tests.
**Specification:**
  Given A confirm-time template with one field item and groups [Absence, Time]
  When  The picker opens
  Then  The options are 'Confirm time to', then the Absence group, then the Time group.
**Parameters:** absenceEventTypeOrder = [Attendance, Sickness, SickChild, Vacation, Absence, ParentalLeave, Supplement]
**Confidence:** Medium: Should the fixed absence-type order be applied in the picker? Right now only tests use it.

### RULE-145: Synced event titles read 'label Lastname Firstname' with forced capitalisation
**App:** vmm
**Capability:** CAP-007
**Category:** Formatting
**Priority:** P2
**Source:** `src/hooks/useSyncCalendar.ts:106-108`
**Plain English:** The birthday event title is the translated 'Birthday' label, two spaces, then last name and first name, each with its first letter upper case and the rest lower case.
**Specification:**
  Given Employee lastName 'McDonald', firstName 'ANNE' and label 'Birthday'
  When  The birthday event is created
  Then  The title is 'Birthday Mcdonald Anne'; the anniversary title (line 183) is 'Anniversary Mcdonald Anne' (double space after the last name)
**Parameters:** Uses personNames[0]; lodash capitalize
**Suspected defect:** capitalize lowercases the rest of the name (McDonald becomes Mcdonald, 'van der Berg' becomes 'Van der berg'); the double space is in a different place in each title; the code crashes if personNames is empty.
**Confidence:** High

### RULE-146: Week numbers are ISO weeks shown on the Monday cell
**App:** vmm
**Capability:** CAP-005
**Category:** Formatting
**Priority:** P2
**Source:** `src/screens/EmployeeCalendarScreen/EmployeeCalendarScreen.tsx:276-277`
**Plain English:** When week numbers are on, each Monday cell shows the ISO-8601 week number.
**Specification:**
  Given Show week numbers = on
  When  The grid shows 2026-09-28 (a Monday)
  Then  That cell shows week number 40
**Parameters:** calendarShowWeekNumbers default true; ISO week (also WeekdayCalendarGrid.tsx:120)
**Confidence:** High

### RULE-147: Month grid weeks start on Monday and move one month per arrow tap
**App:** vmm
**Capability:** CAP-001
**Category:** Formatting
**Priority:** P2
**Source:** `src/screens/EmployeeCalendarScreen/EmployeeCalendarScreen.tsx:428-430 (arrows: 199-205, wired at 230-235)`
**Plain English:** The 7-day grid starts weeks on Monday, month swiping is off, and the arrows move exactly one month back or forward.
**Specification:**
  Given The grid shows September 2026
  When  The user taps the previous-month arrow
  Then  August 2026 is shown with Monday as the first column
**Parameters:** firstDay=1; enableSwipeMonths=false; arrows at lines 199-205
**Confidence:** High

### RULE-148: Entry type decides icon and colour
**App:** vmm
**Capability:** CAP-001
**Category:** Formatting
**Priority:** P2
**Source:** `src/screens/EmployeeCalendarScreen/calendarEventStyles.ts:17-69`
**Plain English:** Vacation shows a green palm tree, Sickness a red medical case, Absence a red away icon, Attendance a blue work icon, Supplement a blue timesheet icon, Allowance an orange allowance icon; any other type shows blue normal time.
**Specification:**
  Given An entry with itemType 'Sickness'
  When  It is drawn in the grid
  Then  It shows the briefcase-medical icon in the error (red) colour on a light red background
**Parameters:** Type-to-icon mapping as listed
**Confidence:** High

### RULE-149: List view subtitle shows hours, quantity or time range
**App:** vmm
**Capability:** CAP-002
**Category:** Formatting
**Priority:** P2
**Source:** `src/screens/EmployeeCalendarScreen/components/EmployeeCalendarAgendaView/EmployeeCalendarAgendaView.tsx:38-50`
**Plain English:** In the list, full-day entries have no subtitle; otherwise an 'Hours' property shows as '<value>h', else a 'Quantity' property as 'x<value>', else a DefiniteTime entry as 'HH:mm - HH:mm'.
**Specification:**
  Given An entry with inputType 'Hours' and property Hours = '7.5'
  When  It appears in the list
  Then  The subtitle reads '7.5h'
**Parameters:** Property names 'Hours', 'Quantity'
**Confidence:** High

### RULE-150: Calendar date headings are capitalised in the app language
**App:** vmm
**Capability:** CAP-002
**Category:** Formatting
**Priority:** P2
**Source:** `src/screens/EmployeeCalendarScreen/components/EmployeeCalendarAgendaView/EmployeeCalendarAgendaView.tsx:62-77`
**Plain English:** The list adds a month heading wherever the month changes, formatted in the app language with the first letter upper case (Nordic month names are lowercase by default); the day sheet header does the same with the long date.
**Specification:**
  Given App language Norwegian and list entries in 'september 2026'
  When  The list is shown
  Then  The sticky header starts with 'September'
**Parameters:** formatLocaleDateHeaderTask / formatLocaleLongDate (utils, outside this area); day sheet at EmployeeCalendarDayDetail.tsx:53-54
**Confidence:** High

### RULE-151: A day cell shows at most two entries plus a '+N' count
**App:** vmm
**Capability:** CAP-001
**Category:** Formatting
**Priority:** P2
**Source:** `src/screens/EmployeeCalendarScreen/components/EmployeeCalendarDayCell.tsx:39-105`
**Plain English:** Each day shows the first two entries (as icons or text labels, depending on the style setting) and '+N' for the rest; days outside the shown month cannot be tapped.
**Specification:**
  Given A day with 5 entries
  When  The grid is shown
  Then  Two entries and '+3' are displayed; tapping a greyed next-month day does nothing
**Parameters:** MAX_VISIBLE_ENTRIES = 2; display mode default 'icons'
**Confidence:** High

### RULE-152: Day sheet time label: 'Full day' or a 24-hour time range
**App:** vmm
**Capability:** CAP-004
**Category:** Formatting
**Priority:** P2
**Source:** `src/screens/EmployeeCalendarScreen/components/EmployeeCalendarDayDetail.tsx:38-91`
**Plain English:** Full-day entries show the 'Full day' label; other entries show 'HH:mm - HH:mm', or nothing if both times are 00:00; a subtitle, if any, comes first followed by ' · '.
**Specification:**
  Given A DefiniteTime entry from 2026-04-09T16:00 to 17:00 without subtitle
  When  The day sheet is shown
  Then  The line reads '16:00 - 17:00'
**Parameters:** Format HH:mm, whatever the locale
**Suspected defect:** Hours and Quantity entries show a clock range here but '7.5h' or 'x3' in the list view, so the same entry reads differently in the two views.
**Confidence:** High

### RULE-153: Hide-weekends grid shows Monday to Friday rows only
**App:** vmm
**Capability:** CAP-005
**Category:** Formatting
**Priority:** P2
**Source:** `src/screens/EmployeeCalendarScreen/components/WeekdayCalendarGrid/WeekdayCalendarGrid.tsx:33-81 (tap blocking: src/screens/EmployeeCalendarScreen/components/EmployeeCalendarDayCell.tsx:54-61)`
**Plain English:** With weekends hidden, the grid runs from the Monday on or before the 1st to the Friday on or after the last day, in rows of 5; days from other months are greyed out and cannot be tapped.
**Specification:**
  Given Hide weekends = on and month October 2026 (ends Saturday 31)
  When  The grid is shown
  Then  It ends with a full row 2 to 6 November 2026, all greyed out; August 2026 (starts Saturday) begins with a greyed row 27 to 31 July
**Parameters:** Row length 5; hide weekends default false
**Suspected defect:** Walking forward to the next Friday when the month ends on a weekend (and back to Monday when it starts on one) adds a whole row with no days of the shown month.
**Confidence:** Medium: Should months that start or end on a weekend get an extra row with only the adjacent month's weekdays?

## Rules requiring SME confirmation

- **RULE-005** (P1, vmm): Is it intended that a 29 February birthday is stored on 28 February (moment clamps the date in non-leap 2026) and then repeats on 28 Feb every year, and that dates are computed in UTC, which can show the event one day early in time zones west of UTC?
- **RULE-006** (P1, vmm): Should the target date be the user's local date? And is details=sickness12months also correct for the sick-child current-year summary?
- **RULE-009** (P2, me-ios): Should weekends come from the company's work calendar or the locale rather than a fixed Saturday and Sunday?
- **RULE-020** (P1, me-ios): Does the server ever send FromDate/ToDate as date-only for predicted registrations?
- **RULE-021** (P1, me-ios): Does the server define 'GreaterThan X' as 'error when the date is greater than X'? The client assumes so.
- **RULE-025** (P1, me-ios): Is clearing an existing comment on focus intended, or should only the placeholder be cleared?
- **RULE-036** (P1, me-ios): Should confirming through the agent apply the same Error and Warning checks as the calendar's Confirm time, or does the prediction service already check them?
- **RULE-039** (P2, me-ios): Can two roster shifts start at the same time (split shifts)? The id would collide.
- **RULE-041** (P2, me-ios): Should public holidays be shown differently from other special days? The client currently discards isPublicHoliday.
- **RULE-047** (P2, vmm): Should the year range be fixed to today's year? It is based on the year shown, so repeated picks (and the arrows) can reach any year, while the list view is capped at 24 months back.
- **RULE-048** (P1, me-ios): What decides dataSource.isEnabled (a company setting, role or feature flag)? The target app has to reproduce it.
- **RULE-054** (P1, me-ios): Should the edit check-in screen refuse to open (invalidInputData) when the update or delete link is missing, as verifyInputData intends?
- **RULE-068** (P2, me-ios): Should a user with absence permissions and expense claims really see the tab as 'Claims' rather than 'Calendar'?
- **RULE-075** (P1, me-ios): Should the server stamp check-in time instead of trusting the device clock?
- **RULE-077** (P1, me-ios): Is ConfirmationRequired only for balance overdraft, or also for other policy warnings? The server decides, and the merged app needs the same confirm step.
- **RULE-080** (P1, me-ios): Should the grid map sent, denied, notApproved, awaitingClearance, open, paid and canceled the way the list does? Right now they show no status in the day detail.
- **RULE-086** (P1, vmm): Should turning sync on keep (or recreate) events that already exist for an employee, instead of deleting them?
- **RULE-096** (P1, me-ios): Is losing the chat history on close intended, or should the conversation be kept for the session?
- **RULE-101** (P1, vmm): Is it acceptable for a production build to show fabricated sickness and vacation entries for real employees, or should the screen be hidden until the live feed (commented out at lines 77-139) is enabled?
- **RULE-114** (P2, me-ios): Is a hard-coded third-party Google Form approved for collecting employee feedback, or should the address come from configuration or an internal channel?
- **RULE-115** (P2, vmm): Is a fixed 2-second wait an acceptable way to decide success, given that event saves are not awaited?
- **RULE-117** (P2, vmm): What does the server do with an empty 'today' value: use its own current date, or ignore future registrations?
- **RULE-120** (P1, me-ios): Should partial hours (e.g. 7.5) be shown with decimals in the registration summary?
- **RULE-124** (P2, me-ios): Claims can be in foreign currencies. Is showing the amount without a currency intended?
- **RULE-126** (P2, me-ios): Should overlapping ongoing vacations or parental leaves each get a card, or be grouped, instead of showing only the first one?
- **RULE-139** (P2, me-ios): Should roster shifts always be listed first in the day sheet, with the other events keeping their original order?
- **RULE-144** (P2, me-ios): Should the fixed absence-type order be applied in the picker? Right now only tests use it.
- **RULE-153** (P2, vmm): Should months that start or end on a weekend get an extra row with only the adjacent month's weekdays?
