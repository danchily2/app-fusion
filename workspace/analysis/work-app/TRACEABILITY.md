# Traceability: work-app

134 of 270 in-scope capabilities are designed (50%), 0 are built, and 196 of 214 design frames trace to a capability. Status rules are at the top of `scripts/trace.py`.

| Id | Capability | Fusion | Status | Screens | New-app notes |
| --- | --- | --- | --- | --- | --- |
| CAP-001 | View a calendar month by month | shared-diverged | designed | 08 · Calendar, Calendar / Team, Calendar / Team employee picker, Calendar / week grid … | - |
| CAP-002 | Browse the calendar as a scrolling list | shared-diverged | designed | Calendar / list view | - |
| CAP-003 | Switch between list and month view of the calendar | shared-diverged | designed | 08 · Calendar, Calendar / list view, Calendar / week grid | - |
| CAP-004 | See the details of a calendar day | shared-diverged | designed | Calendar / today / time confirmation, Calendar / day with entries, Calendar / empty day, Calendar / date range | - |
| CAP-005 | Customize what the calendar shows | shared-diverged | designed | 08 · Calendar, Calendar / Filter view | - |
| CAP-006 | Start a time or absence registration from the calendar | unique | designed | 08 · Calendar, Calendar / list view, Calendar / week grid, Calendar / today / time confirmation … | - |
| CAP-008 | See what needs attention across modules on Home | unique | designed | 01 · Start, Start / expanded module cards | - |
| CAP-009 | View an employee's absence balances | unique | designed | HRM / Employee details, HRM / Employee balances, HRM / Eli Hovland / Employee details, HRM / Mona Hovland / Employee details … | - |
| CAP-010 | See my time and absence balances for a month | unique | designed | 08 · Calendar, Calendar / Summary | - |
| CAP-011 | See my vacation balances on the start page | unique | designed | 01 · Start, Start / expanded module cards | - |
| CAP-012 | Register an absence or time event | unique | designed | Start / expanded module cards, Calendar / Select type, Working hours / From-to, Working hours / Full day … | - |
| CAP-013 | Pick cost-unit dimension values for a registration | unique | designed | Working hours / From-to, Working hours / Full day, Working hours / Hours, Working hours / Test1 unit picker | - |
| CAP-014 | View details of a registered absence | unique | no-design |  | - |
| CAP-015 | Edit a registered absence | unique | no-design |  | - |
| CAP-016 | Delete a registered absence | unique | no-design |  | - |
| CAP-017 | See upcoming and ongoing vacation and parental leave on the start page | unique | designed | Start / expanded module cards | - |
| CAP-018 | Check in and check out for the workday | unique | no-design |  | - |
| CAP-019 | Edit or delete a check-in/check-out registration | unique | no-design |  | - |
| CAP-020 | Confirm worked time up to a date | unique | designed | Calendar / today / time confirmation, Calendar / Confirm time, Calendar / date picker / Confirm time | - |
| CAP-021 | Register time or absence by chatting with the Employee Agent | unique | no-design |  | - |
| CAP-022 | Confirm the time sheet through the Employee Agent | unique | no-design |  | - |
| CAP-023 | Ask the Employee Agent about leave balances | unique | designed | GAiA / conversation answer, GAiA Agent / answer | - |
| CAP-024 | Edit a predicted registration before saving it | unique | no-design |  | - |
| CAP-025 | View, edit or delete an absence created in the agent chat | unique | no-design |  | - |
| CAP-026 | Learn how to use the Employee Agent and try example prompts | unique | no-design |  | - |
| CAP-027 | Send feedback about the Employee Agent | unique | no-design |  | - |
| CAP-028 | Browse my expense claims by year and filter by status | unique | designed | 02 · Expense, Claims · List, Claim · Approved | - |
| CAP-029 | Browse my payslips by payment date, filtered by employer | unique | designed | 07 · Payslips | - |
| CAP-030 | Switch the active Business NXT company | unique | designed | Switch company | - |
| CAP-031 | Open a Business NXT work area | unique | designed | 05 · BNXT, BNXT / Suppliers, BNXT / Purchase, BNXT / Products … | - |
| CAP-032 | Browse Business NXT orders | unique | designed | 05 · BNXT, BNXT / Sort orders, BNXT / Purchase | - |
| CAP-033 | View a Business NXT order | unique | no-design |  | - |
| CAP-034 | Edit a Business NXT order's references, delivery date and lines | unique | no-design |  | - |
| CAP-035 | Create a sales or purchase order | unique | no-design |  | - |
| CAP-036 | Send a purchase order to approval | unique | no-design |  | - |
| CAP-037 | Cancel a purchase order | unique | no-design |  | - |
| CAP-038 | Open an order attachment | unique | no-design |  | - |
| CAP-039 | Track documents sent for approval | unique | no-design |  | - |
| CAP-040 | Withdraw a pending approval task | unique | no-design |  | - |
| CAP-041 | Browse and search archived invoices | unique | no-design |  | - |
| CAP-042 | See money owed by customers or to suppliers | unique | no-design |  | - |
| CAP-043 | Review an associate's open ledger entries | unique | no-design |  | - |
| CAP-044 | View a customer or supplier card | unique | no-design |  | - |
| CAP-045 | Look up products, customers, suppliers and stock | unique | designed | BNXT / Suppliers, BNXT / Sort products, BNXT / Sort items, BNXT / Sort contacts … | - |
| CAP-046 | Check a product's stock | unique | designed | BNXT / Sort items, BNXT / Inventory | - |
| CAP-047 | Ask the AI assistant a question | shared-diverged | designed | GAiA / conversation answer, GAiA Agent / welcome, GAiA Agent / answer | - |
| CAP-048 | Open the assistant for the current screen from the header | shared-diverged | designed | HRM / Mona Hovland / Employee details | - |
| CAP-049 | Ask the assistant about an approval task or past approval | unique | designed | Manager / Inline GAiA search | - |
| CAP-050 | Ask the assistant about an employee | unique | designed | HRM / Eli Hovland / Employee details, HRM / Elin Rike / Employee details, HRM / Daniel Moe / Employee details | - |
| CAP-051 | Ask the assistant from Home, Home search or a list's search band | unique | designed | Manager / Inline GAiA search, GAiA / suggested questions, GAiA / search results, GAiA / no matches … | - |
| CAP-052 | Ask the payslip assistant about a payslip or year-end report | unique | designed | 07 · Payslips, Payslips / year-end list | - |
| CAP-053 | Start from a suggested question | shared-diverged | designed | Manager / Inline GAiA search, GAiA / suggested questions, GAiA Agent / welcome | - |
| CAP-054 | Browse the catalog of questions the assistant can answer | shared-diverged | no-design |  | - |
| CAP-055 | Start a new assistant conversation | unique | designed | GAiA Agent / welcome, GAiA Agent / answer | - |
| CAP-056 | Find and resume a past assistant conversation | unique | no-design |  | - |
| CAP-057 | Rename, pin or delete an assistant conversation | unique | no-design |  | - |
| CAP-058 | Resume the conversation an answer-ready notification announced | unique | no-design |  | - |
| CAP-059 | Rate an assistant answer | shared-diverged | no-design |  | - |
| CAP-060 | Copy an assistant answer | unique | no-design |  | - |
| CAP-061 | Open a source cited in an assistant answer | unique | no-design |  | - |
| CAP-062 | Approve or decline an action the assistant asks permission for | unique | no-design |  | - |
| CAP-063 | Approve or reject an approval task from within the assistant chat | unique | no-design |  | - |
| CAP-064 | Open an approval task linked in an assistant answer | unique | no-design |  | - |
| CAP-065 | Let the assistant navigate the app | unique | no-design |  | - |
| CAP-066 | Dictate a message to the assistant by voice | shared-diverged | designed | GAiA Agent / welcome, GAiA Agent / answer | - |
| CAP-067 | Switch between the app's main areas | shared-diverged | designed | 01 · Start, 04 · HRM, 09 · More, Approval / No tasks … | - |
| CAP-068 | Open any integration from the More sheet | unique | designed | 09 · More, More / edit pinned modules | - |
| CAP-069 | Customize which areas are pinned to the tab bar | unique | designed | 09 · More, More / edit pinned modules | - |
| CAP-070 | Search and sort a work list | unique | designed | 04 · HRM, BNXT / Sort orders, BNXT / Sort products, BNXT / Sort items … | - |
| CAP-071 | Search across approvals, invoices, employees and orders | unique | designed | 01 · Start, GAiA / suggested questions, GAiA / search results, GAiA / no matches | - |
| CAP-073 | Open a pending approval task from Home | unique | designed | Start / expanded module cards | - |
| CAP-074 | Open an upcoming Autopay payment from Home | unique | designed | Start / expanded module cards | - |
| CAP-075 | Follow up on unread dialogues, absent colleagues and new hires from Home | unique | no-design |  | - |
| CAP-076 | Review recent activity across approval, payments and dialogues | unique | no-design |  | - |
| CAP-077 | Jump into a licensed module from Home | unique | designed | Start / expanded module cards | - |
| CAP-078 | Discover and act on What's New announcements | shared-diverged | designed | 01 · Start | - |
| CAP-079 | See personal highlights on the start page | unique | designed | 01 · Start, Start / expanded module cards | - |
| CAP-080 | Open the latest or upcoming payslip from the start page | unique | designed | 01 · Start, Start / expanded module cards | - |
| CAP-081 | Track the status of submitted expense claims from the start page | unique | designed | Claim · Awaiting | - |
| CAP-082 | Resume unsent expense drafts from the start page | unique | designed | 01 · Start, Start / expanded module cards | - |
| CAP-083 | Read important messages, surveys and app-update prompts on Home | unique | no-design |  | - |
| CAP-084 | Start a common task from Home quick selections | unique | no-design |  | - |
| CAP-085 | Reach HR profile, documents and benefits or the employee list from Home shortcuts | unique | no-design |  | - |
| CAP-086 | Open my user menu to reach profile, account and HR pages | unique | designed | Profile sheet | - |
| CAP-087 | Sign out from the user menu | shared-diverged | dropped | Profile sheet | - |
| CAP-088 | Open a specific app section from a link | unique | no-design |  | - |
| CAP-089 | Acknowledge a blocking startup notice | unique | no-design |  | - |
| CAP-090 | Go through first-run onboarding | unique | no-design |  | - |
| CAP-091 | View a financial reporting dashboard for a company and period | unique | no-design |  | - |
| CAP-092 | Choose the customer and tenant to report on | unique | no-design |  | - |
| CAP-093 | Filter a dashboard chart by category and choose which series to show | unique | no-design |  | - |
| CAP-094 | Examine a dashboard chart in detail | unique | no-design |  | - |
| CAP-095 | Read how-to help for the current screen | unique | designed | Manager / About view modal | - |
| CAP-096 | Browse help (FAQ) by topic | unique | designed | 10 · Settings, Settings / appearance menu, Settings / FAQ categories, FAQ / Payslip … | - |
| CAP-097 | Check why a module is not available for my company | unique | designed | FAQ / Payslip, FAQ / Expense / first answer expanded, FAQ / Time & Absence | - |
| CAP-098 | Send feedback about the app | shared-diverged | designed | Settings / FAQ categories, Settings / Send feedback, Settings / Accessibility statement, Profile sheet … | - |
| CAP-099 | Send feedback about Business NXT line editing | unique | no-design |  | - |
| CAP-100 | Rate the app in the store | shared-diverged | no-design |  | - |
| CAP-101 | Answer an NPS satisfaction survey | shared-diverged | no-design |  | - |
| CAP-102 | Decline the NPS survey or stop it from showing again | unique | no-design |  | - |
| CAP-103 | Take or dismiss a survey from the home card | unique | no-design |  | - |
| CAP-104 | Volunteer for user testing | unique | no-design |  | - |
| CAP-105 | Review and share failed request logs | unique | no-design |  | - |
| CAP-106 | Copy account and device details for support | unique | designed | 10 · Settings | - |
| CAP-107 | Read open-source licenses and the accessibility statement | shared-diverged | dropped | 10 · Settings, Settings / Licenses, Settings / Accessibility statement, Privacy & terms | - |
| CAP-108 | Open app settings | shared-diverged | designed | 10 · Settings, Settings / appearance menu, Profile sheet | - |
| CAP-109 | Choose the app language | shared-diverged | designed | 10 · Settings, Settings / appearance menu, Settings / change-language alert | - |
| CAP-110 | Choose light, dark or system appearance | shared-diverged | designed | 10 · Settings, Settings / appearance menu | - |
| CAP-111 | Turn vibration and the holiday theme on or off | unique | no-design |  | - |
| CAP-112 | Control anonymous analytics collection | unique | designed | Privacy & terms | - |
| CAP-113 | Read the accessibility statement | shared-diverged | designed | 10 · Settings, Settings / appearance menu, Settings / Accessibility statement, Privacy & terms | - |
| CAP-114 | Read the terms of service and privacy information | shared-diverged | designed | Privacy & terms | - |
| CAP-115 | View app version and open-source licenses | shared-diverged | designed | 10 · Settings, Settings / appearance menu, Settings / Licenses, Privacy & terms | - |
| CAP-116 | See the signed-in account and device info in Settings | unique | designed | 10 · Settings, Settings / appearance menu, Profile sheet | - |
| CAP-117 | Allow or block screenshots of the app | unique | no-design |  | - |
| CAP-118 | Update the app when a new version is suggested or required | shared-diverged | no-design |  | - |
| CAP-119 | Keep app state after restarting or updating the app | shared-diverged | no-design |  | - |
| CAP-120 | Use internal developer tools and feature flags | shared-diverged | designed | 10 · Settings, Settings / appearance menu, Settings / Feature flags | - |
| CAP-121 | Switch backend environment in test builds | shared-diverged | dropped |  | - |
| CAP-122 | See that an employee's birthday is coming up | unique | no-design |  | - |
| CAP-123 | Turn birthday and work-anniversary reminders on or off | unique | no-design |  | - |
| CAP-124 | Browse the employee directory | shared-diverged | designed | 04 · HRM, HRM / Sort employees | - |
| CAP-125 | Search the employee directory by name | shared-diverged | no-design |  | - |
| CAP-126 | Filter the employee directory with quick filters | shared-diverged | no-design |  | - |
| CAP-127 | Hide or show companies in the employee list | unique | no-design |  | - |
| CAP-128 | View an employee's personal, address and employment details | unique | designed | HRM / Employee employment and salary, HRM / Employee details, HRM / Employee personal details, HRM / Employee post address … | - |
| CAP-129 | View a colleague's Dottie profile | shared-diverged | no-design |  | - |
| CAP-130 | Contact an employee by call, SMS, email or share | unique | designed | HRM / Employee children, HRM / Employee emergency contact, HRM / Employee details, HRM / Employee balances … | - |
| CAP-131 | Copy an employee's post address | unique | designed | HRM / Employee post address | - |
| CAP-132 | Edit an employee's name, phone numbers and emails | unique | no-design |  | - |
| CAP-133 | Edit an employee's postal address | unique | designed | HRM / Edit post address, HRM / Employee post address, HRM / Eli Hovland / Edit post address, HRM / Mona Hovland / Edit post address … | - |
| CAP-134 | Add or edit an employee's child | unique | designed | HRM / Employee children, HRM / Add child, HRM / Edit child, HRM / Eli Hovland / Add child … | - |
| CAP-135 | Remove an employee's child | unique | no-design |  | - |
| CAP-136 | Add or edit an employee's emergency contact | unique | designed | HRM / Employee emergency contact, HRM / Mona Hovland / Employee details | - |
| CAP-137 | Remove an employee's emergency contact | unique | no-design |  | - |
| CAP-138 | Generate an AI birthday or work-anniversary greeting | unique | no-design |  | - |
| CAP-139 | Send a greeting to the employee by share sheet or SMS | unique | no-design |  | - |
| CAP-140 | Save a greeting for later | unique | no-design |  | - |
| CAP-141 | View my personal information | unique | no-design |  | - |
| CAP-142 | Update my phone numbers and home address | unique | no-design |  | - |
| CAP-143 | Change my salary bank account number | unique | no-design |  | - |
| CAP-144 | Add an emergency contact or child | shared-diverged | no-design |  | - |
| CAP-145 | Edit an emergency contact or child | shared-diverged | no-design |  | - |
| CAP-146 | Remove an emergency contact or child | shared-diverged | no-design |  | - |
| CAP-147 | View and update my HR profile | unique | no-design |  | - |
| CAP-148 | Change or remove my profile picture | unique | no-design |  | - |
| CAP-149 | Pick and crop a profile picture (prototype) | unique | no-design |  | - |
| CAP-150 | See my pending approval tasks | unique | designed | 03 · Approval, Approval / Overdue, Approval / Grouped by company, Approval / Selected tasks … | - |
| CAP-151 | Sort approval tasks | unique | designed | 03 · Approval, Approval / Sort tasks, Approval / Grouped by company | - |
| CAP-152 | Search approval tasks and history | unique | designed | 03 · Approval, Approval / History, Approval / Grouped by company, Manager / Inline GAiA search | - |
| CAP-153 | Review an approval task | unique | designed | Approval / Invoice task, Approval / Voucher task, Approval / Reject sheet, Approval / Komplett Bedrift task … | - |
| CAP-154 | Approve an approval task | unique | designed | Approval / Invoice task, Approval / Voucher task, Approval / Approve sheet, Approval / Komplett Bedrift task … | - |
| CAP-155 | Reject an approval task | unique | designed | Approval / Invoice task, Approval / Voucher task, Approval / Reject sheet, Approval / Komplett Bedrift task … | - |
| CAP-156 | Complete a review of a task | unique | no-design |  | - |
| CAP-157 | Send a task for review to a colleague | unique | designed | Approval / Voucher task, Approval / Request review sheet | - |
| CAP-158 | Forward a task to another approver | unique | designed | Approval / Voucher task, Approval / Forward sheet | - |
| CAP-159 | Act on an approval task from the Home screen | unique | no-design |  | - |
| CAP-160 | Approve several tasks at once | unique | designed | 03 · Approval, Approval / Grouped by company, Approval / Selected tasks | - |
| CAP-161 | Review an employee's pending approval tasks | unique | no-design |  | - |
| CAP-162 | Open the requester's employee profile from a task | unique | no-design |  | - |
| CAP-163 | Comment on an approval process | unique | designed | Approval / Invoice task, Approval / Voucher task, Approval / Completed task, Approval / Komplett Bedrift task … | - |
| CAP-164 | View a task's attached documents | unique | designed | Approval / Invoice task, Approval / Voucher task, Approval / Completed task, Approval / Document … | - |
| CAP-165 | Share or download a task document | unique | designed | Approval / Document | - |
| CAP-166 | Browse my approval history | unique | designed | 03 · Approval, Approval / History | - |
| CAP-167 | View a handled approval process | unique | designed | Approval / Completed task | - |
| CAP-168 | See a task's approval workflow and history | unique | designed | Approval / Invoice task, Approval / Voucher task, Approval / Completed task, Approval / Komplett Bedrift task … | - |
| CAP-169 | Approve or reject individual accounting lines | unique | no-design |  | - |
| CAP-170 | Open a task's accounting lines | unique | designed | Approval / Invoice task, Approval / Voucher task, Approval / Completed task, Approval / Voucher line 1 … | - |
| CAP-171 | Edit the accounting lines of an invoice before approving | unique | designed | Approval / Voucher task, Approval / Voucher line 1, Approval / Voucher line 2 | - |
| CAP-172 | Apply one field value to all lines | unique | no-design |  | - |
| CAP-173 | Discard unsaved line edits | unique | no-design |  | - |
| CAP-174 | Choose which line fields to show | unique | designed | Approval / Voucher line 1, Approval / Voucher line 2, Approval / Voucher custom view | - |
| CAP-175 | Jump to a specific invoice line | unique | designed | Approval / Voucher line 1, Approval / Voucher line 2 | - |
| CAP-176 | Receive push notifications on this device | shared-diverged | no-design |  | - |
| CAP-177 | Stop push notifications to this device when signing out | shared-diverged | no-design |  | - |
| CAP-178 | Open a push notification in the right place | shared-diverged | no-design |  | - |
| CAP-179 | See that new HR notifications are waiting | unique | no-design |  | - |
| CAP-180 | Read the combined message inbox | unique | designed | Messages / populated, Messages / empty | - |
| CAP-181 | Dismiss a message from the inbox | unique | designed | Messages / populated | - |
| CAP-182 | Mark an HR notification as read | unique | no-design |  | - |
| CAP-183 | Open a document notification and confirm it as read | unique | no-design |  | - |
| CAP-184 | Read an important message from the employer or Visma | unique | no-design |  | - |
| CAP-185 | Open the app's notification settings | unique | no-design |  | - |
| CAP-186 | Review AutoPay payments waiting for my approval | unique | designed | 06 · Autopay, Autopay / Invoices, Autopay / Salary, Autopay / No payments … | - |
| CAP-187 | Search AutoPay payments | unique | designed | 06 · Autopay | - |
| CAP-188 | Select AutoPay payments for approval | unique | designed | 06 · Autopay, Autopay / Invoices, Autopay / Salary, Autopay / Expanded account … | - |
| CAP-189 | Approve selected AutoPay payments with bank two-factor signing (BankID) | unique | designed | Autopay / Selected payment | - |
| CAP-190 | Track the status of processed AutoPay payments (In progress / Deviation / In bank) | unique | no-design |  | - |
| CAP-191 | View an AutoPay payment's details | unique | no-design |  | - |
| CAP-192 | View the invoice document attached to an AutoPay payment | unique | no-design |  | - |
| CAP-193 | Change the pay date of an AutoPay payment | unique | no-design |  | - |
| CAP-194 | Add, edit or delete a note on an AutoPay payment | unique | no-design |  | - |
| CAP-195 | Review and verify AutoPay payment warnings | unique | no-design |  | - |
| CAP-196 | Cancel an AutoPay payment | unique | no-design |  | - |
| CAP-197 | Sign in with a Visma Connect account | shared-diverged | no-design |  | - |
| CAP-198 | Stay signed in without logging in again | shared-diverged | no-design |  | - |
| CAP-199 | Be signed out and told why when the session ends | shared-diverged | no-design |  | - |
| CAP-200 | Handle an account with no access | shared-diverged | no-design |  | - |
| CAP-201 | Log out | shared-diverged | designed | Profile sheet | - |
| CAP-202 | Switch between saved accounts | unique | no-design |  | - |
| CAP-203 | Add another account | unique | no-design |  | - |
| CAP-204 | Remove a saved account from the device | unique | no-design |  | - |
| CAP-205 | Switch between my employers | unique | designed | 01 · Start, Switch company | - |
| CAP-206 | Protect the app with Face ID, fingerprint or PIN | unique | designed | 10 · Settings, Settings / appearance menu | - |
| CAP-207 | Unlock the app with Face ID, fingerprint or PIN | unique | no-design |  | - |
| CAP-208 | Turn off the app lock | unique | designed | 10 · Settings | - |
| CAP-209 | Switch the backend environment | shared-diverged | no-design |  | - |
| CAP-210 | Choose a sandbox environment at login | unique | no-design |  | - |
| CAP-211 | See my vacation balances on the start page | unique | designed | Start / expanded module cards | - |
| CAP-212 | Preview a day timeline (prototype) | unique | no-design |  | - |
| CAP-213 | Fill in and edit a server-defined form | unique | no-design |  | - |
| CAP-214 | Browse payroll dialogues | unique | designed | HRM / Dialogue, HRM / Sort wage runs | - |
| CAP-215 | Start a new payroll dialogue | unique | no-design |  | - |
| CAP-216 | Read a payroll dialogue conversation | unique | designed | HRM / Department completed dialogue, HRM / Department approval dialogue | - |
| CAP-217 | Browse wage-run splits of a dialogue | unique | designed | HRM / Dialogue, HRM / Wage run | - |
| CAP-218 | Send a message in a payroll dialogue | unique | designed | HRM / Department completed dialogue, HRM / Department approval dialogue | - |
| CAP-219 | Edit a sent dialogue message | unique | no-design |  | - |
| CAP-220 | Delete a dialogue message | unique | no-design |  | - |
| CAP-221 | Rename a dialogue or change its linked wage run | unique | no-design |  | - |
| CAP-222 | Mark a dialogue as completed or reactivate it | unique | no-design |  | - |
| CAP-223 | Delete a dialogue | unique | no-design |  | - |
| CAP-224 | Approve or reject a wage run | unique | designed | HRM / Department approval dialogue | - |
| CAP-225 | View a payslip's details | unique | designed | 07 · Payslips, Payslip / detail, Payslip / detail expanded, Workspace / Prototype / Payslip details | - |
| CAP-226 | Download a payslip PDF | unique | designed | Payslip / detail, Payslip / PDF preview | - |
| CAP-227 | Export all my payslips to one PDF | unique | designed | 07 · Payslips, Payslips / year-end list | - |
| CAP-228 | Browse my year-end reports | unique | designed | 07 · Payslips, Payslips / year-end list | - |
| CAP-229 | View a year-end report | unique | designed | Payslips / year-end list, Year-end report / detail, Year-end report / PDF preview | - |
| CAP-230 | Download a year-end report PDF | unique | designed | Year-end report / detail | - |
| CAP-231 | Learn why I have no payslips | unique | designed | FAQ / Payslip, Start / expanded module cards | - |
| CAP-232 | Browse and search company documents | unique | no-design |  | - |
| CAP-233 | Open a company document | unique | no-design |  | - |
| CAP-234 | Confirm reading a required company document | unique | no-design |  | - |
| CAP-235 | View and open my personal documents | unique | no-design |  | - |
| CAP-236 | Browse employee benefits | unique | no-design |  | - |
| CAP-237 | Open and acknowledge a document from a notification | unique | no-design |  | - |
| CAP-238 | Preview a downloaded image or PDF inside the app | shared-diverged | designed | Payslip / PDF preview, Year-end report / PDF preview | - |
| CAP-239 | Open a downloaded file in another app | unique | no-design |  | - |
| CAP-240 | Browse my unsent expenses in the expenses inbox | unique | designed | 02 · Expense, Expense · Add new menu | - |
| CAP-241 | Start a new receipt, mileage or allowance | unique | designed | 02 · Expense, Claims · List, Start / expanded module cards, Expense · Add new menu | - |
| CAP-242 | Capture or import a receipt image or PDF | unique | designed | Receipt · Upload source, Receipt · Crop photo, Receipt · Crop document, Receipt · Camera | - |
| CAP-243 | Share a photo or PDF into the app to create an expense | unique | no-design |  | - |
| CAP-244 | Auto-fill a receipt from its image and get a suggested expense type | unique | no-design |  | - |
| CAP-245 | Create or edit a receipt | unique | designed | Receipt · Purpose and expense options, Shared · Date picker, Receipt · Select expense type, Receipt · New receipt | - |
| CAP-246 | Enter a receipt in a foreign currency with an exchange rate | unique | designed | Receipt · Purpose and expense options, Receipt · Select currency, Receipt · New receipt | - |
| CAP-247 | Calculate driving distance for a kilometre receipt | unique | no-design |  | - |
| CAP-248 | Add or remove attachments on an expense | unique | designed | Receipt · Delete attachment, Receipt · Attachments, Receipt · Multiple attachments, Receipt · Upload source | - |
| CAP-249 | View or download an expense attachment | unique | designed | Receipt · Attachments, Receipt · Multiple attachments, Receipt · Saved to Photos | - |
| CAP-250 | Link a credit card transaction to a receipt (merge) | unique | no-design |  | - |
| CAP-251 | Delete an unsent expense | unique | no-design |  | - |
| CAP-252 | Send selected expenses to a claim | unique | designed | 02 · Expense, Claims · List | - |
| CAP-253 | Create a new expense claim from selected expenses | unique | designed | Shared · Add expenses to claim, Claim · Create new claim | - |
| CAP-254 | Send an expense claim for approval | unique | designed | Claim · Not-Sent, Claim · Create new claim | - |
| CAP-255 | Add new or existing expenses to a claim from the claim screen | unique | designed | Claim · Edit draft | - |
| CAP-256 | Add a receipt, mileage or allowance to a claim from its form | unique | designed | Allowance · All days, Allowance · Single days, Allowance · Lodging menu, Allowance · Hotel details … | - |
| CAP-257 | Send a single expense straight for approval | unique | designed | Allowance · All days, Allowance · Single days, Allowance · Lodging menu, Allowance · Hotel details … | - |
| CAP-258 | Review an expense claim's details | unique | designed | Claim · Declined, Claim · Canceled, Claim · Not-Sent, Claim · Awaiting … | - |
| CAP-259 | Edit a claim's title and comment | unique | designed | Claim · Edit draft, Claim · Not-Sent | - |
| CAP-260 | Withdraw a claim from approval | unique | no-design |  | - |
| CAP-261 | Delete an expense claim | unique | designed | Claim · Declined, Claim · Canceled, Claim · Not-Sent | - |
| CAP-262 | View, edit or delete an item inside a claim | unique | designed | Claim · Edit draft, Claim · Not-Sent | - |
| CAP-263 | Assign cost units to an expense or claim | unique | designed | Receipt · Purpose and expense options, Mileage · Toll and reimbursement options, Mileage · Other details expanded, Mileage · Cost allocation … | - |
| CAP-264 | Assign project accounting to an expense or claim | unique | no-design |  | - |
| CAP-265 | Log a business-trip mileage and save it as a draft | unique | designed | Mileage · Toll and reimbursement options, Mileage · New mileage, Mileage · Calculated route, Mileage · Other details expanded … | - |
| CAP-266 | Plan a mileage route and calculate its distance | unique | designed | Mileage · New mileage, Mileage · Starting point, Mileage · Select on map, Mileage · Route overview … | - |
| CAP-267 | Calculate road tolls automatically for a mileage trip | unique | designed | Mileage · Toll and reimbursement options, Mileage · Other details expanded, Mileage · Fuel menu | - |
| CAP-268 | Remember my mileage defaults | unique | no-design |  | - |
| CAP-269 | Register or edit a travel allowance (per diem) | unique | designed | Allowance · Other countries, Allowance · Additional travel leg, Allowance · Travel details, Allowance · Multiple travel legs … | - |
| CAP-270 | Set meals and lodging per travel day and see the calculated allowance | unique | designed | Allowance · All days, Allowance · Single days, Allowance · Lodging menu, Allowance · Hotel details … | - |
| CAP-271 | Record hotel stays for an allowance and find the hotel | unique | designed | Allowance · Hotel details, Allowance · Hotel search recents, Allowance · Hotel search results, Allowance · Add or remove another hotel | - |
| CAP-272 | Read what allowances are and the company policy | unique | designed | Allowance · Information | - |
| CAP-273 | View my travel emissions summary | unique | no-design |  | - |
| CAP-274 | See the CO2e emissions of an expense or claim | unique | no-design |  | - |
| CAP-275 | Keep expenses in sync and upload offline drafts automatically | unique | no-design |  | - |

## Capabilities with no design

Each needs a decision in `fuse-review`: design it, carry it as it is, drop it, or defer it.

- **CAP-014** View details of a registered absence (me-ios, me-android)
- **CAP-015** Edit a registered absence (me-ios, me-android)
- **CAP-016** Delete a registered absence (me-ios, me-android)
- **CAP-018** Check in and check out for the workday (me-ios, me-android)
- **CAP-019** Edit or delete a check-in/check-out registration (me-ios, me-android)
- **CAP-021** Register time or absence by chatting with the Employee Agent (me-ios, me-android)
- **CAP-022** Confirm the time sheet through the Employee Agent (me-ios, me-android)
- **CAP-024** Edit a predicted registration before saving it (me-ios, me-android)
- **CAP-025** View, edit or delete an absence created in the agent chat (me-ios, me-android)
- **CAP-026** Learn how to use the Employee Agent and try example prompts (me-ios, me-android)
- **CAP-027** Send feedback about the Employee Agent (me-ios, me-android)
- **CAP-033** View a Business NXT order (vmm)
- **CAP-034** Edit a Business NXT order's references, delivery date and lines (vmm)
- **CAP-035** Create a sales or purchase order (vmm)
- **CAP-036** Send a purchase order to approval (vmm)
- **CAP-037** Cancel a purchase order (vmm)
- **CAP-038** Open an order attachment (vmm)
- **CAP-039** Track documents sent for approval (vmm)
- **CAP-040** Withdraw a pending approval task (vmm)
- **CAP-041** Browse and search archived invoices (vmm)
- **CAP-042** See money owed by customers or to suppliers (vmm)
- **CAP-043** Review an associate's open ledger entries (vmm)
- **CAP-044** View a customer or supplier card (vmm)
- **CAP-054** Browse the catalog of questions the assistant can answer (vmm)
- **CAP-056** Find and resume a past assistant conversation (vmm)
- **CAP-057** Rename, pin or delete an assistant conversation (vmm)
- **CAP-058** Resume the conversation an answer-ready notification announced (vmm)
- **CAP-059** Rate an assistant answer (vmm, me-ios, me-android)
- **CAP-060** Copy an assistant answer (me-ios, me-android)
- **CAP-061** Open a source cited in an assistant answer (vmm)
- **CAP-062** Approve or decline an action the assistant asks permission for (vmm)
- **CAP-063** Approve or reject an approval task from within the assistant chat (vmm)
- **CAP-064** Open an approval task linked in an assistant answer (vmm)
- **CAP-065** Let the assistant navigate the app (vmm)
- **CAP-075** Follow up on unread dialogues, absent colleagues and new hires from Home (vmm)
- **CAP-076** Review recent activity across approval, payments and dialogues (vmm)
- **CAP-083** Read important messages, surveys and app-update prompts on Home (me-android)
- **CAP-084** Start a common task from Home quick selections (me-android)
- **CAP-085** Reach HR profile, documents and benefits or the employee list from Home shortcuts (me-ios, me-android)
- **CAP-088** Open a specific app section from a link (me-android)
- **CAP-089** Acknowledge a blocking startup notice (me-android)
- **CAP-090** Go through first-run onboarding (me-android)
- **CAP-091** View a financial reporting dashboard for a company and period (vmm)
- **CAP-092** Choose the customer and tenant to report on (vmm)
- **CAP-093** Filter a dashboard chart by category and choose which series to show (vmm)
- **CAP-094** Examine a dashboard chart in detail (vmm)
- **CAP-099** Send feedback about Business NXT line editing (vmm)
- **CAP-100** Rate the app in the store (vmm, me-ios, me-android)
- **CAP-101** Answer an NPS satisfaction survey (vmm, me-android)
- **CAP-102** Decline the NPS survey or stop it from showing again (vmm)
- **CAP-103** Take or dismiss a survey from the home card (me-ios, me-android)
- **CAP-104** Volunteer for user testing (vmm)
- **CAP-105** Review and share failed request logs (vmm)
- **CAP-111** Turn vibration and the holiday theme on or off (vmm)
- **CAP-117** Allow or block screenshots of the app (me-android)
- **CAP-118** Update the app when a new version is suggested or required (vmm, me-ios, me-android)
- **CAP-119** Keep app state after restarting or updating the app (vmm)
- **CAP-122** See that an employee's birthday is coming up (vmm)
- **CAP-123** Turn birthday and work-anniversary reminders on or off (vmm)
- **CAP-125** Search the employee directory by name (vmm, me-ios, me-android)
- **CAP-126** Filter the employee directory with quick filters (vmm, me-ios, me-android)
- **CAP-127** Hide or show companies in the employee list (vmm)
- **CAP-129** View a colleague's Dottie profile (vmm, me-ios, me-android)
- **CAP-132** Edit an employee's name, phone numbers and emails (vmm)
- **CAP-135** Remove an employee's child (vmm)
- **CAP-137** Remove an employee's emergency contact (vmm)
- **CAP-138** Generate an AI birthday or work-anniversary greeting (vmm)
- **CAP-139** Send a greeting to the employee by share sheet or SMS (vmm)
- **CAP-140** Save a greeting for later (vmm)
- **CAP-141** View my personal information (me-ios, me-android)
- **CAP-142** Update my phone numbers and home address (me-ios, me-android)
- **CAP-143** Change my salary bank account number (me-ios, me-android)
- **CAP-144** Add an emergency contact or child (me-ios, me-android)
- **CAP-145** Edit an emergency contact or child (me-ios, me-android)
- **CAP-146** Remove an emergency contact or child (me-ios, me-android)
- **CAP-147** View and update my HR profile (me-ios, me-android)
- **CAP-148** Change or remove my profile picture (me-ios, me-android)
- **CAP-149** Pick and crop a profile picture (prototype) (vmm)
- **CAP-156** Complete a review of a task (vmm)
- **CAP-159** Act on an approval task from the Home screen (vmm)
- **CAP-161** Review an employee's pending approval tasks (vmm)
- **CAP-162** Open the requester's employee profile from a task (vmm)
- **CAP-169** Approve or reject individual accounting lines (vmm)
- **CAP-172** Apply one field value to all lines (vmm)
- **CAP-173** Discard unsaved line edits (vmm)
- **CAP-176** Receive push notifications on this device (vmm, me-ios, me-android)
- **CAP-177** Stop push notifications to this device when signing out (vmm, me-ios, me-android)
- **CAP-178** Open a push notification in the right place (me-ios, me-android)
- **CAP-179** See that new HR notifications are waiting (me-ios, me-android)
- **CAP-182** Mark an HR notification as read (me-ios, me-android)
- **CAP-183** Open a document notification and confirm it as read (me-android)
- **CAP-184** Read an important message from the employer or Visma (me-ios, me-android)
- **CAP-185** Open the app's notification settings (me-android)
- **CAP-190** Track the status of processed AutoPay payments (In progress / Deviation / In bank) (vmm)
- **CAP-191** View an AutoPay payment's details (vmm)
- **CAP-192** View the invoice document attached to an AutoPay payment (vmm)
- **CAP-193** Change the pay date of an AutoPay payment (vmm)
- **CAP-194** Add, edit or delete a note on an AutoPay payment (vmm)
- **CAP-195** Review and verify AutoPay payment warnings (vmm)
- **CAP-196** Cancel an AutoPay payment (vmm)
- **CAP-197** Sign in with a Visma Connect account (vmm, me-ios, me-android)
- **CAP-198** Stay signed in without logging in again (me-ios, me-android)
- **CAP-199** Be signed out and told why when the session ends (vmm, me-ios, me-android)
- **CAP-200** Handle an account with no access (vmm, me-ios, me-android)
- **CAP-202** Switch between saved accounts (me-ios, me-android)
- **CAP-203** Add another account (me-ios, me-android)
- **CAP-204** Remove a saved account from the device (me-ios, me-android)
- **CAP-207** Unlock the app with Face ID, fingerprint or PIN (me-ios, me-android)
- **CAP-209** Switch the backend environment (vmm, me-ios, me-android)
- **CAP-210** Choose a sandbox environment at login (vmm)
- **CAP-212** Preview a day timeline (prototype) (vmm)
- **CAP-213** Fill in and edit a server-defined form (me-ios)
- **CAP-215** Start a new payroll dialogue (vmm)
- **CAP-219** Edit a sent dialogue message (vmm)
- **CAP-220** Delete a dialogue message (vmm)
- **CAP-221** Rename a dialogue or change its linked wage run (vmm)
- **CAP-222** Mark a dialogue as completed or reactivate it (vmm)
- **CAP-223** Delete a dialogue (vmm)
- **CAP-232** Browse and search company documents (me-ios, me-android)
- **CAP-233** Open a company document (me-ios, me-android)
- **CAP-234** Confirm reading a required company document (me-ios, me-android)
- **CAP-235** View and open my personal documents (me-ios, me-android)
- **CAP-236** Browse employee benefits (me-ios, me-android)
- **CAP-237** Open and acknowledge a document from a notification (me-ios)
- **CAP-239** Open a downloaded file in another app (me-android)
- **CAP-243** Share a photo or PDF into the app to create an expense (me-android, me-ios)
- **CAP-244** Auto-fill a receipt from its image and get a suggested expense type (me-ios, me-android)
- **CAP-247** Calculate driving distance for a kilometre receipt (me-ios)
- **CAP-250** Link a credit card transaction to a receipt (merge) (me-ios, me-android)
- **CAP-251** Delete an unsent expense (me-ios, me-android)
- **CAP-260** Withdraw a claim from approval (me-ios, me-android)
- **CAP-264** Assign project accounting to an expense or claim (me-ios, me-android)
- **CAP-268** Remember my mileage defaults (me-ios, me-android)
- **CAP-273** View my travel emissions summary (me-ios, me-android)
- **CAP-274** See the CO2e emissions of an expense or claim (me-ios, me-android)
- **CAP-275** Keep expenses in sync and upload offline drafts automatically (me-ios, me-android)

## Design frames that match no legacy capability

New features, or a mapping the agents missed:

- `J4jjulaLJ4QNzqZ1INWydq:3550:12036` Approval / Fjordkraft AS / -
- `J4jjulaLJ4QNzqZ1INWydq:3550:12556` Approval / Statkraft Energi AS / INV-7781
- `J4jjulaLJ4QNzqZ1INWydq:3550:13266` Approval / Bring Logistikk AS / INV-3318
- `J4jjulaLJ4QNzqZ1INWydq:3550:13582` Approval / Vestland Tekstil AS / INV-1120
- `J4jjulaLJ4QNzqZ1INWydq:3561:11848` Update payment state / 01 of 14
- `J4jjulaLJ4QNzqZ1INWydq:3561:11851` Update payment state / 02 of 14
- `J4jjulaLJ4QNzqZ1INWydq:3561:11854` Update payment state / 03 of 14
- `J4jjulaLJ4QNzqZ1INWydq:3561:11857` Update payment state / 04 of 14
- `J4jjulaLJ4QNzqZ1INWydq:3561:11860` Update payment state / 05 of 14
- `J4jjulaLJ4QNzqZ1INWydq:3561:11863` Update payment state / 06 of 14
- `J4jjulaLJ4QNzqZ1INWydq:3561:11866` Update payment state / 07 of 14
- `J4jjulaLJ4QNzqZ1INWydq:3561:11869` Update payment state / 08 of 14
- `J4jjulaLJ4QNzqZ1INWydq:3561:11872` Update payment state / 09 of 14
- `J4jjulaLJ4QNzqZ1INWydq:3561:11875` Update payment state / 10 of 14
- `J4jjulaLJ4QNzqZ1INWydq:3561:11878` Update payment state / 11 of 14
- `J4jjulaLJ4QNzqZ1INWydq:3561:11881` Update payment state / 12 of 14
- `J4jjulaLJ4QNzqZ1INWydq:3561:11884` Update payment state / 13 of 14
- `J4jjulaLJ4QNzqZ1INWydq:3561:11887` Update payment state / 14 of 14
