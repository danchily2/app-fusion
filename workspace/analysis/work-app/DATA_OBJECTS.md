# Data objects: work-app

48 core records the apps hold or exchange.

## CalendarFeedItem (vmm)

Where: `src/services/queryApi/queryEndpointsCalendar/types.ts:35-51`. Used by: Calendar hides entry types the user filtered out, Only pending requests show a status tag in the day sheet, Day sheet time label: 'Full day' or a 24-hour time range, List view subtitle shows hours, quantity or time range, Entry type decides icon and colour.

| Field | Type | Notes |
| --- | --- | --- |
| id | string |  |
| title | string |  |
| dateFrom | string (ISO local datetime) |  |
| dateTo | string |  |
| subtitle | string / null |  |
| message | string / null |  |
| requestStatus | 'none' / 'pending' |  |
| inputType | 'FullDay' / 'DefiniteTime' / 'Hours' / 'Quantity' |  |
| type | 'Absence' |  |
| itemType | 'Sickness' / 'Vacation' / 'Absence' / 'Attendance' / 'Supplement' / 'Allowance' | Allowance mock-only |
| filterableType | 'absence' / 'attendance' / 'supplement' |  |
| properties | {name,value}[] | e.g. Hours, Quantity, Certificate Date, Certificate Percentage |
| month | string |  |
| year | number |  |

## CalendarFeedDay (vmm)

Where: `src/services/queryApi/queryEndpointsCalendar/types.ts:55-60`. Used by: Calendar hides entry types the user filtered out, Calendar list scrolls back at most 24 months, newest first.

| Field | Type | Notes |
| --- | --- | --- |
| date | string |  |
| monthName | string |  |
| year | number |  |
| items | CalendarFeedItem[] |  |

## CalendarFeedRawResponse (companies > employees > calendar) (vmm)

Where: `src/services/queryApi/queryEndpointsCalendar/types.ts:64-83`. Used by: Team absence feed returns 'no absences' on any failure.

| Field | Type | Notes |
| --- | --- | --- |
| data.companies[].companyId | string |  |
| companyName | string |  |
| employees[].employeeId | string |  |
| employees[].name | string |  |
| employees[].employeeNumber | string |  |
| employees[].managerId | string |  |
| employees[].calendar | CalendarFeedDay[] |  |

## AbsenceFeedEmployee / MyEmployeesAbsenceFeedResponse (vmm)

Where: `src/services/queryApi/queryEndpointsCalendar/types.ts:94-108`. Used by: Team absence feed returns 'no absences' on any failure.

| Field | Type | Notes |
| --- | --- | --- |
| employeeId | string |  |
| name | string |  |
| companyId | string |  |
| days | CalendarFeedDay[] |  |
| from (args) | string YYYY-MM-DD |  |

## GetEmployeeCalendarFeedArgs (vmm)

Where: `src/services/queryApi/queryEndpointsCalendar/types.ts:111-118`. Used by: Employee calendar requires the employee's company tenant, Employee calendar month grid shows mock data instead of the employee's real calendar.

| Field | Type | Notes |
| --- | --- | --- |
| companyId | number |  |
| companyTenantId | string |  |
| employeeId | string |  |
| from | string |  |
| offset | number | screen passes 100 |
| direction | 0 / 1 | 0 past, 1 future |

## AbsenceRegistrationResource (vmm)

Where: `src/types/calendar.ts:54-77`. Used by: Only pending requests show a status tag in the day sheet.

| Field | Type | Notes |
| --- | --- | --- |
| Id | string |  |
| EmployeeId | string |  |
| AbsenceTypeId | string |  |
| StartDate | string |  |
| EndDate | string |  |
| Duration | string |  |
| Status | 'Pending' / 'Approved' / 'Rejected' / 'Cancelled' |  |
| Comment | string |  |
| CreatedDate | string |  |
| ModifiedDate | string |  |

## EmployeePositionBalanceResource (vmm)

Where: `src/types/calendar.ts:96-109`. Used by: End-of-year balance request defaults to full expansion with balance sums.

| Field | Type | Notes |
| --- | --- | --- |
| EmployeeId | string |  |
| PositionId | string |  |
| Balance | number |  |
| BalanceType | 'Vacation' / 'Overtime' / 'Flex' / 'Sick' |  |
| Year | number |  |

## EmployeeBalanceTotalResource (vmm)

Where: `src/types/calendar.ts:120-148`. Used by: End-of-year balance request defaults to full expansion with balance sums.

| Field | Type | Notes |
| --- | --- | --- |
| EmployeeId | string |  |
| TotalBalance | number |  |
| BalanceBreakdown | EmployeePositionBalanceResource[] |  |
| Data[].Family.Name | string |  |
| Data[].Data.Items[].Value | {Amount:number, Unit:string} |  |
| Data[].FieldInfo.Items[] | {Id, DisplayName, Required, Validations, DataType, Unit, Conditions} |  |

## BalancesSearchRequest (vmm)

Where: `src/types/calendar.ts:111-118`. Used by: -.

| Field | Type | Notes |
| --- | --- | --- |
| EmployeeIds | string[] |  |
| VacationAgreement | string |  |
| Period | 0 / 1 / 2 / 3 | meaning of values not defined client-side |

## Calendar display settings (persisted) (vmm)

Where: `src/screens/EmployeeCalendarScreen/components/CalendarOptionsMenu/CalendarOptionsMenu.tsx:37-84`. Used by: Calendar hides entry types the user filtered out, Week numbers are ISO weeks shown on the Monday cell, Hide-weekends grid shows Monday to Friday rows only, Turning sync on saves the setting only if the sync run succeeds; turning it off always saves Off.

| Field | Type | Notes |
| --- | --- | --- |
| calendarViewMode | 'grid' / 'agenda' | default grid |
| calendarDisplayMode | 'icons' / 'labels' | default icons |
| calendarHideWeekends | boolean | default false |
| calendarShowWeekNumbers | boolean | default true |
| calendarShowAttendance/Absence/Supplement | boolean | default true; local-only |
| calendarSync | 'sync_off' / 'sync_birthdays' / 'sync_anniversaries' / 'sync_all' | default sync_off |

## AgendaItem (vmm)

Where: `src/screens/EmployeeCalendarScreen/components/EmployeeCalendarAgendaView/EmployeeCalendarAgendaView.tsx:19-22`. Used by: List view subtitle shows hours, quantity or time range, Calendar date headings are capitalised in the app language.

| Field | Type | Notes |
| --- | --- | --- |
| date | string YYYY-MM-DD |  |
| event | CalendarFeedItem |  |

## BalancesOverview (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/BalancesOverview/Model/Domain/BalancesOverview.swift`. Used by: Balances summary hours and amounts formatting, Balances toggle choice is remembered per section, Balance group total shown as expandable row.

| Field | Type | Notes |
| --- | --- | --- |
| sections | [Section] |  |
| Section.id | String |  |
| Section.kind | summary / balance(EmployeeBalanceGroup.Category) |  |
| Section.title | String |  |
| Section.control | Control? |  |
| Section.items | [Item] |  |
| Item.id/analyticsName/title | String |  |
| Item.subtitle | String? |  |
| Item.value | Value | duration(Duration) / amount(Double, unit) / options([String: Value]) / none |
| Item.children | [Item] |  |
| Control.kind | toggle / unsupported |  |
| Control.options | [String] |  |
| Control.defaultOption | String |  |

## BalancesOverviewUIModel (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/BalancesOverview/Model/UI/BalancesOverviewUIModel.swift`. Used by: Balances summary hours and amounts formatting, Balances toggle choice is remembered per section.

| Field | Type | Notes |
| --- | --- | --- |
| sections | [Section(id, icon, title, rows)] |  |
| Row | label / expandable / toggle |  |
| ToggleRow.isOn | Bool |  |
| ToggleRow.onOption/offOption | String |  |
| LabelRow.value | String (formatted) |  |

## CalendarFilterPreferences (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/CalendarFilterPreferences.swift`. Used by: Calendar filters are saved on the device.

| Field | Type | Notes |
| --- | --- | --- |
| hideWeekends | Bool (persisted, default false) |  |
| showLabels | Bool |  |
| hideAbsence | Bool |  |
| hideAttendance | Bool |  |
| hideSupplement | Bool |  |
| hideRoster | Bool |  |
| showWeekNumbers | Bool |  |
| hiddenEventTypes | Set<FilterableType> (derived) |  |

## CalendarGridFeature.State (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/CalendarGridFeature.swift`. Used by: Tapping a calendar day: register on empty day, details otherwise, Long-press and drag registers a period, Roster shifts cannot be opened as registrations.

| Field | Type | Notes |
| --- | --- | --- |
| selectedMonth | Date |  |
| startDate/endDate | Date |  |
| days | [CalendarDayUIModel] |  |
| calendarEvents | Loadable<[CalendarEventUIModel], CalendarGridRepositoryError> |  |
| availableFeatures | [UserPermission] |  |
| selectedDays | DateInterval? |  |
| isWriteAvailable | Bool (derived) |  |
| isConfirmTimeAvailable | Bool (derived) |  |
| daysPerWeek | Int (7 or 5) |  |

## AbsenceRegistrationTypeRepository / EditMode (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/Repository/AbsenceRegistrationTypeRepository/AbsenceRegistrationTypeRepository.sw…`. Used by: Only input type, comment and sickness percentage survive a type change, Delete is available only in edit mode and must be confirmed.

| Field | Type | Notes |
| --- | --- | --- |
| editMode | new(source) / newFromPrediction(source) / edit |  |
| absenceType | async -> AbsenceType? |  |
| linksForEdit | async -> [APIAction] |  |

## CalendarEventSource / AbsenceRegistrationEventType / CalendarCreateEventParams (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/CalendarEventEditing/CalendarEventEditorTypes.swift`. Used by: Check-in edit and delete need server links, Server-requested confirmation before saving (future registration).

| Field | Type | Notes |
| --- | --- | --- |
| CalendarEventSource | list / month / chatbot / checkin / startPage / unknown |  |
| AbsenceRegistrationEventType | timeAndAbsence / checkin |  |
| CalendarCreateEventParams.eventType/inputType | String |  |
| CalendarCreateEventParams.hasComment | Bool |  |

## AbsenceRegistrationViewModel (form state) (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceRegistrationViewModel.swift`. Used by: Save is disabled until every required field has a value, Medical certificate section applies only to sickness and is cleared when switched off, Definite-time registrations combine date and clock time in UTC.

| Field | Type | Notes |
| --- | --- | --- |
| currentType | AbsenceType? |  |
| fieldInfo | [AbsenceField] |  |
| fieldCache | [String: String] |  |
| hasSicknessCertificate | Bool |  |
| defaultCertificatePercentage | String = "100" |  |
| createEventConfirmation/updateEventConfirmation | pending server confirmation |  |
| groups | [[String]] field grouping order |  |

## EditAbsenceAction (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrationCoordinator/EditAbsenceRegistrationCoordinator.swift`. Used by: Satisfaction survey offered after save, not after delete.

| Field | Type | Notes |
| --- | --- | --- |
| case | save / delete |  |

## CalendarViewMode (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarContainerViewController.swift`. Used by: Calendar view mode remembered.

| Field | Type | Notes |
| --- | --- | --- |
| rawValue | list / month |  |

## CalendarGridItem (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Model/Domain/CalendarGridItem.swift:53-77`. Used by: Month grid: confirmed and approved timesheet entries are built separately, Month grid knows only approved, rejected and pending request statuses, Confirmed-time entry is added to a month even when the feed had none.

| Field | Type | Notes |
| --- | --- | --- |
| id | String |  |
| startDate | Date |  |
| endDate | Date? |  |
| itemType | CalendarGridItemType | absence(AbsenceItemType) / confirmTime(confirmed/approved) / roster(useWorkshiftsInHours) / specialDay / invalid |
| title | String |  |
| description | String |  |
| approvalStatus | CalendarGridItemRequestStatus | approved / rejected / pending / none |
| filterableType | FilterableType? | absence / attendance / supplement / unknown |

## CalendarEventUIModel (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Model/UI/CalendarEventUIModel.swift:11-75`. Used by: Month cells show only absence and roster events, filtered by type, Days on or before the confirmation date are marked confirmed or approved, Day detail sheet: which actions appear and how events are listed.

| Field | Type | Notes |
| --- | --- | --- |
| id | String |  |
| startDate | Date |  |
| endDate | Date? |  |
| eventType | EventType |  |
| title | String |  |
| description | String |  |
| approvalStatus | ApprovalStatus |  |
| filterableType | FilterableType? |  |

## CalendarDayUIModel (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Model/UI/CalendarDayUIModel.swift:11-53`. Used by: Days on or before the confirmation date are marked confirmed or approved, Only days of the displayed month show events and respond to taps, Weekend is always Saturday and Sunday.

| Field | Type | Notes |
| --- | --- | --- |
| date | Date |  |
| day | Int |  |
| isCurrentMonth | Bool |  |
| isCurrentDay | Bool |  |
| isTimeConfirmedForThisDay | Bool |  |
| isTimeApprovedForThisDay | Bool |  |
| isWeekendDay | Bool |  |
| isSpecialDay | Bool |  |
| weekOfYear | Int |  |
| events | [CalendarEventUIModel] |  |
| filteredEvents | [CalendarEventUIModel] |  |

## CalendarViewFilterItem / CalendarViewFilterSection (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/Components/CalendarViewFilterItem.swift:4-37`. Used by: Calendar display filter defaults.

| Field | Type | Notes |
| --- | --- | --- |
| id | String | hideWeekends, showWeekNumbers, hideAbsence, hideAttendance, hideSupplement, eventStyleIcons, eventStyleText, showRoster |
| title | String |  |
| type | checkbox(Bool) / radio(Bool) |  |

## DayDetailFeature.State (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/DayDetailFeature.swift:20-38`. Used by: Day detail sheet: which actions appear and how events are listed, Confirming time from the day sheet: errors block, warnings need user approval.

| Field | Type | Notes |
| --- | --- | --- |
| day | CalendarDayUIModel |  |
| title | String |  |
| isConfirmTimeInProgress | Bool |  |
| isConfirmTimeAvailable | Bool |  |
| isWriteAvailable | Bool |  |
| alert | AlertState? |  |

## ConfirmTimeUseCase / ConfirmTimeUseCaseError (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/UseCase/ConfirmTimeUseCase.swift:9-17`. Used by: Confirming time from the day sheet: errors block, warnings need user approval.

| Field | Type | Notes |
| --- | --- | --- |
| confirm | (Date) async throws -> Void |  |
| confirmForced | (Date) async throws -> Void |  |
| failed | String |  |
| warningRequired | (message: String, date: Date) |  |

## CalendarViewModelAbsence / CalendarViewModelConfirmTime (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/ViewModels/CalendarViewModelAbsence.swift:17-30`. Used by: List view: timesheet counts as approved when the approval date is on or after the confirmation date, List calendar groups by UTC month, newest first, without duplicates, Approval status labels.

| Field | Type | Notes |
| --- | --- | --- |
| absenceItem | CalendarItemAbsence |  |
| confirmTimeDetails | ConfirmTimeDetails | confirmer.date, approver.date |
| startDate | Date? |  |
| hasSeparator | Bool |  |
| hideDate | Bool |  |
| title | String? |  |

## CalendarChatBotMessageViewModel and Event (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/ChatbotMessage/CalendarChatBotMessageViewModel.swift:15-131`. Used by: How the agent reports registration results and failures, A deleted absence is shown as struck through in the earlier success message.

| Field | Type | Notes |
| --- | --- | --- |
| sender | Sender |  |
| messageType | text / loading / predictedEventsSummary / registeredEventsSummary / error / absenceRegistrationConfirmationRequired |  |
| timestamp | Date |  |
| text | String |  |
| events | [Event] | Event: id UUID, listIcon, eventDataType, error |
| quickResponseActions | [QuickResponseAction] |  |
| messageAction | MessageAction? |  |

## EventDataType (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Message/EventData/EventDataType.swift:13-95`. Used by: Sick leave missing a required medical certificate date cannot be confirmed directly, Employee Agent confirms the timesheet without checking template validations.

| Field | Type | Notes |
| --- | --- | --- |
| predictedAbsence | AbsenceType |  |
| registeredAbsence | (AbsenceType, retrievalLink APIAction) |  |
| registeredAbsenceDeleted | AbsenceType |  |
| deletedAbsence | AbsenceType |  |
| absenceConfirmationRequired | CreateAbsenceRegistrationConfirmation |  |
| confirmTime | (ConfirmTimeTemplate, updateAction APIAction) |  |
| isReadyToBeConfirmed | Bool |  |

## RegisteredAbsence / PredictedAbsence / PredictedAbsenceResult (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:18-37`. Used by: Absences created in the chat can be opened only if they have a retrieval link, A deleted absence is shown as struck through in the earlier success message.

| Field | Type | Notes |
| --- | --- | --- |
| id | UUID |  |
| absenceType | AbsenceType |  |
| apiAction / retrievalLink | APIAction |  |

## QuickResponseAction (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Message/QuickResponseAction/QuickResponseAction.swift:13-47`. Used by: Agent offers Edit only when exactly one registration was predicted, Confirm actions are locked while a submission is running.

| Field | Type | Notes |
| --- | --- | --- |
| type | QuickResponseActionType | confirmCalendarEventPrediction, confirmConfirmTimePrediction, cancelPrediction, editCalendarEventPrediction, editAbsenceRegistration, cancelAbsenceRegistration, confirmFutureAbsenceRegistration |
| title | String |  |
| message | CalendarChatBotMessageViewModel? |  |
| style | confirmation / primary / normal / cancel |  |
| run | MessageOperation |  |

## RegisterAbsenceEventsUseCase.AbsenceTypeEvent / AbsenceRegistrationState (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/UseCase/RegisterAbsenceEventsUseCase.swift:22-39`. Used by: Agent registers each predicted absence separately and in parallel.

| Field | Type | Notes |
| --- | --- | --- |
| id | UUID |  |
| absenceType | AbsenceType |  |
| state | completed(AbsenceRegistrationResponse) / failed(Error) |  |

## UserPermission calendar groups (me-ios)

Where: `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Extensions/ArrayExtensions.swift:11-34`. Used by: Calendar is available only to users with an absence or time permission, Register-event button needs a write permission, Confirmed-time data is fetched based on company features, not user permissions.

| Field | Type | Notes |
| --- | --- | --- |
| hasCalendarPermissions | Bool | addAbsence/addTime/absenceReadOnly/timeReadOnly/absenceWrite/timeWrite |
| hasCalendarWritePermissions | Bool | addAbsence/addTime/absenceWrite/timeWrite |
| hasAbsencePermissions | Bool |  |
| hasTimePermissions | Bool |  |
| hasConfirmTimePermission | Bool | confirmTime |

## CalendarItemAbsence (me-ios)

Where: `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/CalendarItemAbsence.swift:39-118`. Used by: Start-page absence cards: which vacation and parental leave items become cards, Calendar feed keeps only Absence-type items.

| Field | Type | Notes |
| --- | --- | --- |
| id | String? |  |
| itemType | AbsenceItemType? | Absence, ParentalLeave, SickChild, Sickness, Vacation, Attendance, Supplement, Unknown |
| requestStatus | String? | approved, denied, ... |
| inputType | AbsenceInputType? | FullDay, Hours, Percent, Quantity, DefiniteTime |
| properties | [AbsenceProperty]? |  |
| type/title/year/month/links/dateFrom/dateTo/filterableType | inherited from CalendarItem | dates decoded as UTC date-time |

## AbsenceType (registration template) (me-ios)

Where: `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/AbsenceType.swift:31-119`. Used by: Absence save response lifecycle: Success, ValidationError, Error, ConfirmationRequired, Registration summary text (chatbot style): name, date range, input type, Absence from and to dates accept date-only or date-time.

| Field | Type | Notes |
| --- | --- | --- |
| displayName | String? |  |
| eventType | AbsenceItemType? |  |
| eventTypeShortCode | String? |  |
| fieldInfo | [AbsenceField]? |  |
| balance.remainingVacationDays | Double? |  |
| metadata | postUri, saveButtonText |  |
| onShowNotifications | [text, style] | style Warning |
| additionalInfo | String? |  |

## AbsenceField / FieldOptionItem (me-ios)

Where: `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/AbsenceField.swift:20-278`. Used by: Input-type display: hours rounded to whole numbers, percent divided by 100, quantity as 'Name: value', Empty option values are sent as null, Dimension option display as 'id - name'.

| Field | Type | Notes |
| --- | --- | --- |
| id | String | Comment, InputType, Child, FromDate, ToDate, Percent, Certificate.*, FromTime, ToTime, Dimensions, DefiniteTime |
| dataType | enum | date, string, percent, decimal, bool, idoption, hourpercent, object, time |
| required | Bool |  |
| value | String |  |
| selection | AbsenceFieldSelection? |  |
| options.items | [FieldOptionItem] | id, displayName, dataType (bool/decimal/percent), value |
| hint | value, text |  |
| items | [AbsenceField]? |  |

## AbsenceRegistrationResponse / AbsenceUpdateResponse (me-ios)

Where: `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/AbsenceType.swift:135-237`. Used by: Absence save response lifecycle: Success, ValidationError, Error, ConfirmationRequired.

| Field | Type | Notes |
| --- | --- | --- |
| statusCode | ResponseType | Error, Success, ValidationError, ConfirmationRequired, unknown |
| errors | [String]? |  |
| template | AbsenceType? |  |
| retrievalLink / updateUrl | APIAction? / String? |  |

## ConfirmTimeTemplate and validations (me-ios)

Where: `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/ConfirmTimeTemplate.swift:24-281`. Used by: Confirm-time date validations: the rule name says when the date fails, Confirm-time: first failing validation at a given level.

| Field | Type | Notes |
| --- | --- | --- |
| data.date | Date? |  |
| fieldInfo.items | [TimeTemplateFieldItem] | id 'Date', required, dataType, value, hint |
| validations | [TimeTemplateFieldItemValidation] | type RegEx/Object, name Required/GreaterThan/GreaterThanOrEqual/LessThan/LessThanOrEqual, level Error/Warning, value, displayText |

## ConfirmTimeDetails (me-ios)

Where: `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/ConfirmTimeDetails.swift:13-72`. Used by: Time confirmation and its template: HTTP 403 means the feature is off.

| Field | Type | Notes |
| --- | --- | --- |
| confirmer | ConfirmTimeUser? | date, userId, firstName, lastName |
| approver | ConfirmTimeUser? |  |
| status | ConfirmTimeStatus |  |

## Checkin / CheckinCheckoutStatus (me-ios)

Where: `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/Checkin/Checkin.swift:11-59`. Used by: Check-in and check-out send the device's local time with time zone, Deleting a check-in uses the server's link and HTTP method.

| Field | Type | Notes |
| --- | --- | --- |
| status | CheckinStatus | Idle, CheckedIn, Error, Conflict, unknown |
| timestamp | Date? | ISO-8601 without fractional seconds |
| updateUrl/deleteUrl/checkoutTemplateUrl | String? |  |

## Workshift / WorkshiftResponse (me-ios)

Where: `EmployeeServices/CalendarInterface/Sources/CalendarInterface/DomainModel/Roster/Workshift.swift:3-26`. Used by: Workshift (roster) display: hours mode shows the length, otherwise start and end times, Workshift company setting defaults to time mode, and shifts without a parseable start are dropped.

| Field | Type | Notes |
| --- | --- | --- |
| id | String | 'roster-' + startLocal |
| name | String |  |
| startDate | Date |  |
| endDate | Date? |  |
| lengthInMinutes | Int |  |
| useWorkshiftsInHours | Bool | company-level flag from WorkshiftResponse |

## SpecialDay / SpecialDayResponse (me-ios)

Where: `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/SpecialDayResponse.swift:3-13`. Used by: Special days: unparseable dates dropped, public-holiday flag ignored.

| Field | Type | Notes |
| --- | --- | --- |
| date | String (ISO date) / Date |  |
| displayName | String? |  |
| isPublicHoliday | Bool | dropped when mapped to SpecialDay |

## EmployeeBalanceGroup / EmployeeBalance (me-ios)

Where: `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/Balances/EmployeeBalanceGroup.swift:12-49`. Used by: Balance group categories: vacation, attendance, sickness, sick child, Balance durations shown as hours and minutes, zero units hidden.

| Field | Type | Notes |
| --- | --- | --- |
| category | Category | vacation, attendance, sickness, sickchild, none |
| displayName/categoryDisplayName/subtitle | String? |  |
| total | Double? |  |
| totalUnit | EmployeeBalanceUnit | id e.g. 'Hours' |
| balances | [EmployeeBalance] | displayName, amount Double, unit, options [String: Double] |

## TimeBalanceOverviewResponse (me-ios)

Where: `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/Balances/TimeBalanceOverviewResponse.swift:3-92`. Used by: Balance durations shown as hours and minutes, zero units hidden.

| Field | Type | Notes |
| --- | --- | --- |
| summary | label, items[name,label,hours Double,duration String,items] |  |
| balances.sections | [EmployeeBalanceGroup] |  |
| balances.controls | [type,label,category,options,default] |  |

## CalendarTemplates (me-ios)

Where: `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/CalendarTemplates.swift:13-49`. Used by: Template lookup by event type short code.

| Field | Type | Notes |
| --- | --- | --- |
| groups | [CalendarTemplateGroup] | name, displayName, items [AbsenceTemplateItem: displayName, eventType, eventTypeShortCode, eventTypeDisplayName] |

## PredictCalendarRegistrationResponse (me-ios)

Where: `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/CalendarBot/PredictCalendarRegistrationResponse.swift:10-20`. Used by: Employee Agent rejects an empty prompt, Registration summary text (chatbot style): name, date range, input type.

| Field | Type | Notes |
| --- | --- | --- |
| calendarRegistrations | [AbsenceType]? |  |
| confirmTime | ConfirmTimeTemplateResponse? |  |
| balancesQueryResult | String? |  |

## DimensionValue (me-ios)

Where: `EmployeeServices/CalendarInterface/Sources/CalendarInterface/Model/DimensionValue.swift:12-59`. Used by: Dimension (cost unit) search sends the search term as query 'q'.

| Field | Type | Notes |
| --- | --- | --- |
| id | String? |  |
| displayName | String? |  |
| status | DimensionsValueStatus |  |

## CalendarViewModelClaim (claim row) (me-ios)

Where: `Employee/CalendarLeftover/CalendarViewModelClaim.swift:18-88`. Used by: Claim list row: date as day plus upper-case short month, amount with 2 decimals, status text, Duplicate claims are removed by claim id, Expense claims list is grouped by year, newest first, with undated claims in their own section.

| Field | Type | Notes |
| --- | --- | --- |
| expenseItem | APIData<ExpenseClaim> | id, title, amount, dateFrom, requestStatus.status |
| startDate | Date? |  |
| title | String? |  |
