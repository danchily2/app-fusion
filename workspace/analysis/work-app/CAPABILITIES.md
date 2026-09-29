# Capabilities: work-app

29 capabilities across 2 apps (vmm = Manager, me-ios = Employee), generated 2026-09-28T17:38:59+00:00. Each capability is one thing a person can do. Its fusion class says what the new app must do with it:

- **unique**: one product has it. Carry it over, or a person drops it.
- **shared-same**: both products do it the same way. Build it once.
- **shared-diverged**: both do it differently. A person decides which behavior survives (`fuse-review`).
- **new**: only the design has it. It needs a spec before it can be built.

| Fusion class | Capabilities |
| --- | --- |
| unique | 24 |
| shared-diverged | 5 |

## Matrix

| Id | Capability | Domain | Fusion | vmm | me-ios | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| CAP-001 | View a calendar month by month | Calendar | shared-diverged | yes | yes | Medium |
| CAP-002 | Browse the calendar as a scrolling list | Calendar | shared-diverged | yes | yes | High |
| CAP-003 | Switch between list and month view of the calendar | Calendar | shared-diverged | yes | yes | Medium |
| CAP-004 | See the details of a calendar day | Calendar | shared-diverged | yes | yes | High |
| CAP-005 | Customize what the calendar shows | Calendar | shared-diverged | yes | yes | High |
| CAP-006 | Start a time or absence registration from the calendar | Calendar | unique |  | yes | High |
| CAP-007 | Sync team birthdays and work anniversaries to my calendar | Team overview | unique | yes |  | Medium |
| CAP-008 | See how many team members are absent today | Team overview | unique | yes |  | Medium |
| CAP-009 | View an employee's absence balances | Balances | unique | yes |  | High |
| CAP-010 | See my time and absence balances for a month | Balances | unique |  | yes | High |
| CAP-011 | See my vacation balances on the start page | Balances | unique |  | yes | High |
| CAP-012 | Register an absence or time event | Absence registration | unique |  | yes | High |
| CAP-013 | Pick cost-unit dimension values for a registration | Absence registration | unique |  | yes | High |
| CAP-014 | View details of a registered absence | Absence registration | unique |  | yes | High |
| CAP-015 | Edit a registered absence | Absence registration | unique |  | yes | High |
| CAP-016 | Delete a registered absence | Absence registration | unique |  | yes | High |
| CAP-017 | See upcoming and ongoing vacation and parental leave on the start page | Absence registration | unique |  | yes | High |
| CAP-018 | Check in and check out for the workday | Time tracking | unique |  | yes | High |
| CAP-019 | Edit or delete a check-in/check-out registration | Time tracking | unique |  | yes | High |
| CAP-020 | Confirm worked time up to a date | Time tracking | unique |  | yes | High |
| CAP-021 | Register time or absence by chatting with the Employee Agent | Employee Agent | unique |  | yes | High |
| CAP-022 | Confirm the time sheet through the Employee Agent | Employee Agent | unique |  | yes | High |
| CAP-023 | Ask the Employee Agent about leave balances | Employee Agent | unique |  | yes | High |
| CAP-024 | Edit a predicted registration before saving it | Employee Agent | unique |  | yes | High |
| CAP-025 | View, edit or delete an absence created in the agent chat | Employee Agent | unique |  | yes | High |
| CAP-026 | Learn how to use the Employee Agent and try example prompts | Employee Agent | unique |  | yes | High |
| CAP-027 | Send feedback about the Employee Agent | Employee Agent | unique |  | yes | High |
| CAP-028 | Browse my expense claims by year and filter by status | Expenses | unique |  | yes | High |
| CAP-029 | Browse my payslips by payment date, filtered by employer | Pay | unique |  | yes | High |

## Calendar

Browse, navigate and customize calendars of work, absence, roster and special days (own or an employee's).

### CAP-001: View a calendar month by month

**Fusion:** shared-diverged · **Personas:** Manager, Employee · **Confidence:** Medium

Open a month grid of calendar entries (attendance, absence, supplement and, in Employee, roster shifts and special days) and move between months with arrows, swipes or a month/year picker. The Manager product shows an employee's calendar. The Employee product shows the user's own calendar.

- **vmm** (Manager): screens: `EmployeeCalendarScreen (SCREEN_NAME_EMPLOYEE_CALENDAR = 'EmployeeCalendarScreen…`, `CalendarMonthYearPicker`, `WeekdayCalendarGrid`, `EmployeeCalendarDayCell`; endpoints: `GET https://mobileemployee.visma.net/employee/api/v2/calendar/my-employees/feed…`; storage: `redux settings.calendarViewMode`, `settings.calendarHideWeekends`, `settings.calendarShowWeekNumbers`, `settings.calendarShowAttendance`, `settings.calendarShowAbsence`, `settings.calendarShowSupplement`, `settings.calendarDisplayMode`; platform: `react-native` · evidence `src/screens/EmployeeCalendarScreen/EmployeeCalendarScreen.tsx:128-149`
- **me-ios** (Employee): screens: `CalendarGridFeature`, `CalendarMonthYearNavigationFeature`, `DayDetailFeature (destination)`, `CalendarGridRepository (CalendarFeature)`; endpoints: `GET /employee/api/v2/Calendar/specialdays`, `GET /employee/api/v1/employees/{odpUserId}/calendar/workshift`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/CalendarGridFeature.swift:185-491; Em…`

**How they differ:**
- Subject: vmm shows the calendar of an employee chosen from the manager's HRM or Approval stack (route.params companyId/employeeId, EmployeeCalendarScreen.tsx:105; HrmNavConfig.tsx:141; ApprovalNavConfig.tsx:115). me-ios shows the signed-in user's own calendar (userService.getCurrentUserId, Calendar…
- Endpoint: vmm is wired to the aggregate v2 calendar/my-employees/feed, but it currently serves mock data (queryEndpointsCalendar.ts:72-75). me-ios calls /employee/api/v1/employees/{odpUserId}/calendar/feed (CalendarService.swift:103-110), /employee/api/v1/employees/{odpUserId}/calendar/workshift (G…
- Content: me-ios adds roster shifts, special days and a confirm-time capability (CalendarGridFeature.swift:81, CalendarService.swift:76-101), plus a roster filter (showRoster, CalendarGridFeature.swift:196). vmm filters only attendance, absence and supplement (EmployeeCalendarScreen.tsx:139-147).
- Week start and row count: vmm fixes Monday as the week start (WeekdayCalendarGrid.tsx:37-38) and sizes day height from the number of weeks in the month (EmployeeCalendarScreen.tsx:250-256). me-ios starts on the locale's calendar.firstWeekday and also uses a variable number of weeks (CalendarViewUti…
- Year picker range: vmm offers the current year -2 to +5 (CalendarMonthYearPicker.tsx:20-21,55-63). me-ios offers +/-20 years (CalendarGridConfiguration.swift:25, CalendarMonthYearNavigationFeature.swift:39).
- Navigation: me-ios supports swiping between months (CalendarGridView.swift:117-132, CalendarGridFeature.swift:204-208) and reloads the current month when the app returns to the foreground (CalendarContainerViewController.swift:444-447). vmm offers only the arrow buttons and the month/year picker (E…
- Loading and offline: vmm skips the feed while companyTenantId is unresolved from the cached employees list (EmployeeCalendarScreen.tsx:116-136). me-ios delays its progress indicator by 0.1 s (CalendarGridFeature.swift:170) and shows an offline empty state with S.calendarOfflineText (CalendarGridVie…
- Day tap (missed by the claim): in vmm, tapping a day opens a bottom sheet for that day (EmployeeCalendarScreen.tsx:188-194). In me-ios, tapping an empty day starts creating a new event when write access is available, and tapping a day with events opens DayDetailFeature (CalendarGridFeature.swift:21…
- Agenda mode (missed by the claim): vmm has a grid/agenda view-mode toggle with an infinite-scroll agenda feed (EmployeeCalendarScreen.tsx:152-181). me-ios has view modes too (currentViewMode == .month, CalendarContainerViewController.swift:445). This may belong to a separate capability.

_Note: The two products are classed as one capability because the month grid is the same outcome. The subject differs: a manager sees a report's calendar, an employee sees their own. A person should confirm whether the new app treats these as one screen used with two scopes. referee could not confirm: Divergence claim 'me-ios always uses a fixed 6x7 grid of 42 cells' is false: CalendarGridConfiguration.…_

### CAP-002: Browse the calendar as a scrolling list

**Fusion:** shared-diverged · **Personas:** Manager, Employee · **Confidence:** High

Scroll a chronological list of calendar entries that loads more entries while scrolling. In Employee the list also lets you jump to a date and open an item.

- **vmm** (Manager): screens: `EmployeeCalendarScreen`, `EmployeeCalendarAgendaView`; endpoints: `GET https://mobileemployee.visma.net/employee/api/v2/calendar/my-employees/feed…`; storage: `redux settings.calendarViewMode`; platform: `react-native` · evidence `src/screens/EmployeeCalendarScreen/EmployeeCalendarScreen.tsx:160-218`
- **me-ios** (Employee): screens: `CalendarViewController`, `CalendarHeaderView`, `CalendarFeedPagingControllerDataSource`, `CalendarViewControllerRepresentable`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar/feed?From={date}&Offset={of…`; events: `log: Calendar item tapped`, `log: Date header tapped`, `log: Date selected / Done button tapped`; platform: `ios-native`, `reachability/offline handling`, `NotificationCenter AppMessage.resetCalendar / resetCalendarBackground` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarViewController.swift:322-545; EmployeeServices/Calenda…`

**How they differ:**
- Paging direction: vmm only pages into the past, one month per page, and stops after 24 pages (queryEndpointsCalendar.ts:17, 152-155). me-ios loads older entries when you scroll down and newer ones when you scroll up, using FetchType .past/.future (CalendarViewController.swift:370-398). I found no c…
- Endpoint: vmm is meant to use GET employee/api/v2/calendar/my-employees/feed, but the infinite query currently returns mock data (queryEndpointsCalendar.ts:96, 158-164). me-ios uses GET employee/api/v1/employees/{odpUserId}/calendar/feed?From&Offset&Direction (CalendarService.swift:103-111).
- Paging key: vmm uses the start of each month as the page key. me-ios pages by Offset from a From date.
- Jump to date: in me-ios, tapping a section header (CalendarHeaderView) opens a date picker, and loadFeed(from:) reloads the list from the chosen date (CalendarViewController.swift:308-335). vmm has no jump control; it only carries the visible month back to the grid when you switch views (EmployeeCa…
- Errors and offline: vmm shows employee_calendar_load_error only if the first page fails. If a later page fails, the loaded months stay and it stops retrying on scroll (EmployeeCalendarScreen.tsx:185, 208-210). me-ios shows an offline view based on reachability and a CALENDAR_CANNOT_LOAD_MORE_CONTEN…
- Item tap: me-ios passes the tapped item to its delegate (didSelectItem), which opens the item. vmm rows set selectedDay, which opens the day-detail bottom sheet (EmployeeCalendarAgendaView.tsx:97).
- View mode: vmm puts the agenda behind a grid/agenda toggle stored in settings.calendarViewMode. me-ios's list is the main calendar view and also has confirm-time and new-event buttons (CalendarViewController.swift:491-540).
- Analytics: me-ios logs 'Calendar item tapped' and 'Date header tapped'. I found no equivalent events in the vmm agenda code.

_Note: me-ios reuses CalendarViewController for expense claims (possibleFeatures .expenseClaims). referee could not confirm: vmm endpoint: the claimed URL uses a hard-coded host (https://mobileemployee.visma.net/...). The code builds it as ${base}employee/api/v2/calendar/my-employees/feed (queryEndpointsCalendar.ts:96). The agenda query itself only calls createMockCalendarFeedResponse, so this endpoint…_

### CAP-003: Switch between list and month view of the calendar

**Fusion:** shared-diverged · **Personas:** Manager, Employee · **Confidence:** Medium

Switch the calendar between a list/agenda view and a month grid. The app remembers the chosen view.

- **vmm** (Manager): screens: `CalendarOptionsMenu (headerRight of EmployeeCalendarScreen)`, `EmployeeCalendarAgendaView`; storage: `settings.calendarViewMode`; platform: `react-native` · evidence `src/screens/EmployeeCalendarScreen/components/CalendarOptionsMenu/CalendarOptionsMenu.tsx:53-131; src/screens/EmployeeC…`
- **me-ios** (Employee): screens: `CalendarContainerViewController`, `CalendarViewController (list)`, `CalendarGridView / CalendarGridFeature (month)`; events: `calendarViewMode(list/month)`; storage: `UserPreferences com.employee.vme.calendar.viewMode`; platform: `ios-native`, `CoordinatorAction.showCalendarFeed(initialDate) / showCalendarMonthView handled…`, `reload of the month grid on appWillEnterForeground` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarContainerViewController.swift:57-173`

**How they differ:**
- Entry point: in me-ios the tab title and icon depend on absence/time permissions, or on expenseClaims when those are missing. vmm opens the calendar from the employee detail screen.
- Control: vmm uses a 'View mode' section with Grid/Agenda radio rows inside the header options modal, next to the filter and style options (CalendarOptionsMenu.tsx:94-102). me-ios uses a single nav-bar icon button that toggles between the two views. Its icon and accessibility label change between S.…
- Default view: vmm starts in 'grid' (month) view (settingsReducer.ts:119). me-ios starts in '.list' view (CalendarContainerViewController.swift:52).
- Persistence and sync: vmm keeps the view in redux settings.calendarViewMode and sends it to the backend with the other user settings via PUT users/{id}/settings, falling back to AsyncStorage (apiUserSetting.ts:81, 96-118; validator userSettingsValidator.ts:77). This contradicts the reducer comment…
- Restore gating: me-ios restores the saved view only when possibleFeatures.hasCalendarPermissions() is true (CalendarContainerViewController.swift:70-76). The claim cites 325-370, which is wrong. vmm always uses the stored value.
- Whose calendar: vmm switches the view of another employee's calendar (EmployeeCalendarScreen, reached from the HRM and Approval stacks, feed queried by employeeId, EmployeeCalendarScreen.tsx:169-175). me-ios switches the user's own calendar tab, whose title and icon depend on absence/time/expenseCl…
- Keeping the date when switching: vmm moves the grid to the month last visible in the agenda when switching back (EmployeeCalendarScreen.tsx:152-158). me-ios scrolls the list to the grid's selected month and reloads the grid from the list's current section date (CalendarContainerViewController.swift…
- Analytics: me-ios logs calendarViewMode(list/month) when the screen opens and a log line on every switch (lines 89-95, 161). No equivalent was seen in the vmm menu.

_Note: referee could not confirm: me-ios CalendarContainerViewController.swift:325-370 is cited for the permission-gated restore, but those lines are setTitle and setTabbarItem. The restore is at lines 70-76.; vmm settings.calendarViewMode is described as redux-persist local storage only, but it is also sent to the backend through saveUserSettings (apiUserSetting.ts:81)._

### CAP-004: See the details of a calendar day

**Fusion:** shared-diverged · **Personas:** Manager, Employee · **Confidence:** High

Tap a day to open a sheet listing that day's entries with time or full-day label, title and status. In Employee the sheet also shows the special day and the scheduled roster hours, and entries can be opened.

- **vmm** (Manager): screens: `EmployeeCalendarScreen`, `EmployeeCalendarDayDetail (BottomSheet)`; platform: `react-native` · evidence `src/screens/EmployeeCalendarScreen/components/EmployeeCalendarDayDetail.tsx:40-100`
- **me-ios** (Employee): screens: `DayDetailView`, `DayDetailFeature`, `CalendarGridView`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar/feed?From={date}&Offset={of…`, `GET /employee/api/v1/employees/{odpUserId}/calendar/workshift`, `GET /employee/api/v2/Calendar/specialdays`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/DayDetailView.swift:54-135`

**How they differ:**
- Content: me-ios shows the special day as a red line and roster events as 'Scheduled hours' items, with roster events sorted first (DayDetailFeature.swift:30-31, DayDetailView.swift:55-76). vmm shows only title, subtitle and an HH:mm range or the employee_calendar_full_day label (EmployeeCalendarDay…
- Status tags: vmm shows a tag only when requestStatus is 'pending' (EmployeeCalendarDayDetail.tsx:76-79). me-ios shows green, red and blue tags for approved, rejected and pending (DayDetailView.swift:18-34). The claim missed this.
- Interaction: in me-ios a non-roster event can be tapped and opens it (DayDetailView.swift:81-83, handled at CalendarGridFeature.swift:318). In vmm the EventCard has no onPress, so entries are read-only.
- Actions in the sheet: me-ios shows a 'Register time or absence' button when write is allowed and a 'Confirm time' button with a warning alert flow (DayDetailView.swift:115-128, DayDetailFeature.swift:70-120). vmm has only a close button. The claim missed this.
- Empty day: vmm opens the sheet and shows employee_calendar_empty_day_message (EmployeeCalendarDayDetail.tsx:70-71). In me-ios an empty grid day never opens the sheet. It starts adding a new event if write is allowed, otherwise nothing happens (CalendarGridFeature.swift:217-220), so the NoContentVie…
- Entry points: vmm opens the sheet from a grid day and from an agenda day (EmployeeCalendarScreen.tsx:186-187 and :329). me-ios opens it from a grid dayTapped, which is ignored while dragging (CalendarGridFeature.swift:210-213).
- Data source: vmm reads eventsByDate[selectedDay], which is built from the loaded calendar data (EmployeeCalendarScreen.tsx:137, :452). me-ios builds the day from the feed, workshift and specialdays endpoints (CalendarService.swift:108, GetWorkshifts.swift:26, GetSpecialDays.swift:16).

_Note: referee could not confirm: The cited range vmm EmployeeCalendarDayDetail.tsx:40-100 is slightly off. The component itself spans lines 46-112 and the time-range helper is at lines 38-44.; The me-ios endpoint paths are defined in EmployeeServices/Calendar (Request/GetWorkshifts.swift:26, Request/GetSpecialDays.swift:16, Service/CalendarService.swift:108), not in the cited CalendarFeature repository…_

### CAP-005: Customize what the calendar shows

**Fusion:** shared-diverged · **Personas:** Manager, Employee · **Confidence:** High

Hide weekends, show week numbers, filter entry types and choose icon or text style for events. The choices are saved across sessions.

- **vmm** (Manager): screens: `CalendarOptionsMenu (headerRight of EmployeeCalendarScreen)`; storage: `settings.calendarViewMode`, `settings.calendarHideWeekends`, `settings.calendarShowWeekNumbers`, `settings.calendarShowAttendance`, `settings.calendarShowAbsence`, `settings.calendarShowSupplement`, `settings.calendarDisplayMode`; platform: `react-native` · evidence `src/screens/EmployeeCalendarScreen/components/CalendarOptionsMenu/CalendarOptionsMenu.tsx:53-131`
- **me-ios** (Employee): screens: `CalendarViewFilterView`, `CalendarViewFilterFeature (filter popover)`, `CalendarMonthYearNavigationView`, `CalendarGridView`; storage: `com.employee.vme.calendar.hideWeekends`, `com.employee.vme.calendar.showLabels`, `com.employee.vme.calendar.hideAbsence`, `com.employee.vme.calendar.hideAttendance`, `com.employee.vme.calendar.hideSupplement`, `com.employee.vme.calendar.hideRoster`, `com.employee.vme.calendar.showWeekNumbers`, `userPreferences.calendarHideWeekends` …; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/Components/CalendarViewFilterFeature.…`

**How they differ:**
- Filter types: me-ios adds a Roster checkbox (ItemID.showRoster, S.Calendar.roster, CalendarViewFilterFeature.swift:162-166), stored as hideRoster (CalendarGridFeature.swift:306-308). vmm has only attendance, absence and supplement (CalendarOptionsMenu.tsx:66-83).
- Roster is not in me-ios hiddenEventTypes (CalendarFilterPreferences.swift:45-63 covers only absence, attendance and supplement), so roster is filtered separately.
- Stored polarity: vmm stores show* booleans (calendarShowAttendance, calendarShowAbsence, calendarShowSupplement). me-ios stores hide* booleans and inverts them in the UI (CalendarViewFilterFeature.swift:95-100 and 147-160). Its roster box is show in the UI but hide in storage (CalendarGridFeature.s…
- Style setting: vmm stores calendarDisplayMode as 'icons' or 'labels' (CalendarOptionsMenu.tsx:111-126). me-ios stores a showLabels boolean (CalendarViewFilterFeature.swift:101-104).
- Hide weekends: me-ios drops weekend days and then removes week rows that belong entirely to another month (CalendarViewUtils.filterOtherMonthWeekRows, CalendarGridFeature.swift:385-388). vmm has no such rule: getWeekdayRange (WeekdayCalendarGrid.tsx:33-42) extends to the Monday before the 1st and t…
- Menu scope: the vmm options menu also holds the grid/agenda view-mode radio (settings.calendarViewMode, CalendarOptionsMenu.tsx:95-103). The me-ios filter popover has only a 'filterView' section and an 'eventsStyle' section.
- Persistence: vmm persists the whole settings slice through the redux-persist whitelist (reduxState.ts:107-108), and settingsReadTransform backfills missing keys from their defaults (persistTransforms.ts:139-146). me-ios writes @Shared UserPreferences keys with the prefix com.employee.vme.calendar.*…
- Where it appears: in vmm the menu is mounted in both the HRM and the Approval navigation stacks (HrmNavConfig.tsx:146, ApprovalNavConfig.tsx:120). In me-ios it sits inside CalendarMonthYearNavigationView of the calendar grid.

_Note: referee could not confirm: me-ios Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/CalendarFilterPreferences.swift:45-63 is cited for the rule that removes other-month week rows. Those lines are the hiddenEventTypes computation. The rule is in CalendarGridFeature.swift:385-388 (CalendarViewUtils.filterOtherMonthWeekRows).; The divergence line says 'no such rule is…_

### CAP-006: Start a time or absence registration from the calendar

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

From the calendar list or a day detail, start registering new time or absence for yourself.

- **me-ios** (Employee): screens: `CalendarViewController`, `DayDetailView`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarViewController.swift:322-545; Modules/CalendarFeature/…`

**How they differ:**
- Inside me-ios (not a fusion difference): the calendar-list button pre-fills today's date through AddAbsenceCoordinator.prepare(onDateFrom: today) at CalendarViewController.swift:749-756, while the day-detail button passes the selected day through CalendarGridFeature .addNewEvent(dateFrom: date, dat…
- Inside me-ios: the two entry points use different flows. The list uses the UIKit AddAbsenceCoordinator with source .list, and the day detail uses the TCA grid feature's addNewEvent / addAbsence destination.
- vmm EmployeeCalendarScreen.tsx and EmployeeCalendarDayDetail.tsx have no register action (only month arrows and SheetCloseButton), so there is no second product.

_Note: This action requires calendar write permission (isWriteAvailable). It hands off to AddAbsenceCoordinator (source .list), and the day-detail button action is handled by the parent grid feature. The registration flow itself belongs to another domain. referee could not confirm: CalendarViewController.swift:322-545 misses prepareAddAbsenceCoordinatorIfNeeded and addAbsence (lines 749-761), where the…_

## Absence registration

Register, view, edit and delete absences and time events.

### CAP-012: Register an absence or time event

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee picks a day, a dragged range or the add button in the calendar, chooses an absence or time type from grouped calendar templates, fills the dynamic form (dates, times, hours or percent, comment, cost-unit dimensions, medical certificate) and saves it. If the server asks, the employee confirms a warning for future registrations.

- **me-ios** (Employee): screens: `ItemSelectorView (select type)`, `AbsenceRegistrationTableViewController`, `PostScreenViewController`, `AddAbsenceFeature`, `AbsenceRegistrationViewModel (CalendarFeature)`, `AbsenceEventEditor`, `RegisterAbsenceTypeItemSelectorViewModel`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar/templates`, `GET /employee/api/v1/employees/{odpUserId}/calendar/confirm/template`, `GET {template details link href}`, `GET {absenceType details href from API links}`, `POST /employee/api/v1/employees/{odpUserId}/absenceregistration`; events: `addAbsence (absence_type, inputType, hasComment, source list/month/chatbot)`, `calendarMonthViewSingleDayRegistration`, `calendarMonthViewPeriodRegistration`, `calendarCostUnitsEdited`, `new event created`, `new event created input type`, `new event created with comment`; platform: `ios-native`, `Survicate survey with thank-you toast after save`, `NotificationCenter AppMessage.reloadStartPage` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AddAbsenceCoordinator/AddAbsenceCoordinator.swift:5…`

_Note: Rules: the form is valid only when every required field is filled (AbsenceRegistrationViewModel.swift:428-431). Changing the from-date resets the to-date and the dimension values, and reloads the types. The app fetches templates for the fromDate/toDate window. A confirmationRequired status becomes a warning the user must confirm. An error status code in the response body maps to a validation erro…_

### CAP-013: Pick cost-unit dimension values for a registration

**Fusion:** unique · **Personas:** employee · **Confidence:** High

While registering or editing an absence, the employee picks dimension (cost unit) values from a paged, searchable list. Recently used values appear first.

- **me-ios** (Employee): screens: `Dimension value selector`, `DimensionValueItemSelectorViewModel`; endpoints: `GET {dimension values link href} (optional search query param)`; events: `calendarCostUnitsEdited`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/DimensionValueItemSelectorViewModel.swift…`

**How they differ:**
- The selected value is shown as 'id - name' (DimensionFieldsSectionViewModel.swift:85-89). The currently selected value is added to the recently used list if it is missing (lines 41-47). The claim does not mention either.
- Tapping the selected row again deselects it (selectValueAtIndexPath, DimensionValueItemSelectorViewModel.swift:285-288). The claim misses this.

_Note: The server runs the search only when the link advertises a search parameter. Otherwise the app filters the list locally. Pages default to count 50 and offset 0 (fragment 29). This could be folded into the register and edit capabilities as a sub-step. referee could not confirm: notes: 'Otherwise the app filters the list locally' is wrong. In searchDimensionValue (DimensionValueItemSelectorViewMode…_

### CAP-014: View details of a registered absence

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee opens a registered absence to see its type, fields, comment and approval status.

- **me-ios** (Employee): screens: `AbsenceViewTableViewController`; endpoints: `GET {absence detail link href}`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Absence/AbsenceViewTableViewController.swift:157-280`

**How they differ:**
- Nearby but not the same: vmm src/screens/EmployeeCalendarScreen/components/EmployeeCalendarDayDetail.tsx lists a day's feed items (title, subtitle, time range, and a status tag only when requestStatus === 'pending'). It fetches no detail record and shows no fields, comment or Edit. me-ios loads the…
- me-ios hides the inputType=FullDay field and fields with empty values (AbsenceViewTableViewController.swift:233, 255-259).

_Note: Empty field values are hidden. The Edit button appears only when the server returns edit links. referee could not confirm: S.approvalStatusAwaitingApproval: not referenced in AbsenceViewTableViewController.swift. The status shown comes from requestStatus.fullStatusText (lines 238 and 468). The string key is used in CalendarUtils.swift:338 and AbsenceRegistrationUtils.swift:85 instead._

### CAP-015: Edit a registered absence

**Fusion:** unique · **Personas:** employee · **Confidence:** High

From the absence detail, the employee edits a registered absence, including its type, and saves it through the entry's update link. The employee confirms a future-registration warning when the server asks.

- **me-ios** (Employee): screens: `AbsenceRegistrationTableViewController (edit)`, `PostScreenViewController`, `AbsenceEventEditor`, `AbsenceViewTableViewController`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar/templates`, `GET {absence details href from API links}`, `PUT {update link href}`, `PUT {update href from absence links (rel=update)}`; events: `editAbsence (absence_type)`, `calendarCostUnitsEdited`, `event edited`; platform: `ios-native`, `Survicate survey after save`, `Chatbot entry points (editFromChatbot / editPredictionFromChatbot initializers)` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrationCoordinator/EditAbsenceRegistrat…`

_Note: Editing needs calendar write permission to load templates. An update is possible only when the item carries a rel=update link. Otherwise the app shows unexpectedError. An update that returns confirmationRequired shows a warning and sends the PUT to the updateUrl again (AbsenceEventEditor.swift:73-89). Fragment 13 mixed edit and delete, so it is split here. referee could not confirm: The endpoints…_

### CAP-016: Delete a registered absence

**Fusion:** unique · **Personas:** employee · **Confidence:** High

From the absence detail or editor, the employee deletes a registered absence after a confirmation prompt, using the entry's delete link.

- **me-ios** (Employee): screens: `AbsenceEventEditor`, `AbsenceRegistrationTableViewController (edit)`; endpoints: `DELETE {delete link href}`, `DELETE {delete href from absence links (rel=delete)}`; events: `deleteAbsence (absence_type)`, `event deleted`; platform: `ios-native` · evidence `EmployeeServices/Calendar/Sources/Calendar/Service/AbsenceRegistrationService.swift:93-103; Modules/CalendarFeature/Sou…`

**How they differ:**
- Only me-ios has this capability. vmm has no endpoint, screen or event for deleting an absence (vmm/src/services/apiCalendar/apiCalendar.ts has GET/POST only; the only DELETE, at vmm/src/services/apiApproval/apiApproval.ts:367, is for device unregistration).

_Note: Deleting is possible only when a rel=delete link is present. referee could not confirm: AbsenceEventEditor is listed as a screen, but it is a service-layer class with no UI (CalendarEventEditing/AbsenceEventEditor.swift:56-58). The real screen is AbsenceRegistrationTableViewController in edit mode.; The two endpoints listed ('DELETE {delete link href}' and 'DELETE {delete href from absence links…_

### CAP-017: See upcoming and ongoing vacation and parental leave on the start page

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The start page shows cards for declined, upcoming, ongoing and approved vacations and for parental leave, from one week ago to one month ahead.

- **me-ios** (Employee): screens: `StartPage`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar`; platform: `ios-native` · evidence `Employee/StartPage/Tasks/GetCalendarItemsTask.swift:13-76`

**How they differ:**
- Missed nuance: upcoming parental leave has no 2-week limit; any future approved parental leave in the one-month window gives an upcoming card, and parental leave never gets an 'approved' card (GetCalendarItemsTask.swift:62-65)
- Missed nuance: parental leave cards are never grouped; only ApprovedVacation, DeclinedVacation and UpcomingVacation cards are merged into a GroupedCardViewModel (GetCalendarItemsTask.swift:34-38)
- Missed nuance: pending vacations and denied parental leave give no card (GetCalendarItemsTask.swift:72-73)
- Edge case: the 2-week boundary uses a strict isBefore/isAfter, so a vacation starting exactly at twoWeeksInFuture may get no card (GetCalendarItemsTask.swift:68-71)

_Note: Card rules: a denied vacation that starts today or later gives a declined card. An approved vacation that starts within 2 weeks is upcoming, a later one is approved, and one in progress is ongoing. Parental leave is shown as upcoming or ongoing. Several cards of the same approved, declined or upcoming type are grouped._

## Time tracking

Check in/out, correct time registrations and confirm worked time.

### CAP-018: Check in and check out for the workday

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee checks in from the start page, which sends the current local time, sees the current check-in status, and later checks out. The checkout template is fetched to register the worked time.

- **me-ios** (Employee): screens: `StartPage`, `CheckinHandler`, `ViewControllerCheckinWrapper`, `GetCheckinStatusTask`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar/checkin`, `PUT /employee/api/v1/employees/{odpUserId}/calendar/checkin`, `PUT {checkout href from checkin links (rel=update)}`, `GET {checkoutTemplate href from checkin links, fromDate/toDate query params ups…`; platform: `ios-native` · evidence `EmployeeServices/Calendar/Sources/Calendar/Service/TimeService.swift:128-202`

**How they differ:**
- No counterpart in vmm: no check-in or check-out endpoint, screen or service in vmm/src, so the capability is unique
- Rule the claim missed: checking out less than one minute after check-in throws CheckinError.checkedInForLessThanOneMinute (CheckinHandler.swift:83-85)
- Rule the claim missed: checking out on a different day, or getting status .error, fetches the checkout template and throws checkedOutOnDifferentDay/checkedOutWithError so the user can correct the time (CheckinHandler.swift:87-100)
- Checkout fails with CheckinError.failedToCheckout when the check-in response has no update link (CheckinHandler.swift:74-76)
- Related actions the claim missed: deleting a check-in via its delete link and updating a checkout as an AbsenceType (TimeService.swift:204-228)

_Note: localTime is sent as ISO8601 in the current time zone. No fragment from vmm (Manager) covers this. referee could not confirm: GET {checkoutTemplate href ...} with fromDate/toDate upserted: that variant (TimeService.swift:148-167) is called only from Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift:304, not from the check-in/check-out…_

### CAP-019: Edit or delete a check-in/check-out registration

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee corrects the fields of a check-in/check-out time registration, or deletes it, through the shared registration form or the calendar event editor.

- **me-ios** (Employee): screens: `AbsenceRegistrationTableViewController (checkin mode)`, `PostScreenViewController`, `CheckinEventEditor`; endpoints: `GET {checkout template link href}?fromDate&toDate`, `POST {checkout update link href}`, `{link method} {checkin delete link href}`, `POST {update href from checkin action} (body fieldInfo)`, `{method from delete action} {delete href from checkin action}`; events: `checkinEdited`, `checkinDeleted`, `checkin edited`, `checkin deleted`; platform: `ios-native`, `Launched from the start page CheckinHandler (Employee/StartPage/Time/CheckinHan…` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrationCoordinator/EditCheckoutRegistra…`

_Note: Both the update link and the delete link are required, otherwise the result is invalidInputData (EditCheckoutRegistrationCoordinator.swift:57-64). The server action supplies the HTTP method for delete. The two fragments describe the coordinator/UI layer and the service layer of the same flow. referee could not confirm: Notes cite EditCheckoutRegistrationCoordinator.swift:57-64 as enforcing both l…_

### CAP-020: Confirm worked time up to a date

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee sends the timesheet for confirmation up to a date: a day from the calendar or day detail, the suggested date, or a chosen date from the type selector. The app loads the confirmation status and template. Error-level validations block the confirmation; Warning-level ones need consent before a forced confirm.

- **me-ios** (Employee): screens: `Confirm period action sheet`, `DatePicker`, `PostScreenViewController (period sent)`, `DayDetailView`, `DayDetailFeature`, `CalendarViewController`, `CalendarFeedViewModel`, `ConfirmTimeUseCase` …; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar/confirm`, `GET /employee/api/v1/employees/{odpUserId}/calendar/confirm/template`, `PUT {confirm template update link href}`, `PUT {confirm template _links rel=update href}`, `PUT {confirm href from confirm details} (body date)`; events: `confirmTime`, `confirm time clicked`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AddAbsenceCoordinator/AddAbsenceCoordinator.swift:1…`

**How they differ:**
- No divergence: vmm has only the unused i18n key employee_calendar_confirm_time (vmm/src/assets/i18n/en.json:1806) and no executable confirm-time flow or calendar/confirm endpoint under vmm/src.
- Not in the claim: the chatbot quick response also confirms time, sending registerTimeConfirmation with a predicted event href (QuickResponseAction.confirmPredictedConfirmTimeEvent.swift:42). It skips the template validation checks, so it may be a separate entry point to consider.

_Note: Needs the meapi:absence:confirm-time / confirmTime permission, and the button is hidden without it (CalendarViewController.swift:508-524). HTTP 403 maps to featureDisabled. The optional targetDate query param is supported. The day-level and period-level entry points are one outcome (a date is sent), so they are merged. referee could not confirm: Endpoint 'PUT {confirm href from confirm details} (…_

## Balances

See absence, vacation and time balances.

### CAP-009: View an employee's absence balances

**Fusion:** unique · **Personas:** Manager · **Confidence:** High

A manager sees one employee's absence balances: total vacation balance, sick-child days for the current year and self-certified sickness over the last 12 months. A balance hook combines them for display.

- **vmm** (Manager): screens: `consumer hook useEmployeeBalanceData (src/hooks/useEmployeeBalanceDataClean.ts:…`; endpoints: `GET {calendarBase}/org/{orgId}/balances/employee/{employeeId}/total`, `GET {calendarBase}/org/{orgId}/employee/{employeeId}/summary/template/sickchild…`, `GET {calendarBase}/org/{orgId}/employee/{employeeId}/summary/template/sickness1…`; platform: `react-native` · evidence `src/services/apiCalendar/apiCalendar.ts:211-381`

**How they differ:**
- The screen is more specific than the claim says: the vmm hook is used by HrmEmployeeBalances (src/components/hrm/HrmEmployeeBalances/HrmEmployeeBalances.tsx:27), and HrmEmployeeDetailAccordion.tsx:282 renders that component. The screen also shows vacationDetails (normal, additional, transferred, tr…
- Not a fusion difference: me-ios has a related but separate capability for employees to see their own vacation balance, CalendarService.getVacationBalances (CalendarService.swift:56-63, GetCalendarBalances for the current user's odpUserId). It has no manager view of another employee and no sick-chil…

_Note: calendarBase is CALENDAR_API_BASE_PROD or the staging/sandbox value (src/services/apiBase.ts:48-53). The target date is 31 Dec of the current year. Vacation comes from the 'vacationbalances' family and shows '0 days' when missing. The other apiCalendar methods (year, endofyear, date range, balances/search GET/POST, search/template, calendarapi/FetchPeriodAggregation) are called only from tests._

### CAP-010: See my time and absence balances for a month

**Fusion:** unique · **Personas:** employee · **Confidence:** High

From the calendar toolbar, an employee opens a summary of time and absence balances for the month on screen. They can expand a balance group for details and switch control options, which the app remembers.

- **me-ios** (Employee): screens: `BalancesOverviewHostingController`, `BalancesOverviewModalView`, `BalancesOverview (CalendarFeature)`; endpoints: `GET /employee/api/v2/calendar/time-balance-summary?fromDate&toDate`; events: `showCalendarSummary`, `showCalendarSummaryDetail(groupName)`, `show summary show more`; storage: `UserPreferences com.employee.vme.calendar.balances.control (per control id)`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/BalancesOverview/Features/BalancesOverviewFeature.swift:47-115…`

_Note: The range runs from the first to the last day of the month, and fromDate/toDate are sent as ISO dates. A saved option is used only if the control still offers it. Otherwise the default option applies. showCalendarSummary is logged only when the user has the addAbsence permission._

### CAP-011: See my vacation balances on the start page

**Fusion:** unique · **Personas:** employee · **Confidence:** High

An employee sees their combined vacation and leave balances as cards on the start page.

- **me-ios** (Employee): screens: `StartPage (GetVacationBalancesTask)`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar/balances/combined`; platform: `ios-native` · evidence `EmployeeServices/Calendar/Sources/Calendar/Service/CalendarService.swift:57-64`

**How they differ:**
- The card only appears for users with absence or time permissions (addAbsence, addTime, absenceReadOnly, timeReadOnly, absenceWrite, timeWrite), per StartPageViewModel.swift:237-247. The claim does not mention this condition.
- vmm HrmEmployeeBalances (useEmployeeBalanceDataClean.ts:62-163) lets a manager view an employee's vacation, flexitime, sick-child and self-certification balances in HRM employee detail. This is a separate capability, not a twin of this one.

_Note: referee could not confirm: Description overstates: GetVacationBalancesTask.swift:27-33 shows only the category == .vacation group as a single RemainingVacationCardViewModel card; other leave balances from the combined response are not shown on the start page_

## Team overview

Manager signals about team presence, birthdays and anniversaries.

### CAP-007: Sync team birthdays and work anniversaries to my calendar

**Fusion:** unique · **Personas:** Manager with HRM access · **Confidence:** Medium

A manager with HRM access turns calendar sync on or off. When sync is on, the app creates 'Manager App - Birthdays' and 'Manager App - Anniversaries' device calendars. Each employee gets a yearly all-day event with a reminder one day ahead. When sync is off, both calendars are removed.

- **vmm** (Manager): screens: `CalendarSyncPicker (Settings item; not currently rendered)`; events: `create_calendar_failed`, `sync_birthday_failed`, `sync_anniversary_failed`, `calendar_sync_switch`, `check-calendar-permissions-failed`, `request-calendar-permissions-failed`; storage: `redux settings.calendarSync (SYNC_OFF default)`, `hrm sync list via hrmAddToSync/hrmClearSync`; platform: `calendar (react-native-calendar-events)`, `iOS NSCalendarsFullAccessUsageDescription`, `Android READ_CALENDAR/WRITE_CALENDAR` · evidence `src/hooks/useSyncCalendar.ts:38-258`

**How they differ:**
- (platform parity) Within vmm, iOS events set an endDate and Android events do not (src/hooks/useSyncCalendar.ts)
- (platform parity) Confirmed: in vmm, iOS events set endDate equal to startDate and Android events leave endDate out (useSyncCalendar.ts:111-128 for birthdays, 184-201 for anniversaries).
- Missed by the claim: the hook also supports birthdays-only (SYNC_BIRTHDAYS) and anniversaries-only (SYNC_ANNIVERSARIES) modes and removes the other calendar (useSyncCalendar.ts:236-240). The picker only offers all or off, so a user cannot choose these modes.
- Missed by the claim: events are saved inside async forEach callbacks that nothing waits for. hrmAddToSync is dispatched even if saveEvent fails, so the success/failure toast after 2 s may not be accurate.
- Missed by the claim: the first event date is the employee's birth date or employment date moved to the current year, even when that date has already passed; after that it repeats yearly.

_Note: The feature looks dormant. CalendarSyncPicker is not mounted, and SettingsScreen.tsx:404-405 says it is gated on a dev flag. Rules: the app checks calendar permission, then requests it, and shows a toast if it is denied. It skips an employee whose event already exists (matched by event url = employee id). Events recur yearly with a -1440 min alarm. Turning sync off clears the hrm sync list. A res…_

### CAP-008: See how many team members are absent today

**Fusion:** unique · **Personas:** Manager · **Confidence:** Medium

On the Start screen, the manager sees how many managed employees are absent today. The count comes from the month's calendar feed for all managed employees. If the feed fails, the signal is not shown.

- **vmm** (Manager): screens: `StartScreen (consumer, src/screens/StartScreen/hooks/useStartScreenData.ts:354)`; endpoints: `GET https://mobileemployee.visma.net/employee/api/v2/calendar/my-employees/feed…` · evidence `src/services/queryApi/queryEndpointsCalendar/queryEndpointsCalendar.ts:35-69`

**How they differ:**
- Missed in claim: the query is skipped unless loginManager.hasAccessHRM and features.isEmployeeCalendarEnabled are both true (vmm useStartScreenData.ts:349-357)
- Missed in claim: 'absent today' means a day entry whose date matches today and has an item with filterableType FILTERABLE_TYPE_ABSENCE. Each employee counts once, however many bookings they have (useStartScreenData.ts:359-365)
- Missed in claim: the count is shown in three places: the 'startHrmAbsences' ticket (useStartScreenData.ts:498-499), a list of absent employees with subtitle 'startItemAbsentToday' (useStartScreenData.ts:519-523), and the 'startStatAbsentToday' stat tile plus the awayToday value (StartHub.tsx:374-37…

_Note: vmm calls the Employee-product backend (mobileemployee.visma.net) with a Bearer token and X-Visma-Employee-Version 12.0. No me-ios fragment reports a client for this route. Any error resolves to an empty list, and the fragment says the route currently returns 403 for most manager tokens, so the signal may be missing in practice. The response is flattened from companies to employees to days, with…_

## Employee Agent

Register, confirm and ask questions by chatting with the AI assistant.

### CAP-021: Register time or absence by chatting with the Employee Agent

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee opens the Employee Agent from the calendar toolbar. They type or dictate a sentence such as 'I was sick yesterday', or pick an example prompt. The agent predicts one or more absence or time registrations and shows a summary. The employee confirms to save them all or cancels.

- **me-ios** (Employee): screens: `CalendarChatBotView`, `CalendarChatBotFeature`, `ChatFeature`, `CalendarChatBotMessageView`, `QuickResponseButton`, `CalendarChatBotCoordinator`, `CalendarChatBotViewModel`, `CalendarChatBotRepository`; endpoints: `POST /employee/api/v1/employees/{odpUserId}/chatbot/predictCalendarRegistration`, `POST /employee/api/v1/employees/{odpUserId}/absenceregistration`, `GET /employee/api/v1/employees/{odpUserId}/chatbot/examplePrompts`; events: `calendarBotPredictionRequest(successful:)`, `calendarBotEventCreated(type:code:)`, `calendarBotEventsCreated(count:)`, `calendarBotVoiceInputUsedInMessage`; platform: `ios-native`, `speech recognition / microphone (voice-to-text input)`, `modal presentation (isModalInPresentation)`, `open app Settings on speech permission error` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:231-325;…`

**How they differ:**
- No cross-app divergence: vmm has a Gaia AG-UI chatbot (src/services/aguiService.ts:270), but its tools only open approvals, employees or screens (src/utils/gaiaFrontendTools.ts:27-67) and it cannot create time or absence registrations.
- Scope note: the me-ios agent also handles confirm-time template predictions and balance answers (CalendarChatBotViewModel.processPredictions). The claim describes only absence and time registration predictions.

_Note: The entry point (fragment 17) appears only with calendar permissions. Absence-view events (absenceViewAppeared, editButtonTappedInAbsenceView) reach the chatbot through AppEventsFeature. Empty or whitespace-only prompts are ignored on the client. localTime is sent as ISO8601 in the current time zone. On confirm, the predictions that pass isReadyToBeConfirmed are saved in parallel. The rest need e…_

### CAP-022: Confirm the time sheet through the Employee Agent

**Fusion:** unique · **Personas:** employee · **Confidence:** High

When the agent reads the prompt as a time-confirmation request, it shows a confirm-time event. On confirm, the time sheet for that date is sent for approval.

- **me-ios** (Employee): screens: `CalendarChatBotView`; endpoints: `POST /employee/api/v1/employees/{odpUserId}/chatbot/predictCalendarRegistration`, `PUT {confirmTime template _links rel=update href}`; events: `calendarBotEventCreated(type:code:)`, `calendarBotEventsCreated(count:)`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Message/QuickResponseAction/QuickResponseAction.confir…`

**How they differ:**
- Analytics events are sent indirectly: the action sends ChatbotEventPublisher .eventConfirmed/.eventsConfirmed (QuickResponseAction.confirmPredictedConfirmTimeEvent.swift:48-50), which ChatbotEventsFeature.swift:87-97 maps to calendarBotEventCreated/calendarBotEventsCreated. They are sent after both…
- The confirm-time call is a PUT to the confirmTime template's update link with body {date} (ConfirmTimeToDate.swift:38-44, TimeService.swift:103-111).
- calendar.chatBot.button.cancelRegistration comes from the cancelPrediction action (QuickResponseAction.cancelPrediction.swift:15), not from the confirm-time action.

_Note: The template must have a date item that parses with Constants.dateFormatter and an update link. If either is missing, the action fails with an unexpected error._

### CAP-023: Ask the Employee Agent about leave balances

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee asks the agent about balances. The agent replies with the balance text that the prediction service returns.

- **me-ios** (Employee): screens: `CalendarChatBotView`; endpoints: `POST /employee/api/v1/employees/{odpUserId}/chatbot/predictCalendarRegistration`; events: `calendarBotPredictionRequest(successful:)`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:275-352`

_Note: The balance answer (balancesQueryResult) is shown only when the response has no calendarRegistrations and no confirmTime. referee could not confirm: The endpoint POST /employee/api/v1/employees/{odpUserId}/chatbot/predictCalendarRegistration is not in the cited view model file. It is defined in me-ios/EmployeeServices/Calendar/Sources/Calendar/Request/Chatbot/PostPredictCalendarRegistration.swift…_

### CAP-024: Edit a predicted registration before saving it

**Fusion:** unique · **Personas:** employee · **Confidence:** High

From the agent's suggestion, the employee opens the registration form pre-filled with the prediction, for example to add a medical certificate for sickness. They adjust it and save, and the agent then shows the saved event.

- **me-ios** (Employee): screens: `EditPredictedAbsenceRegistrationView`, `EditPredictedAbsenceRegistrationFeature`, `EditAbsenceRegistrationCoordinator`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar/templates`, `POST /employee/api/v1/employees/{odpUserId}/absenceregistration`; events: `calendarBotEditRegistrationButtonClicked`, `calendarBotEditRegistrationEventCreated(type:code:)`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/EditAbsenceRegistration/EditPredictedAbsenceRegi…`

_Note: The Edit button appears only when the prediction contains exactly one event. The form opens in editMode .newFromPrediction(source: .chatbot) on a clone of the prediction. referee could not confirm: Minor: 'EditAbsenceRegistrationCoordinator' is listed as a screen, but none of the cited files contain it. It is at Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrati…_

### CAP-025: View, edit or delete an absence created in the agent chat

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee taps an event the agent has just registered to open its detail. There they can edit or delete it, and a deletion shows in the chat.

- **me-ios** (Employee): screens: `AbsenceRegistrationView`, `ViewAbsenceRegistrationFeature`, `AbsenceCoordinator`; endpoints: `GET {registration retrievalLink href}`, `PUT {absence _links rel=update href}`, `DELETE {absence _links rel=delete href}`; events: `calendarBotCreatedEventLinkClicked`, `calendarBotEditRegistrationFromPreview`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/AbsenceRegistration/AbsenceRegistrationView.swif…`

_Note: After a delete, the matching registeredEventsSummary message is replaced by a 'deleted' variant (CalendarChatBotViewModel.swift:568-589). The edit and delete requests are in AbsenceCoordinator and resolve through AbsenceEventEditor HATEOAS links. This likely overlaps with the general absence edit/delete capability in the calendar domain. referee could not confirm: The notes say the edit and delet…_

### CAP-026: Learn how to use the Employee Agent and try example prompts

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee opens the info page to read about the agent and see example prompts from the server. Tapping an example puts it in the chat input.

- **me-ios** (Employee): screens: `LearnMoreView`, `LearnMoreFeature`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/chatbot/examplePrompts`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/LearnMore/LearnMoreReducer.swift:14-67`

_Note: Examples load once and are cached in state. A load failure gives an empty list. The DependencyKey liveValue returns no prompts, but CalendarChatBotEnvironment.swift:34 injects the service-backed repository. The request itself is defined in EmployeeServices GetExamplePrompts.swift (fragment 40). referee could not confirm: The string list names the same key twice: S.Calendar.ChatBot.LearnMore.title…_

### CAP-027: Send feedback about the Employee Agent

**Fusion:** unique · **Personas:** employee · **Confidence:** High

From the Learn More page, the employee opens an external feedback form about the agent.

- **me-ios** (Employee): screens: `LearnMoreView`; endpoints: `GET https://forms.gle/hD3FxxN4igj7R47k6 (external web form)`; platform: `ios-native`, `in-app web presentation of external URL` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/LearnMore/LearnMoreReducer.swift:58-63`

**How they differ:**
- Not a divergence, only a note: vmm has per-answer thumbs-up/down feedback on Gaia chat replies (vmm/src/utils/types.ts:438, vmm/src/utils/eventLogging/events/gaiaEvents.ts:139). That is a different capability from the me-ios external feedback form, so it is not a fusion counterpart.
- me-ios opens the form in the app, in a sheet with SFSafariView (LearnMoreView.swift:62-68), not in an external browser.

_Note: The URL is hard-coded to a Google Form in LearnMoreConstants.swift:12. referee could not confirm: The string key SEND_FEEDBACK is a generic shared key (Strings.swift:984 S.Settings.sendFeedback, also used at Employee/Information/FAQv2/Models/FAQTopic.swift:49). It is not specific to the agent.; 'GET https://forms.gle/...' is not an app endpoint. It is a hard-coded external URL loaded in SFSafariV…_

## Expenses

Browse and track expense claims.

### CAP-028: Browse my expense claims by year and filter by status

**Fusion:** unique · **Personas:** employee · **Confidence:** High

An employee sees their expense claims grouped by year, newest first. Claims without a date sit in their own section. Quick filters narrow the list by claim status.

- **me-ios** (Employee): screens: `ClaimsCalendarViewModel`, `ClaimsQuickFilterBar`, `CalendarExpenseCellView`; endpoints: `expense claims feed via ExpenseService.getClaims (claim status empty) and Claim…`; platform: `ios-native` · evidence `Employee/CalendarLeftover/ClaimsCalendarViewModel.swift:30-272`

_Note: Rules: year sections are sorted newest first, and claims within a section are sorted by date, newest first. Duplicate claims are removed by claim id. Changing the filter resets paging to the selected statuses. The exact endpoint URLs were not resolved in this shard. No vmm (Manager) fragment was provided for this capability._

## Pay

Browse payslips.

### CAP-029: Browse my payslips by payment date, filtered by employer

**Fusion:** unique · **Personas:** employee · **Confidence:** High

An employee pages through past and upcoming payslips in a calendar ordered by payment date. They can narrow the list to one or more employers (tenants).

- **me-ios** (Employee): screens: `PayslipsCalendarViewModel`, `PayslipsFeature`; endpoints: `payslips feed via PayslipsPagingControllerDataSource.getUrl - not resolved in t…`; platform: `ios-native` · evidence `Employee/Payslips/PayslipsCalendarViewModel.swift:18-81`

_Note: Rule: changing the employer filter resets the list and rebuilds two cursors, one for past payslips (from today) and one for future payslips (from tomorrow). The endpoint was not resolved in this shard. No Manager (vmm) fragment covers payslips. referee could not confirm: endpoints: 'payslips feed via PayslipsPagingControllerDataSource.getUrl - not resolved in this shard' is not unresolved. It res…_

## Journeys

### JRN-001: An employee registers a sick day and checks what is left

**Persona:** Employee. An employee who wakes up ill logs the absence from the calendar and then checks how their balances are affected.

1. Open the calendar and pick today (CAP-001, CAP-004)
2. Start a sick-leave registration from that day (CAP-006, CAP-012)
3. Charge the absence to the right cost unit (CAP-013)
4. Check the month's time and absence balances (CAP-010)

### JRN-002: An employee plans, corrects and cancels a vacation

**Persona:** Employee. An employee books a vacation, sees it on the start page, changes the dates and later cancels part of it.

1. Check vacation days left on the start page (CAP-011)
2. Register the vacation (CAP-012)
3. See the coming vacation on the start page (CAP-017)
4. Open the vacation and move its dates (CAP-014, CAP-015)
5. Delete a vacation day that is no longer needed (CAP-016)

### JRN-003: An employee tracks the workday and closes the time sheet

**Persona:** Employee. An employee checks in and out each day, fixes a forgotten check-out and confirms the worked time at the end of the period.

1. Check in in the morning and check out at the end of the day (CAP-018)
2. Fix a check-out that was forgotten (CAP-019)
3. Look over the period as a scrolling list (CAP-002, CAP-003)
4. Confirm worked time up to the last day (CAP-020)

### JRN-004: An employee handles time and absence by chatting with the Employee Agent

**Persona:** Employee. An employee new to the Employee Agent learns what it can do, registers leave in a chat, corrects it and confirms the time sheet without opening any forms.

1. Read the introduction and try an example prompt (CAP-026)
2. Ask how much leave is left (CAP-023)
3. Ask the agent to register a day off and adjust its suggestion (CAP-021, CAP-024)
4. Open the created absence from the chat and correct it (CAP-025)
5. Confirm the time sheet through the agent (CAP-022)
6. Rate the conversation (CAP-027)

### JRN-005: An employee checks pay and expense claims

**Persona:** Employee. At month end an employee finds the latest payslip and checks whether submitted expense claims have been paid.

1. Find the latest payslip for the current employer (CAP-029)
2. List this year's expense claims and filter for the ones still open (CAP-028)
3. Check the month's balances against the payslip (CAP-010)

### JRN-006: A manager starts the day with team attendance

**Persona:** Manager. A manager sees who is absent today, looks at the team calendar and checks an employee's remaining leave before agreeing to a request.

1. See how many team members are absent today (CAP-008)
2. Open the team calendar in month view and inspect a busy day (CAP-001, CAP-004)
3. Limit the calendar to the relevant absence types (CAP-005)
4. Check an employee's absence balances (CAP-009)

### JRN-007: A manager keeps track of team birthdays and work anniversaries

**Persona:** Manager with HRM access. A manager with HRM access puts team birthdays and work anniversaries in their own calendar so none of them are missed.

1. Sync team birthdays and anniversaries to the personal calendar (CAP-007)
2. Scroll through upcoming events in list view (CAP-002, CAP-003)
3. Choose which event types the calendar shows (CAP-005)

### JRN-008: A team lead manages the team and their own time in one app

**Persona:** Person who is both a manager and an emp…. A team lead checks who is absent, confirms that their own leave fits the team plan, registers it and closes their own time sheet, all in one app.

1. See who on the team is absent today (CAP-008)
2. Look at the team calendar for the planned leave week (CAP-001, CAP-005)
3. Check their own vacation balance (CAP-011)
4. Register their own vacation from the calendar (CAP-006, CAP-012)
5. Confirm their own worked time before leaving (CAP-020)

## Observations

- The vmm employee calendar currently runs on mock data because the live my-employees/feed aggregate endpoint returns 403 (queryEndpointsCalendar.ts:72-75, 158-164).
- In me-ios, CalendarViewController is reused for expense claims, and the Calendar tab title can change to Claims depending on permissions (CalendarContainerViewController.swift:325-370).
- Fragment 33 (roster shifts and special days) was merged into the month-view capability. me-ios shows these alongside the grid and vmm lacks them, so this is recorded as a divergence.
- Fragment 28 mixed browsing with starting a registration, so it was split. Fragment 7 was given its own view-switching capability. The vmm view-mode evidence for that capability comes from fragments 1 and 3.
- Only vmm (Manager) fragments were provided for the Team overview domain. No me-ios fragment was reported, so both capabilities are unique.
- The absent-today signal depends on an Employee-backend endpoint that reportedly returns 403 for most manager tokens. It needs backend verification before it is carried into the merged app.
- Calendar sync of birthdays and anniversaries is behind a dev flag and is not rendered. A person should decide whether to keep or drop it.
- The manager view of an employee's balances (vmm, fragment 6) and the employee's own vacation balances on the start page (me-ios, fragment 35) are kept apart. They have different personas and different subjects (someone else's balances versus my own), and they use different backends: calendarBase org/employee balances/total versus /employee/api/v1/employees/{odpUserId}/calendar/balances/combined.…
- Fragments 16 and 34 describe the same me-ios monthly balance summary (the same time-balance-summary endpoint and the same BalancesOverview screen), so they were merged.
- me-ios uses two separate balance endpoints: v2 time-balance-summary for the calendar summary and v1 calendar/balances/combined for start page cards. The new app may want to settle on one source.
- Many vmm apiCalendar methods are called only from tests. They are candidates to drop, not capabilities.
- All 8 fragments come from me-ios (Employee product). No fragment from vmm (Manager, react-native) covers this domain, so every capability is unique. There is no shared-same or shared-diverged pair to reconcile.
- Fragment 13 combined edit and delete. It was split into two capabilities and merged with fragments 30 and 31 respectively.
- Fragments 10 and 29 describe the same registration outcome at the UI layer and the service layer. They were merged, and their analytics events (legacy addAbsence and the Snowplow 'new event created' family) were both kept.
- Edit and delete depend on HATEOAS links (rel=update, rel=delete). A unified app needs the same server-driven permission model.
- Missing from the fragments: a Manager-side capability to approve or decline absence requests. If vmm has one, it was not reported in this domain.
- Every fragment in this batch comes from me-ios (Employee). No vmm (Manager) fragment was provided for Time tracking, so every capability is unique.
- Fragments 15, 26 and 39 describe one confirm-time flow from different entry points (the type selector period sheet, the calendar/day detail and the service layer). They share the template endpoint and the confirmTime event.
- Fragments 14 and 38 are the UI layer and the service layer of the same edit/delete check-in flow. Event names differ in form (checkinEdited vs 'checkin edited'), probably an enum case vs its analytics string.
- Every fragment in the Employee Agent domain comes from me-ios (Employee). vmm (Manager, react-native) has no Employee Agent fragments, so every capability is unique.
- Fragment 17 (opening the agent from the calendar toolbar) is an entry point, not a separate outcome. It is merged into the chat registration capability.
- Fragment 40 (EmployeeServices service layer) covers the same outcome as fragment 18, so it is merged there. Its example-prompts request also backs the Learn More capability.
- One predictCalendarRegistration endpoint serves absence/time registration, time-sheet confirmation and balance queries. Which one runs depends on the response shape: calendarRegistrations, then confirmTime, then balancesQueryResult.
- Only one fragment was supplied for the Expenses domain. It comes from me-ios (Employee), so nothing could be reconciled against vmm (Manager).
- The fragment lives under 'CalendarLeftover', which suggests legacy code that was reused from the calendar feature.
- The Pay domain has only one fragment, and it comes from me-ios (Employee). No vmm (Manager) fragment covers pay, so there is nothing to merge across products.
- The actual payslips feed URL is still unknown: the fragment names only PayslipsPagingControllerDataSource.getUrl.
