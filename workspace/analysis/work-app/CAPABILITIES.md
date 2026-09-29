# Capabilities: work-app

273 capabilities across 3 apps (vmm = Manager, me-ios = Employee, me-android = Employee), generated 2026-09-29T13:51:31+00:00. Each capability is one thing a person can do. Its fusion class says what the new app must do with it:

- **unique**: one product has it. Carry it over, or a person drops it.
- **shared-same**: both products do it the same way. Build it once.
- **shared-diverged**: both do it differently. A person decides which behavior survives (`fuse-review`).
- **new**: only the design has it. It needs a spec before it can be built.

| Fusion class | Capabilities |
| --- | --- |
| unique | 228 |
| shared-diverged | 45 |

## Matrix

| Id | Capability | Domain | Fusion | vmm | me-ios | me-android | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CAP-001 | View a calendar month by month | Time and absence | shared-diverged | yes | yes | yes | High |
| CAP-002 | Browse the calendar as a scrolling list | Time and absence | shared-diverged | yes | yes | yes | High |
| CAP-003 | Switch between list and month view of the calendar | Time and absence | shared-diverged | yes | yes | yes | High |
| CAP-004 | See the details of a calendar day | Time and absence | shared-diverged | yes | yes | yes | High |
| CAP-005 | Customize what the calendar shows | Time and absence | shared-diverged | yes | yes | yes | High |
| CAP-006 | Start a time or absence registration from the calendar | Time and absence | unique |  | yes | yes | High |
| CAP-008 | See what needs attention across modules on Home | Home and navigation | unique | yes |  |  | High |
| CAP-009 | View an employee's absence balances | Time and absence | unique | yes |  |  | High |
| CAP-010 | See my time and absence balances for a month | Time and absence | unique |  | yes | yes | Medium |
| CAP-011 | See my vacation balances on the start page | Home and navigation | unique |  | yes | yes | High |
| CAP-012 | Register an absence or time event | Time and absence | unique |  | yes | yes | High |
| CAP-013 | Pick cost-unit dimension values for a registration | Time and absence | unique |  | yes | yes | High |
| CAP-014 | View details of a registered absence | Time and absence | unique |  | yes | yes | High |
| CAP-015 | Edit a registered absence | Time and absence | unique |  | yes | yes | High |
| CAP-016 | Delete a registered absence | Time and absence | unique |  | yes | yes | High |
| CAP-017 | See upcoming and ongoing vacation and parental leave on the start page | Home and navigation | unique |  | yes | yes | High |
| CAP-018 | Check in and check out for the workday | Time and absence | unique |  | yes | yes | High |
| CAP-019 | Edit or delete a check-in/check-out registration | Time and absence | unique |  | yes | yes | High |
| CAP-020 | Confirm worked time up to a date | Time and absence | unique |  | yes | yes | High |
| CAP-021 | Register time or absence by chatting with the Employee Agent | Time and absence | unique |  | yes | yes | High |
| CAP-022 | Confirm the time sheet through the Employee Agent | Time and absence | unique |  | yes | yes | High |
| CAP-023 | Ask the Employee Agent about leave balances | Time and absence | unique |  | yes |  | High |
| CAP-024 | Edit a predicted registration before saving it | Time and absence | unique |  | yes | yes | High |
| CAP-025 | View, edit or delete an absence created in the agent chat | Time and absence | unique |  | yes | yes | High |
| CAP-026 | Learn how to use the Employee Agent and try example prompts | Time and absence | unique |  | yes | yes | High |
| CAP-027 | Send feedback about the Employee Agent | Time and absence | unique |  | yes | yes | High |
| CAP-028 | Browse my expense claims by year and filter by status | Expenses | unique |  | yes | yes | High |
| CAP-029 | Browse my payslips by payment date, filtered by employer | Pay and payroll | unique |  | yes | yes | High |
| CAP-030 | Switch the active Business NXT company | Business NXT | unique | yes |  |  | High |
| CAP-031 | Open a Business NXT work area | Business NXT | unique | yes |  |  | High |
| CAP-032 | Browse Business NXT orders | Business NXT | unique | yes |  |  | High |
| CAP-033 | View a Business NXT order | Business NXT | unique | yes |  |  | High |
| CAP-034 | Edit a Business NXT order's references, delivery date and lines | Business NXT | unique | yes |  |  | High |
| CAP-035 | Create a sales or purchase order | Business NXT | unique | yes |  |  | High |
| CAP-036 | Send a purchase order to approval | Business NXT | unique | yes |  |  | High |
| CAP-037 | Cancel a purchase order | Business NXT | unique | yes |  |  | High |
| CAP-038 | Open an order attachment | Business NXT | unique | yes |  |  | High |
| CAP-039 | Track documents sent for approval | Business NXT | unique | yes |  |  | High |
| CAP-040 | Withdraw a pending approval task | Business NXT | unique | yes |  |  | High |
| CAP-041 | Browse and search archived invoices | Business NXT | unique | yes |  |  | High |
| CAP-042 | See money owed by customers or to suppliers | Business NXT | unique | yes |  |  | High |
| CAP-043 | Review an associate's open ledger entries | Business NXT | unique | yes |  |  | High |
| CAP-044 | View a customer or supplier card | Business NXT | unique | yes |  |  | High |
| CAP-045 | Look up products, customers, suppliers and stock | Business NXT | unique | yes |  |  | High |
| CAP-046 | Check a product's stock | Business NXT | unique | yes |  |  | High |
| CAP-047 | Ask the AI assistant a question | AI assistant | shared-diverged | yes | yes | yes | Medium |
| CAP-048 | Open the assistant for the current screen from the header | AI assistant | shared-diverged | yes |  |  | High |
| CAP-049 | Ask the assistant about an approval task or past approval | AI assistant | unique | yes |  |  | High |
| CAP-050 | Ask the assistant about an employee | AI assistant | unique | yes |  |  | High |
| CAP-051 | Ask the assistant from Home, Home search or a list's search band | AI assistant | unique | yes |  |  | High |
| CAP-052 | Ask the payslip assistant about a payslip or year-end report | AI assistant | unique |  | yes | yes | High |
| CAP-053 | Start from a suggested question | AI assistant | shared-diverged | yes | yes | yes | Medium |
| CAP-054 | Browse the catalog of questions the assistant can answer | AI assistant | shared-diverged | yes |  |  | High |
| CAP-055 | Start a new assistant conversation | AI assistant | unique | yes |  |  | High |
| CAP-056 | Find and resume a past assistant conversation | AI assistant | unique | yes |  |  | High |
| CAP-057 | Rename, pin or delete an assistant conversation | AI assistant | unique | yes |  |  | High |
| CAP-058 | Resume the conversation an answer-ready notification announced | AI assistant | unique | yes |  |  | High |
| CAP-059 | Rate an assistant answer | AI assistant | shared-diverged | yes | yes | yes | High |
| CAP-060 | Copy an assistant answer | AI assistant | unique |  | yes | yes | High |
| CAP-061 | Open a source cited in an assistant answer | AI assistant | unique | yes |  |  | High |
| CAP-062 | Approve or decline an action the assistant asks permission for | AI assistant | unique | yes |  |  | High |
| CAP-063 | Approve or reject an approval task from within the assistant chat | AI assistant | unique | yes |  |  | High |
| CAP-064 | Open an approval task linked in an assistant answer | AI assistant | unique | yes |  |  | High |
| CAP-065 | Let the assistant navigate the app | AI assistant | unique | yes |  |  | High |
| CAP-066 | Dictate a message to the assistant by voice | AI assistant | shared-diverged | yes | yes | yes | Medium |
| CAP-067 | Switch between the app's main areas | Home and navigation | shared-diverged | yes | yes | yes | High |
| CAP-068 | Open any integration from the More sheet | Home and navigation | unique | yes |  |  | High |
| CAP-069 | Customize which areas are pinned to the tab bar | Home and navigation | unique | yes |  |  | High |
| CAP-070 | Search and sort a work list | Home and navigation | unique | yes |  |  | Medium |
| CAP-071 | Search across approvals, invoices, employees and orders | Home and navigation | unique | yes |  |  | High |
| CAP-073 | Open a pending approval task from Home | Home and navigation | unique | yes |  |  | High |
| CAP-074 | Open an upcoming Autopay payment from Home | Home and navigation | unique | yes |  |  | High |
| CAP-075 | Follow up on unread dialogues, absent colleagues and new hires from Home | Home and navigation | unique | yes |  |  | High |
| CAP-076 | Review recent activity across approval, payments and dialogues | Home and navigation | unique | yes |  |  | High |
| CAP-077 | Jump into a licensed module from Home | Home and navigation | unique | yes |  |  | High |
| CAP-078 | Discover and act on What's New announcements | Home and navigation | shared-diverged | yes | yes | yes | High |
| CAP-079 | See personal highlights on the start page | Home and navigation | unique |  | yes | yes | High |
| CAP-080 | Open the latest or upcoming payslip from the start page | Home and navigation | unique |  | yes | yes | High |
| CAP-081 | Track the status of submitted expense claims from the start page | Home and navigation | unique |  | yes | yes | High |
| CAP-082 | Resume unsent expense drafts from the start page | Home and navigation | unique |  | yes | yes | High |
| CAP-083 | Read important messages, surveys and app-update prompts on Home | Home and navigation | unique |  |  | yes | Medium |
| CAP-084 | Start a common task from Home quick selections | Home and navigation | unique |  |  | yes | High |
| CAP-085 | Reach HR profile, documents and benefits or the employee list from Home shortcuts | Home and navigation | unique |  | yes | yes | High |
| CAP-086 | Open my user menu to reach profile, account and HR pages | Home and navigation | unique |  | yes | yes | High |
| CAP-087 | Sign out from the user menu | Home and navigation | shared-diverged |  | yes | yes | Medium |
| CAP-088 | Open a specific app section from a link | Home and navigation | unique |  |  | yes | High |
| CAP-089 | Acknowledge a blocking startup notice | Home and navigation | unique |  |  | yes | Medium |
| CAP-090 | Go through first-run onboarding | Home and navigation | unique |  |  | yes | Medium |
| CAP-091 | View a financial reporting dashboard for a company and period | Financial reporting | unique | yes |  |  | High |
| CAP-092 | Choose the customer and tenant to report on | Financial reporting | unique | yes |  |  | High |
| CAP-093 | Filter a dashboard chart by category and choose which series to show | Financial reporting | unique | yes |  |  | High |
| CAP-094 | Examine a dashboard chart in detail | Financial reporting | unique | yes |  |  | High |
| CAP-095 | Read how-to help for the current screen | Help and feedback | unique | yes |  |  | High |
| CAP-096 | Browse help (FAQ) by topic | Help and feedback | unique |  | yes | yes | High |
| CAP-097 | Check why a module is not available for my company | Help and feedback | unique |  | yes | yes | Medium |
| CAP-098 | Send feedback about the app | Help and feedback | shared-diverged | yes | yes | yes | High |
| CAP-099 | Send feedback about Business NXT line editing | Help and feedback | unique | yes |  |  | High |
| CAP-100 | Rate the app in the store | Help and feedback | shared-diverged | yes | yes | yes | High |
| CAP-101 | Answer an NPS satisfaction survey | Help and feedback | shared-diverged | yes |  | yes | Medium |
| CAP-102 | Decline the NPS survey or stop it from showing again | Help and feedback | unique | yes |  |  | High |
| CAP-103 | Take or dismiss a survey from the home card | Help and feedback | unique |  | yes | yes | High |
| CAP-104 | Volunteer for user testing | Help and feedback | unique | yes |  |  | High |
| CAP-105 | Review and share failed request logs | Help and feedback | unique | yes |  |  | High |
| CAP-106 | Copy account and device details for support | Help and feedback | unique |  | yes |  | High |
| CAP-107 | Read open-source licenses and the accessibility statement | Help and feedback | shared-diverged |  | yes | yes | Medium |
| CAP-108 | Open app settings | Settings and legal | shared-diverged | yes |  |  | High |
| CAP-109 | Choose the app language | Settings and legal | shared-diverged | yes | yes | yes | High |
| CAP-110 | Choose light, dark or system appearance | Settings and legal | shared-diverged | yes | yes | yes | High |
| CAP-111 | Turn vibration and the holiday theme on or off | Settings and legal | unique | yes |  |  | High |
| CAP-112 | Control anonymous analytics collection | Settings and legal | unique | yes |  |  | High |
| CAP-113 | Read the accessibility statement | Settings and legal | shared-diverged | yes | yes | yes | High |
| CAP-114 | Read the terms of service and privacy information | Settings and legal | shared-diverged | yes | yes | yes | Medium |
| CAP-115 | View app version and open-source licenses | Settings and legal | shared-diverged | yes | yes | yes | High |
| CAP-116 | See the signed-in account and device info in Settings | Settings and legal | unique |  |  | yes | High |
| CAP-117 | Allow or block screenshots of the app | Settings and legal | unique |  |  | yes | High |
| CAP-118 | Update the app when a new version is suggested or required | Settings and legal | shared-diverged | yes | yes | yes | Medium |
| CAP-119 | Keep app state after restarting or updating the app | Settings and legal | shared-diverged | yes |  |  | Medium |
| CAP-120 | Use internal developer tools and feature flags | Settings and legal | shared-diverged | yes | yes |  | Medium |
| CAP-121 | Switch backend environment in test builds | Settings and legal | shared-diverged |  |  | yes | High |
| CAP-122 | See that an employee's birthday is coming up | People and HR | unique | yes |  |  | High |
| CAP-123 | Turn birthday and work-anniversary reminders on or off | People and HR | unique | yes |  |  | High |
| CAP-124 | Browse the employee directory | People and HR | shared-diverged | yes | yes | yes | Medium |
| CAP-125 | Search the employee directory by name | People and HR | shared-diverged | yes | yes | yes | High |
| CAP-126 | Filter the employee directory with quick filters | People and HR | shared-diverged | yes | yes | yes | High |
| CAP-127 | Hide or show companies in the employee list | People and HR | unique | yes |  |  | High |
| CAP-128 | View an employee's personal, address and employment details | People and HR | unique | yes |  |  | High |
| CAP-129 | View a colleague's Dottie profile | People and HR | shared-diverged | yes | yes | yes | High |
| CAP-130 | Contact an employee by call, SMS, email or share | People and HR | unique | yes |  |  | High |
| CAP-131 | Copy an employee's post address | People and HR | unique | yes |  |  | High |
| CAP-132 | Edit an employee's name, phone numbers and emails | People and HR | unique | yes |  |  | High |
| CAP-133 | Edit an employee's postal address | People and HR | unique | yes |  |  | High |
| CAP-134 | Add or edit an employee's child | People and HR | unique | yes |  |  | High |
| CAP-135 | Remove an employee's child | People and HR | unique | yes |  |  | High |
| CAP-136 | Add or edit an employee's emergency contact | People and HR | unique | yes |  |  | High |
| CAP-137 | Remove an employee's emergency contact | People and HR | unique | yes |  |  | High |
| CAP-138 | Generate an AI birthday or work-anniversary greeting | People and HR | unique | yes |  |  | High |
| CAP-139 | Send a greeting to the employee by share sheet or SMS | People and HR | unique | yes |  |  | High |
| CAP-140 | Save a greeting for later | People and HR | unique | yes |  |  | High |
| CAP-141 | View my personal information | People and HR | unique |  | yes | yes | High |
| CAP-142 | Update my phone numbers and home address | People and HR | unique |  | yes | yes | High |
| CAP-143 | Change my salary bank account number | People and HR | unique |  | yes | yes | High |
| CAP-144 | Add an emergency contact or child | People and HR | shared-diverged |  | yes | yes | High |
| CAP-145 | Edit an emergency contact or child | People and HR | shared-diverged |  | yes | yes | High |
| CAP-146 | Remove an emergency contact or child | People and HR | shared-diverged |  | yes | yes | High |
| CAP-147 | View and update my HR profile | People and HR | unique |  | yes | yes | High |
| CAP-148 | Change or remove my profile picture | People and HR | unique |  | yes | yes | High |
| CAP-149 | Pick and crop a profile picture (prototype) | People and HR | unique | yes |  |  | Low |
| CAP-150 | See my pending approval tasks | Approvals | unique | yes |  |  | High |
| CAP-151 | Sort approval tasks | Approvals | unique | yes |  |  | High |
| CAP-152 | Search approval tasks and history | Approvals | unique | yes |  |  | High |
| CAP-153 | Review an approval task | Approvals | unique | yes |  |  | High |
| CAP-154 | Approve an approval task | Approvals | unique | yes |  |  | High |
| CAP-155 | Reject an approval task | Approvals | unique | yes |  |  | High |
| CAP-156 | Complete a review of a task | Approvals | unique | yes |  |  | High |
| CAP-157 | Send a task for review to a colleague | Approvals | unique | yes |  |  | High |
| CAP-158 | Forward a task to another approver | Approvals | unique | yes |  |  | High |
| CAP-159 | Act on an approval task from the Home screen | Approvals | unique | yes |  |  | High |
| CAP-160 | Approve several tasks at once | Approvals | unique | yes |  |  | High |
| CAP-161 | Review an employee's pending approval tasks | Approvals | unique | yes |  |  | High |
| CAP-162 | Open the requester's employee profile from a task | Approvals | unique | yes |  |  | High |
| CAP-163 | Comment on an approval process | Approvals | unique | yes |  |  | High |
| CAP-164 | View a task's attached documents | Approvals | unique | yes |  |  | High |
| CAP-165 | Share or download a task document | Approvals | unique | yes |  |  | High |
| CAP-166 | Browse my approval history | Approvals | unique | yes |  |  | High |
| CAP-167 | View a handled approval process | Approvals | unique | yes |  |  | High |
| CAP-168 | See a task's approval workflow and history | Approvals | unique | yes |  |  | High |
| CAP-169 | Approve or reject individual accounting lines | Approvals | unique | yes |  |  | High |
| CAP-170 | Open a task's accounting lines | Approvals | unique | yes |  |  | High |
| CAP-171 | Edit the accounting lines of an invoice before approving | Approvals | unique | yes |  |  | High |
| CAP-172 | Apply one field value to all lines | Approvals | unique | yes |  |  | High |
| CAP-173 | Discard unsaved line edits | Approvals | unique | yes |  |  | High |
| CAP-174 | Choose which line fields to show | Approvals | unique | yes |  |  | High |
| CAP-175 | Jump to a specific invoice line | Approvals | unique | yes |  |  | High |
| CAP-176 | Receive push notifications on this device | Notifications and inbox | shared-diverged | yes | yes | yes | Medium |
| CAP-177 | Stop push notifications to this device when signing out | Notifications and inbox | shared-diverged | yes | yes | yes | Medium |
| CAP-178 | Open a push notification in the right place | Notifications and inbox | shared-diverged |  | yes | yes | High |
| CAP-179 | See that new HR notifications are waiting | Notifications and inbox | unique |  | yes | yes | High |
| CAP-180 | Read the combined message inbox | Notifications and inbox | unique |  | yes | yes | High |
| CAP-181 | Dismiss a message from the inbox | Notifications and inbox | unique |  | yes | yes | High |
| CAP-182 | Mark an HR notification as read | Notifications and inbox | unique |  | yes | yes | High |
| CAP-183 | Open a document notification and confirm it as read | Notifications and inbox | unique |  |  | yes | Medium |
| CAP-184 | Read an important message from the employer or Visma | Notifications and inbox | unique |  | yes | yes | High |
| CAP-185 | Open the app's notification settings | Notifications and inbox | unique |  |  | yes | Medium |
| CAP-186 | Review AutoPay payments waiting for my approval | Payments | unique | yes |  |  | High |
| CAP-187 | Search AutoPay payments | Payments | unique | yes |  |  | High |
| CAP-188 | Select AutoPay payments for approval | Payments | unique | yes |  |  | High |
| CAP-189 | Approve selected AutoPay payments with bank two-factor signing (BankID) | Payments | unique | yes |  |  | High |
| CAP-190 | Track the status of processed AutoPay payments (In progress / Deviation / In bank) | Payments | unique | yes |  |  | High |
| CAP-191 | View an AutoPay payment's details | Payments | unique | yes |  |  | High |
| CAP-192 | View the invoice document attached to an AutoPay payment | Payments | unique | yes |  |  | High |
| CAP-193 | Change the pay date of an AutoPay payment | Payments | unique | yes |  |  | High |
| CAP-194 | Add, edit or delete a note on an AutoPay payment | Payments | unique | yes |  |  | High |
| CAP-195 | Review and verify AutoPay payment warnings | Payments | unique | yes |  |  | High |
| CAP-196 | Cancel an AutoPay payment | Payments | unique | yes |  |  | High |
| CAP-197 | Sign in with a Visma Connect account | Sign-in and accounts | shared-diverged | yes | yes | yes | High |
| CAP-198 | Stay signed in without logging in again | Sign-in and accounts | shared-diverged |  | yes | yes | High |
| CAP-199 | Be signed out and told why when the session ends | Sign-in and accounts | shared-diverged | yes | yes | yes | Medium |
| CAP-200 | Handle an account with no access | Sign-in and accounts | shared-diverged | yes | yes | yes | Medium |
| CAP-201 | Log out | Sign-in and accounts | shared-diverged | yes | yes | yes | High |
| CAP-202 | Switch between saved accounts | Sign-in and accounts | unique |  | yes | yes | High |
| CAP-203 | Add another account | Sign-in and accounts | unique |  | yes | yes | High |
| CAP-204 | Remove a saved account from the device | Sign-in and accounts | unique |  | yes | yes | High |
| CAP-205 | Switch between my employers | Sign-in and accounts | unique |  | yes | yes | High |
| CAP-206 | Protect the app with Face ID, fingerprint or PIN | Sign-in and accounts | unique |  | yes | yes | High |
| CAP-207 | Unlock the app with Face ID, fingerprint or PIN | Sign-in and accounts | unique |  | yes | yes | High |
| CAP-208 | Turn off the app lock | Sign-in and accounts | unique |  | yes | yes | High |
| CAP-209 | Switch the backend environment | Sign-in and accounts | shared-diverged | yes | yes | yes | Medium |
| CAP-210 | Choose a sandbox environment at login | Sign-in and accounts | unique | yes |  |  | High |
| CAP-211 | See my vacation balances on the start page | Time and absence | unique |  | yes |  | Medium |
| CAP-212 | Preview a day timeline (prototype) | Time and absence | unique | yes |  |  | Low |
| CAP-213 | Fill in and edit a server-defined form | Time and absence | unique |  | yes |  | Low |
| CAP-214 | Browse payroll dialogues | Pay and payroll | unique | yes |  |  | High |
| CAP-215 | Start a new payroll dialogue | Pay and payroll | unique | yes |  |  | High |
| CAP-216 | Read a payroll dialogue conversation | Pay and payroll | unique | yes |  |  | High |
| CAP-217 | Browse wage-run splits of a dialogue | Pay and payroll | unique | yes |  |  | High |
| CAP-218 | Send a message in a payroll dialogue | Pay and payroll | unique | yes |  |  | High |
| CAP-219 | Edit a sent dialogue message | Pay and payroll | unique | yes |  |  | High |
| CAP-220 | Delete a dialogue message | Pay and payroll | unique | yes |  |  | High |
| CAP-221 | Rename a dialogue or change its linked wage run | Pay and payroll | unique | yes |  |  | High |
| CAP-222 | Mark a dialogue as completed or reactivate it | Pay and payroll | unique | yes |  |  | High |
| CAP-223 | Delete a dialogue | Pay and payroll | unique | yes |  |  | High |
| CAP-224 | Approve or reject a wage run | Pay and payroll | unique | yes |  |  | High |
| CAP-225 | View a payslip's details | Pay and payroll | unique |  | yes | yes | High |
| CAP-226 | Download a payslip PDF | Pay and payroll | unique |  | yes | yes | High |
| CAP-227 | Export all my payslips to one PDF | Pay and payroll | unique |  | yes | yes | High |
| CAP-228 | Browse my year-end reports | Pay and payroll | unique |  | yes | yes | High |
| CAP-229 | View a year-end report | Pay and payroll | unique |  | yes | yes | High |
| CAP-230 | Download a year-end report PDF | Pay and payroll | unique |  | yes | yes | High |
| CAP-231 | Learn why I have no payslips | Pay and payroll | unique |  | yes | yes | High |
| CAP-232 | Browse and search company documents | Documents and benefits | unique |  | yes | yes | High |
| CAP-233 | Open a company document | Documents and benefits | unique |  | yes | yes | High |
| CAP-234 | Confirm reading a required company document | Documents and benefits | unique |  | yes | yes | High |
| CAP-235 | View and open my personal documents | Documents and benefits | unique |  | yes | yes | High |
| CAP-236 | Browse employee benefits | Documents and benefits | unique |  | yes | yes | High |
| CAP-237 | Open and acknowledge a document from a notification | Documents and benefits | unique |  | yes |  | High |
| CAP-238 | Preview a downloaded image or PDF inside the app | Documents and benefits | shared-diverged |  | yes | yes | Medium |
| CAP-239 | Open a downloaded file in another app | Documents and benefits | unique |  |  | yes | Medium |
| CAP-240 | Browse my unsent expenses in the expenses inbox | Expenses | unique |  | yes | yes | High |
| CAP-241 | Start a new receipt, mileage or allowance | Expenses | unique |  | yes | yes | High |
| CAP-242 | Capture or import a receipt image or PDF | Expenses | unique |  | yes | yes | High |
| CAP-243 | Share a photo or PDF into the app to create an expense | Expenses | unique |  | yes | yes | Medium |
| CAP-244 | Auto-fill a receipt from its image and get a suggested expense type | Expenses | unique |  | yes | yes | High |
| CAP-245 | Create or edit a receipt | Expenses | unique |  | yes | yes | High |
| CAP-246 | Enter a receipt in a foreign currency with an exchange rate | Expenses | unique |  | yes | yes | High |
| CAP-247 | Calculate driving distance for a kilometre receipt | Expenses | unique |  | yes |  | High |
| CAP-248 | Add or remove attachments on an expense | Expenses | unique |  | yes | yes | High |
| CAP-249 | View or download an expense attachment | Expenses | unique |  | yes | yes | High |
| CAP-250 | Link a credit card transaction to a receipt (merge) | Expenses | unique |  | yes | yes | High |
| CAP-251 | Delete an unsent expense | Expenses | unique |  | yes | yes | High |
| CAP-252 | Send selected expenses to a claim | Expenses | unique |  | yes | yes | High |
| CAP-253 | Create a new expense claim from selected expenses | Expenses | unique |  | yes | yes | High |
| CAP-254 | Send an expense claim for approval | Expenses | unique |  | yes | yes | High |
| CAP-255 | Add new or existing expenses to a claim from the claim screen | Expenses | unique |  | yes | yes | High |
| CAP-256 | Add a receipt, mileage or allowance to a claim from its form | Expenses | unique |  | yes | yes | High |
| CAP-257 | Send a single expense straight for approval | Expenses | unique |  | yes | yes | High |
| CAP-258 | Review an expense claim's details | Expenses | unique |  | yes | yes | High |
| CAP-259 | Edit a claim's title and comment | Expenses | unique |  | yes | yes | High |
| CAP-260 | Withdraw a claim from approval | Expenses | unique |  | yes | yes | High |
| CAP-261 | Delete an expense claim | Expenses | unique |  | yes | yes | High |
| CAP-262 | View, edit or delete an item inside a claim | Expenses | unique |  | yes | yes | High |
| CAP-263 | Assign cost units to an expense or claim | Expenses | unique |  | yes | yes | High |
| CAP-264 | Assign project accounting to an expense or claim | Expenses | unique |  | yes | yes | High |
| CAP-265 | Log a business-trip mileage and save it as a draft | Expenses | unique |  | yes | yes | High |
| CAP-266 | Plan a mileage route and calculate its distance | Expenses | unique |  | yes | yes | High |
| CAP-267 | Calculate road tolls automatically for a mileage trip | Expenses | unique |  | yes | yes | High |
| CAP-268 | Remember my mileage defaults | Expenses | unique |  | yes | yes | High |
| CAP-269 | Register or edit a travel allowance (per diem) | Expenses | unique |  | yes | yes | High |
| CAP-270 | Set meals and lodging per travel day and see the calculated allowance | Expenses | unique |  | yes | yes | High |
| CAP-271 | Record hotel stays for an allowance and find the hotel | Expenses | unique |  | yes | yes | High |
| CAP-272 | Read what allowances are and the company policy | Expenses | unique |  | yes | yes | High |
| CAP-273 | View my travel emissions summary | Expenses | unique |  | yes | yes | High |
| CAP-274 | See the CO2e emissions of an expense or claim | Expenses | unique |  | yes | yes | Medium |
| CAP-275 | Keep expenses in sync and upload offline drafts automatically | Expenses | unique |  | yes | yes | High |

## Approvals

Handling approval tasks for invoices, expenses and other documents: inbox, review, approve, reject, forward, bulk actions, voucher and invoice line coding, documents, workflow and history

### CAP-150: See my pending approval tasks

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

A manager opens the Approval tab and sees their inbox of open approval tasks (invoices, expenses, other) with amounts, due/overdue badges and optional company grouping with collapsible groups. They pull to refresh, the app icon badge shows the pending count, and they open a task.

- **vmm** (Manager): screens: `ApprovalScreen (Tasks tab / TabPresent)`, `ApprovalTaskScreen`, `HRM > ApprovalTaskScreen (employee approval tasks)`; endpoints: `GET approval/rest/my-tasks`, `GET approval/task?taskId={taskId}&skipFinancials=true`; events: `approval_task_count`, `approval_overdue_task_count`, `clicked_on_approval_task_item`, `load_status_changed`, `pull_to_refresh_triggered`, `triggered_multiselect_reset`; storage: `hrmDialogueCollapsedGroups.approvalTasks (persisted, encrypted MMKV)`, `settings.approvalSortOrder (persisted)`, `redux approval.activeTab`, `redux approvalMultiSelect.selected`; platform: `app icon badge count (setBadgeCount)`, `Firebase Remote Config (user testing phase)`, `Android hardware back handler`, `Survicate survey after closing a task` · evidence `src/components/approval/ApprovalList/ApprovalList.tsx:47-150; src/screens/manager/ApprovalScreen/components/TabPresent/…`

_Note: Overdue computed against task dueDate when sorting by task due, else documentDueDate (ApprovalListItem.tsx:213-214); only company sort renders collapsible headers; employee-approval tasks navigate into the HRM tab (ApprovalListItem.tsx:194-204). First mount forces refetch then 60s RTK cache; Christmas theme when list empty. referee could not confirm: The endpoint URLs are not in the cited src/ser…_

### CAP-151: Sort approval tasks

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

A manager orders the task list by company, document due date or task due date; the choice is remembered.

- **vmm** (Manager): screens: `ApprovalScreen (Tasks tab)`; events: `sort_applied`; storage: `settings.approvalSortOrder (persisted)` · evidence `src/components/approval/ApprovalSortSection/ApprovalSortSection.tsx:26-60`

**How they differ:**
- Clarification, not a fusion difference: 'company' groups tasks into collapsible sections by company name (approvalSelectors.ts:194-200, ApprovalList.tsx:63) rather than giving a flat list. When company is chosen, the header label is hidden (ApprovalSortSection.tsx:57).
- The default order is taskDue (settingsReducer.ts:109). Tasks without a date sort last (approvalSelectors.ts:121-128).
- The chosen sort also decides which overdue indicator a task shows, task due date or document due date (ApprovalListItem.tsx:131,214).

_Note: Values company / documentDueDate / taskDue; applying scrolls to top. referee could not confirm: The cited range src/components/approval/ApprovalSortSection/ApprovalSortSection.tsx:26-60 is off slightly; the component spans lines 27-62._

### CAP-152: Search approval tasks and history

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

A manager searches pending tasks or history by free text (or asks Gaia), reuses recent searches, or swipes a history row to search everything from the same requester.

- **vmm** (Manager): screens: `ApprovalScreen (Tasks and History tabs)`; endpoints: `GET approval/rest/my-history?page={page}&text={searchInputText}`; events: `approval_used_search`, `search_completed`; storage: `approvalRecentSearches.recentSearches (persisted)`, `approval.searchInputText`, `approval.showSearchBar` · evidence `src/components/approval/ApprovalSearchBar/ApprovalSearchBar.tsx:17-40; src/screens/manager/ApprovalScreen/components/Ta…`

_Note: Recent search added on end-editing; history swipe pre-fills requesterName (ProcessListSwipeItem.tsx:22-25); swipe buttons hidden with screen reader; search analytics debounced 600ms. referee could not confirm: The History tab search is cited under TabPresent.tsx:49-284, but TabPresent only renders the Tasks tab search. The history search field and gaia_approval_history_search_placeholder are in s…_

### CAP-153: Review an approval task

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

A manager opens one pending task to see its document, company, amount or hours/days, due dates, workflow and Gaia hints, and acts on it from the task actions.

- **vmm** (Manager): screens: `ApprovalTaskScreen`, `ApprovalTaskNoContent`, `ApprovalTaskHeaderRight`; endpoints: `GET /approval/task?taskId={taskId}&skipFinancials=true`, `GET /approval/rest/my-tasks`, `GET /approval/rest/tasks/{taskId}/progress-details`; events: `task_load_change`, `task_load_details`, `task_details_load_status_changed`, `task_workflow_details_load_status_changed`, `approval_task_details_opened_info_modal`, `clicked_back_button`; storage: `redux approval.currentTaskId`, `redux approval.closedListItemTaskId`, `redux approval.taskWasHandled`, `redux documentView.fullscreen`; platform: `Android hardware back / beforeRemove handling for fullscreen document`, `orientation (landscape layout)` · evidence `src/screens/manager/ApprovalTaskScreen/ApprovalTaskScreen.tsx:69-466`

_Note: Timesheet/leave tasks show hours or days; a task handled elsewhere shows 'task was handled'; closing emits APPROVAL_TASK_CLOSE_EVENT. Action endpoints listed here are covered by the approve/reject/forward/review capabilities._

### CAP-154: Approve an approval task

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

A manager approves a task with an optional comment (up to 400 characters, saved as a draft) in the action drawer, from the task detail, by swiping a list row (quick approve), or directly from the document viewer.

- **vmm** (Manager): screens: `ApprovalTaskScreen`, `ApprovalScreen (swipe right)`, `Document viewer`, `TaskActionsDrawer`, `TaskActionsDrawerHeader`, `TaskActionsDrawerComment`, `TaskActionsDrawerBottom`, `ApprovalTaskActionsDrawer`; endpoints: `POST approval/rest/tasks/{taskId}/approve`, `GET approval/task?taskId={taskId}&skipFinancials=true`; events: `clicked_on_main_action_button`, `clicked_on_close_task_from_action_drawer`, `task_action_completed`, `task_close_complete`, `task_close_complete_with_comment`, `swipe_quick_approve_completed`, `doc_view_direct_approve_pressed`, `doc_view_direct_approve_completed` …; storage: `approval.draftComments (persisted)`, `approval.closeTask.comment`; platform: `haptics not used here`, `DeviceEventEmitter APPROVAL_TASK_CLOSE_EVENT resets stack` · evidence `src/components/approval/ApprovalTaskActionsDrawer/ApprovalTaskActionsDrawer.tsx:155-240; src/components/common/TaskActi…`

**How they differ:**
- Missing from the claim: if the new endpoint fails, or the task has no uid/displayId, vmm falls back to the old POST {base}ApprovalAction with {taskId, isAccepted, processId, comments} (apiApproval.ts:84-91, 176-187). This second endpoint should be in the evidence.
- Missing from the claim: the approve endpoint path uses taskUid (uid, or displayId if there is no uid), not taskId (apiApproval.ts:74-75, 582). The endpoint should be written as POST approval/rest/tasks/{taskUid}/approve.

_Note: Comment optional, omitted when empty, debounced 500 ms into the draft; if voucher lines unhandled and review not allowed, main button highlights a warning (TaskActions.tsx:105-121); 409 = already handled -> info toast; success bumps app-rate/NPS counters. The shared drawer (fragment 62) also serves reject/review/forward. referee could not confirm: POST approval/rest/tasks/{taskId}/approve: the pa…_

### CAP-155: Reject an approval task

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

A manager rejects a task, giving a mandatory comment.

- **vmm** (Manager): screens: `ApprovalTaskScreen`, `TaskActionsDrawer`; endpoints: `POST approval/rest/tasks/{taskId}/reject`; events: `clicked_on_reject_button`, `clicked_on_close_task_from_action_drawer`, `task_action_completed`, `task_close_complete_with_comment`, `task_close_complete`; storage: `approval.draftComments (persisted)` · evidence `src/components/approval/TaskActions/TaskActions.tsx:141-151`

_Note: Reject enabled only when trimmed comment non-empty (ApprovalTaskActionsDrawer.tsx:126-128)._

### CAP-156: Complete a review of a task

**Fusion:** unique · **Personas:** Reviewer · **Confidence:** High

A reviewer marks a task sent to them for review as reviewed, with a mandatory comment.

- **vmm** (Manager): screens: `ApprovalTaskScreen`, `TaskActionsDrawer`; endpoints: `POST approval/rest/tasks/{taskId}/complete-review`; events: `clicked_on_main_action_button`, `task_action_completed`, `task_close_complete_with_comment`; storage: `approval.draftComments (persisted)` · evidence `src/components/approval/ApprovalTaskActionsDrawer/ApprovalTaskActionsDrawer.tsx:63-70`

_Note: Main action is review when actions contain 'review' and not 'approve'; review tasks cannot be multi-selected._

### CAP-157: Send a task for review to a colleague

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

A manager picks a colleague from the process's user list and sends the task to them for review with a mandatory comment.

- **vmm** (Manager): screens: `ApprovalTaskScreen`, `TaskActionsDrawer (recipient search)`; endpoints: `GET approval/rest/processes/{processId}/users?prefix={searchText}`, `POST approval/rest/tasks/{taskId}/review`; events: `clicked_on_send_for_review_button`, `clicked_on_recipient_input`, `clicked_on_reset_search_icon`, `task_action_completed`; storage: `approvalForwardReview.selectedForwardReviewUser`, `approvalForwardReview.searchInputText` · evidence `src/components/approval/TaskActions/TaskActions.tsx:153-165`

_Note: User search waits for non-empty debounced prefix; submit needs comment and selected user._

### CAP-158: Forward a task to another approver

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

A manager hands the task over to another user of the process with a mandatory comment.

- **vmm** (Manager): screens: `ApprovalTaskScreen`, `TaskActionsDrawer (recipient search)`; endpoints: `GET approval/rest/processes/{processId}/users?prefix={searchText}`, `POST approval/rest/tasks/{taskId}/forward`; events: `clicked_on_forward_button`, `task_action_completed`; storage: `approvalForwardReview.selectedForwardReviewUser` · evidence `src/components/approval/TaskActions/TaskActions.tsx:167-179`

**How they differ:**
- Claim missed a second vmm entry point: the Start hub approval card row offers Forward as its quick action (second in order, after approve) via useApprovalActionDrawer.ts:30-35 and StartHub.tsx:127/300. It opens the same drawer with source 'start_card'.
- Confirmed likely bug: in TaskActions.tsx:108 canForward is computed but not destructured, and the Forward button at line 167 is shown when canSendForReview is true. A task that allows forward but not send-for-review never shows the button on the task screen, and one that allows only send-for-review…
- Mandatory input confirmed: ApprovalTaskActionsDrawer.tsx:131-132 requires a non-empty trimmed comment and a selected recipient before the forward can be submitted.

_Note: Forward button gated by canSendForReview, not canForward (TaskActions.tsx:167) - likely a bug to decide on; body {comment, recipientUserId}._

### CAP-159: Act on an approval task from the Home screen

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

From a task row on the Home approval card, the manager taps one quick-action button (approve, forward, review or reject) that opens the shared action drawer for that task.

- **vmm** (Manager): screens: `StartHub approval card`, `ApprovalTaskActionsDrawer (source 'start_screen')`; events: `home_task_action_opened`; storage: `redux approval.currentTaskId, clearOnCancel, taskActionSource='start_card'` · evidence `src/screens/StartScreen/hooks/useApprovalActionDrawer.ts:31-81`

_Note: One button per row by precedence approve > submitforward > review > reject; sendforreview excluded (needs recipient)._

### CAP-160: Approve several tasks at once

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

A manager long-presses to multi-select tasks (or selects all) in the approval list or on an employee's profile, sees totals per currency split by invoices/expenses/other, confirms and approves them in bulk with progress and per-task error reporting.

- **vmm** (Manager): screens: `ApprovalScreen (multiselect bar)`, `MultiApproveModal`, `TabPresent`, `HrmEmployeeDetailScreen (floating multiselect bar)`; endpoints: `GET approval/task?taskId={taskId}`, `POST approval/rest/tasks/{taskId}/approve`; events: `long_pressed_on_approval_item`, `triggered_multiselect_item`, `triggered_multiselect_all`, `triggered_multiselect_reset`, `clicked_on_approve_selected_items`, `multi_approval_task_skipped_not_found`, `multi_approval_confirm_dialog_rejected`, `multi_approval_error_details` …; storage: `approvalMultiSelect.selected`, `approvalMultiSelect.blockedForMultiSelect`, `redux hrmEmployeeDetail.selectedApprovalTasks`; platform: `vibration on select (if vibration setting on)` · evidence `src/components/approval/ApprovalList/ApprovalListMultiselectBar/ApprovalListMultiselectBar.tsx:157-330; src/screens/man…`

**How they differ:**
- Within vmm (not a fusion choice): the approval-list bar skips tasks that return 404, tracks multi_approval_task_skipped_not_found and refreshes the list (ApprovalListMultiselectBar.tsx:210-231, 296-299). The HRM bar has no 404 handling and counts those tasks as not approved (HrmEmployeeApprovalTask…
- Within vmm: the approval-list bar sends multi_approval_error_details telemetry for each error. The HRM bar does not.
- Within vmm: the approval-list bar stores its selection in approvalMultiSelect.selected. The HRM bar stores it in hrmEmployeeDetail.selectedApprovalTasks.

_Note: Two implementations inside vmm (list bar and HRM bar) with slightly different rules: review tasks unselectable in both; each task re-fetched and blocked if unhandled/rejected lines (services/approvalCloseTask.ts:64-89); HRM bar uses 60s timeout and simple confirm for single task; task detail adds tasks with unapproved lines to the blocked list (ApprovalTaskScreen.tsx:99-107). Consolidate into one…_

### CAP-161: Review an employee's pending approval tasks

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

On an employee's profile the manager expands Approval tasks (badge shows count) to see tasks that employee submitted, swipe a row for quick actions or multi-select them.

- **vmm** (Manager): screens: `HrmEmployeeDetailScreen`; endpoints: `GET approval/rest/my-tasks`; storage: `redux hrmEmployeeDetail.selectedApprovalTasks` · evidence `src/components/hrm/HrmEmployeeApprovalTasks/HrmEmployeeApprovalTasks.tsx:28-79; src/screens/hrm/HrmEmployeeDetailScreen…`

**How they differ:**
- Missed by the claim: the multi-select bar approves the selected tasks in bulk (MultiApproveModal, apiApproval, useCloseTaskMutation in HrmEmployeeApprovalTasksMultiselectBar.tsx), so this is more than reviewing.
- Missed by the claim: tapping a task row opens SCREEN_NAME_APPROVAL_TASK inside the HRM tab rather than the Approval tab (ApprovalListItem.tsx:194-197).

_Note: Tasks filtered where requestor.userId equals employee odpUserId (string or number); one swipeable open at a time._

### CAP-162: Open the requester's employee profile from a task

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

A manager jumps from an approval task or handled process to the HR profile of the employee who requested it.

- **vmm** (Manager): screens: `ApprovalTaskScreen`, `HrmEmployeeDetailScreen`; events: `clicked_on_employee_icon` · evidence `src/components/approval/TaskActions/TaskActions.tsx:68-80`

**How they differ:**
- (same app, not a fusion difference) vmm opens the profile inside the Approval tab when started from a task (TaskActions.tsx:75, TAB_ROUTE_NAME_APPROVAL) and inside the HRM tab when started from a handled process (ApprovalProcessDetailsScreen.tsx:87, TAB_ROUTE_NAME_HRM).
- The claim is missing evidence for the handled-process entry point: src/screens/manager/ApprovalProcessDetailsScreen/ApprovalProcessDetailsScreen.tsx:80-92 and :235-237 (screen ApprovalProcessDetailsScreen) should be added.

_Note: Shown only when requester email matches an HRM employee (useQueryHookHRMEmployeeByEmail)._

### CAP-163: Comment on an approval process

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

A manager adds a free-text comment to a task's process from the task screen; the draft is autosaved per task.

- **vmm** (Manager): screens: `ApprovalTaskScreen (CommentInput + CommentBottomSheet)`; endpoints: `POST approval/rest/processes/{processId}/comments`; storage: `approval.draftComments[taskId] (persisted)` · evidence `src/components/approval/CommentBottomSheet/CommentBottomSheet.tsx:120-140`

_Note: Trimmed; blocked when empty or no processId; draft cleared on success._

### CAP-164: View a task's attached documents

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

A manager views a task's invoice/receipt attachments (PDF, image, TIFF, HTML) as thumbnails and full screen, zooms and pages with a page counter, switches documents, approves from the viewer footer, and can preview the document while editing lines.

- **vmm** (Manager): screens: `ApprovalTaskScreen`, `Document viewer (fullscreen)`, `ApprovalProcessDetailsScreen (history documents)`, `ApprovalTaskVoucherlinesScreen`, `ApprovalTaskDocumentView`, `ApprovalDocumentThumbnail`, `ApprovalTaskEditFinancialsLinesScreen header thumbnail`; endpoints: `GET approval/rest/tasks/{taskUid}/original-attachments?attachmentIds={ids}`, `GET approval/rest/processes/{processUid}/original-attachments?attachmentIds={id…`; events: `attachment_opened`; storage: `approval.taskLocalFilePaths`, `device cache files via react-native-blob-util`, `redux documentView (fullscreen, pageScrollIndex, pageScrollLocked, pdf page/sca…`, `redux documentView.documentSelectorOpened`; platform: `file system cache (react-native-blob-util)`, `TIFF to PNG conversion`, `react-native-pdf`, `WebView for HTML documents` · evidence `src/components/approval/ApprovalDocumentThumbnail/ApprovalDocumentThumbnail.tsx:40-110; src/components/common/DocumentV…`

**How they differ:**
- Within vmm, the up/down page buttons show only on Android, for multi-page TIFF documents that are not zoomed (DocumentViewFloatingFooter.tsx showNavButtons = isAndroid && isTiff). This is not a fusion difference.

_Note: History tasks use the processes attachment endpoint (src/utils/attachments.ts:267); counter shows 'zoomed' when zoom != 1; up/down page buttons Android-only for multi-page TIFF; approve button only when canApprove. referee could not confirm: Screen names 'ApprovalProcessDetailsScreen' and 'ApprovalTaskVoucherlinesScreen' were not checked: the grep for them failed with a shell glob error, so it pr…_

### CAP-165: Share or download a task document

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

A manager exports a task's attachment(s) through the system share sheet; image attachments are combined into one PDF first.

- **vmm** (Manager): screens: `Document viewer header (download icon)`; events: `pdf_downloaded`; storage: `CacheDir/Approval_Document_{MM-DD_HH-mm-ss}.pdf`; platform: `share sheet (react-native-share)`, `PDF generation (react-native-images-to-pdf)`, `file system (react-native-blob-util)` · evidence `src/components/approval/ApprovalDocumentShare/ApprovalDocumentShare.tsx:118-168`

**How they differ:**
- Missed by the claim: the share button always reads state.approval.taskLocalFilePaths (ApprovalDocumentShare.tsx:115), but in history mode the viewer header shows historyTaskLocalFilePaths (ApprovalDocumentViewerHeaderRight.tsx:30). Sharing a document from history may therefore export the current ta…
- The event name pdf_downloaded is also logged when a single non-image file is shared, not only for PDFs (ApprovalDocumentShare.tsx:155).
- No progress or loading UI appears while the PDF is built, because the progress modal is never used.

_Note: 30 s PDF timeout, iOS falls back to first image; non-images share first file only; hardcoded English alert 'Failed to share document' (localisation gap). referee could not confirm: src/components/approval/ApprovalDocumentShareModal/ApprovalDocumentShareModal.tsx: defined but never imported or rendered anywhere in vmm/src, so it is dead code.; strings 'loading', 'error', 'dismiss': these come only…_

### CAP-166: Browse my approval history

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

A manager switches to the History tab to list processes they acted on, with status (awaiting, approved, rejected, cancelled), paging and pull-to-refresh, and opens a process.

- **vmm** (Manager): screens: `ApprovalScreen (History tab)`, `ApprovalProcessTaskScreen`, `ProcessList`; endpoints: `GET approval/rest/my-history?page={page}&text={text}&rows={rows}`; events: `triggered_load_process_list`, `load_process_list_complete`, `pull_to_refresh_triggered_process_list`, `approval_screen_tab_switch`; storage: `approvalProcesses.processListByIds`, `redux approval.activeTab` · evidence `src/components/approval/ProcessList/ProcessList.tsx:80-190; src/screens/manager/ApprovalScreen/ApprovalScreen.tsx:158-1…`

**How they differ:**
- Minor accuracy note: the query builder only adds '&text=' when a search term is set and only adds '&rows=' when rows is non-zero (queryEndpointsApproval.ts:585-590). ProcessList never passes rows, so in practice the request is GET approval/rest/my-history?page={page}[&text={text}].

_Note: Page resets on search/tab change; errors toasted only when loading more; tapping active tab scrolls to top._

### CAP-167: View a handled approval process

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

A manager opens a history item to see document, company, amount, description, due date, resolution status, workflow history and Gaia hints.

- **vmm** (Manager): screens: `ApprovalProcessTaskScreen`, `ApprovalTaskHistoryNoContent`, `ApprovalProcessHeaderRight`; endpoints: `GET /approval/rest/processes/{processId}`, `GET /approval/rest/processes/{processId}/progress-details`; events: `task_load_change`, `process_details_load_change`, `process_workflow_details_load_change`, `clicked_on_employee_icon`, `approval_task_details_opened_info_modal`; storage: `redux approvalProcesses.processListByIds` · evidence `src/screens/manager/ApprovalProcessDetailsScreen/ApprovalProcessDetailsScreen.tsx:52-249`

_Note: Refresh failure with cached data shows toast. referee could not confirm: ApprovalTaskHistoryNoContent and ApprovalProcessHeaderRight are components inside the screen, not separate screens. 'ApprovalProcessTaskScreen' is the route name (consts/screens.ts:4) for ApprovalProcessDetailsScreen.; src/screens/manager/ApprovalProcessDetailsScreen/components/ApprovalTaskHistoryNoContent/ApprovalTaskHistor…_

### CAP-168: See a task's approval workflow and history

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

A manager sees the workflow steps (initial source, current step with pending approvers, future/skipped steps, due dates) and the event history of a task or process.

- **vmm** (Manager): screens: `ApprovalTaskScreen`, `ApprovalProcessDetailsScreen`; events: `triggered_show_workflow_skipped_steps` · evidence `src/components/approval/WorkflowDetails/index.tsx:24-60`

_Note: Data from progress-details endpoints loaded by the screens; skipped steps behind a toggle._

### CAP-169: Approve or reject individual accounting lines

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

An approver sets each voucher line of an expense/claim to approved or rejected; when all their lines are decided the matching approve/reject drawer opens automatically.

- **vmm** (Manager): screens: `ApprovalTaskVoucherlinesScreen`; endpoints: `POST approval/rest/tasks/{taskId}/accounting-grid/lineapproval/{rowIndex}/{1/-1}`, `GET /approval/task?taskId={taskId}&skipFinancials=true`; events: `clicked_on_approve_line_button`, `clicked_on_reject_line_button`, `voucher_line_action_completed`; storage: `approvalVoucherlines.voucherlineOngoingApproval`, `approvalVoucherlines.voucherlineChangeError`, `redux approvalVoucherlines.voucherlinesShowAllLines`, `redux approval.currentTaskId` · evidence `src/components/approval/voucherlines/VoucherlinesBottomRow/VoucherlinesBottomRow.tsx:97-155; src/screens/manager/Approv…`

**How they differ:**
- Nuance the claim misses: the drawer opens only when all of the approver's lines have the same decision. If approved and rejected lines are mixed, no drawer opens; instead the task goes on the multi-select blocked list (approvalMultiAddToBlocked, queryEndpointsApproval.ts:193-195). The recommendatio…

_Note: If-Match rowVersion header; 'disabled' lines read-only; screen empty without claim lines; auto-recommend via approvedLineRecommendedAction (queryEndpointsApproval.ts:176-197)._

### CAP-170: Open a task's accounting lines

**Fusion:** unique · **Personas:** Manager / approver · **Confidence:** High

From a task, a manager opens its voucher lines or Financials/Business NXT/Compello posting lines with a count of lines awaiting approval or editable, and switches between only their lines and all lines.

- **vmm** (Manager): screens: `ApprovalTaskScreen`, `ApprovalTaskVoucherlinesScreen`, `ApprovalTaskVoucherlinesEditorScreen`, `ApprovalTaskFinancialsLinesScreen`, `ApprovalTaskBXNLineEditScreen`, `ApprovalTaskBXNLineEditFeedbackScreen`, `ApprovalTaskCompelloLinesScreen`, `InfoModal` …; endpoints: `GET financials/invoices/{referenceNumber}?assignedLines={lines}`, `GET approval/task?taskId={taskId}&skipFinancials=true`; events: `clicked_on_view_voucher_lines_button`, `clicked_on_document_editor_button`, `clicked_on_view_voucher_lines_bxn_button`, `clicked_on_view_voucher_lines_compello_button`, `approval_document_editor_opened_info_modal`, `triggered_show_all_lines_switch_to`; storage: `approval.singleTaskVoucherLines`, `redux approval.currentTaskId`, `redux approval showAllLines (via approvalShowAllVoucherLines)` · evidence `src/components/approval/DocumentEditorButton/DocumentEditorButton.tsx:62-215; src/screens/manager/ApprovalTaskFinancial…`

_Note: Type 'clame' when claimLines, else 'financials'; ipp-company-id header; only owned lines counted. ApprovalTaskFinancialsLinesScreen appears unregistered in ApprovalNavConfig (likely dead code). referee could not confirm: src/screens/manager/ApprovalTaskFinancialsLinesScreen/ApprovalTaskFinancialsLinesScreen.tsx:27-71 - dead code: nothing imports it and ApprovalNavConfig does not register it, so i…_

### CAP-171: Edit the accounting lines of an invoice before approving

**Fusion:** unique · **Personas:** Manager / invoice approver · **Confidence:** High

An approver edits the coding of an invoice's lines in the connected ERP (Visma.net Financials, Business NXT or Compello): text, accounts, subaccounts/org units, project and task, quantities, dates, tax codes, lookups; adds/deletes lines where allowed; and saves all changed lines in one go with progress and per-field error feedback.

- **vmm** (Manager): screens: `ApprovalTaskEditFinancialsLinesScreen (route ApprovalTaskVoucherlinesEditorScre…`, `FinancialLineEditItem`, `FinancialLineEditComponent`, `EditableSelectRow`, `EditableTextRow`, `FieldEditModal`, `TextEditModal`, `FinancialFieldSelector` …; endpoints: `GET /approval/task?taskId={taskId}&skipFinancials=true`, `GET /financials/invoices/{referenceNumber}?assignedLines={lines}`, `GET /financials/accounts`, `GET /financials/subaccounts`, `GET /financials/projects`, `GET /financials/validate/subaccount/{subAccountNumber}`, `PUT /financials/{documentType}/{displayId}`, `POST /api/graphql (GraphQL query GetBatchNumber / GET_BATCH_BY_WORKFLOW_ID)` …; events: `line_edit_save_completed`, `financials_line_update_error`, `task_load_error`, `approval_task_bxn_line_edit_screen`, `fetch_bxn_lines`, `fetch_bxn_lines_error`, `update_bxn_line`, `update_bxn_line_error` …; storage: `redux approval.financialLineChanges`, `redux approval.financialFieldErrors`, `redux approval.currentTaskId`, `redux approval.singleTaskVoucherLines`, `redux approvalBxn.companyMaps[companyId] (accounts, org unit, currency, tax cod…`, `redux approvalVoucherlines.lineChanges`, `redux approvalVoucherlines.fieldErrors`, `redux settings.selectedLocale`; platform: `Android hardware back / iOS swipe-back intercepted via beforeRemove`, `Android hardware back closes field overlay first` · evidence `src/screens/manager/ApprovalTaskEditFinancialsLinesScreen/ApprovalTaskEditFinancialsLinesScreen.tsx:385-429; src/screen…`

_Note: Three ERP-specific editors inside vmm with different rules. Financials: only Financials tasks; pre-booked invoices lock fields; project 'X' disables task; task required when project set; subaccount validated before PUT. BXN: read-only when tableAccess.canUpdate false; debit/credit accounts > 999 grouped by type; locked lines (lockedByProcessNo) auto-retry; GraphQL error path mapped to field. Comp…_

### CAP-172: Apply one field value to all lines

**Fusion:** unique · **Personas:** Manager / invoice approver · **Confidence:** High

While editing a field on one invoice line, the approver taps 'Apply to all lines' to copy that value onto every other line, pending save.

- **vmm** (Manager): screens: `TextEditModal`, `FieldEditModal`, `EditableSelectRow`, `EditableTextRow`, `ApprovalTaskCompelloLinesScreen`; storage: `in-memory BulkApplyContext overridesMap (per lineNo)`, `in-memory BulkApplyContext overridesMap` · evidence `src/screens/manager/ApprovalTaskBXNLineEditScreen/context/BulkApplyContext.tsx:31-140; src/screens/manager/ApprovalTask…`

**How they differ:**
- Within vmm only (not a fusion difference): the same logic is copied three times, once per ERP. BXN keys lines by lineNo, Financials by lineNumber and Compello by lineId.
- Within vmm: I found no clearAllOverrides call on the Compello screen, only the per-line clearOverrides in CompelloLineEditContext. BXN and Financials do clear all overrides on save or revert (BXN ApprovalTaskBXNLineEditScreen.tsx:86-88; Financials ApprovalTaskEditFinancialsLinesScreen.tsx:99-102,35…

_Note: Source line excluded; overrides cleared on save or revert. Duplicated per ERP. referee could not confirm: src/screens/manager/ApprovalTaskBXNLineEditScreen/context/BulkApplyContext.tsx:31-140: the file has only 138 lines; Missing from the screens and files lists: the Compello UI and context that are part of this capability, namely ApprovalTaskCompelloLinesScreen/components/CompelloTextEditModal/C…_

### CAP-173: Discard unsaved line edits

**Fusion:** unique · **Personas:** Manager / invoice approver · **Confidence:** High

The approver reverts all unsaved line changes after a confirmation, or confirms before leaving the line editor with unsaved changes.

- **vmm** (Manager): screens: `ApprovalTaskBXNLineEditScreen revert dialog`, `ApprovalTaskBXNLineEditScreen exit-without-saving dialog`, `ApprovalTaskEditFinancialsLinesScreen revert dialog`, `ApprovalTaskEditFinancialsLinesScreen exit-without-saving dialog`, `ApprovalTaskCompelloLinesScreen`; endpoints: `GET /financials/invoices/{referenceNumber}?assignedLines={lines}`; events: `line_edit_abandoned`; storage: `redux approvalVoucherlines.lineChanges`, `redux approvalVoucherlines.fieldErrors`, `redux approval.financialLineChanges`, `redux approval.financialFieldErrors`; platform: `beforeRemove navigation guard for hardware back and swipe-back` · evidence `src/screens/manager/ApprovalTaskBXNLineEditScreen/ApprovalTaskBXNLineEditScreen.tsx:398-536; src/screens/manager/Approv…`

**How they differ:**
- Within vmm (not a fusion split): the ERP financials screen refetches GET financials/invoices/{ref}?assignedLines= on revert and remounts the lines (ApprovalTaskEditFinancialsLinesScreen.tsx:361-373). The BXN screen only clears redux and resets its components, with no refetch (ApprovalTaskBXNLineEdi…
- Within vmm: the Compello lines screen offers revert only. It resets resetCounter and changedLineIds, which are local state and not redux (ApprovalTaskCompelloLinesScreen.tsx:264-270). No beforeRemove or exit-without-saving guard was found in that file.

_Note: Back closes topmost layer first (document selector, preview, edit overlay, then dialog); event property 'reverted' or 'navigated_away'. referee could not confirm: ApprovalTaskCompelloLinesScreen is listed alongside the exit-without-saving guard, but that file has only a revert dialog. It has no beforeRemove listener and no unsaved_changes/exit_without_saving dialog.; The endpoint GET /financials/…_

### CAP-174: Choose which line fields to show

**Fusion:** unique · **Personas:** Manager / invoice approver · **Confidence:** High

The approver turns on Custom mode and picks which fields each invoice line shows; the choice is remembered across restarts.

- **vmm** (Manager): screens: `ApprovalTaskBXNLineEditScreen header Custom switch`, `FieldSelectionModal`, `ApprovalTaskEditFinancialsLinesScreen header switch and filter button`, `CompelloFieldSelectionModal`; events: `custom_fields_picker_opened`, `custom_fields_selection_confirmed`; storage: `redux settings.voucherLineCustomMode (persisted settings slice)`, `redux settings.selectedVoucherLineFields (persisted settings slice)`, `redux settings.financialLineCustomMode (persisted, settings is in the whitelist)`, `redux settings.selectedFinancialLineFields (persisted)`, `redux settings.compelloLineCustomMode`, `redux settings.selectedCompelloLineFields` · evidence `src/screens/manager/ApprovalTaskBXNLineEditScreen/components/FieldSelectionModal/FieldSelectionModal.tsx:38-80; src/scr…`

**How they differ:**
- Within vmm only, not a fusion difference: the Compello picker sends no custom_fields_picker_opened or custom_fields_selection_confirmed event, while BXN (label 'BNXT') and Financials (label 'ERP') send both.
- Within vmm only: the Financials picker scrolls to the first selected field when it opens; the BXN picker does not.
- Missing from the claim's files list: ApprovalTaskCompelloLinesScreen.tsx, which holds the Compello Custom switch (lines 86, 140, 497).

_Note: Separate persisted selection per ERP (BXN, Financials, Compello). BXN fields from company columnsData; Financials subaccount keys subaccount_{segmentId}; Compello hidden columns excluded._

### CAP-175: Jump to a specific invoice line

**Fusion:** unique · **Personas:** Manager / invoice approver · **Confidence:** High

On invoices with many lines, the approver taps a line number in a quick index rail to scroll to it and sees which lines have unsaved changes or errors.

- **vmm** (Manager): screens: `ApprovalTaskBXNLineEditScreen quick index`, `ApprovalTaskEditFinancialsLinesScreen quick index`; storage: `redux approvalVoucherlines.lineChanges`, `redux approvalVoucherlines.fieldErrors`, `redux approval.financialLineChanges`, `redux approval.financialFieldErrors` · evidence `src/screens/manager/ApprovalTaskBXNLineEditScreen/ApprovalTaskBXNLineEditScreen.tsx:465-499; src/screens/manager/Approv…`

**How they differ:**
- Correction to the claim's note: the gap divider (QuickIndexGapDivider) appears in both screens, not only in Financials (BXN ApprovalTaskBXNLineEditScreen.tsx:720-724 and Financials ApprovalTaskEditFinancialsLinesScreen.tsx:624-627).
- Correction to the hook's documentation: the comment says 15 indices by default, but the code uses maxIndices = 12. The shown line numbers also wait 500 ms after scrolling stops before they update (useQuickIndexNavigation.ts).

_Note: Active index = line nearest viewport centre; Financials shows dividers for gaps._

## Payments

AutoPay bank payments: review, select and sign payments for approval, warnings, notes, pay date, cancel, and track status after approval

### CAP-186: Review AutoPay payments waiting for my approval

**Fusion:** unique · **Personas:** manager / payment approver · **Confidence:** High

A manager (AutoPay approver) sees all bank payments waiting for approval, grouped by company and bank account, with balance, total due, pay date, reference, warning marker and salary or domestic type. Groups can be expanded or collapsed, the list supports pull-to-refresh and reloads when the app comes back to the foreground.

- **vmm** (Manager): screens: `AutopayHomeScreen (SCREEN_NAME_AUTOPAY_HOME)`, `AutopayHomeTabPaymentsScreen`, `Autopay home, Payments tab`; endpoints: `GET /api/autopay/transaction/list?rows=2000`; events: `autopay_payments_load_time`, `autopay_expand_agreement`; storage: `redux autopay (persisted slice)`, `redux hrmDialogueCollapsedGroups.autopayPayments (persisted)`, `Firebase Remote Config REMOTE_CONFIG_USER_TESTING_PHASE`; platform: `AppState foreground reload`, `Firebase Remote Config` · evidence `src/screens/autopay/AutopayHomeTabPaymentsScreen/AutopayHomeTabPaymentsScreen.tsx:158-180; src/components/autopay/FlatA…`

_Note: The list request times out after 180s. On error it shows a toast when cached data exists, otherwise a retryable error card. Sections are sorted by title (autopaySelectors.ts:266-267). The empty-list message is picked at random from 4 options. A group header opens an InfoModal. A user-testing banner shows when remote config integrations include 'autopay'._

### CAP-187: Search AutoPay payments

**Fusion:** unique · **Personas:** manager / payment approver · **Confidence:** High

A manager opens a search bar on the AutoPay home and filters payments and accounts by free text. Recent searches are remembered and all accounts are shown expanded while a search is active.

- **vmm** (Manager): screens: `Autopay home top bar`, `AutopayHomeTabPaymentsScreen`, `AutopayHomeTabOverviewScreen`; events: `autopay_used_search`, `autopay_search_results`; storage: `redux autopayRecentSearches.recentSearches`, `AutopayHomeScreenContext searchInputText (in memory)` · evidence `src/screens/autopay/AutopaySearchBar/AutopaySearchBar.tsx:13-54; src/components/autopay/AutopayTopBar/AutopayTopBar.tsx…`

**How they differ:**
- Internal inconsistency in vmm (not a fusion difference): the Overview tab always shows the legacy AutopaySearchBar (AutopayHomeTabOverviewScreen.tsx:177,194), while the Payments tab shows GaiaAssistBand under a non-legacy assist style (AutopayHomeTabPaymentsScreen.tsx:401,457). The top-bar toggle i…
- The same-IBAN filter from the notes is also in AutopayHomeTabOverviewScreen.tsx:106-111. It probably drops account headers that have no matching transaction rows rather than being a business rule; a person should confirm.

_Note: Closing the search bar clears the text. With an active search only companies with more than one transaction on the same IBAN are kept (AutopayHomeTabPaymentsScreen.tsx:99-110), which looks odd and should be checked. The GAiA assist band replaces the legacy search bar depending on useGaiaAssistStyle. The search toggle is hidden unless the assist style is 'legacy'. referee could not confirm: Autopa…_

### CAP-188: Select AutoPay payments for approval

**Fusion:** unique · **Personas:** manager / payment approver · **Confidence:** High

A manager ticks single payments, selects a whole bank account, or selects all salary payments in one tap. They see the selected count and amount, then press Approve to continue to signing or cancel the selection.

- **vmm** (Manager): screens: `Autopay home, Payments tab (list items)`, `AutopayHomeTabPaymentsScreen`, `AutopayListMultiselectBar`, `AutopayInvoiceDetailsScreen`; events: `autopay_select_transaction`, `autopay_select_all_agreement`, `autopay_expand_agreement`, `autopay_approve_button_clicked`, `autopay_select_all_salaries`, `autopay_select_all_salaries_visible`, `autopay_transaction_checked`; storage: `redux autopayMultiselect.accountsChecked / transactionsChecked`, `vibration setting (useVibration)`; platform: `vibration (android.permission.VIBRATE)`, `Android hardware back clears selection` · evidence `src/components/autopay/TransactionListItem/TransactionListItem.tsx:71-78; src/screens/autopay/AutopayHomeScreen/Autopay…`

_Note: The checkbox shows a partial state when 0 < selected < total. The selected due amount is shown as negative. Select-all-salaries stays disabled until the list is loaded and while everything is already selected. The selection resets when the screen mounts. When a search is active, accounts are forced open._

### CAP-189: Approve selected AutoPay payments with bank two-factor signing (BankID)

**Fusion:** unique · **Personas:** manager / payment approver · **Confidence:** High

A manager sends the ticked payments for approval and signs them with BankID or bank 2FA in an embedded web page. They get a success toast, or return to the list if they cancel.

- **vmm** (Manager): screens: `AutopayApproveTransaction (SCREEN_NAME_AUTOPAY_APPROVE_TRANSACTION = 'AutopayAp…`; endpoints: `POST /api/autopay/transactions/approve`; events: `autopay_approve_transaction_screen_load`, `autopay_approve_authorizing`, `autopay_approve_success`, `autopay_approve_cancelled`, `autopay_approve_error`, `autopay_approve_transaction_error`, `autopay_approve_webview_load_failed`, `autopay_approve_auth_duration` …; storage: `redux autopayMultiselect.transactionsChecked (read; reset through autopayResetC…`, `redux loginManager.countryCode (read)`; platform: `react-native-webview (incognito, cache disabled, popups loaded in the same view)`, `Linking.openURL for custom app schemes such as bankid://` · evidence `src/components/autopay/AutopayApproveTransaction/AutopayApproveTransaction.tsx:201-251`

_Note: twoFaOptions redirects: success https://visma-manager.firebaseapp.com/ and cancel https://visma-manager.web.app/, detected in onNavigationStateChange (:132, :145). The CSS depends on the country (SE/NO/default) (apiAutopay.ts:114-116). A non-empty rejectedTransactions shows an error. The URL policy blocks javascript/data/file/blob/intent/content/filesystem, allows http/https/about and hands other…_

### CAP-190: Track the status of processed AutoPay payments (In progress / Deviation / In bank)

**Fusion:** unique · **Personas:** manager / payment approver · **Confidence:** High

On an Overview tab, a manager reviews payments from the last 60 days in three buckets (in progress, deviation, in bank). Each bucket shows a count, a colour-coded status and the approvals still missing, with retry on failure and a notice when the limit cuts the list short.

- **vmm** (Manager): screens: `Autopay home, Overview tab`, `AutopayHomeTabOverviewScreen`, `Autopay home top bar`; endpoints: `GET /api/autopay/overview/transaction/list?transactionLimit=200&payDateFromDays…`; events: `autopay_expand_agreement`, `autopay_screen_tab_switch`; storage: `redux autopayOverview.overviewTab / listInProcess / listDeviation / listInBank`, `redux autopay.activeTab`, `redux features.showAutopayOverviewTab (feature flag)` · evidence `src/components/autopay/AutopayOverviewSwitcher/AutopayOverviewSwitcher.tsx:26-109; src/screens/autopay/AutopayHomeScree…`

_Note: The Payments/Overview tab switch (fragment 40) is navigation into this capability. The Overview tab shows only when the showAutopayOverviewTab flag is on (AutopayHomeScreen.tsx:40-49), and choosing a tab scrolls its list to the top. Limits are 200 transactions and 60 days (apiAutopay.ts:213). In bank means PAID only (apiAutopay.ts:285). The three lists load in parallel and one failure does not ca…_

### CAP-191: View an AutoPay payment's details

**Fusion:** unique · **Personas:** manager / payment approver · **Confidence:** High

A manager opens a payment from the Payments list or the Overview list and sees its status, creditor and debtor, references, original pay date and amount, events, and the approvers still missing. Processed payments open in a read-only variant.

- **vmm** (Manager): screens: `AutopayInvoiceDetailsScreen (SCREEN_NAME_AUTOPAY_INVOICE_DETAILS)`, `AutopayInvoiceOverviewDetailsScreen (SCREEN_NAME_AUTOPAY_INVOICE_OVERVIEW_DETAI…`; endpoints: `GET /api/autopay/transaction?transactionId={id}`, `GET /api/autopay/transactions/{id}/invoiceimage`, `GET /api/autopay/transactions/{id}/invoiceImage/pdf`; events: `autopay_open_transaction_details`, `autopay_transaction_details_opened_info_modal`, `autopay_details_load_time`, `autopay_invoice_details_screen_loaded`; storage: `redux autopayImageDocuments`, `redux documentView` · evidence `src/screens/autopay/AutopayInvoiceDetailsScreen/AutopayInvoiceDetailsScreen.tsx:61-470; src/components/autopay/Transact…`

_Note: The pending and processed details screens are merged because the user outcome is the same. The processed variant is read-only (pay date readonly at line 181) and fires the same screen-loaded event. The header info icon opens an InfoModal with 5 help lines. The original pay date is hidden when it is 01/01/0001. The details fetch is in contexts/AutopayInvoiceDetails/AutopayInvoiceDetailsProvider.ts…_

### CAP-192: View the invoice document attached to an AutoPay payment

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager previews the invoice attachment as a thumbnail and opens it full screen, as a PDF or, if the PDF fails, as page images.

- **vmm** (Manager): screens: `AutopayInvoiceDetailsScreen`, `Autopay document view`; endpoints: `GET /api/autopay/transactions/{transactionId}/invoiceImage/pdf`, `GET /api/autopay/transactions/{transactionId}/invoiceimage`; events: `autopay_document_thumbnail_open`; storage: `local file autopay_invoice_{transactionId} (PDF written from base64, apiAutopay…`, `redux autopayImageDocuments.documentsUrls / documentsByUrl`, `redux documentView.pageScrollIndex / activeDocumentIndex`; platform: `local file system (PDF cache)`, `PDF viewer` · evidence `src/components/autopay/AutopayDocumentThumbnail/AutopayDocumentThumbnail.tsx:20-78`

_Note: The PDF is preferred and TIFF or image pages are the fallback. There is one retry after 10s when a 'replacement/not_found' placeholder comes back (fragment 201). The floating footer offers document actions for the PDF. referee could not confirm: storage citation 'apiAutopay.ts:198' is wrong: the PDF local-file write (generatePathForFile autopay_invoice_{transactionId} + RNBlobUtil.fs.writeFile) i…_

### CAP-193: Change the pay date of an AutoPay payment

**Fusion:** unique · **Personas:** manager / payment approver · **Confidence:** High

A manager picks a new pay date from a date picker on the payment details. Past dates cannot be chosen and read-only payments cannot be changed.

- **vmm** (Manager): screens: `AutopayInvoiceDetailsScreen`; endpoints: `PUT /api/autopay/transactions/{transactionId}/payDate`; events: `autopay_changed_paydate_success`, `autopay_changed_paydate_failed`; platform: `native date picker modal (react-native-date-picker)` · evidence `src/components/autopay/AutopayTransactionPaydate/AutopayTransactionPaydate.tsx:35-87`

**How they differ:**
- Missed detail: AutopayInvoiceOverviewDetailsScreen.tsx:181 shows the same pay-date component with readonly set, so the date is displayed there but cannot be changed. Only AutopayInvoiceDetailsScreen.tsx:352 allows editing.
- Missed string key: if the change fails, the Provider shows the error toast 'autopay_failed_to_change_pay_date' (AutopayInvoiceDetailsProvider.tsx:123).
- No other app has this: neither me-ios nor me-android has autopay or pay-date code; the only matches are me-ios test JSON files (User.json, User_MultipleCompanies.json).

_Note: minimumDate is today. The date is sent as YYYY-MM-DD (Provider:115) and shown as DD/MM/YYYY._

### CAP-194: Add, edit or delete a note on an AutoPay payment

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager writes, saves, changes or clears a free-text note on a payment.

- **vmm** (Manager): screens: `AutopayInvoiceDetailsScreen`; endpoints: `PUT /api/autopay/transactions/{transactionId}/note`, `DELETE /api/autopay/transactions/{transactionId}/note`; events: `autopay_note_added`, `autopay_note_changed`, `autopay_note_deleted` · evidence `src/components/autopay/AutopayTransactionWarningSection/AutopayTransactionWarningSection.tsx:92-125`

_Note: An empty text sends DELETE and any other text sends PUT (apiAutopay.ts:174). Save is enabled only after a change and delete only when a note exists. A second save is ignored while one is in progress._

### CAP-195: Review and verify AutoPay payment warnings

**Fusion:** unique · **Personas:** manager / payment approver · **Confidence:** High

A manager sees fraud and risk warnings on a payment (new or changed creditor or debtor, duplicate invoice, Inyett detection) and marks them verified, one at a time or all at once, or removes a verification.

- **vmm** (Manager): screens: `AutopayWarningsOverview (SCREEN_NAME_AUTOPAY_WARNINGS_OVERVIEW)`, `AutopayInvoiceDetailsScreen warning section`; endpoints: `POST /api/autopay/transactions/{transactionId}/warnings/verify`, `DELETE /api/autopay/transactions/{transactionId}/warnings/{warningType}/verific…`; events: `autopay_verify_warning`, `autopay_delete_verify_warning`, `autopay_open_warning_details` · evidence `src/components/autopay/AutopayWarningsOverviewScreen/AutopayWarningsOverviewScreen.tsx:31-159`

_Note: Verify buttons appear only when some warning has isVerifiable. A warning counts as verified when it has verifiedOn. A single warning is verified inline, while several warnings send the manager to the Warnings overview screen. Pressing verify on a verified warning deletes the verification (Provider:213)._

### CAP-196: Cancel an AutoPay payment

**Fusion:** unique · **Personas:** manager / payment approver · **Confidence:** High

A manager cancels a pending payment from its details screen after confirming a warning dialog. The payment then disappears from the list.

- **vmm** (Manager): screens: `AutopayInvoiceDetailsScreen`; endpoints: `POST /api/autopay/transactions/cancel`; events: `autopay_trans_cancelled_success`, `autopay_trans_cancelled_failed`; storage: `redux autopay (completed transactions removed)` · evidence `src/screens/autopay/AutopayInvoiceDetailsScreen/AutopayInvoiceDetailsScreen.tsx:275-299`

**How they differ:**
- Employee product (me-ios / me-android): no AutoPay cancel implementation; the only match is fixture data at me-ios/EmployeeServices/TestResources/Sources/TestResources/Resources/JSON/User.json:153
- vmm shows the cancel button with no status check (AutopayInvoiceDetailsScreen.tsx:474-479), so it is not limited to pending payments in this component

_Note: useCallOnce guards against a double submit. On success the payment is removed from the list and the app navigates back._

## Business NXT

Business NXT ERP work: orders, offers, products and stock, customers and suppliers, invoices, money in and out, BXN approval tracking and company switch

### CAP-030: Switch the active Business NXT company

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager with access to several Business NXT companies picks which company every BXN order, invoice, money and approval screen shows, from an initials-avatar dropdown in the header.

- **vmm** (Manager): screens: `BnxtHeaderRight (headerRight of BXN root screens)`, `CompanyPicker`; storage: `redux bnxtOrders.selectedCompanyId`, `redux bnxtOrders.companies`; platform: `react-native` · evidence `src/components/bnxtOrders/CompanyPicker/CompanyPicker.tsx:27-71`

**How they differ:**
- Not a divergence, a nearby capability: me-ios has an employer-company selector on the start page (Employee/StartPage/StartPageViewController.swift:118-402, CompanySelectorTableViewCell.swift). It switches the employee's employer, not the Business NXT company, so it should be its own capability ('sw…
- Claim leaves out: when the company list loads and the saved selection is no longer in it, the selection resets to the first company (vmm src/reducers/bnxtOrdersReducer.ts:46-53). The whole slice, including the selection, is cleared on logout (lines 43-45).

_Note: Hidden when there is no selected company or fewer than 2 companies. Initials come from the first two words of the name. The reducer ignores ids that are not in the companies list (reducers/bnxtOrdersReducer.ts:58-61)._

### CAP-031: Open a Business NXT work area

**Fusion:** unique · **Personas:** BXN user, manager · **Confidence:** High

A Business NXT user opens sales orders, purchase orders, offers, invoices, approvals, money in/out or the registers, either from the BXN hub list or from the tabbed workspace. Areas the user has no access to are hidden.

- **vmm** (Manager): screens: `BnxtHubScreen`, `BnxtWorkspaceScreen`; endpoints: `POST https://business.visma.net/api/graphql (mutation GetBnxtOrderTableAccess)`; events: `bnxt_hub_area_opened`; storage: `redux bnxtOrders.selectedCompanyId`, `redux bnxtOrders edit access`, `redux features.isBnxtTabbedHubEnabled`; platform: `react-native` · evidence `src/screens/manager/BnxtHubScreen/BnxtHubScreen.tsx:55-247; src/screens/manager/BnxtWorkspaceScreen/BnxtWorkspaceScreen…`

**How they differ:**
- Minor precision: the hub's sales, purchase and offers rows, and the workspace's order tabs, are never hidden by access. Only invoices, approvals, money in/out and the registers are hidden (bnxtAreaAccess.ts cases 'sales'/'purchase'/'offers' return true).
- Minor precision: when the whole registers section is denied, the hub shows an information banner (bnxt_lookup_no_access) instead of hiding the section. The money section is hidden entirely.

_Note: The hub and the tabbed workspace are two layouts for the same outcome. The tabbed workspace replaces the hub when integration AND isBnxtTabbedHubEnabled are on (bnxtOrdersSelectors.ts:19-20). Rows stay visible while the access probe is unresolved and are dropped once access is denied. Money in needs openCustomerEntry+customerBalance read; money out needs openSupplierEntry+supplierBalance read. Th…_

### CAP-032: Browse Business NXT orders

**Fusion:** unique · **Personas:** Business NXT manager · **Confidence:** High

A Business NXT user lists sales orders, purchase orders or offers, searches them, sorts by date, number or name, and filters by creator, approval state and invoiced. Tapping an order opens it; from sales or purchases the user can also start a new order.

- **vmm** (Manager): screens: `BnxtOrdersScreen (SCREEN_NAME_BNXT_ORDERS)`, `BnxtOrdersPane`, `OrderListTab`; endpoints: `POST https://business.visma.net/api/graphql (Apollo, via hooks/useBnxtOrderList)`; storage: `redux bnxtOrders.companies/selectedCompanyId`, `redux features.isBnxtOrdersIntegrationEnabled`, `features.isBnxtOrderEditEnabled`; platform: `react-native` · evidence `src/screens/manager/BnxtOrdersScreen/components/BnxtOrdersPane/BnxtOrdersPane.tsx:50-230; src/components/bnxtOrders/Ord…`

_Note: Access requires the dev-tools flag AND at least one BXN company (bnxtOrdersSelectors.ts:9-15). The offers area is read-only, with no create. The edit gate is ANDed with the view gate. Fragment 1 (the shared presentational list rows and detail components) is used here and in the other BXN list capabilities._

### CAP-033: View a Business NXT order

**Fusion:** unique · **Personas:** BXN user, buyer, sales person · **Confidence:** High

A user opens a sales order, purchase order or offer to see its status, totals, VAT, delivery date, counterparty, lines and approval status. From there they can jump to the customer or supplier card, or to a line's product card.

- **vmm** (Manager): screens: `BnxtOrderDetailScreen`, `BnxtAssociateCardScreen`, `BnxtProductDetailScreen`; endpoints: `POST https://business.visma.net/api/graphql (query GetBnxtOrderWithLines)`, `POST https://business.visma.net/api/graphql (mutation GetBnxtOrderTableAccess)`; storage: `redux bnxtOrders.selectedCompanyId`; platform: `react-native` · evidence `src/screens/manager/BnxtOrderDetailScreen/BnxtOrderDetailScreen.tsx:104-865; BnxtOrderDetailScreen.tsx:438-461`

_Note: Invoiced orders show the amount invoiced so far instead of the net total. The detail hero shows at most 3 stats. The counterparty link needs associateNo and associate read access; the product link needs product read access. referee could not confirm: The GetBnxtOrderTableAccess mutation lives in src/services/apiNXT/orderMutations.ts:168, which is not in the cited file list (the endpoint itself ex…_

### CAP-034: Edit a Business NXT order's references, delivery date and lines

**Fusion:** unique · **Personas:** BXN user, buyer, sales person · **Confidence:** High

A user edits an order's delivery date, our reference and your reference, and updates, adds or deletes lines. They can then save or revert, and are warned about unsaved changes.

- **vmm** (Manager): screens: `BnxtOrderDetailScreen`, `TextEditModal`, `OrderLineCard`, `NewOrderLineCard`; endpoints: `POST https://business.visma.net/api/graphql (query GetBnxtEmployees)`, `POST https://business.visma.net/api/graphql (query GetBnxtContacts)`, `POST https://business.visma.net/api/graphql (query GetBnxtStockBalance)`, `POST https://business.visma.net/api/graphql (query GetBnxtDefaultWarehouse)`, `POST https://business.visma.net/api/graphql (mutation UpdateBnxtOrder)`, `POST https://business.visma.net/api/graphql (mutation UpdateBnxtOrderLine)`, `POST https://business.visma.net/api/graphql (mutation CreateBnxtOrderLine)`, `POST https://business.visma.net/api/graphql (mutation DeleteBnxtOrderLine)`; storage: `redux bnxtOrders.selectedCompanyId`; platform: `native date picker`, `beforeRemove unsaved-changes guard`, `Android back closes field overlay first` · evidence `src/screens/manager/BnxtOrderDetailScreen/BnxtOrderDetailScreen.tsx:104-865`

_Note: Split from the order-detail fragment 167. Editing is gated by order.canUpdate and by orderLine canUpdate/canInsert/canDelete. The header update sends prior values for optimistic concurrency; a stale write reloads the order and shows an alert. Save runs in this order: header, line updates, line creates, deletions. It stops at the first failure._

### CAP-035: Create a sales or purchase order

**Fusion:** unique · **Personas:** BXN user, buyer, sales person · **Confidence:** High

A user builds a new BXN order: they pick a customer (sales) or supplier (purchase), add products with quantities, preview totals calculated by the server, and confirm to create it.

- **vmm** (Manager): screens: `BnxtOrderCreateScreen`, `PickerOverlay`; endpoints: `POST https://business.visma.net/api/graphql (query GetBnxtSuppliers)`, `POST https://business.visma.net/api/graphql (query SearchBnxtCustomers)`, `POST https://business.visma.net/api/graphql (query GetBnxtProducts)`, `POST https://business.visma.net/api/graphql (mutation CreateBnxtOrder)`; storage: `redux bnxtOrders.selectedCompanyId`, `redux bnxtOrders list invalidation`; platform: `react-native` · evidence `src/screens/manager/BnxtOrderCreateScreen/BnxtOrderCreateScreen.tsx:69-446`

_Note: Product search needs at least 2 characters. Customer search is debounced by 600 ms. Every line quantity must parse to more than 0. The preview is CreateBnxtOrder with temporary:true, and any edit invalidates it. On success the screen is replaced by the order detail._

### CAP-036: Send a purchase order to approval

**Fusion:** unique · **Personas:** buyer · **Confidence:** High

A buyer sends a purchase order into the BXN approval flow, with an optional comment.

- **vmm** (Manager): screens: `BnxtOrderDetailScreen`; endpoints: `POST https://business.visma.net/api/graphql (mutation BnxtOrderSendToApproval)`; platform: `react-native` · evidence `src/screens/manager/BnxtOrderDetailScreen/BnxtOrderDetailScreen.tsx:289-295`

_Note: Only offered for purchase orders, when the user can update the order, is not editing, and no active approval task exists (BnxtOrderDetailScreen.tsx:711-720)._

### CAP-037: Cancel a purchase order

**Fusion:** unique · **Personas:** buyer · **Confidence:** High

A buyer cancels a BXN purchase order after a destructive confirmation.

- **vmm** (Manager): screens: `BnxtOrderDetailScreen`; endpoints: `POST https://business.visma.net/api/graphql (mutation BnxtOrderCancel)`; platform: `react-native` · evidence `src/screens/manager/BnxtOrderDetailScreen/BnxtOrderDetailScreen.tsx:297-314`

_Note: Shown for purchase orders when the user can update and is not editing (BnxtOrderDetailScreen.tsx:711-728). A failure shows the raw server message; success refreshes the order._

### CAP-038: Open an order attachment

**Fusion:** unique · **Personas:** BXN user · **Confidence:** High

A user opens a PDF attached to a BXN order. It is downloaded, cached locally and shown in an in-app PDF viewer.

- **vmm** (Manager): screens: `BnxtOrderDetailScreen`, `BnxtAttachmentViewerScreen`; endpoints: `POST https://business.visma.net/api/graphql (query GetBnxtOrderAttachment)`; events: `bnxt_order_attachment_opened`; storage: `file cache bnxt-order-{orderNo}-{attachmentNo}.pdf`; platform: `local file cache write (base64)`, `react-native-pdf viewer` · evidence `src/screens/manager/BnxtOrderDetailScreen/BnxtOrderDetailScreen.tsx:480-509`

_Note: Requires orderAttachment read access. Only inline blobs (fileNo 0 or null) can be opened; attachments held in the file service are labelled web-only. One attachment opens at a time._

### CAP-039: Track documents sent for approval

**Fusion:** unique · **Personas:** BXN user, order sender · **Confidence:** High

A user views the Business NXT approval board, with paginated 'In approval' and 'History' segments. They open a task to see its status, document, sender, current approver and latest comment, and can jump to the purchase order.

- **vmm** (Manager): screens: `BnxtApprovalsScreen`, `BnxtApprovalsPane`, `BnxtApprovalTaskScreen`; endpoints: `POST https://business.visma.net/api/graphql (query BnxtApprTasksActive)`, `POST https://business.visma.net/api/graphql (query BnxtApprTasksDone)`, `POST https://business.visma.net/api/graphql (query BnxtApprTaskByNo)`, `POST https://business.visma.net/api/graphql (query BnxtApprTaskLog)`; storage: `redux bnxtOrders.selectedCompanyId`; platform: `react-native` · evidence `src/screens/manager/BnxtApprovalsScreen/components/BnxtApprovalsPane/BnxtApprovalsPane.tsx:35-134; src/screens/manager/…`

**How they differ:**
- Not a divergence, a scope note: BnxtApprovalTaskScreen.tsx:252-260 also has a sender-side 'Cancel approval' button (bnxt_appr_cancel_action, cancelApprovalTask) for pending tasks. The claim does not include it, and it should be tracked as its own capability.
- The approver name is fetched only for pending tasks (BnxtApprovalTaskScreen.tsx:78). The latest comment is also read from the log rows for actions 3 and 9, so terminal (History) tasks show no comment or approver. The claim's description ('latest comment') does not state this limit.

_Note: Active means active status AND not booked. Booked leftovers are dropped client-side, and the list auto-pages past them. The count shows loaded rows, not the server total. Requires approvalTask read access. The approver is parsed from the change log (action 3 or 9 marks the holder row). Status 8 is shown in an error tone. Approving or rejecting happens in Visma.net Approval, not in this app._

### CAP-040: Withdraw a pending approval task

**Fusion:** unique · **Personas:** order sender, BXN user · **Confidence:** High

From a Business NXT approval task, the sender cancels the pending task after a confirmation.

- **vmm** (Manager): screens: `BnxtApprovalTaskScreen`; endpoints: `POST https://business.visma.net/api/graphql (mutation BnxtApprovalCancel)`; storage: `redux bnxtOrders.selectedCompanyId`; platform: `react-native` · evidence `src/screens/manager/BnxtApprovalTaskScreen/BnxtApprovalTaskScreen.tsx:39-265`

**How they differ:**
- The Employee apps' 'cancel approval flow' on expense claims (me-ios ExpenseViewController.swift:850, EditExpenseViewModel.swift:96; also appears in me-android's expense module) is a separate capability, withdrawing an expense claim from approval. It is not a twin of this Business NXT task withdrawa…

_Note: Only possible while the task is pending. A re-entry guard prevents a duplicate cancel. Server errors are shown untranslated._

### CAP-041: Browse and search archived invoices

**Fusion:** unique · **Personas:** BXN user · **Confidence:** High

A user lists the company's BXN invoices, searches by customer name or invoice number, sorts by date, number, name or amount, and opens the order an invoice came from. A Gaia assist is also available.

- **vmm** (Manager): screens: `BnxtInvoicesScreen`, `BnxtInvoicesPane`; endpoints: `POST https://business.visma.net/api/graphql (query BrowseBnxtInvoices{SortSuffi…`; storage: `redux bnxtOrders.selectedCompanyId`; platform: `react-native` · evidence `src/screens/manager/BnxtInvoicesScreen/components/BnxtInvoicesPane/BnxtInvoicesPane.tsx:43-175`

_Note: Search and sort run on the server, and the count is the server totalCount. Rows without an orderNo cannot be tapped (InvoiceListItem.tsx:44). A missing transactionType falls back to sales. Requires orderDocument read access. referee could not confirm: The file list leaves out where the network call is made: src/services/apiNXT/useApiNXTLookup.ts:448 (fetchInvoices) and the endpoint constant src/s…_

### CAP-042: See money owed by customers or to suppliers

**Fusion:** unique · **Personas:** BXN user, finance manager · **Confidence:** High

A user opens Money in or Money out to see the total outstanding, the overdue total and the overdue count, plus a paged list of customer or supplier balances to drill into.

- **vmm** (Manager): screens: `BnxtMoneyScreen`, `BnxtMoneyPane`; endpoints: `POST https://business.visma.net/api/graphql (query GetBnxtArMoneySummary)`, `POST https://business.visma.net/api/graphql (query GetBnxtApMoneySummary)`, `POST https://business.visma.net/api/graphql (query BrowseBnxtCustBalances)`, `POST https://business.visma.net/api/graphql (query BrowseBnxtSupBalances)`; storage: `redux bnxtOrders.selectedCompanyId`; platform: `react-native` · evidence `src/screens/manager/BnxtMoneyScreen/components/BnxtMoneyPane/BnxtMoneyPane.tsx:38-176`

_Note: Customer balances are sorted descending, supplier balances ascending. Overdue stats turn red when overdueCount > 0. Requires open entry and balance read access on that side._

### CAP-043: Review an associate's open ledger entries

**Fusion:** unique · **Personas:** BXN user, finance manager · **Confidence:** High

A user sees a customer's or supplier's open ledger entries, paged, with the outstanding total, and can jump to the associate card.

- **vmm** (Manager): screens: `BnxtOpenEntriesScreen`; endpoints: `POST https://business.visma.net/api/graphql (query GetBnxtCustOpenEntries)`, `POST https://business.visma.net/api/graphql (query GetBnxtSupOpenEntries)`; storage: `redux bnxtOrders.selectedCompanyId`; platform: `react-native` · evidence `src/screens/manager/BnxtOpenEntriesScreen/BnxtOpenEntriesScreen.tsx:32-164`

_Note: The outstanding amount is shown only when the caller passes it in; the screen never sums pages. Overdue is computed against today's BNXT date int. The card link requires associate read access._

### CAP-044: View a customer or supplier card

**Fusion:** unique · **Personas:** BXN user · **Confidence:** High

A user views a BXN customer's or supplier's outstanding balance, open-entry count, oldest due date, company details, contact info with tap-to-call or email, and contact persons, and can drill into open entries.

- **vmm** (Manager): screens: `BnxtAssociateCardScreen`; endpoints: `POST https://business.visma.net/api/graphql (query GetBnxtCustomerCard)`, `POST https://business.visma.net/api/graphql (query GetBnxtSupplierCard)`; storage: `redux bnxtOrders.selectedCompanyId`; platform: `Linking tel: and mailto:` · evidence `src/screens/manager/BnxtAssociateCardScreen/BnxtAssociateCardScreen.tsx:28-273`

_Note: The oldest due date is shown red when it is before today. Negative supplier balances are valid. The open-entries link requires role-specific open-entry read access. The org number is kept as a string to preserve leading zeros._

### CAP-045: Look up products, customers, suppliers and stock

**Fusion:** unique · **Personas:** Business NXT manager · **Confidence:** High

A Business NXT user searches the product, customer, supplier or inventory registers and opens an entry.

- **vmm** (Manager): screens: `BnxtRegistersScreen (SCREEN_NAME_BNXT_REGISTERS)`, `BnxtRegistersPane`, `ProductListTab`, `AssociateListTab`, `InventoryListTab`; endpoints: `POST https://business.visma.net/api/graphql (SearchBnxtProducts, BrowseBnxtProd…`; platform: `react-native` · evidence `src/screens/manager/BnxtRegistersScreen/components/BnxtRegistersPane/BnxtRegistersPane.tsx:34-107`

_Note: Each area is gated by its own table read permission (product, associate or stockBalance canRead) from useBnxtLookupAccess. Products stocked in several warehouses show a warehouse count instead of a quantity (ProductListItem.tsx:38-41). A GAiA assist band can draft a question into SCREEN_NAME_GAIA_CHAT_MODAL. referee could not confirm: The endpoint list leaves out SearchBnxtInventory (services/api…_

### CAP-046: Check a product's stock

**Fusion:** unique · **Personas:** Business NXT manager · **Confidence:** High

A Business NXT user opens a product to see its physical, available, reserved and incoming stock, and whether it is suspended.

- **vmm** (Manager): screens: `BnxtProductDetailScreen (SCREEN_NAME_BNXT_PRODUCT_DETAIL)`; endpoints: `POST https://business.visma.net/api/graphql (GetBnxtProductStock)`; platform: `react-native` · evidence `src/screens/manager/BnxtProductDetailScreen/BnxtProductDetailScreen.tsx:20-147`

_Note: The incoming row is shown only when it is non-zero._

## Financial reporting

OneStop Reporting dashboards, charts, filters and customer or tenant choice

### CAP-091: View a financial reporting dashboard for a company and period

**Fusion:** unique · **Personas:** Manager · **Confidence:** High

A manager with OneStop Reporting access picks a company, a dashboard and a reporting interval and sees each dashboard element as a card. A card shows one figure or a line or column chart. Each element loads on its own, and a failed load offers a retry.

- **vmm** (Manager): screens: `DashboardScreen (SCREEN_NAME_OSR_HOME)`, `DashboardsHeader`, `CompaniesDropdown`, `DashboardsDropdown`, `IntervalsDropdown`, `OSR Dashboard (DashboardElementListItem)`; endpoints: `GET /api/osr/context`, `GET /api/osr/context/companies?customerId={c}&&tenantId={t}`, `GET /api/osr/dashboards/intervals?companyId={id}&&customerId={c}&&tenantId={t}`, `GET /api/osr/dashboards?companyId={id}&&customerId={c}&&tenantId={t}`, `GET osr/dashboards/element?customerId&tenantId&companyId&id&from&to&category&fi…`; events: `show_osr_dashboard`, `osr_dashboard_opened`, `osr_interval_changed`, `load_osr_dashboard_element`; storage: `redux osr (persisted: selected customer/tenant/company/interval)`, `redux osr.dashboardElementsById / dashboardElementsStatusById / dashboardElemen…`; platform: `react-native` · evidence `src/screens/osr/Dashboard/DashboardScreen.tsx:50-215; src/components/osr/DashboardElement/DashboardElementListItem.tsx:…`

_Note: Rules from the fragments: the default dashboard is the one flagged isSelected, otherwise the first one (DashboardProvider.tsx:35). A card shows a single figure when data.values has one row, otherwise a chart. The element request is skipped when the customer, tenant, company or element id is missing (apiOSR.ts:161-164). No earlier capability in capability_index.json covers financial reporting._

### CAP-092: Choose the customer and tenant to report on

**Fusion:** unique · **Personas:** Manager · **Confidence:** High

A manager with OneStop Reporting access picks the customer and tenant that the dashboards report on. The choice is persisted.

- **vmm** (Manager): screens: `CustomerTenantScreen (SCREEN_NAME_OSR_CUSTOMER_TENANT_SELECT)`, `CustomersDropdown`, `TenantDropdown`; endpoints: `GET /api/osr/context`; events: `show_osr_customer_tenant`, `osr_customer_selected`, `osr_tenant_selected`; storage: `redux osr.selectedCustomerId`, `osr.selectedTenantId`; platform: `react-native` · evidence `src/screens/osr/CustomerTenantScreen/components/CustomersDropdown.tsx:55-66`

_Note: Opened from DashboardScreen.tsx:68-73._

### CAP-093: Filter a dashboard chart by category and choose which series to show

**Fusion:** unique · **Personas:** Manager · **Confidence:** High

On a dashboard card or its detail screen, the manager picks a category, which reloads the element for the selected interval. The manager also chooses which data series the chart draws.

- **vmm** (Manager): screens: `OSR Dashboard`, `OSR Dashboard Element Details`; endpoints: `GET osr/dashboards/element?customerId&tenantId&companyId&id&from&to&category&fi…`; events: `osr_detail_filter_applied`; platform: `react-native` · evidence `src/components/osr/DashboardElement/context/DashboardElementProvider.tsx:50-67`

_Note: The default category is the one that matches the first data column's systemName, otherwise the first category. All configured series are shown at first. The dropdowns are disabled while the element loads and hidden when it has no data._

### CAP-094: Examine a dashboard chart in detail

**Fusion:** unique · **Personas:** Manager · **Confidence:** High

The manager taps a dashboard card to open that element full-screen, keeping the current category and series selection. The detail screen shows a legend and lets the manager show or hide value labels.

- **vmm** (Manager): screens: `DashboardElementDetailsScreen (SCREEN_NAME_OSR_DASHBOARD_ELEMENT_DETAILS)`, `DetailedChart`; events: `show_osr_dashboard_element_details`, `osr_dashboard_element_tap`; platform: `react-native`, `screen orientation/dimensions` · evidence `src/screens/osr/DashboardElementDetails/DashboardElementDetailsScreen.tsx:60-120; src/components/osr/DashboardElement/D…`

**How they differ:**
- Refinement: the show/hide value labels toggle is only rendered when isLandscape (DashboardElementDetailsScreen.tsx:100-108; DetailedChart.tsx:186,228), so a manager in portrait cannot toggle labels.
- Refinement: when the element has a single value, the detail screen shows a subtitle and value instead of DetailedChart (DashboardElementDetailsScreen.tsx:71,94-97).
- Refinement: the detail screen includes CategoriesDropdown and SeriesDropdown (source='detail'), so the manager can change the category and series there, not only keep them (DashboardElementDetailsScreen.tsx:99,109).

_Note: Unsupported chart types show osr_chart_not_supported. The title is truncated before it is passed to the detail screen._

## People and HR

Employee directory, employee and own profiles, personal information, relatives, profile picture, birthdays, anniversaries and greetings

### CAP-122: See that an employee's birthday is coming up

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager sees a cake badge on the HRM tab, a birthday/anniversary badge on list rows and a days-until countdown on the employee profile when an employee's birthday or work anniversary is within 10 days.

- **vmm** (Manager): screens: `HRM bottom tab icon`, `HRM tab (TAB_ROUTE_NAME_HRM='HRM') employees tab`, `HrmEmployeeDetailScreen (SCREEN_NAME_HRM_EMPLOYEE_DETAIL)`; endpoints: `GET employee/companies/employees`; storage: `redux features.isForceAnniversaryEnabled` · evidence `src/components/themed/EmployeeBottomTabBadgeIcon.tsx:12-55; src/components/hrm/HrmEmployeeList/HrmEmployeeList.tsx:27-2…`

_Note: The work-anniversary badge on the tab icon is hard-coded false because of bug VMM-7758 (EmployeeBottomTabBadgeIcon.tsx:27-31), so the present and fireworks icons never show. The countdown uses getDaysUntilEmployeeBirthdayNew / getDaysUntilEmployeeWorkAnniversaryNew. referee could not confirm: src/components/hrm/HrmEmployeeList/HrmEmployeeList.tsx:27-214 does not render the birthday/anniversary ba…_

### CAP-123: Turn birthday and work-anniversary reminders on or off

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager with HRM access switches reminders for employee birthdays and work anniversaries on or off in Settings.

- **vmm** (Manager): screens: `SettingsScreen`; endpoints: `PUT /users/{userId}/settings`; events: `reminders_toggled` · evidence `src/screens/common/SettingsScreen/SettingsScreen.tsx:96-99,381-403`

_Note: Shown only when loginManager.hasAccessHRM and the user is logged in. Generating and clearing the reminders happens in useReminderSync, which is outside this area._

### CAP-124: Browse the employee directory

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** Medium

A person opens the employee directory and scrolls through the people they can see, pulls to refresh, and taps a person to open their profile. In Manager the list covers the manager's employees across companies (HRM and optionally Dottie). In Employee it is the Dottie colleague directory.

- **vmm** (Manager): screens: `HRM tab (TAB_ROUTE_NAME_HRM='HRM') employees tab`, `HrmScreen (SCREEN_NAME_HRM_SCREEN)`, `HrmEmployeeListScreen`, `HrmEmployeeDetailScreen`, `HrmDottieEmployeeDetailScreen`; endpoints: `GET employee/companies/employees`, `GET {meBaseUrl}api/v1/authorization/currentsession`, `GET {meBaseUrl}api/v2/dottie/employees?Page={page}&PageSize={DOTTIE_PAGE_SIZE}`, `GET {meBaseUrl}api/v2/dottie/employees?Page=&PageSize=&Statuses=&QuickFilter=`; events: `clicked_on_employee`, `load_employee_list_complete`, `triggered_load_employee_list`; storage: `redux hrmDialogueCollapsedGroups.employees (persisted)`, `redux features.isDottieIntegrationEnabled (persisted)`, `redux hrmEmployeeList (persisted, src/configs/reduxState.ts:115)`, `loginManager.hasAccessHRM`, `loginManager.hasAccessDialog` · evidence `src/components/hrm/HrmEmployeeList/HrmEmployeeList.tsx:27-214; src/screens/hrm/HrmEmployeeListScreen/HrmEmployeeListScr…`
- **me-ios** (Employee): screens: `EmployeeListFeature`, `EmployeeListView`, `EmployeeListNavigationFeature`, `EmployeeListNavigationView`, `EmployeeListCoordinator`; endpoints: `GET /employee/api/v2/dottie/employees`, `GET /employee/api/v2/dottie/employee/{id}/profile-image` · evidence `Modules/DottieFeature/Sources/DottieFeature/Features/EmployeeList/EmployeeListFeature.swift:63-240; Employee/Accounts/F…`
- **me-android** (Employee): screens: `EmployeesScreen`, `EmployeesKey`, `EmployeesList`; endpoints: `GET /api/v2/dottie/employees`, `GET /api/v2/dottie/employee/{id}/profile-image` · evidence `dottie/src/main/java/com/visma/employee/dottie/presentation/employees/DottieEmployeesViewModel.kt:47-259; app/src/main/…`

**How they differ:**
- Data source: vmm merges HRM employees (GET employee/companies/employees) with optional Dottie employees (HrmEmployeeList.tsx:27-214). Employee lists only Dottie employees (GET /employee/api/v2/dottie/employees, EmployeeListFeature.swift:63-240).
- Layout: vmm groups employees by company, sorted by last name, with collapsible company groups and empty companies dropped. Employee shows one flat paged list (page size 25, next page loads near the end, DottieEmployeesViewModel.kt:47-259).
- Access: vmm shows the tabs only for loginManager.hasAccessHRM / hasAccessDialog, and Dottie only when features.isDottieIntegrationEnabled (HrmScreen.tsx:32-34,78-84). Employee needs Dottie access (EmployeeListNavigationFeature.swift:22-42).
- Row target: vmm routes DOTTIE_ID_PREFIX ids to HrmDottieEmployeeDetailScreen and other ids to HrmEmployeeDetailScreen. Employee always pushes employeeDetail(source: .employee(id:)).
- Extras: vmm shows birthday/anniversary badges on rows, redirects to Terms of Service when the user must agree, and persists collapsed groups. Employee lazily loads a profile image per row once.
- Analytics: vmm fires clicked_on_employee, load_employee_list_complete and triggered_load_employee_list. The Employee fragments report no events.
- (platform parity) iOS calls /employee/api/v2/dottie/... and Android calls /api/v2/dottie/... Both look like the same API behind a different base-path split. The fragments do not confirm this.
- Data scope: vmm merges HRM employees (GET employee/companies/employees, queryEndpointsEmployees.ts:47) with Dottie employees for each session context that has MEAPI_DOTTIE_HR (useUnifiedEmployeeList.ts). Employee lists only Dottie colleagues (GetEmployees.swift resourceName /employee/api/v2/dottie/…
- Paging: vmm fetches every Dottie page up front for each company with Promise.all (queryEndpointsDottie.ts fetchAllPagesForCompany). Employee loads 25 per page and asks for the next page on scroll (EmployeeListFeature.swift:13 and didScrollToBottom; DottieEmployeesViewModel.kt EMPLOYEES_PAGE_SIZE=25…
- Grouping: vmm shows company sections (collapsible CollapsibleListHeader with the flag off; PlainSectionHeader with per-company QuickFilterRow and hideable companies with the flag on, HrmEmployeeList.tsx). Employee shows one flat list with global quick filters (fetchPossibleQuickFilters) and a name…
- Refresh: vmm has pull-to-refresh (HrmEmployeeListScreen.tsx CustomRefreshControl onRefresh=reloadList). Employee has no pull-to-refresh, only a retry action (EmployeeListFeature.swift retryTapped; DottieEmployeesViewModel.kt onRetryTapped).
- Search: vmm filters the loaded list on the client (hrmEmployeeListSearchTextChange, HrmEmployeeSearchBar or GaiaAssistBand). Employee sends a debounced search to the server (name query param in GetEmployees.swift; searchText in DottieEmployeesViewModel.kt fetchPage), and choosing a filter clears th…
- Access: vmm shows the tab when loginManager.hasAccessHRM is set, and Dottie data only with features.isDottieIntegrationEnabled (HrmScreen.tsx, useUnifiedEmployeeList.ts). iOS Employee opens the list only when hasDottieAccess is true (UserProfileCoordinator.swift:42).
- Row target: vmm opens the Dottie or HRM detail screen depending on the DOTTIE_ID_PREFIX of the id (EmployeeCardRow.tsx:75-89). Employee always opens the Dottie employee info screen (EmployeeListNavigationFeature.swift employeeDetail(source: .employee(id:)); DottieEntries.kt NavigateToEmployeeInfo).
- Extras only in vmm: birthday and anniversary badges on rows (EmployeeCardRow.tsx:104-174), a redirect to Terms of Service when the user must agree (HrmEmployeeListScreen.tsx mustAgreeTos), and analytics events clicked_on_employee, load_employee_list_complete and triggered_load_employee_list. Employ…
- Extra only in Employee: a profile image loaded lazily per row (EmployeeListFeature.swift rowAppeared -> fetchProfileImage).
- (platform parity) iOS builds its paths on /employee/api/v2/dottie/... (APIInterfaceConstants.swift:49). Android Retrofit uses relative api/v2/dottie/... (DottieServiceImpl.kt:489,497,506), which is probably the same API behind another base URL. vmm's meBaseUrl also ends in /employee/ (mswHandlersEm…

_Note: The Manager outcome (look up an employee I manage) and the Employee outcome (find a colleague) are merged because the user action and the Dottie backend are the same. They stay diverged because the data scope and layout differ. A person should confirm whether managers and employees get one directory or two views. referee could not confirm: The description says pull-to-refresh works in both produc…_

### CAP-125: Search the employee directory by name

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** High

A person types a name in the directory search bar to narrow the list.

- **vmm** (Manager): screens: `HRM tab employees tab`, `HrmEmployeeListScreen`; events: `hrm_used_search`; storage: `redux hrmEmployeeList.searchInputText / searchExpanded (slice persisted)`, `redux hrmEmployeeRecentSearches.recentSearches (not on persist whitelist)` · evidence `src/components/hrm/HrmEmployeeSearchBar/HrmEmployeeSearchBar.tsx:15-38; src/screens/hrm/HrmEmployeeListScreen/HrmEmploy…`
- **me-ios** (Employee): screens: `EmployeeListFeature`, `EmployeeListView`; endpoints: `GET /employee/api/v2/dottie/employees` · evidence `Modules/DottieFeature/Sources/DottieFeature/Features/EmployeeList/EmployeeListFeature.swift:63-240`
- **me-android** (Employee): screens: `EmployeesScreen`; endpoints: `GET /api/v2/dottie/employees` · evidence `dottie/src/main/java/com/visma/employee/dottie/presentation/employees/DottieEmployeesViewModel.kt:47-259`

**How they differ:**
- Matching: vmm fuzzy-filters locally on full name or first email with stringFuzzyIncludes (HrmEmployeeSearchBar.tsx:15-38). Employee searches on the server through the `name` query parameter (EmployeeListFeature.swift:63-240, DottieEmployeesViewModel.kt:47-259).
- Debounce: Employee debounces 500 ms and trims the input. vmm filters on each keystroke, with no debounce reported.
- Recent searches: vmm lets the user reuse or remove recent searches (redux hrmEmployeeRecentSearches). Employee has no recent searches.
- Interaction with filters: in Employee, typing a search clears the quick filters and vice versa. vmm keeps per-company quick filters separate from search, and closing the search toggle clears the text (HrmEmployeeTopBar.tsx:46-54).
- vmm offers a Gaia ask entry in the search placeholder (gaia_hrm_list_search_placeholder). Employee has no equivalent.
- Analytics: vmm fires hrm_used_search. Employee reports no events.
- Matching: vmm filters on the device over the list it has already loaded, with stringFuzzyIncludes on 'firstName lastName' or the first email, and sorts the results by last name (useQueryHookHRMEmployeeListFiltered.ts:9-22). Employee searches on the server with the `name` query parameter on GET .../…
- Debounce: Employee waits 500 ms before searching (EmployeeListFeature.swift:14, DottieEmployeesViewModel.kt:257). vmm updates redux on every change, and the filter runs in a useMemo with no debounce (HrmEmployeeSearchBar.tsx:35, useQueryHookHRMEmployeeListFiltered.ts:45-49).
- Recent searches: vmm saves the text on end-editing and lets the user remove it (HrmEmployeeSearchBar.tsx:21-36, hrmRecentSearchesReducer). This happens only in the legacy search bar, not in the Gaia assist band (HrmEmployeeListScreen.tsx:123,135). Employee has no recent searches.
- Filter interaction: in Employee, typing clears the quick filters and toggling a filter clears the search (EmployeeListFeature.swift:88-114, DottieEmployeesViewModel.kt:75-126). In vmm, closing the search toggle clears the text (HrmEmployeeTopBar.tsx:46-54), and the text filter does not touch compan…
- Gaia: vmm can show a GaiaAssistBand with the placeholder gaia_hrm_list_search_placeholder ('Search or ask about employees') in place of the legacy search bar, depending on assistStyle (HrmEmployeeListScreen.tsx:53-68,123). Employee has nothing equivalent.
- Analytics: vmm fires hrm_used_search on end-editing, and only in the legacy bar (HrmEmployeeSearchBar.tsx:21-23). The cited Employee code fires no search event.
- Trimming (platform parity): Android trims the text before searching (DottieEmployeesViewModel.kt:171). iOS sends state.searchText untrimmed (EmployeeListFeature.swift:138).
- Closing search on filter tap (platform parity): Android sets isSearchActive=false when a filter tap clears the search (DottieEmployeesViewModel.kt:99,119). iOS only empties searchText (EmployeeListFeature.swift:89,97).
- Cancelling search (platform parity): Android onSearchClosed clears the query and fetches again (DottieEmployeesViewModel.kt:59-73). iOS relies on .searchable binding the text to an empty value (EmployeeListView.swift:60-63).

_Note: referee could not confirm: The claim says Employee trims the input. Only Android does; iOS EmployeeListFeature.swift has no trim.; The claim ties recent searches and hrm_used_search to vmm in general. Both exist only in the legacy HrmEmployeeSearchBar, which the GaiaAssistBand replaces when assistStyle is not 'legacy' (HrmEmployeeListScreen.tsx:123)._

### CAP-126: Filter the employee directory with quick filters

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** High

A person taps a quick-filter chip (for example same leader, department or country) to narrow the directory, and taps it again or Show all to clear it.

- **vmm** (Manager): screens: `HRM tab employees tab (Dottie path)`; endpoints: `GET {meBaseUrl}api/v2/dottie/employees/possible-quick-filters`, `GET {meBaseUrl}api/v2/dottie/employees?Page={page}&PageSize={DOTTIE_PAGE_SIZE}&…`; events: `dottie_quick_filter_chip_selected`; storage: `redux hrmEmployeeList.quickFilterByCompany (persisted)` · evidence `src/components/hrm/QuickFilterRow/QuickFilterRow.tsx:26-65`
- **me-ios** (Employee): screens: `EmployeeListFeature`, `EmployeeListView`; endpoints: `GET /employee/api/v2/dottie/employees/possible-quick-filters`, `GET /employee/api/v2/dottie/employees` · evidence `Modules/DottieFeature/Sources/DottieFeature/Features/EmployeeList/EmployeeListFeature.swift:63-240`
- **me-android** (Employee): screens: `QuickFiltersRow`, `EmployeesScreen`; endpoints: `GET /api/v2/dottie/employees/possible-quick-filters`, `GET /api/v2/dottie/employees` · evidence `dottie/src/main/java/com/visma/employee/dottie/presentation/employees/DottieEmployeesViewModel.kt:47-259`

**How they differ:**
- Scope: vmm keeps one active filter per company (odpCompanyId), and the chip row sits under each company header (QuickFilterRow.tsx:26-65). Employee applies filters to the whole list, and Android repeats the QuickFilter parameter (DottieEmployeesViewModel.kt:47-259).
- Labels: vmm uses fixed labels for same leader, department and country (hrm_dottie_quick_filter_same_*). Employee renders the server-provided options with a Show all chip (S.EmployeeList.QuickFilter.showAll / dottie_employee_list_quick_filter_show_all).
- Search coupling: in Employee, quick filters and name search clear each other. vmm keeps them independent.
- Persistence: vmm persists filters in redux hrmEmployeeList.quickFilterByCompany. Employee does not persist filters, as far as the fragments report.
- Headers: vmm Dottie calls send the VN-CompanyId and X-Connect-Tenant-Id headers. The Employee fragments report no such headers.
- Analytics: vmm fires dottie_quick_filter_chip_selected. Employee reports no events.
- Selection model: vmm allows one active value per company (activeValue string/null, QuickFilterRow.tsx:34, reducer payload value: string/null in hrmActions.ts:212). Employee is multi-select: iOS selectedFilters is an OrderedSet toggled in EmployeeListFeature.swift:22,90, Android adds and removes fro…
- Scope: vmm shows one chip row under each company header with filter options per company (useEmployeeListSections.ts:102-112, possible-quick-filters fetched per company in queryEndpointsDottie.ts:102-121). Employee has a single filter bar for the whole list (EmployeeListView.swift:72-77, QuickFilter…
- Clearing: vmm clears a filter only by tapping the active chip again and has no Show all chip. Employee clears with tap-again or a Show all chip (S.EmployeeList.QuickFilter.showAll at EmployeeListView.swift:77; dottie_employee_list_quick_filter_show_all in QuickFiltersRow.kt).
- Labels: vmm maps same-leader, same-department and same-country to local i18n keys (hrm_dottie_quick_filter_same_*) and falls back to the server name only for other values (QuickFilterRow.tsx:14-18,46-47). It also shows an hrm_dottie_quick_filter_label caption. Employee always shows the server-provi…
- Search coupling: in Employee, choosing a filter clears the search text and typing a search clears the filters (EmployeeListFeature.swift:89,108-110; DottieEmployeesViewModel.kt onSearchQueryChanged and onFilterToggled). The vmm quick-filter action only sets the value for a company. No coupling to s…
- Persistence: correcting the claim, vmm keeps filters for the session only. persistTransforms.ts:28-37 strips quickFilterByCompany when writing state and resets it when reading. Employee keeps filters in memory only. Both lose the filter on restart, so this is not a divergence.
- Headers: vmm sends VN-CompanyId, X-Connect-Tenant-Id and X-Visma-Employee-Version: 12.0 on each call for each company (queryEndpointsDottie.ts:54-59,106-111). Employee calls go through the shared apiClient with no company-specific headers at the cited sites.
- Paging: vmm fetches every page for each company eagerly (fetchAllPagesForCompany, queryEndpointsDottie.ts:65-74) and adds a Statuses filter. Employee pages lazily with 25 per page and a 500 ms debounce (EmployeeListFeature.swift:13-14,124; DottieEmployeesViewModel.kt EMPLOYEES_PAGE_SIZE and SEARCH_…
- Analytics: vmm fires dottie_quick_filter_chip_selected (hrmEvents.ts:237, QuickFilterRow.tsx:36-37). No analytics event was found at the cited sites in me-ios or me-android.
- (platform parity) iOS clears search on every filter toggle (EmployeeListFeature.swift:89). Android clears search and also closes the search bar only when the query is non-blank (isSearchActive = false in DottieEmployeesViewModel.kt onFilterToggled). The endpoint base differs only in how it is built…

_Note: referee could not confirm: vmm storage 'redux hrmEmployeeList.quickFilterByCompany (persisted)': not persisted. persistTransforms.ts:28-37 forces it empty on write and read (session only).; vmm divergence 'fixed labels': QuickFilterRow.tsx:47 falls back to the server option.name for unmapped values, so labels are not purely fixed._

### CAP-127: Hide or show companies in the employee list

**Fusion:** unique · **Personas:** manager · **Confidence:** High

With the Dottie integration on, a manager ticks or unticks companies in the overflow menu to hide or show them. Showing a company again scrolls the list to it.

- **vmm** (Manager): screens: `HRM tab employees tab (overflow menu)`; events: `dottie_company_menu_opened`, `dottie_company_visibility_toggled`; storage: `redux hrmEmployeeList.hiddenCompanyNames (persisted)` · evidence `src/components/hrm/CompanyVisibilityMenu/CompanyVisibilityMenu.tsx:17-53`

_Note: The menu is offered only when features.isDottieIntegrationEnabled and the employees tab is active. Only companies with at least one employee are listed._

### CAP-128: View an employee's personal, address and employment details

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager opens an HRM employee and expands accordion sections to read personal details, post address and current position (employee id, position type, employment date, start/end, form, work type, work time agreement, salary type), with a Gaia ask box.

- **vmm** (Manager): screens: `HrmEmployeeDetailScreen (SCREEN_NAME_HRM_EMPLOYEE_DETAIL)`; endpoints: `GET employee/companies/employees`; events: `clicked_on_accordeon_list_item`; storage: `redux settings locale` · evidence `src/components/hrm/HrmEmployeeDetailAccordeon/HrmEmployeeDetailAccordion.tsx:44-388; src/screens/hrm/HrmEmployeeDetailS…`

**How they differ:**
- Scope note, not a fusion difference: the Personal details and Post address sections also have edit buttons that open SCREEN_NAME_HRM_EDIT_PERSONAL_DETAILS and SCREEN_NAME_HRM_EDIT_POST_ADDRESS (HrmEmployeeDetailAccordion.tsx:240-250, 311-312, 333-334). Post address also has a copy-address button (l…
- Evidence correction: the route parameter is employeeId (HrmEmployeeDetailScreen.tsx:41). It is compared against ids.id; ids.id is not itself the route parameter.

_Note: The current position is the first one with no activeEnd or an activeEnd in the future. Empty fields are hidden. The 'Balances' and 'Post address' titles are hard-coded in English. The employee is resolved from the cached all-employees list by the ids.id route parameter. Employee has no view of a colleague's HRM record; it only has the Dottie colleague profile._

### CAP-129: View a colleague's Dottie profile

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** High

A person opens a Dottie-sourced employee from the directory and reads their profile photo, name, job and organization details, contact, employment dates, manager and location, read-only.

- **vmm** (Manager): screens: `HrmDottieEmployeeDetailScreen (SCREEN_NAME_HRM_DOTTIE_EMPLOYEE_DETAIL)`; endpoints: `GET {meBaseUrl}api/v2/dottie/employee/{id}`, `GET {meBaseUrl}api/v2/dottie/employee/{id}/profile-image`; events: `dottie_employee_row_pressed`, `dottie_employee_detail_view`; platform: `authenticated image load with Bearer header` · evidence `src/components/hrm/HrmDottieEmployeeDetailAccordion/HrmDottieEmployeeDetailAccordion.tsx:26-98; src/screens/hrm/HrmDott…`
- **me-ios** (Employee): screens: `DottieEmployeeInfoFeature (source: .employee)`, `DottieEmployeeInfoView`, `EmployeeListNavigationFeature.Path.employeeDetail`; endpoints: `GET /employee/api/v2/dottie/employee/{id}`, `GET /employee/api/v2/dottie/employee/{id}/template`, `GET /employee/api/v2/dottie/employee/{id}/profile-image` · evidence `Modules/DottieFeature/Sources/DottieFeature/Features/EmployeeInfo/DottieEmployeeInfoFeature.swift:33-36,209-219,233-235`
- **me-android** (Employee): screens: `EmployeeInfoScreen`, `EmployeeInfoKey`; endpoints: `GET /api/v2/dottie/employee/{id}`, `GET /api/v2/dottie/employee/{id}/template`, `GET /api/v2/dottie/employee/{id}/profile-image`; platform: `clipboard` · evidence `dottie/src/main/java/com/visma/employee/dottie/presentation/employee_info/EmployeeInfoViewModel.kt:46-116; app/src/main…`

**How they differ:**
- Layout: vmm shows fixed, hard-coded English sections from GET {meBaseUrl}api/v2/dottie/employee/{id} (HrmDottieEmployeeDetailAccordion.tsx:26-98). Employee lays out fields from a server template (GET /employee/api/v2/dottie/employee/{id}/template, DottieEmployeeInfoFeature.swift:209-219).
- Localization: vmm section labels are not translated. Employee uses localized strings (S.Settings.PersonalInformation.employeeInformation / dottie_employee_info_title_other_user).
- Preconditions: vmm strips DOTTIE_ID_PREFIX and skips the query unless id, odpCompanyId and tenantId are present, and the avatar falls back to initials. Employee uses the plain employee id.
- Screen reuse: Employee reuses the own-profile screen in read-only mode (isReadOnly when source is .employee; Android is editable only when employeeId <= ID_ME). vmm has a separate read-only screen.
- Analytics: vmm fires dottie_employee_row_pressed and dottie_employee_detail_view. Employee reports no events.
- (platform parity) Android lets the user copy profile values to the clipboard (ClipboardCopier.kt, EmployeeInfoViewModel.kt:46-116). The iOS fragment reports no copy action.
- Layout/fields: vmm renders a fixed set of fields in three hard-coded accordions: Personal details, Manager and Post address (HrmDottieEmployeeDetailAccordion.tsx:42-95). Employee builds its fields from a server template, GET /employee/api/v2/dottie/employee/{id}/template (GetDottieEmployeeTemplateB…
- Localization: vmm labels are hard-coded English literals such as 'Job title' and 'Personal details' (HrmDottieEmployeeDetailAccordion.tsx:43-92). Employee uses localized titles: S.Settings.PersonalInformation.employeeInformation (DottieEmployeeInfoFeature.swift:43) and R.string.dottie_employee_info…
- Preconditions/scope: vmm strips DOTTIE_ID_PREFIX, needs odpCompanyId and tenantId, and skips the query otherwise (HrmDottieEmployeeDetailScreen.tsx:42-56). It sends VN-CompanyId and X-Connect-Tenant-Id headers for each company, so it can open an employee in any company (queryEndpointsDottie.ts:138-…
- Error handling: vmm shows an 'error_unknown' toast and renders nothing (HrmDottieEmployeeDetailScreen.tsx:63-67, 84). Employee shows an inline load error with a retry: loadDataError (DottieEmployeeInfoFeature.swift:113), and dottie_employee_info_load_error with onRetry (EmployeeInfoScreen.kt:102; E…
- Header content: the vmm header shows the company name passed from the directory (HrmDottieEmployeeDetailScreen.tsx:95). Employee builds its header from the profile itself (DottieProfileHeader.make / ProfileHeader.make).
- Screen reuse: Employee reuses the own-profile screen in read-only mode. On iOS, isReadOnly is true when source is .employee (DottieEmployeeInfoFeature.swift:33-36). On Android, the screen is editable only when employeeId <= ID_ME (EmployeeInfoViewModel.kt:47-48, 95). vmm has a separate read-only sc…
- Analytics: vmm fires dottie_employee_detail_view and dottie_employee_row_pressed (HrmDottieEmployeeDetailScreen.tsx:59-60; HrmDottieEmployeeDetailAccordion.tsx:65-66). No events were found in the Employee code for this flow.
- (platform parity) Android copies profile values to the clipboard through EmployeeInfoUiEvent.CopyToClipboard (DottieEntries.kt:109-113; ClipboardCopier.kt). No copy action was found in the iOS DottieFeature sources.

### CAP-130: Contact an employee by call, SMS, email or share

**Fusion:** unique · **Personas:** manager · **Confidence:** High

From the employee detail header or any phone or email field, a manager calls, texts, emails or shares the employee's contact value through the device apps.

- **vmm** (Manager): screens: `HrmEmployeeDetailScreen`; endpoints: `GET employee/companies/employees`; events: `clicked_on_phone_icon`, `clicked_on_message_icon`, `clicked_on_email_icon`, `triggered_open_contacts`, `clicked_on_share_icon`; platform: `Linking tel:/sms:/mailto:`, `native Share sheet` · evidence `src/components/hrm/HrmEmployeeDetailHead/HrmEmployeeDetailHead.tsx:125-214`

_Note: The business phone or email is preferred over the private one. Buttons are disabled when the value is missing. A canOpenURL failure shows the 'contact_is_not_available' alert. The Employee colleague profile only offers copy to clipboard (Android). referee could not confirm: notes: 'The Employee colleague profile only offers copy to clipboard (Android)' is not supported. me-android clipboard use i…_

### CAP-131: Copy an employee's post address

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager copies the employee's full post address (street, city, zip, localized country) to the clipboard.

- **vmm** (Manager): screens: `HrmEmployeeDetailScreen`; events: `clicked_on_copy_to_clipboard`; platform: `clipboard (@react-native-clipboard/clipboard)` · evidence `src/components/hrm/HrmEmployeeDetailAccordeon/HrmEmployeeDetailAccordion.tsx:252-266`

_Note: The parts are joined with ', ', empty values are skipped, and a success toast shows._

### CAP-132: Edit an employee's name, phone numbers and emails

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager taps Edit on an employee's personal details, updates first and last name, business and private phone and email, and saves them to the HR system.

- **vmm** (Manager): screens: `HrmEmployeeDetailScreen`, `HrmEditPersonalDetailsScreen (SCREEN_NAME_HRM_EDIT_PERSONAL_DETAILS)`; endpoints: `PUT employee/companies/{companyId}/employees/{employeeId}`, `GET employee/companies/{companyId}/jobs/{jobId}`; events: `hrm_employee_updated`, `hrm_employee_update_error`, `employee_updated`, `employee_update_error` · evidence `src/screens/hrm/HrmEditPersonalDetailsScreen/HrmEditPersonalDetailsScreen.tsx:147-283; src/components/hrm/HrmEmployeeDe…`

**How they differ:**
- Not a divergence, just a note: Employee (me-ios/me-android) has no manager-side edit of another employee's name, phones or emails. Its self-service contact update is a separate capability.
- Missed by the claim: when the job fails with validationResults, the hook returns validationErrors and skips the generic toast (useEmployeeUpdate.ts:119-122). HrmEditPersonalDetailsScreen.tsx:271-274 only tracks the error event and never shows those errors, so the user gets no feedback.
- Missed by the claim: the toast 'Please fix errors before saving' is hard-coded and untranslated (untranslatedMessage: true) in HrmEditPersonalDetailsScreen.tsx:198-202.
- Missed by the claim: phones are stored as integers (parseInt of digits only, HrmEditPersonalDetailsScreen.tsx:215-225), so a leading '+' or leading zeros are lost.

_Note: Names are required. Emails get a format check and phones must have 8-15 digits. Emails with isEditable=false are read-only and carry a 'linked to user' badge. The update is an async job that the app polls 5 times with 500 ms exponential backoff (useEmployeeUpdate.ts:41-74). The backend needs the payload key 'personname' in lowercase. The phone type selector title 'Add new contact' is hard-coded.…_

### CAP-133: Edit an employee's postal address

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager taps Edit on the post address section and updates street, postal code, city and country (from a searchable picker) for an employee.

- **vmm** (Manager): screens: `HrmEditPostAddressScreen (SCREEN_NAME_HRM_EDIT_POST_ADDRESS)`; endpoints: `PUT employee/companies/{companyId}/employees/{employeeId}`, `GET employee/companies/{companyId}/jobs/{jobId}`; events: `hrm_employee_updated`, `hrm_employee_update_error`, `employee_updated`, `employee_update_error` · evidence `src/screens/hrm/HrmEditPostAddressScreen/HrmEditPostAddressScreen.tsx:102-171; src/components/hrm/HrmEmployeeDetailAcco…`

**How they differ:**
- Related but separate capability, not a divergence of this one: the Employee product lets an employee edit their own address with PUT {employeeApiV2}/dottie/employee/me (me-ios Modules/DottieFeature/Sources/DottieFeature/Service/Request/PutDottieEmployee.swift:6; me-android dottie/src/main/java/com/…

_Note: Country is required. The country picker searches by name or code. Server job validation errors are mapped to fields by message substring (zipcode/street/city/country)._

### CAP-134: Add or edit an employee's child

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager sees an employee's children sorted by name. They tap Add child to register a new one (name, year of birth, sole custody), or open one to edit it from a read-only view.

- **vmm** (Manager): screens: `HrmEmployeeDetailScreen`, `HrmChildEditScreen (SCREEN_NAME_HRM_CHILD_EDIT)`; endpoints: `PUT employee/companies/{companyId}/employees/{employeeId}`, `GET employee/companies/{companyId}/jobs/{jobId}`; events: `hrm_child_updated`, `hrm_child_update_error`, `child_updated`, `child_update_error` · evidence `src/components/hrm/HrmEmployeeDetailAccordeon/ChildrenSection/ChildrenSection.tsx:27-79; src/screens/hrm/HrmChildEditSc…`

**How they differ:**
- The claim leaves out one action: the same screen also removes a child. handleRemove (HrmChildEditScreen.tsx:350-377) filters the child out of relatives, sends PUT, and fires hrm_child_removed / child_removed (hrmEvents.ts:34); the Remove button is at about line 451. Either add removal here or make…
- Not a fusion divergence, but worth knowing: the Employee product has a self-service counterpart. It calls .../EmpMan/employees/me (me-ios PostEmpManEmployee.swift:50) and sends an etag. vmm calls PUT employee/companies/{companyId}/employees/{employeeId} and then polls a job.
- In the Employee app a child has more fields: chronicallyIll, chronicallyIllFrom and chronicallyIllTo (me-ios Model/Domain/Models.swift:107-110; me-android ChronicallySickChildFieldViewModel.kt). vmm has only first name, last name, year of birth and sole custody.
- The Employee app sends a full date of birth (UserContactUIModelToUserContactMapper.employee.swift:25-36). vmm only takes a year and stores it as YYYY-01-01 (HrmChildEditScreen.tsx:290).

_Note: All three fields are required. The year must be between 1900 and the current year and is stored as YYYY-01-01. The whole relatives array is sent with PUT. The child is matched by id, then by name and birth year, because the server reassigns relative ids. The Employee app has a self-service counterpart with more child fields (chronic illness)._

### CAP-135: Remove an employee's child

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager removes a child from an employee's relatives.

- **vmm** (Manager): screens: `HrmChildEditScreen`; endpoints: `PUT employee/companies/{companyId}/employees/{employeeId}`, `GET employee/companies/{companyId}/jobs/{jobId}`; events: `hrm_child_removed`, `hrm_child_remove_error`, `child_removed`, `child_remove_error` · evidence `src/screens/hrm/HrmChildEditScreen/HrmChildEditScreen.tsx:350-380`

**How they differ:**
- No confirmation dialog: pressing 'remove' calls handleRemove straight away (vmm HrmChildEditScreen.tsx:451-456 -> 350).
- The Remove button only shows in edit mode for an existing child (the !isNewChild guard, HrmChildEditScreen.tsx:450).
- Success and failure toasts come from the shared useEmployeeUpdate hook ('hrm_employee_updated_successfully' / 'hrm_employee_update_failed', hooks/hrm/useEmployeeUpdate.ts:97-126). The claim did not list them.
- Employee product (me-ios/me-android): no child removal. Removing relatives in me-ios PersonalInformationFeature.swift:309/371 is about the employee's own emergency contacts, not a manager removing children.

_Note: The fragment found no confirmation dialog. The relatives array is sent with PUT without the child._

### CAP-136: Add or edit an employee's emergency contact

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager sees an employee's non-child relatives as emergency contacts. They add a new one or open one to edit it (name, phone, email, main contact flag), with tappable phone and email in the read-only view.

- **vmm** (Manager): screens: `HrmEmployeeDetailScreen`, `HrmEmergencyContactEditScreen (SCREEN_NAME_HRM_EMERGENCY_CONTACT_EDIT)`; endpoints: `PUT employee/companies/{companyId}/employees/{employeeId}`, `GET employee/companies/{companyId}/jobs/{jobId}`; events: `hrm_emergency_contact_updated`, `hrm_emergency_contact_update_error`, `emergency_contact_updated`, `emergency_contact_update_error` · evidence `src/components/hrm/HrmEmployeeDetailAccordeon/RelativesSection/RelativesSection.tsx:27-78; src/screens/hrm/HrmEmergency…`

**How they differ:**
- Claim omission: the vmm edit screen also removes an existing contact (HrmEmergencyContactEditScreen.tsx:332-359, 'remove' button at lines 446-456, events hrm_emergency_contact_removed / emergency_contact_removed / *_remove_error in hrmEvents.ts:89,94). The claim's name and events leave this out.
- Related, but a separate capability: me-ios PersonalInformationFeature.swift:200-245 (addContactButtonTapped / editContactCellTapped leading to ContactDetailsFeature) and me-android RelativeDetailsViewModel.kt let employees edit their own relatives. These cover all relation types, with a relation-ty…

_Note: Names are required. Emails get a format check and phones must have 8-15 digits. A new contact gets relation=Other, and contacts are relatives with relation != Child. contactIdentity is passed as a fallback when ids go stale._

### CAP-137: Remove an employee's emergency contact

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager deletes an emergency contact from an employee's record.

- **vmm** (Manager): screens: `HrmEmergencyContactEditScreen`; endpoints: `PUT employee/companies/{companyId}/employees/{employeeId}`, `GET employee/companies/{companyId}/jobs/{jobId}`; events: `hrm_emergency_contact_removed`, `hrm_emergency_contact_remove_error`, `emergency_contact_removed`, `emergency_contact_remove_error` · evidence `src/screens/hrm/HrmEmergencyContactEditScreen/HrmEmergencyContactEditScreen.tsx:332-360`

**How they differ:**
- Context only, not a fusion difference: Employee (me-ios, me-android) has its own self-service capability for removing a relative from your own record. vmm removes another employee's contact at once with PUT employees/{employeeId} plus job polling (HrmEmergencyContactEditScreen.tsx:348-358). me-ios…
- vmm removes the contact with no confirmation dialog: the Remove button calls handleRemove directly (HrmEmergencyContactEditScreen.tsx:447-452). me-android asks for confirmation first (relative_details_delete_relative_title, RelativeDetailsScreen.kt:131-139). The UX teams may want to line these up.

### CAP-138: Generate an AI birthday or work-anniversary greeting

**Fusion:** unique · **Personas:** manager · **Confidence:** High

When an employee's birthday or milestone work anniversary is within 10 days, a manager taps Create greeting on the employee profile or a celebration row on the Home HRM card. The bot writes a message in the app language, which the manager can regenerate up to a limit. If a greeting is already saved, the app opens it instead.

- **vmm** (Manager): screens: `HrmEmployeeDetailScreen`, `StartHub HRM card`, `HrmBotGenerateMessageScreen (SCREEN_NAME_BOT_GENERATE_MESSAGE)`, `HrmBotGeneratingFinishedScreen (SCREEN_NAME_BOT_GENERATING_FINISHED_SCREEN)`; endpoints: `POST hrm/anniversary`, `GET employee/companies/employees`; events: `hab_anniversary`, `hab_birthday`, `hab_generate_message`, `hab_try_again`, `hab_four_limit_reached`, `home_item_opened`; storage: `redux hrmAnniversary.birthdayMessages / anniversaryMessages (persisted, src/con…`, `redux hrmAnniversary.birthdayMessageGenerationTries / anniversaryMessageGenerat…`, `redux features.isForceAnniversaryEnabled`; platform: `may be opened from a notification (cold start on boot tab), HrmBotGenerateMessa…` · evidence `src/components/hrm/HrmEmployeeDetailHead/HrmEmployeeDetailHead.tsx:157-260; src/screens/hrm/HrmBirthdayBot/HrmBotGenera…`

_Note: MAX_RETRIES=4 per employee (HrmBotGeneratingFinishedScreen.tsx:77-82,142-165). The tone is informal, and the manager's name and locale language are sent. Back from Finished pops two screens so generation is not triggered again. On Home, birthdays come before anniversaries on the same day, and anniversary years = completed years, or +1 if upcoming. A separate Celebrations section exists but is dis…_

### CAP-139: Send a greeting to the employee by share sheet or SMS

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager edits the generated greeting and sends it through the system share sheet or an SMS pre-filled with the employee's phone number.

- **vmm** (Manager): screens: `HrmBotGeneratingFinishedScreen`; events: `hab_share`, `hab_share_sms`; storage: `redux hrmAnniversary shared birthday/anniversary (hrmSaveToSharedBirthday / hrm…`; platform: `react-native-share share sheet`, `sms: URL via Linking.openURL` · evidence `src/screens/hrm/HrmBirthdayBot/HrmBotGeneratingFinishedScreen/HrmBotGeneratingFinishedScreen.tsx:181-248`

_Note: The recipient is the first phone number and the email is the first email. was_edited is tracked. After sharing, the app returns to the employee detail._

### CAP-140: Save a greeting for later

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager stores the greeting, edited or not, against the employee and returns to their profile.

- **vmm** (Manager): screens: `HrmBotGeneratingFinishedScreen`; events: `hab_save_and_close`; storage: `redux hrmAnniversary.birthdayMessages / anniversaryMessages (persisted)` · evidence `src/screens/hrm/HrmBirthdayBot/HrmBotGeneratingFinishedScreen/HrmBotGeneratingFinishedScreen.tsx:126-140`

_Note: Stored on the device only, with no server call, so a saved greeting does not follow the manager to another device._

### CAP-141: View my personal information

**Fusion:** unique · **Personas:** employee · **Confidence:** High

An employee opens Personal Information to see their email, business and private phone, address, bank account or cash payment, tax table and tax percentage, and their emergency contacts and children. For Dottie companies, the profile menu routes to the Dottie HR profile instead.

- **me-ios** (Employee): screens: `PersonalInformationFeature`, `PersonalInformationView`, `PersonalInformationCoordinator`, `DottieEmployeeInfoCoordinator`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/EmpMan/employees/me`, `GET /employee/api/v1/employees/{odpUserId}/EmpMan/selections` · evidence `Modules/PersonalInformation/Sources/PersonalInformation/PersonalInformationFeature.swift:278-297; Employee/Accounts/Fea…`
- **me-android** (Employee): screens: `PersonalInformationScreen`, `PersonalInformationKey`, `UserInformationTopBar`; endpoints: `GET /api/v1/employees/{odpUserId}/EmpMan/employees/me`, `GET /api/v1/employees/{odpUserId}/EmpMan/selections` · evidence `app/src/main/java/com/visma/employee/about/user_information/presentation/personal_information/PersonalInformationViewMo…`

**How they differ:**
- (platform parity) Entry points: iOS opens it by a Start page push (StartPageViewController.swift:834-836) and a User profile modal (UserProfileCoordinator.swift:118-125). On Android the settings row is hard-disabled (hasPersonalInformation=false at SettingsViewModel.kt:39), so the screen is reachab…
- (platform parity) Routing: iOS sends Dottie companies from the profile menu to DottieEmployeeInfoCoordinator and everyone else to PersonalInformationCoordinator (UserProfileCoordinator.swift:41-47). No equivalent switch is reported for Android.
- (platform parity) iOS shows email and bank/tax info tooltips and tolerates a relative-type load failure (try?). Android shows a tooltip via IconWithDisappearingPopUp and a personal_information_failed_to_load error, and no tolerance rule is reported.
- (platform parity) Entry points: iOS opens it by a Start page push (StartPageViewController showPersonalInformation) and a User profile modal (UserProfileCoordinator.swift:118-125). On Android the settings row is hard-disabled (hasPersonalInformation=false, SettingsViewModel.kt:39), so the user menu…
- Correction to the claim: Dottie routing matches on both twins. iOS uses UserProfileCoordinator.swift:41-47 (hasDottieAccess -> DottieEmployeeInfoCoordinator). Android uses dottie/.../UserMenuContent.kt:143-148 (hasDottieHrPermission -> EmployeeInfoKey, ComposeBottomModalSheetDelegate.kt:94-96). Thi…
- (platform parity) Failure handling: iOS still loads if the relative-types call fails (try? in PersonalInformationFeature.swift:286). I did not confirm the same tolerance on Android. Android shows personal_information_failed_to_load (PersonalInformationScreen.kt:273).
- (platform parity) Tooltips: iOS has separate tooltips for email and for bank and taxes. Android uses IconWithDisappearingPopUp in EmailFieldViewModel.kt:43 and LabelFieldViewModel.kt:31.

_Note: The address section shows only if an address exists, and the tax section only if taxInformation exists. For cash payment the payment type text replaces the account. The tax fields are always read-only. referee could not confirm: The claim says 'No equivalent switch is reported for Android' for Dottie routing. That is wrong: legacy/me-android/dottie/src/main/java/com/visma/employee/dottie/presenta…_

### CAP-142: Update my phone numbers and home address

**Fusion:** unique · **Personas:** employee · **Confidence:** High

An employee edits their business and private phone, street, zip code and city, picks a country from a searchable list, and saves the changes to their payroll/HR record. A slow backend shows an 'update pending' or timeout dialog.

- **me-ios** (Employee): screens: `PersonalInformationFeature`, `PersonalInformationView`, `SearchList (editCountry)`; endpoints: `POST /employee/api/v1/employees/{odpUserId}/EmpMan/employees/me`; events: `personalInformationSaveChangesSuccess`, `personalInformationSaveChangesFailure`, `personalInformationSaveChangesPollingTimeout` · evidence `Modules/PersonalInformation/Sources/PersonalInformation/PersonalInformationFeature.swift:255-269`
- **me-android** (Employee): screens: `PersonalInformationScreen`, `PersonalInformationKey`, `Personal information country picker`; endpoints: `POST /api/v1/employees/{odpUserId}/EmpMan/employees/me`; events: `PersonalInformation - Save changes success`, `PersonalInformation - Save changes failed`, `PersonalInformation - Save changes polling timeout` · evidence `app/src/main/java/com/visma/employee/about/user_information/presentation/personal_information/PersonalInformationViewMo…`

**How they differ:**
- (platform parity) Country picker: iOS uses a SearchList (editCountry). Android uses a searchable bottom sheet built from Locale.getISOCountries that matches name or ISO code (CountryData.kt:13-22).
- (platform parity) Failure handling: on iOS a non-504 error shows a toast and keeps the unsaved flag, and back, swipe or modal dismiss with unsaved changes shows a discard dialog (PersonalInformationFeature.swift:255-269). Android uses UnsavedChangesHandlerImpl and SaveChangesDialogs with a personal…
- (platform parity) Phone input: iOS uses a phonePad keyboard. Android formats phones with PhoneVisualTransformation.
- (platform parity) Country picker: iOS opens SearchList (editCountry) with the current countryCode preselected (PersonalInformationFeature.swift countryButtonTapped). Android sends ShowCountrySelectionModalBottomSheet, with countries from Locale.getISOCountries and names in the 'en' locale (CountryD…
- (platform parity) Non-timeout failure: iOS shows a toast and keeps hasUnsavedChanges=true (PersonalInformationFeature.swift saveChangesResponse failure). Android sends UiEvent.ShowErrorDialog(message), a dialog rather than a toast (PersonalInformationViewModel.kt saveChanges).
- (platform parity) Where the 504 is handled: iOS maps 504 to updatePending in EmpManService.employee.swift:49-50, and closing that alert dismisses the screen. Android maps it with BACKEND_POLLING_TIME_OUT_ERROR_CODE=504 (PersonalInformationServiceImpl.kt:101) to ShowPollingTimeOutDialog. I did not v…
- (platform parity) Values sent: Android sends only fields where getValueIfVisible() returns a value, copied onto originalPersonalInformationData. iOS maps the whole UI model through userPersonalInformationUIModelToDomainMapper. So a field that Android hides could be sent differently.
- (platform parity) Phone input: the claim says iOS uses a phonePad keyboard and Android uses PhoneVisualTransformation. I did not check this line by line.

_Note: Save is enabled only when the form differs from its initial state. The POST body carries the full record with its etag, and HTTP 504 counts as a polling timeout on both platforms. Manager edits the same kind of data through a different API ('Edit an employee's postal address')._

### CAP-143: Change my salary bank account number

**Fusion:** unique · **Personas:** employee · **Confidence:** High

An employee paid by bank transfer, whose company grants the change-bank-account permission, edits their salary bank account number and saves it. Otherwise the field is read-only.

- **me-ios** (Employee): screens: `PersonalInformationView`, `BankAccountTextField`; endpoints: `POST /employee/api/v1/employees/{odpUserId}/EmpMan/employees/me`; events: `personalInformationSaveChangesSuccess`, `personalInformationSaveChangesFailure`, `personalInformationSaveChangesPollingTimeout` · evidence `Modules/PersonalInformation/Sources/PersonalInformation/UserPersonalInformationToUIModelMapper.swift:37-40`
- **me-android** (Employee): screens: `PersonalInformationScreen`; endpoints: `POST /api/v1/employees/{odpUserId}/EmpMan/employees/me`; events: `PersonalInformation - Save changes success`, `PersonalInformation - Save changes failed`, `PersonalInformation - Save changes polling timeout` · evidence `app/src/main/java/com/visma/employee/about/user_information/presentation/personal_information/PersonalInformationViewMo…`

**How they differ:**
- (platform parity) Editability: iOS requires bankAccount.canEdit from the server AND userService.hasAccessForCompany(.changeBankAccount) AND paymentType == bankPayment (PersonalInformationView.swift:110-124). Android checks hasChangeBankAccountPermissionInCurrentContext and a non-cash payment type (…
- (platform parity) Display: Android masks the bank account when the field is not focused and formats it as international or domestic (BankAccountFieldViewModel.kt, BankAccountVisualTransformation.kt). iOS uses a BankAccountTextField with a phonePad keyboard and no reported masking.
- (platform parity) Payment type gate: iOS shows the bank field only for paymentType == .bankPayment, shows a cash cell for .cashPayment, and shows nothing for any other type (PersonalInformationView.swift:112-125). Android treats every type that is not CashPayment as a bank account and shows a field…
- (platform parity) Keyboard: iOS uses .phonePad (BankAccountTextField.swift:29). Android uses KeyboardType.Text (BankAccountFieldViewModel.kt:23).
- (platform parity) Formatting: iOS formats as IBAN or local Norwegian through BankAccountNumber (UserPersonalInformationToUIModelMapper.swift:36). Android formats as international or domestic through BankAccountVisualTransformation and strips spaces before saving (BankAccountFieldViewModel.kt:34-37)…
- Correction to the claim: Android does check the server's canEdit flag (PersonalInformationFieldMapper.kt:88: bankAccount?.canEdit == true && hasChangeBankAccountPermission). The permission-plus-canEdit rule is therefore the same on both twins.

_Note: referee could not confirm: me-android UserInfoEntries.kt:17-69 is cited in the divergence line, but no file of that name exists in legacy/me-android. The real editability logic is in presentation/util/mapper/PersonalInformationFieldMapper.kt:76-92.; The divergence line saying 'No server canEdit check is reported for Android' is wrong. PersonalInformationFieldMapper.kt:88 checks bankAccount?.canEd…_

### CAP-144: Add an emergency contact or child

**Fusion:** shared-diverged · **Personas:** employee · **Confidence:** High

An employee adds a relative (partner, contact person or child) with name, email, phone and main-contact flag. For children they also enter date of birth, sole custody and a chronic illness period. The relative is saved to their employee record straight away.

- **me-ios** (Employee): screens: `ContactDetailsFeature`, `ContactDetailsView`, `PersonalInformationView (addContact sheet)`; endpoints: `POST /employee/api/v1/employees/{odpUserId}/EmpMan/employees/me`, `GET /employee/api/v1/employees/{odpUserId}/EmpMan/selections`; events: `personalInformationSaveChangesSuccess`, `personalInformationSaveChangesFailure`, `personalInformationSaveChangesPollingTimeout` · evidence `Modules/PersonalInformation/Sources/PersonalInformation/ContactDetails/ContactDetailsFeature.swift:133-155`
- **me-android** (Employee): screens: `RelativeDetailsScreen`, `RelativeDetailsKey`; endpoints: `POST /api/v1/employees/{odpUserId}/EmpMan/employees/me`, `GET /api/v1/employees/{odpUserId}/EmpMan/selections`; events: `PersonalInformation - Save changes success`, `PersonalInformation - Save changes failed`, `PersonalInformation - Save changes polling timeout` · evidence `app/src/main/java/com/visma/employee/about/user_information/presentation/relative_details/RelativeDetailsViewModel.kt:1…`

**How they differ:**
- (platform parity) Defaults: iOS starts a new contact as type partner with dates = now (ContactDetailsFeature.swift:133-155). Android reports no default type; the type is picked in a dialog (relative_details_relative_type_selection_dialog_title).
- Not unique: the Manager app (vmm) also adds relatives. HrmEmergencyContactEditScreen.tsx:277-288 adds a contact and HrmChildEditScreen.tsx:297-309 adds a child to employee.relatives[]. The Employee app does the same on iOS (ContactDetailsFeature.swift:133-138) and Android (RelativeDetailsViewModel.…
- Persona and scope: in vmm a manager edits another employee's record (employeeId and companyId come from the route, HrmEmergencyContactEditScreen.tsx:59-65). In the Employee app the employee edits their own record (EmpMan/employees/me).
- Endpoint: vmm sends PUT employee/companies/{companyId}/employees/{employeeId} and then polls GET employee/companies/{companyId}/jobs/{jobId} (queryEndpointsEmployees.ts:99-113, useEmployeeUpdate.ts:104-111). The Employee app sends POST /employee/api/v1/employees/{odpUserId}/EmpMan/employees/me (Pos…
- Relative type: vmm hard-codes the relation, RELATIVE_RELATION_OTHER for a contact and RELATIVE_RELATION_CHILD for a child, and has two separate screens. The Employee app lets the user pick a type from the EmpMan selections list on one screen (RelativeDetailsViewModel.kt:233-241, ContactDetailsFeatu…
- Child date of birth: vmm asks only for a required year of birth and saves it as YYYY-01-01 (HrmChildEditScreen.tsx:116-118, 290). The Employee app asks for a full date of birth.
- Chronic illness: vmm's child form has no chronically-ill flag and no from/to dates, and sets isMainContact to false (HrmChildEditScreen.tsx:299-307). The Employee app has chronicallyIll with From/To dates (RelativeDetailsViewModel.kt:175-180).
- Validation: vmm requires first and last name, checks the email format and requires phone numbers to have 8-15 digits (HrmEmergencyContactEditScreen.tsx:198-215). The claim reports no such validation in the Employee app. On iOS the contact saves without field checks (ContactDetailsFeature.swift:133-…
- (platform parity) Defaults: when iOS adds a new contact it starts with type .partner and sets dateOfBirth, chronicallyIllFrom and chronicallyIllTo to now (PersonalInformationFeature.swift:200-214, not the cited ContactDetailsFeature.swift:133-155). On Android a new relative starts as Relative() wit…

_Note: Relative types come from the EmpMan selections. Child types hide email and show date of birth, sole custody and chronically ill (with from/to dates when on). The relative is appended to relatives[] and the whole record is POSTed, then the screen reloads. A 504 shows the pending alert and then reloads. referee could not confirm: me-ios ContactDetailsFeature.swift:133-155 is cited for the partner/n…_

### CAP-145: Edit an emergency contact or child

**Fusion:** shared-diverged · **Personas:** employee · **Confidence:** High

An employee opens an existing relative, changes its details and saves them to their employee record.

- **me-ios** (Employee): screens: `ContactDetailsFeature`, `ContactDetailsView`, `PersonalInformationView (editContact sheet)`; endpoints: `POST /employee/api/v1/employees/{odpUserId}/EmpMan/employees/me`; events: `personalInformationSaveChangesSuccess`, `personalInformationSaveChangesFailure`, `personalInformationSaveChangesPollingTimeout` · evidence `Modules/PersonalInformation/Sources/PersonalInformation/PersonalInformationFeature.swift:235-246`
- **me-android** (Employee): screens: `RelativeDetailsScreen`, `RelativeDetailsKey`; endpoints: `POST /api/v1/employees/{odpUserId}/EmpMan/employees/me`; events: `PersonalInformation - Save changes success`, `PersonalInformation - Save changes failed`, `PersonalInformation - Save changes polling timeout` · evidence `app/src/main/java/com/visma/employee/about/user_information/presentation/relative_details/RelativeDetailsViewModel.kt:1…`

**How they differ:**
- (platform parity) iOS enables Save only when something changed, and cancel with changes shows a discard confirmation (PersonalInformationFeature.swift:235-246). The Android fragment reports only that a relative save forces a reload (UserInfoEntries.kt:17-69); discard handling on the relative screen…
- Persona and target differ: me-ios and me-android edit the signed-in employee's own record (EmpMan/employees/me, PostEmpManEmployee.swift:50). vmm lets a manager edit a chosen employee's relatives (route param employeeId, useCurrentEmployee(employeeId), HrmEmergencyContactEditScreen.tsx:58-64; the e…
- Endpoint differs: Employee uses POST /employee/api/v1/employees/{odpUserId}/EmpMan/employees/me (me-ios PostEmpManEmployee.swift:50, me-android PersonalInformationServiceImpl.kt:110). vmm uses PUT employee/companies/{companyId}/employees/{employeeId} with a partial body {relatives} and then polls G…
- Screens differ: vmm has separate screens for emergency contacts and children (HrmEmergencyContactEditScreen, HrmChildEditScreen), and the contact screen opens read-only with an edit mode (isEditMode). Employee uses one relative-details form with a relative-type picker (ContactDetailsView / Relative…
- Fields differ: the vmm emergency-contact form has only firstName, lastName, phone, email and isMainContact (HrmEmergencyContactEditScreen.tsx:280-305). The Employee form also has relative type, date of birth, sole custody, and chronically ill with from/to dates (RelativeDetailsViewModel.kt:160-185).
- Validation differs: vmm makes first and last name required, validates email, and requires 8-15 digits for phone, with a 'Please fix errors before saving' toast (HrmEmergencyContactEditScreen.tsx:197-240). The cited Employee save paths do no such client-side validation before they post.
- Stale-id handling differs: vmm falls back to matching contactIdentity (first and last name) because the server reassigns relative ids, and it shows hrm_relative_no_longer_exists (HrmEmergencyContactEditScreen.tsx:70-86, 236-241). In Employee, iOS silently returns .none if the id is missing (Contact…
- Pending-update and error handling differ: iOS shows an 'update pending' alert on .updatePending and a toast on API errors (ContactDetailsFeature.swift:160-175). Android shows a polling-timeout dialog and an error dialog (RelativeDetailsViewModel.kt:194-198). vmm shows a toast and tracks hrm_emergen…
- Analytics differ: Employee logs personalInformationSaveChanges{Success,Failure,PollingTimeout} (me-ios Events.swift:167-169, me-android PersonalInformationEventHandlerImpl.kt:11). vmm logs hrm_emergency_contact_updated / hrm_emergency_contact_update_error and HRM_EVENTS.EMERGENCY_CONTACT_UPDATED.
- Correction to the claim (platform parity): Android does enable Save only when something changed (RelativeDetailsScreen.kt:155 enabled = hasUnsavedChanges) and does ask before discarding changes on back (RelativeDetailsScreen.kt:94-106, UnsavedChangesConfirmationDialog). This matches iOS (PersonalIn…
- (platform parity) Android seeds the relative screen from the parent screen's unsaved edits (getPersonalInformationDataWithCurrentUserChangedFieldValues, UserInfoEntries.kt:43-45) and forces a reload after saving. iOS seeds the edit sheet from the loaded state.userInfo (PersonalInformationFeature.sw…

_Note: Both platforms replace the relative by id in the full record before they POST it (ContactDetailsFeature.swift:139-142). referee could not confirm: The claim says fusion is 'unique', but vmm/src/screens/hrm/HrmEmergencyContactEditScreen/HrmEmergencyContactEditScreen.tsx and vmm/src/screens/hrm/HrmChildEditScreen/HrmChildEditScreen.tsx implement the same outcome for the Manager product.; The claime…_

### CAP-146: Remove an emergency contact or child

**Fusion:** shared-diverged · **Personas:** employee · **Confidence:** High

An employee deletes a relative from their personal information.

- **me-ios** (Employee): screens: `PersonalInformationView`, `ContactDetailsView`; endpoints: `POST /employee/api/v1/employees/{odpUserId}/EmpMan/employees/me`; events: `personalInformationSaveChangesSuccess`, `personalInformationSaveChangesFailure` · evidence `Modules/PersonalInformation/Sources/PersonalInformation/PersonalInformationFeature.swift:308-313`
- **me-android** (Employee): screens: `RelativeDetailsScreen`; endpoints: `POST /api/v1/employees/{odpUserId}/EmpMan/employees/me`; events: `PersonalInformation - Save changes success`, `PersonalInformation - Save changes failed`, `PersonalInformation - Save changes polling timeout` · evidence `app/src/main/java/com/visma/employee/about/user_information/presentation/relative_details/RelativeDetailsViewModel.kt:1…`

**How they differ:**
- (platform parity) Persistence: on iOS, swipe or Delete removes the relative only locally and marks the form unsaved; the removal is saved only through the main Save changes button (PersonalInformationFeature.swift:308-313,370-374). On Android, delete filters the relative by id and POSTs the full re…
- (platform parity) Confirmation: Android asks for confirmation before deleting (relative_details_delete_relative_title / _body). No delete confirmation is reported for iOS.
- Actor and data subject: in Employee (me-ios/me-android) the employee removes a relative from their own record (EmpMan/employees/me). In Manager (vmm) a manager removes a relative from another employee's record, chosen by the employeeId route param (HrmEmergencyContactEditScreen.tsx:59-65).
- Endpoint: Employee sends POST api/v1/employees/{odpUserId}/EmpMan/employees/me (PersonalInformationServiceImpl.kt:110; iOS resource /employee/api/v1/employees/{id}/EmpMan/employees/me, GetEmpManEmployeeTests.swift:16). Manager sends PUT employee/companies/{companyId}/employees/{employeeId} and poll…
- Relative types: Manager has two separate screens, one for emergency contacts and one for children (HrmEmergencyContactEditScreen, HrmChildEditScreen). Employee uses one relative/contact details screen for all relative types.
- Missing relative: Manager shows the toast 'hrm_relative_no_longer_exists' and tracks a remove_error event when the relative is gone (HrmEmergencyContactEditScreen.tsx:337-342). Neither Employee twin has this guard in the cited code.
- Analytics: Manager tracks hrm_emergency_contact_removed / hrm_child_removed (plus the HRM_EVENTS equivalents). Employee has no event specific to removal; it reuses the PersonalInformation save success/failure events.
- (platform parity) Persistence: on iOS a delete only changes local state and marks the form unsaved; it is saved only through Save changes (PersonalInformationFeature.swift:308-313,370-374). On Android the full record is POSTed as soon as the delete is confirmed (RelativeDetailsViewModel.kt:210-230).
- (platform parity) Confirmation: Android shows a delete confirmation dialog (relative_details_delete_relative_title/_body, RelativeDetailsScreen.kt:131-135). On iOS, deleteButtonTapped goes straight to the delegate with no confirmation (ContactDetailsFeature.swift:127-128), and swipe-to-delete has n…

_Note: referee could not confirm: Evidence range RelativeDetailsViewModel.kt:147-240 mostly covers saveChanges (add/edit). The delete code is delete() and onConfirmDelete() at about lines 206-230._

### CAP-147: View and update my HR profile

**Fusion:** unique · **Personas:** employee · **Confidence:** High

An employee in a Dottie company opens their own HR profile, a server-template-driven form (names, contacts, addresses, bank accounts, children, next of kin and more). They edit the allowed fields and save.

- **me-ios** (Employee): screens: `DottieEmployeeInfoFeature (source: .currentUser)`, `DottieEmployeeInfoView`, `DottieEmployeeInfoCoordinator`; endpoints: `GET /employee/api/v2/dottie/employee/me`, `GET /employee/api/v2/dottie/employee/me/template`, `PUT /employee/api/v2/dottie/employee/me`; storage: `DottieProfileCacheStore (in-memory, key userId_tenantId, name refreshed)`; platform: `modal sheet presented from Start page and User profile (StartPageViewController…` · evidence `Modules/DottieFeature/Sources/DottieFeature/Features/EmployeeInfo/DottieEmployeeInfoFeature.swift:87-158,193-208,242-251`
- **me-android** (Employee): screens: `EmployeeInfoScreen`, `DottieFieldEditSheet`, `CountryPickerSheet`, `DottieSheetContainer`; endpoints: `GET /api/v2/dottie/employee/me`, `GET /api/v2/dottie/employee/me/template`, `PUT /api/v2/dottie/employee/me`, `GET /api/v2/dottie/employee/job-titles`; platform: `clipboard`, `back handler discard prompt` · evidence `dottie/src/main/java/com/visma/employee/dottie/presentation/employee_info/EmployeeInfoViewModel.kt:120-176; app/src/mai…`

**How they differ:**
- (platform parity) Android also calls GET /api/v2/dottie/employee/job-titles (DottieEntries.kt:80-157). It supports repeatable groups edited in a bottom sheet, redacted fields that can be revealed, normalized bank segments and clipboard copy (EmployeeInfoViewModel.kt:120-176). The iOS fragment repor…
- (platform parity) iOS presents the profile as a modal sheet from the Start page and User profile (StartPageViewController.swift:842, UserProfileCoordinator.swift:144) and keeps an in-memory DottieProfileCacheStore (key userId_tenantId). Android opens it as EmployeeInfoScreen in navigation with a ba…
- (platform parity) On iOS, saving is blocked when fields are invalid: saveChangesButtonTapped runs DynamicFormFieldUtils.updateFieldsValidity and returns early if there are errors (DottieEmployeeInfoFeature.swift:132-139). On Android, saveChanges() never checks the main form. It sets onChangeValidat…
- (platform parity) Android fetches job titles through fetchJobTitles (GET api/v2/dottie/employee/job-titles, DottieServiceImpl.kt:271-284,540). iOS has no job-titles request (Service/Request has none).
- (platform parity) Android adds repeatable groups edited in a bottom sheet (DottieBottomSheetReducer.kt, DottieRepeatableBottomSheetTriggerRows.kt), redacted fields (DottieRedactedField.kt) and copy to clipboard (DottieEntries.kt, CopyToClipboard event). I found none of these in the iOS EmployeeInfo…
- (platform parity) iOS shows the profile as a modal sheet from the Start page and User profile (StartPageViewController.swift:843, UserProfileCoordinator.swift:146) and keeps an in-memory DottieProfileCacheStore (Repository/Cache/DottieProfileCacheStore.swift). Android pushes EmployeeInfoKey onto th…
- Missed by the claim: both platforms let the user change their profile photo from this screen. iOS uses ProfileImageSheetFeature with CircularCrop and ImagePicker (Sheets/ProfileImageSheet, DottieEmployeeInfoFeature.swift:172-194). Android uses CropProfileImageKey/CircularCropScreen with POST/DELETE…
- Missed by the claim: the same feature on both platforms also opens another employee's profile read-only. iOS uses Source.employee(id) with isReadOnly (DottieEmployeeInfoFeature.swift:12-48, EmployeeListNavigationFeature.swift:31). Android uses the employeeId arg with an isMe guard (EmployeeInfoView…

_Note: On both platforms, validation runs on save and then live after the first failed save. Leaving with unsaved changes asks the user to discard. The update request is built from the changed fields merged with the original record. This overlaps in data with 'View my personal information' (EmpMan) but uses the Dottie API. Which one a user sees depends on whether their company uses Dottie. referee could…_

### CAP-148: Change or remove my profile picture

**Fusion:** unique · **Personas:** employee · **Confidence:** High

An employee takes a photo or picks one from the library, crops it to a circle and uploads it as their HR profile picture, or deletes the current picture after confirming.

- **me-ios** (Employee): screens: `ProfileImageSheetFeature`, `ProfileImageSheetView`, `ImagePickerFeature`, `ImagePickerView`, `CircularCropFeature`, `CircularCropView`; endpoints: `GET /employee/api/v2/dottie/employee/me/profile-image`, `POST /employee/api/v2/dottie/employee/me/profile-image`, `DELETE /employee/api/v2/dottie/employee/me/profile-image`; storage: `@Shared inMemory key dottieCurrentUserProfileImage`, `DottieProfileCacheStore (in-memory actor, key userId_tenantId)`; platform: `camera (UIImagePickerController .camera)`, `photo library` · evidence `Modules/DottieFeature/Sources/DottieFeature/Features/EmployeeInfo/Sheets/ProfileImageSheet/ProfileImageSheetFeature.swi…`
- **me-android** (Employee): screens: `ProfileImageBottomSheet`, `CircularCropScreen`, `CropProfileImageKey`, `EmployeeInfoScreen`; endpoints: `GET /api/v2/dottie/employee/me/profile-image`, `POST /api/v2/dottie/employee/me/profile-image`, `DELETE /api/v2/dottie/employee/me/profile-image`; storage: `DottieProfileCacheStore (in-memory, keyed by user name + tenant)`, `DottieCurrentProfileImageHolder`, `FileProvider temp file for the camera capture`, `Dottie profile cache (image per tenant key) via DottieProfileRepositoryImpl`; platform: `camera (ActivityResultContracts.TakePicture, runtime CAMERA permission)`, `photo picker (PickVisualMedia ImageOnly)`, `FileProvider` · evidence `dottie/src/main/java/com/visma/employee/dottie/presentation/image/ProfileImageViewModel.kt:25-51; dottie/src/main/java/…`

**How they differ:**
- (platform parity) Upload format: iOS uploads a multipart JPEG at quality 0.85 named {uuid}.jpg (ProfileImageSheetFeature.swift:59-134). Android renders an 800x800 JPEG at quality 85 in multipart field 'Image' with file name 'profile-image' (CropProfileImageViewModel.kt:21-59).
- (platform parity) Camera: Android asks for the CAMERA permission at runtime and uses a FileProvider temp file (ProfileImageViewModel.kt:25-51). iOS uses UIImagePickerController .camera. The fragment reports no permission handling for iOS.
- (platform parity) iOS treats the profile cache as stale after 15 min and shares the image through @Shared inMemory dottieCurrentUserProfileImage so the Start page and User profile avatars refresh. Android updates DottieProfileCacheStore and DottieCurrentProfileImageHolder and shows an error snackba…
- (platform parity) Upload file: iOS sends a JPEG at quality 0.85 named {uuid}.jpg (CircularCropFeature.swift:62-69). Android renders an 800x800 JPEG (CropGeometry.kt:14, CropRenderer.kt:39) named 'profile-image' (DottieServiceImpl.kt:465). Both use the multipart field 'Image' (PostMyProfileImage.swi…
- (platform parity) Camera permission: Android checks for the CAMERA permission and requests it at runtime, and uses a FileProvider temp file (rememberImagePickerLaunchers.kt:40-45, 118). iOS goes straight to ImagePickerFeature with source .camera (ProfileImageSheetFeature.swift takePhotoTapped).
- (platform parity) Cache: iOS treats the cache as stale after 15 minutes (DottieEmployeeRepository.Live.swift:7 staleThreshold = 15*60) and shares the image in memory. Android updates DottieProfileCacheStore and DottieCurrentProfileImageHolder, and shows an error flag (errorMessageShown) when an upl…
- (platform parity) Crop upload failure: when the upload from the crop screen fails, Android closes the crop screen and passes back null, with no error shown there (CropProfileImageViewModel.kt:53-56). iOS shows a toast with profileImageInvalid when the JPEG cannot be encoded (CircularCropFeature.swi…

_Note: Own profile only. vmm has only a developer prototype that picks and crops an image without saving it (see 'Pick and crop a profile picture (prototype)'). It is not the same outcome, so it is kept apart. referee could not confirm: The iOS upload format (quality 0.85, {uuid}.jpg) is cited at ProfileImageSheetFeature.swift:59-134, but it is actually in CircularCropFeature.swift:45-69.; The Android c…_

### CAP-149: Pick and crop a profile picture (prototype)

**Fusion:** unique · **Personas:** developer · **Confidence:** Low

A prototype reachable only from developer tools lets a person choose a gallery photo cropped to a circle. The image is not saved or uploaded.

- **vmm** (Manager): screens: `ProfilePictureScreen (SCREEN_NAME_PROFILE_PICTURE = 'ProfilePictureScreen')`; platform: `photo library (react-native-image-crop-picker)` · evidence `src/screens/common/ProfilePictureScreen/ProfilePictureScreen.tsx:6-36`

**How they differ:**
- Reachable only behind dev-tools access (useDevToolsAccess plus a tap counter, vmm SettingsScreen.tsx:91,136-158), so end users never see it
- The picked image is held only in component state (ProfilePictureScreen.tsx:7,20): nothing persists or uploads it, unlike Employee's 'Change or remove my profile picture'

_Note: Crops to a 400x400 JPG at quality 0.8, with hard-coded English strings. Reachable only from dev tools (SettingsDevToolsScreen.tsx:516-520). This is not an end-user capability. It is likely dropped or replaced by Employee's 'Change or remove my profile picture'; a person decides._

## Documents and benefits

Company and personal documents, read confirmation and employee benefits

### CAP-232: Browse and search company documents

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

An employee with Dottie access opens Documents and benefits from the profile menu and sees the organization's shared documents grouped by category, with read/unread status, new badge and must-read/should-read tags, and filters them with a case-insensitive search on name or description.

- **me-ios** (Employee): screens: `DocumentsAndBenefitsFeature`, `DocumentsAndBenefitsView (Common tab)`, `DocumentsAndBenefitsCoordinator`, `DocumentsAndBenefitsNavigationView`; endpoints: `GET /employee/api/v2/dottie/documents/organization`; events: `Documents and Benefits opened`, `Documents and Benefits retry tapped`, `Documents and Benefits common tab tapped`, `Documents and Benefits search query changed, length: {n}` · evidence `Modules/DottieFeature/Sources/DottieFeature/Features/DocumentsAndBenefits/DocumentsAndBenefitsFeature.swift:26-37,115-1…`
- **me-android** (Employee): screens: `DocumentsAndBenefitsScreen`, `DocumentsAndBenefitsKey`, `CommonDocumentsTab`; endpoints: `GET /api/v2/dottie/documents/organization` · evidence `dottie/src/main/java/com/visma/employee/dottie/presentation/documents_and_benefits/DocumentsAndBenefitsViewModel.kt:83-…`

**How they differ:**
- (platform parity) me-ios sends analytics events ('Documents and Benefits opened', 'common tab tapped', 'search query changed, length: {n}', 'retry tapped'); me-android reports no events for this screen.
- (platform parity) Endpoint path reported as /employee/api/v2/dottie/documents/organization on me-ios vs /api/v2/dottie/documents/organization on me-android (likely base-URL difference, to verify).
- (platform parity) me-ios clears the search when the tab changes and loads all three lists in parallel on first appear (DocumentsAndBenefitsFeature.swift:115-125); me-android fragment does not report these rules.
- (platform parity) me-ios logs 'Documents and Benefits opened', 'retry tapped', 'common tab tapped' and 'search query changed, length: n' (AnalyticsFeature.swift:10-22). me-android has no analytics on this screen; it only logs QUICK_SELECTION_DOCUMENTS_AND_BENEFITS when the entry button is tapped (H…
- (platform parity) The paths differ only in prefix: me-ios uses APIConstants.URL.employeeApiV2 + '/dottie/documents/organization' (GetOrganizationDocuments.swift) and me-android uses @GET("api/v2/dottie/documents/organization") (DottieServiceImpl.kt:474). This looks like a base-URL difference on the…
- (platform parity) Both twins clear the search on tab change and load the three lists in parallel (iOS DocumentsAndBenefitsFeature.swift:122-125,280-305; Android DocumentsAndBenefitsViewModel.kt:66-69,218-222). The claim says Android does not report this, but it does. The difference is that me-andro…
- (platform parity) me-android also shows a Documents and benefits quick-selection button on the Dottie home, enabled only when the network is available (HomeButtonsProvider.kt:84-95, RootNavDisplay.kt:538), next to the menu entry (ComposeBottomModalSheetDelegate.kt:100). On me-ios the only cited ent…

_Note: Entry point is the profile/user menu on both platforms and requires the Dottie company feature (DocumentsAndBenefitsCoordinator.swift:19-36). referee could not confirm: me-android DocumentsAndBenefitsViewModel.kt:83-125 covers tapping a document, external links and arming mark-as-read, not browsing or searching. Loading is at :218-276 and the case-insensitive filter at :362-393.; The notes cite D…_

### CAP-233: Open a company document

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

An employee opens an organization document, either downloading the file and previewing it or opening its external link in the app, optionally from the document's description/details sheet.

- **me-ios** (Employee): screens: `DocumentsAndBenefitsView`, `DocumentDescriptionFeature`, `DocumentDescriptionView`; endpoints: `GET /employee/api/v2/dottie/documents/organization/{id}/download`; events: `Documents and Benefits document link opened`; storage: `temporary files via CoreUtils.saveTemporaryDataToFileSystem`; platform: `Quick Look preview`, `in-app browser (openURLInApp)`, `temporary file storage` · evidence `Modules/DottieFeature/Sources/DottieFeature/Features/DocumentsAndBenefits/DocumentsAndBenefitsFeature.swift:131-170,189…`
- **me-android** (Employee): screens: `DocumentsAndBenefitsScreen`, `CommonDocumentsTab`; endpoints: `GET /api/v2/dottie/documents/organization/{id}/download`; storage: `cacheDir downloaded files (cleared when the screen first loads, deleted after p…`; platform: `file download to cache dir`, `external link / file viewer intent`, `open external URL`, `open downloaded file` · evidence `dottie/src/main/java/com/visma/employee/dottie/presentation/documents_and_benefits/DocumentsAndBenefitsViewModel.kt:83-…`

**How they differ:**
- (platform parity) me-ios previews downloaded files in Quick Look and links in an in-app browser (openURLInApp); me-android opens files via a viewer intent / in-app preview and links as external URLs (DottieEntries.kt:159-192).
- (platform parity) me-ios deletes the temp file when the preview closes and cancels an in-flight download on a new one (DocumentsAndBenefitsFeature.swift:131-170); me-android clears the cache dir when the screen first loads and deletes after preview, and sanitizes file names cut to 100 characters (D…
- (platform parity) me-android tapping a card shows details only if there is a description or no action, otherwise opens directly; me-ios opens 'optionally from its description sheet' without a reported rule.
- (platform parity) me-ios logs 'Documents and Benefits document link opened'; me-android reports no event.
- (platform parity) me-ios shows downloaded files in Quick Look and opens external links in an in-app browser (DocumentsAndBenefitsView.swift:59-62). me-android sends OpenExternalLink and OpenDownloadedFile to host callbacks, which open the link or file in a viewer outside the screen (DottieEntries.k…
- (platform parity) Card tap: on me-ios, a non-empty description opens the description sheet; otherwise the tap downloads the file or opens the link (DocumentsAndBenefitsView.swift:140-149). On me-android, the details sheet opens when there is a description OR when the document has no action (no link…
- (platform parity) Temporary files: me-ios deletes the previous temp file when a new download succeeds, deletes the current one when the preview closes, and cancels an in-flight download when a new one starts (DocumentsAndBenefitsFeature.swift:192-201, 203-211, 321-331). me-android deletes the downl…
- (platform parity) Mark-as-read after opening: me-ios offers the mark-as-read confirmation after the preview or external URL closes (Feature.swift:203-215). me-android arms mark-as-read before launching an external link and clears it if the launch fails (ViewModel.kt:83-100). Both then show a confir…
- (platform parity) me-ios logs the analytics event 'Documents and Benefits document link opened' (AnalyticsFeature.swift:24). No matching event was found on me-android.

_Note: referee could not confirm: me-android: I could not confirm the claim that file names are cut to 100 characters. I found no take(100) or sanitize call in dottie/src/main/java, and DocumentsAndBenefitsViewModel.kt:83-125 does not do it.; me-ios: the claim says the card-tap rule was 'not reported', but DocumentsAndBenefitsView.swift:140-149 does have one._

### CAP-234: Confirm reading a required company document

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

After closing a must-read or should-read company document that is not yet read, the employee is asked to mark it as read; on confirm it is flagged read on the server and in the list, 'Maybe later' dismisses without calling the API.

- **me-ios** (Employee): screens: `MarkAsReadConfirmationFeature`, `MarkAsReadConfirmationView`; endpoints: `POST /employee/api/v2/dottie/documents/organization/{id}/mark-as-read` · evidence `Modules/DottieFeature/Sources/DottieFeature/Features/DocumentsAndBenefits/DocumentsAndBenefitsFeature.swift:207-242,307…`
- **me-android** (Employee): screens: `MarkAsReadConfirmationSheet`, `DocumentsAndBenefitsScreen`; endpoints: `POST /api/v2/dottie/documents/organization/{id}/mark-as-read` · evidence `dottie/src/main/java/com/visma/employee/dottie/presentation/documents_and_benefits/DocumentsAndBenefitsViewModel.kt:157…`

**How they differ:**
- (platform parity) Endpoint path /employee/api/v2/... on me-ios vs /api/v2/... on me-android (likely base-URL difference, to verify).
- (platform parity) me-android rebuilds the badges locally with isRead=true on success (DocumentsAndBenefitsViewModel.kt:157-216); me-ios flags the item read in the list (DocumentsAndBenefitsFeature.swift:307-319) - same outcome, implementation detail only.
- (platform parity) Endpoint path: me-ios uses /employee/api/v2/dottie/documents/organization/{id}/mark-as-read (APIInterfaceConstants.swift:49, employeeApiV2 = "/employee/api/v2"); me-android uses the relative Retrofit path api/v2/dottie/documents/organization/{id}/mark-as-read (DottieServiceImpl.kt…
- (platform parity) Sheet content: me-ios shows the document name with a Must read or Should read tag (MarkAsReadConfirmationView.swift, switch on readPolicy); me-android shows the title, the date label and the full DocumentBadges list (MarkAsReadConfirmationSheet.kt).
- (platform parity) Error toast: me-ios adds error.localizedDescription after the markAsReadError string (DocumentsAndBenefitsFeature.swift, markAsReadFailed); me-android shows only R.string.dottie_documents_and_benefits_mark_as_read_error (DocumentsAndBenefitsViewModel.kt onMarkAsReadConfirmed).
- (platform parity) Trigger: me-android sets up the prompt when the external link opens or the download succeeds, and cancels it in onExternalLinkLaunchFailed; me-ios checks state.previewDocument when documentPreviewDismissed or externalUrlDismissed fires.
- (platform parity) List update on success: me-android rebuilds the badges with isRead=true (applyMarkedAsRead); me-ios only sets isRead=true on the item (markDocumentAsRead). The user sees the same result.

### CAP-235: View and open my personal documents

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

An employee lists their own HR documents grouped by category, searches them by name, reads a document's description and downloads it to open it.

- **me-ios** (Employee): screens: `DocumentsAndBenefitsView (Personal tab)`, `DocumentDescriptionView`; endpoints: `GET /employee/api/v2/dottie/documents/my`, `GET /employee/api/v2/dottie/documents/my/{id}/download`; events: `Documents and Benefits personal tab tapped`, `Documents and Benefits search query changed, length: {n}`; storage: `temporary files via CoreUtils.saveTemporaryDataToFileSystem`; platform: `Quick Look preview`, `temporary file storage` · evidence `Modules/DottieFeature/Sources/DottieFeature/Features/DocumentsAndBenefits/DocumentsAndBenefitsFeature.swift:39-47,137-1…`
- **me-android** (Employee): screens: `DocumentsAndBenefitsScreen`, `PersonalDocumentsTab`; endpoints: `GET /api/v2/dottie/documents/my`, `GET /api/v2/dottie/documents/my/{id}/download`; storage: `cacheDir downloaded files`; platform: `file download and open via viewer intent` · evidence `dottie/src/main/java/com/visma/employee/dottie/presentation/documents_and_benefits/DocumentsAndBenefitsViewModel.kt:103…`

**How they differ:**
- (platform parity) me-ios opens the file in Quick Look; me-android opens it via a viewer intent (PersonalDocumentsTab / DocumentsAndBenefitsViewModel.kt:103-143).
- (platform parity) me-ios shows a description sheet and new badge for personal documents (DocumentsAndBenefitsFeature.swift:172-187); me-android fragment reports no description view or new badge string for this tab.
- (platform parity) me-ios logs 'personal tab tapped' analytics; me-android reports none.
- (platform parity) me-ios opens the downloaded file in a Quick Look preview (DocumentsAndBenefitsFeature.swift:163-170). me-android opens it with a viewer intent from cacheDir (DocumentsAndBenefitsViewModel.kt:103-106).
- (platform parity) me-ios logs 'Documents and Benefits personal tab tapped' and 'search query changed, length: {n}' (AnalyticsFeature.swift:16,22). No analytics logging was found in me-android's documents_and_benefits code.
- (platform parity) me-android opens the detail sheet when you tap a card that has a description or cannot be downloaded, and downloads directly otherwise (DocumentsAndBenefitsViewModel.kt:127-133). me-ios has separate personalDocumentDescriptionTapped and personalDocumentTapped actions, chosen in th…
- CORRECTION to claim: me-android does have a personal document description sheet (DocumentsAndBenefitsScreen.kt:205-222) and a New badge (PersonalDocumentsTab.kt:61-66). The claim's second divergence line is wrong.

_Note: referee could not confirm: The divergence line saying me-android has no description view or new badge for personal documents is refuted by DocumentsAndBenefitsScreen.kt:205-222 and PersonalDocumentsTab.kt:61-66._

### CAP-236: Browse employee benefits

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

An employee browses the company's benefits grouped by category, searches them by name, body or supplier, opens a benefit's detail and follows its link to more information.

- **me-ios** (Employee): screens: `DocumentsAndBenefitsView (Benefits tab)`, `BenefitDetailFeature`, `BenefitDetailView`; endpoints: `GET /employee/api/v2/dottie/benefits`; events: `Documents and Benefits benefits tab tapped`, `Documents and Benefits benefit tapped`; platform: `in-app browser (openURLInApp)` · evidence `Modules/DottieFeature/Sources/DottieFeature/Features/DocumentsAndBenefits/DocumentsAndBenefitsFeature.swift:49-61,127-1…`
- **me-android** (Employee): screens: `DocumentsAndBenefitsScreen`, `BenefitsTab`; endpoints: `GET /api/v2/dottie/benefits`; platform: `external link` · evidence `dottie/src/main/java/com/visma/employee/dottie/presentation/documents_and_benefits/DocumentsAndBenefitsViewModel.kt:145…`

**How they differ:**
- (platform parity) me-ios opens the benefit link in an in-app browser; me-android opens it as an external link (https only per RootHostFileActions.kt:62-138).
- (platform parity) me-ios logs 'benefits tab tapped' and 'benefit tapped'; me-android reports no events.
- (platform parity) me-ios opens the benefit link inside the app, in an in-app browser (BenefitDetailView.swift Link + .openURLInApp()). me-android opens it outside the app with Intent.ACTION_VIEW, and only for https links; any other scheme shows a 'cannot open' toast (RootHostFileActions.kt:47-60, S…
- (platform parity) me-ios logs 'Documents and Benefits benefits tab tapped' and 'Documents and Benefits benefit tapped' (AnalyticsFeature.swift:18,20). me-android's dottie module logs no events for benefits.
- (platform parity) me-ios shows the link as an underlined 'link to more information' text inside the detail sheet. me-android shows it as an action button labelled R.string.open_button that also closes the sheet (DocumentsAndBenefitsScreen.kt:170-176).
- (platform parity) me-android opens and closes search explicitly (onSearchOpened/onSearchClosed, isSearchActive), and switching tabs does nothing if that tab is already selected. me-ios clears the search query on every tab selection.

_Note: referee could not confirm: me-android string 'action_open_link' is used by CommonDocumentsTab.kt:108 for documents, not benefits. The benefit link button uses R.string.open_button (DocumentsAndBenefitsScreen.kt:172).; RootHostFileActions.kt:62-138 is the wrong range for the https-only rule. openExternalLink and its https check are at RootHostFileActions.kt:47-60.; The me-ios events are logged in…_

### CAP-237: Open and acknowledge a document from a notification

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

From a document read-request, reminder or document-link notification, the employee opens the document (external link or download preview) and is then asked to mark it as read.

- **me-ios** (Employee): screens: `OrgDocumentReadRequestNotificationFeature`, `OrgDocumentReadRequestNotificationView`, `OrgDocumentPreviewFeature`, `OrgDocumentPreviewView`, `MarkAsReadConfirmationView`; endpoints: `GET {href of link rel download}`, `POST {href of link rel mark-org-document-as-read}`; storage: `temporary files via CoreUtils.saveTemporaryDataToFileSystem`; platform: `Quick Look preview`, `in-app browser (openURLInApp)`, `temporary file storage` · evidence `Modules/DottieFeature/Sources/DottieFeature/Features/OrgDocumentPreview/OrgDocumentPreviewFeature.swift:70-167`

**How they differ:**
- (platform parity) Only me-ios reports a notification-driven document open and mark-as-read flow using HAL link hrefs; no me-android fragment in this domain covers it - to verify whether Android lacks it or it lives in another shard.
- (platform parity) Correction: me-android does implement this flow, so the claim's line saying it may be missing is wrong. It lives in the app module's message inbox: MessageInboxScreenViewModel.kt:119 onDottieCellTapped, :167 onPreviewDismissed, :185 onMarkAsReadConfirmed, with MarkAsReadConfirmati…
- (platform parity) Where the document opens: me-ios shows a Quick Look preview of a temporary file or the in-app browser (OrgDocumentPreviewFeature). me-android sends a UiEvent (OpenDownloadedFile with path and mimeType, or OpenExternalLink) and the host opens it (MessageInboxScreen.kt:306-309), lik…
- (platform parity) Screen structure: me-ios wraps each document cell in a dedicated OrgDocumentReadRequestNotificationFeature/View with its own store. me-android handles the tap inside MessageInboxScreenViewModel, with no separate feature.
- (platform parity) Failed launch: me-android clears the pending mark-as-read prompt when an external link fails to open (onExternalLinkLaunchFailed, MessageInboxScreenViewModel.kt:200). me-ios has no equivalent; it prompts when the in-app browser is dismissed.
- (platform parity) Where read state comes from: me-ios starts from notification.documentIsRead (DottieNotificationsInboxProvider.swift:160). me-android checks the inbox item's isRead (MessageInboxScreenViewModel.kt:173). After confirming, me-android also marks the inbox item as read locally (markIte…

### CAP-238: Preview a downloaded image or PDF inside the app

**Fusion:** shared-diverged · **Personas:** Employee · **Confidence:** Medium

A person opens a downloaded or attached image or PDF full screen inside the app with pinch-to-zoom and pan, then closes it.

- **me-android** (Employee): screens: `ImagePreviewScreen`, `PdfPreviewScreen`, `ImagePreviewKey`, `PdfPreviewKey`; platform: `android.graphics.pdf.PdfRenderer (local file, read-only)`, `Coil image loading` · evidence `core/src/main/java/com/visma/employee/core/preview/image/ImagePreviewScreen.kt:36-97; app/src/main/java/com/visma/emplo…`
- **me-ios** (Employee): storage: `temporary files via CoreUtils.saveTemporaryDataToFileSystem`; platform: `Quick Look preview`, `temporary file storage` · evidence `Modules/DottieFeature/Sources/DottieFeature/Features/DocumentsAndBenefits/DocumentsAndBenefitsFeature.swift:131-170`

**How they differ:**
- (platform parity) me-android uses its own image/PDF preview screens with zoom clamped 1x-5x and PDF pages at 2x (ImagePreviewScreen.kt:36-97); me-ios uses the system Quick Look preview for any downloaded type (DocumentsAndBenefitsFeature.swift:131-170).
- Products: vmm (Manager) also previews images and PDFs in the app (BnxtAttachmentViewerScreen.tsx:19-42; DocumentView/fullscreen/TaskDocumentImage.tsx:25-80), so the capability is shared, not unique.
- Supported types: vmm's approval DocumentView also renders TIFF and HTML task documents in the app (DocumentView/fullscreen/TaskDocumentTIFF, TaskDocumentHtml.tsx). me-android handles only image/* and application/pdf in the app and sends everything else to an external app (RootHostFileActions.kt:67-…
- Zoom rules: vmm image zoom allows a minimum scale of 0.3 and locks page scrolling while zoomed, with a reset event (TaskDocumentImage.tsx:40-74). me-android limits zoom to 1x-5x and pans only when the scale is above 1 (ImagePreviewScreen.kt:48-55; PdfPreviewScreen.kt:56-63).
- PDF viewer in vmm: the BNXT attachment viewer is PDF only, has no zoom handling of its own beyond react-native-pdf, and shows an error banner 'bnxt_attachment_open_failed' when it fails (BnxtAttachmentViewerScreen.tsx:25-39). me-android renders pages to bitmaps at 2x and shows a loader until they a…
- Context: in vmm the preview is part of approval-task and BNXT order screens (a document pane that can be opened full screen, or a pushed screen). In the Employee product it is a generic viewer reached from downloads (documents, payslips, expense attachments).
- (platform parity) me-android uses custom Compose image and PDF preview screens with 1x-5x zoom and PDF pages at 2x (ImagePreviewScreen.kt:36-97, PdfPreviewScreen.kt:42-150), and sends other types to an external app. me-ios uses the system Quick Look for all types (DocumentsAndBenefitsView.swift:62-…

_Note: Cross-cutting utility also used by attachments outside this domain. Android routes images/PDFs here and other types to an external app (RootHostFileActions.kt:72-77). referee could not confirm: me-ios DocumentsAndBenefitsFeature.swift:131-170 does not contain the preview. That range covers navigation to the description sheet and the download cases. previewDocumentURL is set at lines 176-195 and c…_

### CAP-239: Open a downloaded file in another app

**Fusion:** unique · **Personas:** Employee · **Confidence:** Medium

A person opens a downloaded attachment, year-end report or exported payslips in a viewer app chosen from the system chooser, e.g. from an Open snackbar, with a first-page PDF preview available in-app.

- **me-android** (Employee): screens: `ImagePreviewKey`, `PdfPreviewKey`; platform: `FileProvider`, `FileProvider content URI`, `ACTION_VIEW chooser`, `PdfRenderer` · evidence `app/src/main/java/com/visma/employee/navigation/RootHostFileActions.kt:62-138; core/src/main/java/com/visma/employee/co…`

**How they differ:**
- (platform parity) No me-ios fragment reports handing a file to another app via a system chooser; iOS relies on Quick Look - to verify.
- (platform parity) me-android hands the year-end report and exported payslips to another app through an ACTION_VIEW chooser (RootHostFileActions.kt:95-107, 124-131). In me-ios PayslipsFeature I found no share sheet, UIActivityViewController or chooser for these files; QuickLook (UIUtils.swift:141) i…
- (platform parity) me-android shows downloaded images and PDFs in the app via ImagePreviewKey and PdfPreviewKey (RootHostFileActions.kt:70-78). me-ios uses QuickLook only in the expense receipt detail screen.
- Scope correction: openDownloadedFile only hands non-image, non-PDF mime types to the external chooser (RootHostFileActions.kt:80-86). Images and PDFs stay in the app.
- Related, but a separate outcome: vmm (Manager) shares approval documents to other apps with react-native-share Share.open (vmm/src/components/approval/ApprovalDocumentShare/ApprovalDocumentShare.tsx:26-59). It is not merged here, because it is a share action on approval documents, not opening a dow…

_Note: Rules: falls back when no viewer app found (open_file_cant_find_suitable_app); default mime application/pdf; FileWriter guards against path traversal; external links open only with https. Touches Pay (year-end report, exported payslips). referee could not confirm: The description's 'first-page PDF preview available in-app' points to PdfUtils.decryptPDFToSingleBitmapAsync (PdfUtils.kt:46-62). That…_

## Pay and payroll

Payslips, year-end reports and PDFs for employees; payroll dialogues and wage-run approval for managers

### CAP-029: Browse my payslips by payment date, filtered by employer

**Fusion:** unique · **Personas:** employee, employee with several employers · **Confidence:** High

An employee pages through past and upcoming payslips from every connected company, ordered by payment date. Each shows company, payment day and net amount. An employee with several employers picks which companies' payslips (and year-end reports) are shown, and the choice is remembered.

- **me-ios** (Employee): screens: `MainPayslipView`, `MainPayslipFeature`, `PayslipsListView`, `PayslipsListFeature`, `PayslipCompanySelectorHeaderView`, `PayslipCompanySelectorNavBarButton`, `PayslipCompanySelectorFeature`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/allpayslips?From={date}&Offset={n}&D…`, `GET /employee/api/v1/employees/{odpUserId}/payslips`; storage: `inMemory isConnected (shared)`, `UserDefaults Keys.selectedPayslips (selected tenant ids, JSON-encoded) AppUserP…`; platform: `ios-native`, `network reachability monitor (offline overlay)` · evidence `Modules/PayslipsFeature/Sources/PayslipFeature/Features/PayslipsList/PayslipsListFeature.swift:87-168; Employee/Payslip…`
- **me-android** (Employee): screens: `SalaryFeedScreen`, `SalaryFeedKey`, `SalaryFeedScreen (CompanyFilter)`; endpoints: `GET /api/v1/employees/{odpUserId}/allpayslips`, `GET {next/previous link url}`, `GET /api/v1/employees/allreports`; storage: `UserPreferencesRepository selectedCompaniesForPayslipFiltering (per user email,…`; platform: `android-native`, `in-app review request on resume (onRequestReview)` · evidence `payslip/src/main/java/com/visma/employee/payslip/feed/SalaryFeedViewModel.kt:146-333; payslip/src/main/java/com/visma/e…`

**How they differ:**
- (platform parity) Grouping and paging: iOS groups payslips by payment-date year, newest first, and loads the next page when the bottom row appears (PayslipsListFeature.swift:87-168). Android loads future and historical batches around a center date and follows next/previous link URLs (SalaryFeedView…
- (platform parity) Refresh: iOS resets the list when the app returns to the foreground (PayslipsListCoordinator.swift:101-102). Android shows an in-app review request on resume (onRequestReview). iOS instead prompts for a rating after the user leaves payslip detail.
- (platform parity) Company filter visibility: iOS shows the selector only when online and the user has more than 1 context with payslips permission, and the last selected company cannot be deselected (PayslipCompanySelectorFeature.swift:51-109). Android lists only companies with the Payslips feature…
- (platform parity) Saved filter: iOS keeps it in UserDefaults Keys.selectedPayslips as JSON-encoded tenant ids. Android keeps it in UserPreferencesRepository selectedCompaniesForPayslipFiltering, per user email, as comma-separated connectTenantIds.
- (platform parity) Latest payslip: the iOS service gets the latest payslip from two parallel Offset-1 calls from today and sends contextId as the company-id header (PayslipService.swift:55-170). No equivalent was reported for Android.
- (platform parity) Grouping and paging: iOS groups payslips into year sections, newest first, and loads the next page from the bottom row (PayslipsListFeature.swift:108-114, 162-166). Android keeps one flat sorted list, loads future and historical items around mCenterDate, and follows next/previous…
- (platform parity) Refresh: iOS resets the list when the app returns to the foreground (PayslipsListCoordinator.swift:101-102). Android instead calls onRequestReview every time the feed screen resumes (PayslipEntries.kt:57-61).
- (platform parity) Filter visibility: iOS shows the selector only when online and when there are more than 1 payslip contexts (MainPayslipFeature.swift:330, MainPayslipView.swift:38/65), and the last selected company cannot be deselected (PayslipCompanySelectorFeature.swift:92-108). Android applies…
- (platform parity) Saved filter: iOS keeps a JSON-encoded list of tenant ids in UserDefaults Keys.selectedPayslips (AppUserPreferences.swift:177-183). Android keeps it in UserPreferencesRepository per user email (SalaryFeedViewModel.kt:119).
- (platform parity) Latest payslip: I did not check the claim that iOS gets it from two parallel Offset-1 calls (PayslipService.swift:55-170), and nothing equivalent was found on Android.

_Note: Keeps the earlier name (CAP-029). The company filter also reloads the year-end reports list on both platforms (MainPayslipFeature.swift:212-224, SalaryFeedViewModel.kt:115-132). All companies are selected by default. referee could not confirm: Divergence line 3 presents the connectTenantId-and-name company filter as Android-only, but iOS PayslipCompanySelectorFeature.swift:75-78 applies the same…_

### CAP-214: Browse payroll dialogues

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager sees payroll and wage-run conversations grouped by company. Each row shows title, creator, created date, unread count, payout date, approvers and wage-run status. The manager can switch between active and completed dialogues, collapse groups and open one.

- **vmm** (Manager): screens: `HrmScreen dialogue tab`, `DialogueHomeScreen`, `HRM tab dialogue tab`; endpoints: `GET dialogue/companies?Status={type}&includingMessages=true&includingSplits=true`; events: `view_dialogues`, `total_dialog_count`, `dialogue_filter_opened`, `dialogue_filter_selected`; storage: `redux hrmDialogueCollapsedGroups.home (persisted, src/configs/reduxState.ts:127)`, `redux hrmDialogue.dialogueTypeSelectContextMenuVisible` · evidence `src/screens/hrm/DialogueHomeScreen/DialogueHomeScreen.tsx:36-245; src/components/hrm/DialogueHomeListItem/DialogueHomeL…`

_Note: Rules: split-parent unread is the sum of its splits. A wage-run dialogue with 1 split opens that split, with more than 1 split opens the splits list, otherwise the dialogue detail opens. The status selector shows only with hasAccessDialog on the dialogue tab. The status label shows only when a wage run id is present. referee could not confirm: storage citation src/configs/reduxState.ts:127 is off…_

### CAP-215: Start a new payroll dialogue

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager creates a conversation with a title, a company and an optional linked wage run, then lands in it.

- **vmm** (Manager): screens: `DialogueCreateScreen (SCREEN_NAME_DIALOGUE_CREATE_SCREEN)`; endpoints: `GET dialogue/companies`, `GET dialogue/companies/{companyId}/wageruns`, `POST dialogue/companies/{companyId}/dialogues`; events: `new_dialog`; storage: `redux hrmDialogue.allCompanies`, `redux hrmDialogue.allWageruns` · evidence `src/screens/hrm/DialogueCreateScreen/DialogueCreateScreen.tsx:36-178`

_Note: Rules: title max 64 characters. Title and company are required. A single company is auto-selected and locked. Selecting the same wage run again clears it._

### CAP-216: Read a payroll dialogue conversation

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager opens a dialogue or split, from the list or from a push notification, and reads its messages under a company and wage-run header. The dialogue is marked read.

- **vmm** (Manager): screens: `DialogueDetailsScreen (SCREEN_NAME_DIALOGUE_TASK_SCREEN)`; endpoints: `GET dialogue/companies/{companyId}/dialogues/{dialogueId}?includingMessages={in…`, `GET dialogue/companies/{companyId}/dialogues/{dialogueId}/splits/{splitId}?incl…`, `POST dialogue/companies/{companyId}/dialogues/{dialogueId}/markasread`, `POST dialogue/companies/{companyId}/dialogues/{parentDialogueId}/splits/{splitI…`, `GET dialogue/companies/{companyId}/wageruns`; events: `view_messages`, `single_dialog_messages_count`, `single_dialog_person_count`; platform: `push notification entry (fromNotification route param)`, `AppState foreground refetch`, `Android hardware back handler`, `Android keyboard adjustResize` · evidence `src/screens/hrm/DialogueDetailsScreen/DialogueDetailsScreen.tsx:51-352`

_Note: The dialogue is marked read on focus, and again when unread > 0 while focused. Back from a notification goes to the splits list if the parent has more than 1 split, else to HRM home. The composer is hidden when the dialogue is completed._

### CAP-217: Browse wage-run splits of a dialogue

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager sees the splits of a wage-run dialogue grouped by approval status (rejected, for approval, approved) and opens one.

- **vmm** (Manager): screens: `DialogueSplitsScreen (SCREEN_NAME_DIALOGUE_SPLITS_SCREEN)`; endpoints: `GET dialogue/companies/{companyId}/dialogues/{dialogueId}?includingMessages=fal…`, `GET dialogue/companies/{companyId}/dialogues/{dialogueId}/splits?includingMessa…`; storage: `redux hrmDialogueCollapsedGroups.splits (persisted)`; platform: `Android hardware back handler` · evidence `src/screens/hrm/DialogueSplitsScreen/DialogueSplitsScreen.tsx:70-225`

_Note: The status order is fixed: Rejected, ForApproval, Approved. Status comes from approval.status, else from wagerunDetails.status._

### CAP-218: Send a message in a payroll dialogue

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager writes and sends a message to a dialogue or split. Unsent drafts are kept per dialogue.

- **vmm** (Manager): screens: `DialogueDetailsScreen`; endpoints: `POST dialogue/companies/{companyId}/dialogues/{dialogueId}/messages`, `POST dialogue/companies/{companyId}/dialogues/{parentDialogueId}/splits/{splitI…`; events: `new_message`; storage: `redux hrmDialogue.draftMessages (persisted via REDUX_NODE_NAME_HRM_DIALOGUE, sr…` · evidence `src/screens/hrm/DialogueDetailsScreen/components/AddMessageSection.tsx:147-194`

_Note: Max 1024 characters, with a remaining-characters warning. The draft is saved to redux with a 500 ms debounce and restored if the send fails. A blank message is not sent._

### CAP-219: Edit a sent dialogue message

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager long-presses one of their messages, edits its text and saves.

- **vmm** (Manager): screens: `DialogueDetailsScreen`; endpoints: `PUT dialogue/companies/{companyId}/dialogues/{dialogueId}/messages/{messageId}?…`, `PUT dialogue/companies/{companyId}/dialogues/{parentDialogueId}/splits/{splitId…`; storage: `redux hrmDialogue.longPressedMessage`, `redux hrmDialogue.messageEditState` · evidence `src/screens/hrm/DialogueDetailsScreen/components/AddMessageSection.tsx:369-402`

**How they differ:**
- Only one product: vmm (Manager) has dialogue message editing. me-ios and me-android have no dialogue code, so there is no twin parity gap.
- Correction: long-press is allowed when the message's attributes.actions includes DELETE and the dialogue is active (MessageListSection.tsx:157-158). The code never checks isOwner, so 'their messages' really means messages the server allows the user to act on.
- Missing from the claim: the edit text is limited to 1024 characters (MAX_MESSAGE_LENGTH, AddMessageSection.tsx:52, 477), the send icon is disabled while the text is unchanged (line 494), and the caches are updated optimistically (queryEndpointsDialogue.ts:1260+).
- Missing from the claim: edited messages then show a 'dialogue_edited' flag (MessageListSection.tsx:166-170).

_Note: No request is sent if the text is unchanged or blank. Optimistic concurrency uses the message version. referee could not confirm: string 'save' is not used by the message-edit flow; it labels the SaveButton of the edit-dialogue (title/wagerun) flow at AddMessageSection.tsx:447-449. Message edit is confirmed with SendIcon at AddMessageSection.tsx:492-499_

### CAP-220: Delete a dialogue message

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager long-presses a message and deletes it.

- **vmm** (Manager): screens: `DialogueDetailsScreen`; endpoints: `DELETE dialogue/companies/{companyId}/dialogues/{dialogueId}/messages/{messageI…`, `DELETE dialogue/companies/{companyId}/dialogues/{parentDialogueId}/splits/{spli…` · evidence `src/screens/hrm/DialogueDetailsScreen/components/AddMessageSection.tsx:203-227`

**How they differ:**
- Missing from the claim: the delete option only appears when the message's actions include ACTION_DELETE and the dialogue is active (vmm MessageListSection.tsx:150-163).
- Missing from the claim: the delete sends the message version (?version=), so the server can reject a delete made against an outdated copy; the app removes the message from the cache before the server answers (vmm queryEndpointsDialogue.ts:551-575).
- Domain label is doubtful: the feature sits in the HRM dialogue screens (src/screens/hrm/DialogueDetailsScreen), not in 'Pay and payroll'.

### CAP-221: Rename a dialogue or change its linked wage run

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager edits a dialogue's title and links, changes or unlinks its wage run. The edit menu opens from the dialogue context menu, prefilled with the current values.

- **vmm** (Manager): screens: `DialogueDetailsScreen (edit mode)`, `Dialogue chat screen (edit dialogue menu)`; endpoints: `PUT dialogue/companies/{companyId}/dialogues/{dialogueId}?version={version}`, `DELETE dialogue/companies/{companyId}/dialogues/{dialogueId}/wageruns?version={…`, `GET dialogue/companies/{companyId}/wageruns`; events: `new_dialog_title`, `dialogue_link_to_wagerun_changed`, `dialogue_wagerun_unlinked`; storage: `redux hrmDialogue.dialogueNewTitle`, `redux hrmDialogue.onEditWagerun`, `redux hrmDialogue.showEditDialogueMenu`, `redux hrmDialogue.newTitle / selectedWagerun` · evidence `src/screens/hrm/DialogueDetailsScreen/components/AddMessageSection.tsx:229-355; src/components/hrm/DialogueDetailsConte…`

**How they differ:**
- Missed by the claim, vmm only: handleSave (AddMessageSection.tsx:333-335) runs only the unlink when the user unlinks the wagerun. It skips handleEditDialogue, so a title change made in the same save is not sent. Because of this, the title change and the unlink are not a single atomic edit.
- Claim note is imprecise: DialogueDetailsScreen.tsx:246-249 checks ACTION_DELETE or ACTION_UPDATE to show the header options. The check that shows the edit option only with ACTION_UPDATE is in DialogueDetailsContextMenu.tsx:112.

_Note: Offered only when attributes.actions includes ACTION_UPDATE (DialogueDetailsScreen.tsx:246-249). Title max 64 characters. The version is refetched before saving. Splits cannot be unlinked. referee could not confirm: Note 'Offered only when attributes.actions includes ACTION_UPDATE (DialogueDetailsScreen.tsx:246-249)': those lines compute canChange (DELETE or UPDATE) for the header; the edit optio…_

### CAP-222: Mark a dialogue as completed or reactivate it

**Fusion:** unique · **Personas:** manager · **Confidence:** High

From the dialogue context menu a manager marks a dialogue complete or re-enables a completed one.

- **vmm** (Manager): screens: `Dialogue chat screen (context menu)`; endpoints: `GET dialogue/companies/{companyId}/dialogues/{dialogueId}?includingMessages=tru…`, `GET dialogue/companies/{companyId}/dialogues/{dialogueId}/splits/{splitId}?incl…`, `PUT dialogue/companies/{companyId}/dialogues/{dialogueId}?version={version}`; events: `dialogue_completed`; storage: `redux hrmDialogue.contextMenuVisible (slice persisted)` · evidence `src/components/hrm/DialogueDetailsContextMenu/DialogueDetailsContextMenu.tsx:64-101`

_Note: Not offered for split dialogues. Needs attributes.version, else an error toast shows. PUT body is {title, isCompleted, wagerunDetails?}. The cache is updated optimistically. referee could not confirm: Screen name 'Dialogue chat screen (context menu)' is not the real screen name: the menu is mounted in src/screens/hrm/DialogueDetailsScreen/DialogueDetailsScreen.tsx:344_

### CAP-223: Delete a dialogue

**Fusion:** unique · **Personas:** manager · **Confidence:** High

From the dialogue context menu a manager chooses Delete, confirms in a modal that warns the deletion cannot be undone, and sees a success or failure toast.

- **vmm** (Manager): screens: `DialogueDeleteModalScreen`, `HrmDialogueDeleteModal (SCREEN_NAME_DELETE_DIALOGUE_MODAL)`; endpoints: `DELETE dialogue/companies/{companyId}/dialogues/{dialogueId}?version={version}`; events: `delete_dialog`, `delete_dialog_failed` · evidence `src/components/modals/HrmDialogueDeleteModal/HrmDialogueDeleteModal.tsx:37-62; src/components/hrm/DialogueDetailsContex…`

**How they differ:**
- No counterpart in the Employee product: no dialogue code found in legacy/me-ios or legacy/me-android.
- A split is deleted through the same DELETE dialogues/{dialogueId} endpoint, with splitId passed as dialogueId (DialogueDetailsContextMenu.tsx:145; queryEndpointsDialogue.ts:476). The claim's note calls this unclear.

_Note: Offered only when actions include ACTION_DELETE. Needs a version, and passes either dialogueId or splitId. The dialogue is removed optimistically from the getSingleDialogue and getAllDialogues caches. Two screens are popped on both success and failure. Only a dialogue DELETE endpoint was reported, so how a split is deleted is unclear._

### CAP-224: Approve or reject a wage run

**Fusion:** unique · **Personas:** manager, payroll approver · **Confidence:** High

Inside a wage-run dialogue or split that awaits approval, the manager approves or rejects the payroll run.

- **vmm** (Manager): screens: `DialogueDetailsScreen`; endpoints: `PUT dialogue/companies/{companyId}/dialogues/{dialogueId}/approval/{approve/rej…`, `PUT dialogue/companies/{companyId}/dialogues/{parentDialogueId}/splits/{splitId…`; events: `approval_action_button_clicked` · evidence `src/screens/hrm/DialogueDetailsScreen/components/WagerunApproveButtonsSection/WagerunApproveButtonsSection.tsx:43-163`

_Note: The buttons appear after 700 ms when approval status is ForApproval, Approved or Rejected and the dialogue is not completed. Double submits are guarded._

### CAP-225: View a payslip's details

**Fusion:** unique · **Personas:** employee · **Confidence:** High

An employee opens a payslip to see payment date, net total, line items and the employer message. It opens from the list, from a start-page or home card, or from a new-payslip push notification.

- **me-ios** (Employee): screens: `PayslipDetailView`, `PayslipDetailFeature`, `PayslipView`, `MainPayslipDetailView`, `MainPayslipDetailFeature`, `MainPayslipFeature.Path.detailItem`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/payslips/{payslipId}`; events: `payslipOpen`; platform: `ios-native`, `push notification (new payslip) opens modal detail: Employee/PushNotifications/…`, `StoreKit app rating prompt after leaving detail`, `Survicate survey after leaving detail` · evidence `Modules/PayslipsFeature/Sources/PayslipFeature/Features/PayslipDetail/PayslipDetailFeature.swift:77-119; Employee/Paysl…`
- **me-android** (Employee): screens: `PayslipDetailsScreen`, `PayslipDetailsKey`; endpoints: `GET /api/v1/employees/{odpUserId}/payslips/{payslipId}`; events: `Payslip - Payslip open`; platform: `android-native`, `can open from a payslip id or company id (PayslipDetailsKey), e.g. from a notif…` · evidence `payslip/src/main/java/com/visma/employee/navigation/entries/PayslipEntries.kt:101-128`

**How they differ:**
- (platform parity) Line items: iOS shows earning and deduction line items (PayslipDetailFeature.swift:77-119). Android shows rows grouped by category with a net-total bottom card (PayslipDataContainer / PayslipDataBottomCard).
- (platform parity) Opening from a push: iOS fetches the payslip only if contextId resolves and the push odpId equals the current user (PayslipService.swift:55-71). Android opens from PayslipDetailsKey payslipId/companyId, and no such user check was reported (PayslipEntries.kt:101-128).
- (platform parity) After leaving detail: iOS shows a StoreKit rating prompt, else a Survicate survey (MainPayslipFeature.swift:301-305). No post-detail prompt was reported for Android; its review request fires on feed resume.
- (platform parity) Error handling: Android shows payslip_failed_to_load_latest with a snackbar retry. iOS shows a generic S.error alert.
- (platform parity) Line items: iOS maps them through PayslipUIModel.Mapper inside PayslipDetailFeature.swift:100-105. Android shows PayslipDataContainer rows with a PayslipDataBottomCard that holds the payment date and net total (PayslipDataBottomCard.kt:49,62).
- (platform parity) Opening from a push: the iOS getPayslip guard needs contextId to resolve and odp == odpId (EmployeeServices/Payslips/Sources/Payslips/Service/PayslipService.swift:55-60). Android builds the screen from the PayslipDetailsKey payslipId/companyId (PayslipEntries.kt:101-110) and has n…
- (platform parity) After leaving detail: iOS shows a Survicate survey when appRating.willPresentReview() is false (MainPayslipFeature.swift:301-305). The Android detail back handler only calls viewModel.onNavigatedBack() (PayslipEntries.kt:115-118).
- (platform parity) Load error: iOS shows an S.error alert with the error's description (PayslipDetailFeature.swift:108-118). Android shows payslip_failed_to_load_latest with a snackbar_retry_action retry (PayslipRowsViewModel.kt:85,112,161).

_Note: On both platforms a payslip opened from the list is shown without a new fetch. iOS uses the already-loaded payslip, Android hands it over through PayslipResultHolder. referee could not confirm: For iOS, the push-open path uses Employee/Payslips/Coordinator/ShowPayslipCoordinator.swift, not PresentPayslipCoordinator.swift:33-70. The cited PresentPayslipCoordinator range covers only the case where…_

### CAP-226: Download a payslip PDF

**Fusion:** unique · **Personas:** employee · **Confidence:** High

From the payslip details an employee downloads the payslip document as a PDF from any tenant to preview or share it.

- **me-ios** (Employee): screens: `PayslipDetailView`, `PayslipDetailFeature`; endpoints: `GET /employee/api/v1/payslip/getpayslipdocumentanytenantfile?payslipId={payslip…`; storage: `temporary file (filename from Content-Disposition, else UUID+payslip.pdf)`, `temporary file on disk (CoreUtils.saveTemporaryDataToFileSystem)`; platform: `ios-native`, `QuickLook preview` · evidence `Modules/PayslipsFeature/Sources/PayslipFeature/Features/PayslipDetail/PayslipDetailFeature.swift:120-155; EmployeeServi…`
- **me-android** (Employee): screens: `PayslipDetailsScreen`; endpoints: `GET /api/v1/payslip/getpayslipdocumentanytenantfile`; platform: `android-native`, `open file with external app (intent)` · evidence `payslip/src/main/java/com/visma/employee/payslip/payslip_detail/components/PayslipDetailsScreen.kt:155-168`

**How they differ:**
- (platform parity) Viewing: iOS previews and shares in Quick Look (PayslipDetailFeature.swift:120-155). Android opens the file in an external app via intent and shows open_file_cant_find_suitable_app if no app can open it (PayslipDetailsScreen.kt:155-168).
- (platform parity) File name: iOS takes it from the Content-Disposition header, else UUID + payslip.pdf (PayslipService.swift:27-52). Android defaults to payslip.pdf (PayslipServiceImpl.kt:231).
- (platform parity) Feedback: Android shows retrieving, retrieved and failed snackbars (document_retrieving / document_retrieved / document_retrieval_failed). iOS shows only a 'could not load PDF' alert on failure.
- (platform parity) Viewing: iOS keeps the file URL in pdfModel and shows it in a QuickLook preview (PayslipDetailFeature.swift:137-139, PayslipService.swift imports QuickLook). Android opens the file in an external app through PdfUtils.previewPdf and shows a snackbar with open_file_cant_find_suitabl…
- (platform parity) File name: the claim is only partly right. Both platforms take the name from the server response and fall back to a default. iOS reads the Content-Disposition filename, else uses UUID + payslip.pdf (PayslipService.swift:45-50). Android uses response.getFileName(), else DEFAULT_PAY…
- (platform parity) Feedback: Android shows a document_retrieving snackbar, then document_retrieved with an Open action (snackbar_open_action), or document_retrieval_failed with a Retry action (snackbar_retry_action) (PayslipRowsViewModel.kt:150-175). iOS shows a loading state and, on failure, only a…
- (platform parity) Offline: Android does nothing when there is no network, because onOpenPayslipDocument checks mConnectionManager.isNetworkAvailable() (PayslipRowsViewModel.kt:139-143). iOS has no such check and fails through the error alert.
- (platform parity) Delivery: Android opens the file only after the user taps Open on the snackbar. iOS shows the preview as soon as pdfLoaded arrives.

_Note: referee could not confirm: me-android evidence PayslipDetailsScreen.kt:155-168 only covers the download icon button. The download is in PayslipServiceImpl.kt:124-146 and the endpoint at PayslipServiceImpl.kt:251. The snackbars are in PayslipRowsViewModel.kt:139-175 and the intent in PayslipDetailsScreen.kt:229-240. The files list leaves out PayslipServiceImpl.kt and PayslipRowsViewModel.kt.; Pari…_

### CAP-227: Export all my payslips to one PDF

**Fusion:** unique · **Personas:** employee · **Confidence:** High

An employee exports all their payslips as one document. If they have payslips from several companies they first pick a company. They then preview or open the document.

- **me-ios** (Employee): screens: `MainPayslipView`, `MainPayslipFeature`, `CompanyMenuButton`; endpoints: `GET /employee/api/v1/Payslip/Export`, `GET /employee/api/v1/employees/{odpUserId}/payslips/exportFromAllTenants?tenant…`; events: `exportAllPayslips (Snowplow 'Export all payslips', category Payslip)`; storage: `documents file from base64 contentBase64 + fileName`, `document saved to file system (CoreUtils.saveDocumentToFileSystem)`; platform: `ios-native`, `QuickLook preview` · evidence `Modules/PayslipsFeature/Sources/PayslipFeature/Features/Main/MainPayslipFeature.swift:234-272; EmployeeServices/Payslip…`
- **me-android** (Employee): screens: `SalaryFeedScreen (export company picker)`; endpoints: `GET /api/v1/employees/{odpUserId}/payslips/exportFromAllTenants`; events: `Payslip - Export all payslips`; platform: `android-native`, `open exported document with external app` · evidence `payslip/src/main/java/com/visma/employee/payslip/feed/SalaryFeedViewModel.kt:464-537`

**How they differ:**
- (platform parity) Endpoints: iOS has both GET /employee/api/v1/Payslip/Export (current company) and exportFromAllTenants with a single tenant id (MainPayslipFeature.swift:234-272). Android calls only GET /api/v1/employees/{odpUserId}/payslips/exportFromAllTenants (SalaryFeedViewModel.kt:464-537).
- (platform parity) Button visibility: Android shows the export button only if the user has the Payslips feature. iOS reported no such gate, but a 404 or missing content maps to a noPayslips error (S.pdfExportNoPayslips).
- (platform parity) Viewing: iOS saves the document to the documents folder and previews it in Quick Look. Android opens the exported document in an external app.
- (platform parity) Analytics: iOS logs exportAllPayslips on success or noPayslips (AnalyticsFeature.swift:21-22). Android logs 'Payslip - Export all payslips'.
- (platform parity) Endpoints: iOS calls GET /Payslip/Export with no tenant when the user has one company, and exportFromAllTenants?tenantGuids=<one id> after the user picks a company (MainPayslipFeature.swift:234-258, PayslipService.swift:116-134). Android always calls exportFromAllTenants with filt…
- (platform parity) Company list: Android offers only the companies that have the Payslips feature (allCompaniesWithPayslipFeature, SalaryFeedViewModel.kt:59, 531-537). iOS lists store.companies (MainPayslipView.swift:118-127).
- (platform parity) No payslips: on iOS, a response without content maps to PayslipError.noPayslips (S.pdfExportNoPayslips), shown in an alert. The 404 branch in decodePayslips can never run, because the request is made outside its do block (PayslipService.swift:117, 137-149). Android maps a missing…
- (platform parity) Progress feedback: iOS shows a progress indicator in the toolbar button (MainPayslipView.swift:119-137). Android shows an indefinite snackbar with my_page_report_retrieving (SalaryFeedViewModel.kt:467-472).
- (platform parity) Viewing: iOS saves the file to the file system with CoreUtils.saveDocumentToFileSystem and previews it with QuickLook. Android writes the file to the cache folder and passes it to onOpenExportedPayslipsDocument to open externally (SalaryFeedScreen.kt:158-159).
- (platform parity) Analytics timing: iOS logs exportAllPayslips from the analytics reducer (AnalyticsFeature.swift:22). Android logs EXPORT_ALL_PAYSLIPS as soon as the export starts, before the result is known (SalaryFeedViewModel.kt:466).

_Note: On both platforms the response is base64 content plus a file name. referee could not confirm: The claim that iOS maps a 404 to noPayslips is only partly true: the 404 catch in PayslipService.swift:137-149 wraps only the guard, not the request, so it can never run.; Android: 'shows the export button only if the user has the Payslips feature' is not confirmed. The code only limits the export compan…_

### CAP-228: Browse my year-end reports

**Fusion:** unique · **Personas:** employee · **Confidence:** High

An employee switches to the year-end reports segment or tab to see the annual tax and income reports for their selected companies.

- **me-ios** (Employee): screens: `PayslipSummaryView`, `PayslipSummaryFeature`, `MainPayslipView segment picker`; endpoints: `GET /employee/api/v1/employees/allreports?tenantIds=...&from={date}&offset={n}&…`; events: `payslipYearEndReportsTabOpened`; storage: `UserDefaults Keys.selectedPayslips (read)`; platform: `ios-native` · evidence `Modules/PayslipsFeature/Sources/PayslipFeature/Features/PayslipSummary/PayslipSummaryFeature.swift:588-632; EmployeeSer…`
- **me-android** (Employee): screens: `SalaryFeedScreen (Year-end reports tab)`; endpoints: `GET /api/v1/employees/allreports`; events: `Payslip - Year-end reports tab opened`; platform: `android-native` · evidence `payslip/src/main/java/com/visma/employee/payslip/report_detail/presentation/components/ReportDetailsScreen.kt:60-110; p…`

**How they differ:**
- (platform parity) Tab visibility: iOS shows the segment picker only when at least one report exists (MainPayslipFeature.swift:190-206). Android always has a Year-end reports tab on SalaryFeedScreen, and no condition was reported.
- (platform parity) Sorting and paging: Android sorts reports by year, then company name (SalaryFeedViewModel.kt:453). iOS asks for past reports with offset 100 when there are no tenants, else 25 per tenant (GetYearEndReports.swift:39). Neither side reported the other's rule.
- (platform parity) Sorting: Android sorts reports by year, newest first, then by company name (SalaryFeedViewModel.kt:393, 453-457). iOS keeps the server's order and drops items that have no id or an empty documentTitle (PayslipSummaryUIModel.Mapper.swift:18-24).
- (platform parity) Page size basis: iOS sets the offset to 25 per selected tenant, or 100 when none are selected (GetYearEndReports.swift:37-38, tenant IDs from userPreferences.getSelectedPayslipTenantIds). Android sets it to 25 per company with the payslip feature, or 100 when there are none (Salar…
- (platform parity) Deep link: Android can open straight on the Year-end reports tab from a notification (NotificationHandler.kt:84 REQUESTED_TAB_ARG=yearEndReports; SalaryFeedViewModel.kt:97, 434-441, allowed only when hasReports). I found no matching requested-segment entry on iOS in MainPayslipFea…
- (platform parity) Tab visibility is the same on both, contrary to the claim. iOS shows the segment picker only when there are reports (MainPayslipFeature.swift:190-206), and Android shows the tab only when feedState.hasReports is true (SalaryFeedScreen.kt:239).

_Note: referee could not confirm: me-ios Modules/PayslipsFeature/Sources/PayslipFeature/Features/PayslipSummary/PayslipSummaryFeature.swift:588-632: out of range, the file has only 120 lines. The load logic is at lines 64-100.; me-android payslip/.../report_detail/presentation/components/ReportDetailsScreen.kt:60-110: this is the screen for one report's detail and PDF download, not the reports list or t…_

### CAP-229: View a year-end report

**Fusion:** unique · **Personas:** employee · **Confidence:** High

An employee opens a year-end report to see its titled field and value lines. It opens from the reports list or from a year-end push notification.

- **me-ios** (Employee): screens: `YearEndReportDetailView`, `YearEndReportDetailFeature`, `YearEndReportView`, `MainYearEndReportView`, `MainYearEndReportFeature`, `MainPayslipFeature.Path.yearEndReport`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/reports/{reportId}`; platform: `ios-native`, `push notification (year-end report) opens modal: Employee/PushNotifications/Eve…` · evidence `Modules/PayslipsFeature/Sources/PayslipFeature/Features/YearEndReport/YearEndReportDetailFeature.swift:69-106; Employee…`
- **me-android** (Employee): screens: `ReportDetailsScreen`, `ReportDetailsKey`; endpoints: `GET /api/v1/employees/report/{reportId}`; platform: `android-native` · evidence `payslip/src/main/java/com/visma/employee/payslip/report_detail/presentation/components/ReportDetailsScreen.kt:60-110`

**How they differ:**
- (platform parity) Endpoint: iOS uses GET /employee/api/v1/employees/{odpUserId}/reports/{reportId}, and only in the modal opened from a push (YearEndReportDetailFeature.swift:69-106). Android uses GET /api/v1/employees/report/{reportId} (ReportDetailsScreen.kt:60-110).
- (platform parity) Push entry: iOS opens a modal from a year-end push notification (YearEndNotificationPayload.swift:29). No push entry was reported for Android's ReportDetailsKey.
- (platform parity) Endpoint: iOS fetches with GET {employeeApiV1}/employees/{odpUserId}/reports/{reportId} (GetYearEndReport.swift:24-26), but only in the push modal. The list path reuses the report it already has (MainPayslipFeature.swift:229-231; YearEndReportDetailFeature.swift:70-72). Android fe…
- (platform parity) Push entry: both twins open the report from a year-end push. iOS presents a modal (YearEndNotificationPayload.swift:29-37 -> ShowEndYearCoordinator.swift:61-66). Android reads data['reportId'] (DefaultFirebaseMessagingService.kt:53,162) and pushes ReportDetailsKey onto the Salary…
- (platform parity) Error handling: iOS shows an alert with S.error/S.ok (YearEndReportDetailFeature.swift:95-106). Android uses a snackbar with a retry action (snackbar_retry_action).

_Note: referee could not confirm: Claim divergence 'No push entry was reported for Android's ReportDetailsKey' is wrong: legacy/me-android/app/src/main/java/com/visma/employee/navigation/RootDeepLinks.kt:75-81 and DefaultFirebaseMessagingService.kt:53 route a year-end push to ReportDetailsKey; Android evidence range ReportDetailsScreen.kt:60-110 contains only the UI. The endpoint it lists is defined at…_

### CAP-230: Download a year-end report PDF

**Fusion:** unique · **Personas:** employee · **Confidence:** High

An employee downloads a year-end report as a PDF and previews, shares or opens it.

- **me-ios** (Employee): screens: `YearEndReportDetailView`, `YearEndReportDetailFeature`; endpoints: `GET {report.export.href} (server-provided export URL)`; storage: `temporary file {documentTitle}.pdf, deleted when preview is dismissed`; platform: `ios-native`, `QuickLook preview` · evidence `Modules/PayslipsFeature/Sources/PayslipFeature/Features/YearEndReport/YearEndReportDetailFeature.swift:107-149`
- **me-android** (Employee): screens: `ReportDetailsScreen`; endpoints: `GET /api/v1/employees/report/{reportId}/export/pdf`; platform: `android-native`, `open downloaded PDF with external app` · evidence `payslip/src/main/java/com/visma/employee/payslip/report_detail/presentation/components/ReportDetailsScreen.kt:60-110`

**How they differ:**
- (platform parity) Endpoint: iOS follows the server-provided report.export.href (YearEndReportDetailFeature.swift:107-149). Android calls the fixed GET /api/v1/employees/report/{reportId}/export/pdf (ReportDetailsScreen.kt:60-110).
- (platform parity) Offline: iOS disables the button when offline and requires an export href and a non-empty documentTitle. No offline rule was reported for Android.
- (platform parity) File handling: iOS writes a temporary {documentTitle}.pdf, previews it in Quick Look and deletes it when the preview is dismissed. Android opens the PDF in an external app and shows retrieving, retrieved and failed snackbars.
- (platform parity) Endpoint: iOS follows the export URL the server provides in report.export.href (YearEndReportsPdfRepository.ReportsService.swift, guard on export?.href). Android calls the fixed GET api/v1/employees/report/{reportId}/export/pdf (ReportsServiceImpl.kt:158).
- (platform parity) Offline: iOS disables the Show PDF / download button when !store.isConnected (YearEndReportDetailView.swift:36,43). Android keeps the button enabled; when mConnectionManager.isNetworkAvailable() is false, or there is no report id, it shows the my_page_report_retrieval_failed snack…
- (platform parity) Preconditions: iOS requires export.href and a non-empty documentTitle (year - companyName) before it downloads (YearEndReportsPdfRepository.ReportsService.swift, ViewModel.YearEndReport.documentTitle.swift). Android only needs a report id and shows the download icon only once the…
- (platform parity) File name: iOS uses {documentTitle}.pdf (ReportsService.swift:50). Android uses the file name from the server response, falling back to report.pdf, in cacheDir/SHARED_DOCUMENTS_DIR (ReportsServiceImpl.kt:57-61).
- (platform parity) File handling: iOS previews the PDF and deletes the temporary file when the preview is dismissed (YearEndReportDetailFeature.swift pdfViewDismissed). Android keeps the file in the cache and opens it in an external app from an 'Open' snackbar action; if no app can open it, it shows…
- (platform parity) Feedback: iOS shows a loading state on the button and an alert on failure (S.couldNotLoadPdfTitle, S.ok). Android shows retrieving, retrieved (with Open) and failed (with Retry) snackbars.

_Note: referee could not confirm: me-android evidence ReportDetailsScreen.kt:60-110 covers only the UI. The download logic and network check are in payslip/.../report_detail/presentation/ReportDetailsViewModel.kt:84-138, and the endpoint is in payslip/.../report_detail/data/ReportsServiceImpl.kt:49-79,158. Neither file is listed.; The string open_file_cant_find_suitable_app is not used in ReportDetailsS…_

### CAP-231: Learn why I have no payslips

**Fusion:** unique · **Personas:** employee · **Confidence:** High

When the payslip list is empty, the employee taps a link to open the payslips FAQ.

- **me-ios** (Employee): screens: `PayslipsListView empty state`; platform: `ios-native` · evidence `Modules/PayslipsFeature/Sources/PayslipFeature/Features/PayslipsList/PayslipsListView.swift:108-123`
- **me-android** (Employee): screens: `SalaryFeedScreen`; platform: `android-native` · evidence `payslip/src/main/java/com/visma/employee/payslip/feed/SalaryFeedViewModel.kt:146-333`

**How they differ:**
- (platform parity) Entry point: iOS shows a 'why no payslips' link in the empty state, and the coordinator intercepts .list(.openFaqTapped) and sends .showPayslipsFAQ (PayslipsListCoordinator.swift:56-57,112-118). Android shows an empty-state action button to the Payslip FAQ (payslips_feed_empty_act…
- (platform parity) Entry point: iOS has a 'why no payslips' button (S.Payslips.whyNoPayslips) in the NoContentView overlay, shown when orderedSections is empty (PayslipsListView.swift:108-123). Android has a GaiaTertiaryButton (payslips_feed_empty_action_button_text) in PayslipFeedEmptyContent (Sala…
- (platform parity) FAQ destination: iOS dispatches .showPayslipsFAQ, and TabbarCoordinator opens FAQDetailCoordinator(roleType: .payslip, permissions: [.payslips]) as a modal (TabbarCoordinator.swift:184-186, 204-211). Android pushes FaqKey(preselectedContext = PAYSLIP) onto the nav stack (SalaryFee…
- (platform parity) Offline state: Android shows a separate offline empty state (payslips_feed_offline) with no FAQ link (SalaryFeedScreen.kt:181-185). No such state was found in the iOS empty-state overlay.

_Note: referee could not confirm: me-android payslip/src/main/java/com/visma/employee/payslip/feed/SalaryFeedViewModel.kt:146-333 has no empty state or FAQ action. The real evidence is SalaryFeedScreen.kt:280-330 (PayslipFeedEmptyView/PayslipFeedEmptyContent, onOpenFaq(PreselectedFaqContext.PAYSLIP) at line 325)._

## Expenses

Receipts, mileage, allowances, credit card transactions, attachments, claims, sending for approval, offline drafts and emissions

### CAP-028: Browse my expense claims by year and filter by status

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee opens the Claims part of the Expenses tab, pages through their claims (older and newer) and narrows the list with status filter chips loaded from the server.

- **me-ios** (Employee): screens: `ExpensesView`, `ExpensesFeature`, `CalendarViewController`, `ClaimsQuickFilterBar`; endpoints: `GET /employee/api/v2/Expense/claims/possible-filters`, `GET /employee/api/v1/employees/{odpUserId}/expense/claims?From={date}&Offset={n…`, `GET /employee/api/v1/employees/{odpUserId}/expense/claims?fromdate={date}&todat…`; platform: `ios-native` · evidence `Employee/Expenses/Coordinators/ExpensesCoordinator.swift:69-97; Modules/EmployeeExpenses/Sources/EmployeeExpenses/Claim…`
- **me-android** (Employee): screens: `ExpenseInboxScreen (Claims tab)`, `ClaimsFeedScreen`, `ClaimsStatusFilterRow`, `ExpenseRowsKey`; endpoints: `GET /api/v1/employees/{odpUserId}/expense/claims`, `GET /api/v2/expense/claims/possible-filters`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/feed/compose/ClaimsFeedScreen.kt:65-464; expense/src/main/java/com/vis…`

**How they differ:**
- (platform parity) iOS groups claims by year and fetches undated claims once per reset into a 'claims without date' section (ExpensesCoordinator.swift:69-97); Android shows a date-centred feed loading future and historical pages sized by screen height, and no undated section is reported (ClaimsFeedV…
- (platform parity) Android shows a status label on each claim (not sent, awaiting approval, approved, declined, paid, cancelled, awaiting clearance) and a 'total amount unavailable' state (ClaimsFeedScreen.kt:65-464). iOS status labels on list rows are not reported.
- (platform parity) iOS paging is gated by the company feature expenseApiWrite (ClaimsFilterModel.swift); on Android only write actions need expense write permission (ClaimsFeedViewModel.kt).
- (platform parity) iOS groups claims into year sections and fetches undated claims once per reset into a 'claims without date' section with the status filter applied (ClaimsCalendarViewModel.swift:90-99,206). Android loads a date-centred feed of future and historical pages, batch size set by the cal…
- (platform parity) Android shows a status label on each claim: approved, not sent, declined, cancelled, paid, awaiting approval, awaiting clearance (ClaimsFeedScreen.kt:445-451). I did not check the iOS list rows for status labels.
- (platform parity) iOS switches claims paging off unless the company has the expenseApiWrite feature (ClaimsPagingControllerDataSource.swift:30-32). I found no matching check on the Android feed load.
- (platform parity) Android keeps searching linked pages when the first result is empty (chaseLinkedPagesWhileEmpty in ClaimsFeedViewModel.kt). I did not find this on iOS.

_Note: Earlier name kept: this is the same outcome as CAP-028. referee could not confirm: The iOS gate on expenseApiWrite is in ClaimsPagingControllerDataSource.swift:31, not in ClaimsFilterModel.swift as the claim's divergence says._

### CAP-240: Browse my unsent expenses in the expenses inbox

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee sees every unsent receipt, credit card transaction, mileage and allowance in one list, with a collapsible credit card section, per-row sync status, offline and no-permission states, and opens an item to review or edit it.

- **me-ios** (Employee): screens: `ReceiptsListFeature`, `ReceiptsListView`, `ReceiptsSectionedList`, `ReceiptRowView`, `ReceiptsCoordinator`, `ReceiptDetailViewController`, `EditMileagePresenter`, `EditAllowanceCoordinator`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/expense/claims?status=editable`; events: `retry load button tapped`, `credit card section header tapped`, `receipt row tapped`, `mileage row tapped`, `allowance row tapped`, `credit card row tapped`; storage: `DatabaseService.allReceiptsInContext (local receipt DB, per user context)`, `DatabaseService.allReceiptsForUploadInContext (offline)`, `SyncService.receiptUploadTaskState`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/Features/ReceiptsList/ReceiptsListFeature.swift:194-305; Mod…`
- **me-android** (Employee): screens: `ExpenseInboxScreen (Expenses tab)`, `ExpenseDraftsScreen`; endpoints: `GET api/v1/employees/{odpUserId}/expense/inbox`, `GET api/v1/employees/{odpUserId}/expense/templates/{type}`, `GET api/v1/employees/{odpUserId}/expense/currencies`; storage: `cached templates (TemplateServiceModelMapper.isTemplateCached)`; platform: `offline banner` · evidence `expense/src/main/java/com/visma/employee/expense/inbox/compose/ExpenseDraftsScreen.kt:121-310`

**How they differ:**
- (platform parity) iOS offers quick filter chips (mail-sourced, credit card, unlinked expense, mileage, allowance), only for kinds present in the data (ReceiptsListFeature.swift:194-305). No inbox filter is reported on Android (ExpenseDraftsScreen.kt:121-310).
- (platform parity) When offline, iOS lists only the drafts waiting to upload (ReceiptsListView.swift:18-133). Android shows an offline empty state (expense_inbox_empty_offline) and opens credit card details only when templates are cached (ExpenseDraftsScreen.kt).
- (platform parity) Without write permission iOS shows 'closed for registration' and hides the bottom bar (S.Expense.closedForRegistrationWarning). Android shows expense_inbox_disabled_write_permission.
- (platform parity) iOS shows quick filter chips (QuickFilterBar fed by store.availableFilters, ReceiptsListView.swift:~70; filterToggled in ReceiptsListFeature.swift:~290). The Android inbox list has no filter bar: the only filters in inbox/ are claim-status filters (ExpensesInboxServiceImpl.kt:163).
- (platform parity) When offline, iOS loads only the drafts waiting to upload (ReceiptsRepositoryClient.Live.swift:308-310, allReceiptsForUploadInContext) and shows a limitedFunctionalityWhenOffline banner. When offline, Android keeps its list and shows expense_inbox_empty_offline only when the list…
- (platform parity) Without write permission, iOS shows S.Expense.closedForRegistrationWarning as the empty text (ReceiptsListView.swift:~55). Android shows expense_inbox_disabled_write_permission (ExpenseDraftsScreen.kt:939) and hides all toolbar buttons (ExpenseDraftsScreen.kt:~215).

_Note: referee could not confirm: me-ios endpoint 'GET /employee/api/v1/employees/{odpUserId}/expense/claims?status=editable' does not load the inbox. It loads editable claims for the send/add-to-claim routing (ReceiptsRepositoryClient.Live.swift:166, getClaims(by: .editable)). The inbox itself comes from GET .../employees/{odpUserId}/expense/inbox (EmployeeServices/Expense/Sources/Expense/Request/GetRe…_

### CAP-241: Start a new receipt, mileage or allowance

**Fusion:** unique · **Personas:** employee · **Confidence:** High

From the expenses list add menu or the start/home page quick actions, the employee starts a new receipt (camera), a mileage or an allowance. The start is blocked when templates are missing, and allowance needs its own permission and a connection.

- **me-ios** (Employee): screens: `AddNewReceiptCoordinator`, `ReceiptScannerController`, `AddMileageCoordinator`, `AddAllowanceCoordinator`, `ReceiptsListView add menu (confirmationDialog)`; events: `quickSelection(addReceipt)`, `quickSelection(addMileage)`, `quickSelection(addAllowance)`, `add new expense menu button tapped`, `create new receipt option tapped`, `create new mileage option tapped`, `create new allowance option tapped`; platform: `ios-native` · evidence `Employee/Expenses/Coordinators/ExpensesCoordinator.swift:299-366; Employee/StartPage/StartPageService.swift:92-126; Mod…`
- **me-android** (Employee): screens: `HomeButtonsList`, `ExpenseDraftAddModalBottomSheet`; events: `StartPage - Quick selection: add mileage`, `StartPage - Quick selection: add receipt`, `StartPage - Quick selection: add allowance`; storage: `cached expense/mileage templates (TemplateServiceModelMapper)`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/home/HomeButtonsProvider.kt:160-209; expense/src/main/java/com/visma/employee/expe…`

**How they differ:**
- (platform parity) The Android home quick selections show a badge counting pending receipts (HomeButtonsProvider.kt:160-209). No badge is reported on iOS (StartPageService.swift).
- (platform parity) On Android the allowance quick selection is hidden offline (HomeViewModel.kt:1507-1531). On iOS it is disabled offline (StartPageService.swift:101-108).
- (platform parity) Mileage offline: Android lets mileage start online even when templates are not cached, and blocks it only when it is offline with no cached mileage template (HomeViewModel.kt:1517-1525). iOS blocks mileage whenever hasMissingMileageTemplates() is true, whatever the connection (Exp…
- (platform parity) Missing-template message: iOS picks the message from the template sync error and the online state, falling back to S.offlineReceiptsMissingTemplatesMessage or S.connectAndRetry (ExpensesCoordinator.swift:303-308, 350-355). Android shows the fixed strings templates_not_found_descri…
- (platform parity) Android expenses-list add menu: tapping mileage opens it without any template check, and only receipt checks for cached templates (ExpenseDraftsScreen.kt:752-767). The iOS list menu sends delegates that go through the same addNewMileage/addNewReceipt template guards (ReceiptsListV…
- (platform parity) Allowance in the list menu: iOS shows it only when canCreateAllowances is true and disables it offline (ReceiptsListView.swift:234-239). Android shows it by hasAllowanceCreationPermission, and no offline disable appears in the cited menu code (ExpenseDraftsScreen.kt:768-777).
- (platform parity) Allowance quick selection offline: on both twins it stays visible and is disabled offline. Android uses VisibleStateCondition for permission and EnabledStateCondition for isNetworkAvailable (HomeButtonsProvider.kt:193-200); iOS uses enabled: reachabilityService.isOnline (StartPage…

_Note: referee could not confirm: Claimed divergence 'Android home quick selections show a badge counting pending receipts (HomeButtonsProvider.kt:160-209)': those lines have no badge. The receipt badge is set on the ButtonType.RECEIPTS button in HomeViewModel.kt:442-452, not on the add quick selections.; Claimed divergence 'On Android the allowance quick selection is hidden offline (HomeViewModel.kt:15…_

### CAP-242: Capture or import a receipt image or PDF

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee photographs a receipt with automatic edge or object detection, flash and cropping, or picks an image or PDF from the device, to start a receipt or add an attachment.

- **me-ios** (Employee): screens: `ReceiptScannerController`, `CameraViewController`, `CropImageViewController`, `CameraPermissionsView`, `MediaPickerCoordinator action sheet`; events: `autocrop found item`, `createNewReceiptDuration`; platform: `camera (AVCaptureDevice authorization)`, `WeScan library`, `UIImagePickerController photo library`, `UIDocumentPicker (pdf, image)` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Wescan/CameraViewController.swift:112-226; Modules/EmployeeExpenses/S…`
- **me-android** (Employee): screens: `CameraEntry`, `CameraKey`, `FragmentCameraBinding`; events: `AUTO_CROP_FOUND_ITEM`; storage: `Room UserPreferenceDbModel.capture_mode`, `cache dir scan_result_<ts>.jpg`; platform: `camera (CameraX)`, `ML Kit object detection (STREAM_MODE)`, `ACTION_GET_CONTENT file picker (image/*, application/pdf)` · evidence `app/src/main/java/com/visma/employee/camera/CameraCoordinator.kt:199-233; app/src/main/java/com/visma/employee/navigati…`

**How they differ:**
- (platform parity) iOS uses WeScan edge detection with manual crop editing (CameraViewController.swift:112-226). Android uses CameraX with ML Kit prominent-object detection and stores the capture mode in Room (ProminentObjectProcessor.kt:18-121, CameraCoordinator.kt:199-233).
- (platform parity) iOS resizes images to Full HD JPEG and keeps PDFs, accepting only jpeg and pdf as attachments (AddNewReceiptCoordinator.swift:48-215). Android rejects unsupported types through FileValidator; its size rules are not reported.
- (platform parity) When camera permission is denied, Android shows a toast, opens app settings and closes (CameraEntry.kt). iOS shows CameraPermissionsView with an 'enable in settings' action (CameraViewController.swift).
- (platform parity) iOS uses WeScan quad edge detection with a crop editor (CameraViewController.swift captureImageSuccess withQuad, CropImageViewController.swift). Android uses CameraX with ML Kit STREAM_MODE prominent-object detection (ProminentObjectProcessor.kt:27).
- (platform parity) Android persists the auto/manual capture mode per user through userPreferencesRepository.getCaptureMode (CameraViewModel.kt:111) and defaults to MANUAL. For iOS, only the toggle itself was confirmed (CameraViewController.swift toggleAutoscanTapped); whether iOS saves the mode was…
- (platform parity) iOS converts images to Full HD JPEG and keeps PDFs (AddNewReceiptCoordinator.swift:136-142). Android validates picked files with FileValidator (CameraEntry.kt:48,68) and saves captures as scan_result_<ts>.jpg in cache (CameraViewModel.kt:209). Android resize rules were not found.
- (platform parity) On denied permission, Android shows the camera_permission_is_needed message and opens app settings (CameraEntry.kt:148-151). iOS shows an in-screen CameraPermissionsView with an enable-in-settings action (CameraViewController.swift showCameraPermissionsView).
- (platform parity) Android's gallery picker accepts image/* and application/pdf through one ACTION_GET_CONTENT chooser (CameraCoordinator.kt:199-217). iOS splits this into two options in an action sheet: photo library, and a document browser for pdf and image (MediaPickerCoordinator.swift:54-68, 121…

_Note: referee could not confirm: me-android storage 'Room UserPreferenceDbModel.capture_mode': the capture mode is read through userPreferencesRepository.getCaptureMode at CameraViewModel.kt:111, not at the cited CameraCoordinator.kt:199-233 (that range is the gallery picker and onFileCreated). UserPreferenceDbModel exists (core module); the column name capture_mode was not confirmed._

### CAP-243: Share a photo or PDF into the app to create an expense

**Fusion:** unique · **Personas:** employee · **Confidence:** Medium

The employee shares an image or PDF from another app into the Employee app, picks an employer with expense access when needed, and continues in the receipt flow.

- **me-android** (Employee): screens: `MainActivityDialogs (EmployerPicker, Information)`, `EmployerPicker`, `CameraKey(shareUri)`; platform: `ACTION_SEND intent filter image/*, application/pdf, application/x-pdf` · evidence `app/src/main/java/com/visma/employee/home/MainActivity.kt:465-570; app/src/main/java/com/visma/employee/share/ShareActi…`
- **me-ios** (Employee): screens: `ShareReceiptCoordinator (share extension)`; platform: `share extension (ExpenseShareExtension)` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Smartscan/EmployeeSmartscanService.swift:58-120 (lists ShareReceiptCo…`

**How they differ:**
- (platform parity) Android blocks sharing when the user is not logged in, has no Expense role, has no write permission, or is offline without cached templates, and shows a non-cancelable employer picker (ShareAction.kt:20-42, MainActivity.kt:465-570). On iOS the share extension is only seen as a Sma…
- (platform parity) Employer picker: Android uses a non-cancelable ListPickerDialog, and pressing back finishes the activity (MainActivityDialogs.kt:41-51, MainActivity.kt:531-534). iOS uses a UIAlertController with a Cancel action that closes the extension (ShareReceiptCoordinator.swift:100-116). Th…
- (platform parity) Write permission: Android greys out employers that lack the Expense WritePermission and blocks sharing with expense_inbox_disabled_write_permission when every employer lacks it (ShareAction.kt:28-33, 48-49). iOS filters only on .expenseClaims and never checks write permission (Sha…
- (platform parity) Single employer: Android goes straight to the camera only when the one expense employer is already the current context, and shows the picker otherwise (ShareAction.kt:34). iOS always goes straight to the flow with that employer and switches context silently (ShareReceiptCoordinato…
- (platform parity) Templates: Android blocks sharing only when the device is offline and the templates are not cached, and checks this after the employer is picked (MainActivity.kt:518-527, ShareAction.kt:38-42). iOS blocks whenever templates are missing for the chosen context, online or not (ShareR…
- (platform parity) Next step: Android opens CameraKey(shareUri) inside the main app (MainActivity.kt:500). iOS stays in the extension, sends images to CropImageViewController and PDFs straight to ReceiptDetailViewController (ShareReceiptCoordinator.swift:150-170, 185-200, 245+).
- (platform parity) File checks: iOS rejects missing data, files over ReceiptsConstants.maxAttachmentFileSize, corrupted PDFs and encrypted PDFs before the receipt detail opens (ShareReceiptCoordinator.swift:210-240). The cited Android share code has none of these checks.
- (platform parity) Gating: Android holds the share until the app-lock unlock and the welcome screen are done (MainActivity.kt:468-478, 547-565). The iOS extension shows no such gating in ShareReceiptCoordinator.start (lines 76-91).

_Note: Medium confidence: the iOS side is inferred from one screen name in a Smartscan fragment. referee could not confirm: me-ios Modules/EmployeeExpenses/Sources/EmployeeExpenses/Smartscan/EmployeeSmartscanService.swift:58-120: it does not list ShareReceiptCoordinator or ExpenseShareExtension (a grep finds neither name). It only calls machineLearningService.annotateDocument and maps the Smartscan resu…_

### CAP-244: Auto-fill a receipt from its image and get a suggested expense type

**Fusion:** unique · **Personas:** employee · **Confidence:** High

A scanned or shared receipt is sent to the machine-learning service. It pre-fills date, amount, VAT, currency, kilometres, flight duration and route, and suggests an expense type. When the employee saves, feedback and the chosen type are sent back to train the model.

- **me-ios** (Employee): screens: `AddNewReceiptCoordinator`, `ReceiptDetailViewController`, `ShareReceiptCoordinator (share extension)`; endpoints: `POST /employee/api/v1/machineLearning/AnnotateDocument`, `POST /employee/api/v1/machineLearning/SendFeedback`; events: `expenseTypeSuggestionWasGiven`, `expenseTypePredictionWasEdited`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Smartscan/EmployeeSmartscanService.swift:58-120; Modules/EmployeeExpe…`
- **me-android** (Employee): screens: `ExpenseDraftDetailsScreen`, `ExpenseDraftDetailsKey`; endpoints: `POST api/v1/machineLearning/AnnotateDocument`, `POST api/v1/machineLearning/predictExpenseType`, `POST api/v1/machineLearning/SendFeedback`, `POST api/v1/machineLearning/trainExpenseTypePredictionModel`; events: `expenseTypeSuggestionGiven`, `Receipts - Expense Type Prediction was Edited`; storage: `SavedStateHandle SMARTSCAN_RESPONSE_TEXT`, `SavedStateHandle SMARTSCAN_ALREADY_RUN`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/inbox/details/ExpenseDraftDetailsViewModel.kt:1180-1310; expense/src/m…`

**How they differ:**
- (platform parity) iOS uses a scanned value only at high or veryHigh confidence (EmployeeSmartscanService.swift:58-120). Android fragments disagree: ExpenseDraftDetailsViewModel.kt:1180-1310 applies only High or VeryHigh, but MachineLearningServiceImpl.kt:44-128 lists VeryHigh through Unknown as all…
- (platform parity) Android calls predictExpenseType and trainExpenseTypePredictionModel (MachineLearningServiceImpl.kt). iOS prediction is described as on-device, and its PredictExpenseType and TrainExpenseTypePredictionModel endpoints were not resolved (ExpenseTypePredictor.Employee.swift:1-17).
- (platform parity) Android marks the expense as abroad when the scanned currency differs from the default (ExpenseDraftDetailsViewModel.kt). iOS maps the currency code to a country ID (EmployeeSmartscanService.swift).
- (platform parity) The expense-type suggestion is picked differently. Android takes the prediction with the highest confidence and applies it if it is High or better (ExpenseDraftDetailsViewModel.kt:1281-1286). iOS takes the first prediction that is high or veryHigh (ReceiptDetailViewModel.swift:102…
- (platform parity) Both twins call the same four server endpoints: AnnotateDocument, predictExpenseType, SendFeedback and trainExpenseTypePredictionModel. iOS: me-ios/EmployeeServices/Expense/Sources/Expense/Request/*.swift. Android: MachineLearningServiceImpl.kt:105-127. Android also sends the comp…
- (platform parity) After the scan, Android fetches the exchange rate and recalculates the local amount straight away (ExpenseDraftDetailsViewModel.kt:1239-1251). iOS only sets the abroad flag (ReceiptDetailViewModel.swift:235 and 607-616). A person should check whether iOS recalculates the amount el…

_Note: referee could not confirm: Divergence claim: 'MachineLearningServiceImpl.kt:44-128 lists VeryHigh through Unknown as allowed'. That file has no confidence-level filter.; Divergence claim: 'iOS prediction is described as on-device; PredictExpenseType and TrainExpenseTypePredictionModel endpoints were not resolved'. They are server endpoints: me-ios/EmployeeServices/Expense/Sources/Expense/Request/…_

### CAP-245: Create or edit a receipt

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee fills in or edits a receipt from its template (expense type, amount, date, VAT, purpose, flight duration and other fields), sees validation errors, and saves it as a draft in the inbox. The draft is kept locally and uploaded later when offline.

- **me-ios** (Employee): screens: `ReceiptDetailViewController (storyboard Receipts/receiptDetailView)`; endpoints: `POST /employee/api/v1/expense/upsert-draft`, `DELETE {receipt.deleteLink}`; events: `Save button tapped`, `newReceiptSaveButtonClicked`, `saveNewReceiptDraft`, `saveEditedReceiptDraft`, `frequentlyUsedExpenseTypeSelected`, `Expense type cell tapped`; storage: `Local receipts database (saveReceipt)`, `Receipt templates in local DB`, `DatabaseService.receipt(id:) local drafts`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/ReceiptDetailViewController.swift:601-663; Modules/EmployeeE…`
- **me-android** (Employee): screens: `ExpenseDraftDetailsScreen`, `ExpenseDraftDetailsKey`, `ExpenseDraftDetailsBottomSheetLayout`, `FlightDurationPicker`; endpoints: `GET api/v1/employees/{odpUserId}/expense/templates/expense`, `GET /api/v1/employees/{odpUserId}/expense/templates/{type}`, `POST api/v1/expense/upsert-draft`; events: `NEW_RECEIPT_SAVE_BUTTON_CLICKED`, `NEW_RECEIPT_CREATED`, `RECEIPT_EDITED`, `CAMERA_USED`, `FILE_BROWSER_USED`, `GALLERY_USED`, `SHARE_EXTENSION_USED`, `EXPENSE_TYPE_FREQUENTLY_USED_SELECTED`; storage: `offline draft storage when upsert fails with UnknownHostException (ExpenseDraft…`; platform: `Survicate NPS survey trigger after a save` · evidence `expense/src/main/java/com/visma/employee/expense/inbox/details/ExpenseDraftDetailsViewModel.kt:1706-1736; expense/src/m…`

**How they differ:**
- (platform parity) Android has a wheel picker for flight duration (hours 0..99, minutes 0..59) (FlightDurationPicker.kt:31-110). On iOS flight duration is only reported as a Smartscan-filled value (EmployeeSmartscanService.swift).
- (platform parity) On Android, fixed-price templates lock currency and amount, with amount = fixedPrice x quantity (ExpenseDraftDetailsViewModel.kt:1531-1545). On iOS, fixed-price expense types force the local currency (ReceiptDetailViewController.swift:601-663).
- (platform parity) Android lists server rule types Required, Min, Max, MaxLength, Regex, InvalidCharacters and MaxByReference, plus visibility conditions EqualsTo, NotEqualsTo, LessThan and MoreThan (ExpenseDraftDetailsModalBottomSheetLayout.kt, ExpenseTypeFieldViewModel.kt). iOS does not list its r…
- (platform parity) Correction to the claim: both platforms let the user enter flight duration manually with a 0-99 hour picker. iOS: ReceiptDetailViewController.swift:504,2147 (createFlightDurationField / FormFlightDurationTableViewCell) and FlightDurationFormRow.swift:28,47-55 (maxHours = 99, TimeS…
- (platform parity) Fixed-price templates: Android recalculateAmount forces the default currency and sets amount = fixedPrice x quantity (ExpenseDraftDetailsViewModel.kt:1531-1545). iOS checks fixed price in isExpenseFixedPrice (ReceiptDetailViewController.swift:1938-1946), not at the cited lines 601…
- (platform parity) Offline save: iOS always writes the receipt to the local DB first and then uploads it, keeping the local copy on noInternet (DraftRepository.receiptDatabase.swift:37-49). Android saves locally only when the upsert fails with UnknownHostException and saveOfflineOnError is true, and…
- (platform parity) After a save, both platforms show a Survicate survey: iOS via requestSurveyShowingThankYouToast (ExpensesCoordinator.swift:167-168), Android via SurvicateTrigger.NPS (ExpenseDraftDetailsViewModel.kt:1738-1740).

_Note: referee could not confirm: The me-android implementation's platform field says "Survicate NPS survey trigger after a save" instead of android-native.; Android endpoint "GET api/v1/employees/{odpUserId}/expense/templates/expense" is not a literal in the code. The code has the parameterised GET api/v1/employees/{odpUserId}/expense/templates/{type} (ExpenseTemplatesServiceImpl.kt:226).; The claim sa…_

### CAP-246: Enter a receipt in a foreign currency with an exchange rate

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee picks the receipt currency, with frequently used currencies first. The app fetches a suggested exchange rate for the date and converts the amount to the company currency. The same currency gives a rate of 1.

- **me-ios** (Employee): screens: `ReceiptDetailViewController`; endpoints: `GET /employee/api/v1/expense/currencies/{from}/exchangerate?to={to}&date={date}`; storage: `Frequently used currencies (DatabaseService.updateFrequentlyUsedCurrency)`, `realm-model:RealmLocalFrequentlyUsedCurrencies`, `realm-model:RealmDefaultCurrency`, `realm-model:RealmCurrency`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/ReceiptDetailViewController.swift:601-663; EmployeeServices/…`
- **me-android** (Employee): screens: `ExpenseDraftDetailsScreen`, `currency picker modal bottom sheet`; endpoints: `GET api/v1/employees/{odpUserId}/expense/currencies`, `GET api/v1/expense/currencies/{currencyCode}/exchangerate`; storage: `frequently used currencies (local cache via ExpenseServiceModelMapper)`, `Room CurrencyDbModel (frequent/default currencies)`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/inbox/details/ExpenseDraftDetailsViewModel.kt:1091-1147; expense/src/m…`

**How they differ:**
- (platform parity) Android shows at most 4 frequently used currencies and waits up to 5 s for a pending rate fetch (ExpenseDraftDetailsViewModel.kt:1091-1147). iOS keeps a caller-given limit of recent currencies (RealmService.swift:849-895) and waits for any in-flight rate fetch before saving, with…
- (platform parity) Android checks the entered rate against an allowed deviation from the suggested rate on the field itself (ExchangeRateViewModel.kt:59-133). iOS reports the deviation check during bulk validation before sending to a claim (ReceiptsListFeature.swift:307-420).
- (platform parity) None confirmed for the frequent-currency limit: both platforms show at most 4 (iOS ReceiptDetailViewModel.swift:23 frequentlyUsedCurrenciesLimit = 4; Android ExpenseDraftDetailsViewModel.kt:2486 MAX_FREQUENTLY_USED_CURRENCY_AMOUNT = 4).
- (platform parity) None confirmed for the wait before saving: both wait up to 5 s for a pending rate fetch (iOS ReceiptSaveSubmitGate.swift:34 fetchAwaitTimeout .seconds(5); Android ExpenseDraftDetailsViewModel.kt:2491 EXCHANGE_RATE_AWAIT_TIMEOUT_MS = 5_000L). If the fetch is late, iOS logs that it…
- (platform parity) Both platforms check the deviation from the suggested rate on the field itself (iOS ReceiptFieldViewModel.swift:139-160 and ExpenseFieldValueValidator.swift:213; Android ExchangeRateViewModel.kt:81-86 with AllowedDeviationPercentage.kt:9). Both also run a bulk check (iOS BulkRecei…
- (platform parity) Android hides the exchange-rate and converted-amount fields when the receipt currency equals the default currency (ExchangeRateViewModel.kt:70-79). I did not verify matching hide logic on iOS.

_Note: referee could not confirm: ReceiptsListFeature.swift:307-420 (cited in the claim's divergence): no such source file exists under me-ios/Modules/EmployeeExpenses/Sources; only a test, Tests/.../Features/ReceiptsListFeatureTests.swift, has that name; Divergence claim 'iOS keeps a caller-given limit ... no timeout reported' is refuted by ReceiptDetailViewModel.swift:23 (limit 4) and ReceiptSaveSubmi…_

### CAP-247: Calculate driving distance for a kilometre receipt

**Fusion:** unique · **Personas:** employee · **Confidence:** High

On a receipt with a kilometres field, the employee picks from and to places (with recent suggestions) and an optional return trip, and the app fills in the distance from a route calculation.

- **me-ios** (Employee): screens: `ReceiptDetailViewController`, `FormPlaceSelectionTableViewCell`, `PlaceSelectionFormRow`; endpoints: `POST /employee/api/v1/maps/directions`; events: `{calculate distance button displayName} button pressed`; storage: `UserDefaults key com.visma.employee.expense.receipts.calculateDistance.suggesti…`; platform: `Google Places search (place picker)` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/Models/ReceiptDetailViewModel.swift:1401-1441`

**How they differ:**
- (platform parity) No kilometre-distance calculation on the receipt form is reported for me-android. Android only calculates distance for mileages.
- (platform parity) The claim says me-android has no kilometre-distance calculation on the receipt form. That is wrong. me-android/expense/src/main/java/com/visma/employee/expense/inbox/compose/expense_draft_details/ExpenseDraftDetailsBottomSheetLayout.kt:596-604 embeds ExpenseMileageCalculator for t…
- (platform parity) The input differs between the twins. iOS uses a 'Calculate distance' toggle field plus From and To place-selection rows and a Return trip boolean, all shown or hidden by visibility conditions (ReceiptFieldViewModel+KilometersCalculation.swift). Android reuses the mileage route man…
- (platform parity) iOS stores recent place suggestions under the UserDefaults key com.visma.employee.expense.receipts.calculateDistance.suggestions (SuggestionsRepository.allowanceSuggestions.swift:16). An equivalent receipt-specific suggestion store was not confirmed on Android.
- (platform parity) On iOS, a failed directions call clears the kilometres field (ReceiptDetailViewModel.swift:1435 setValue(nil)). On Android, only a successful Overwrite event updates the field (ExpenseDraftDetailsBottomSheetLayout.kt:780-786).

_Note: referee could not confirm: The claimed divergence 'Android only calculates distance for mileages' is refuted by me-android ExpenseDraftDetailsBottomSheetLayout.kt:596-604 and :776-790.; The recent-suggestions storage key lives in Allowance/Repository/Suggestions/SuggestionsRepository.allowanceSuggestions.swift:16. It is not in any of the cited receipt files._

### CAP-248: Add or remove attachments on an expense

**Fusion:** unique · **Personas:** employee · **Confidence:** High

From an expense's attachments sheet the employee adds more files (scan, photo or file) or removes an attachment after confirming, on a draft or on an item in an editable claim.

- **me-ios** (Employee): screens: `AttachmentsView`, `ReceiptScannerFeature`, `AttachmentsView confirmationDialog`; endpoints: `DELETE /employee/api/v1/expense/drafts/{draftId}/attachments/{attachmentId}?cla…`; storage: `DatabaseService saveReceipt (draft with local attachment)`; platform: `camera / document scanner via ReceiptScannerController`, `photo library picker`, `file picker`, `UISheetPresentationController` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Attachments/AttachmentsFeature.swift:242-336; Modules/EmployeeExpense…`
- **me-android** (Employee): screens: `AttachmentsBottomSheet`, `AttachmentsSheet`, `ExpenseDraftDetailsScreen`; endpoints: `DELETE api/v1/expense/drafts/{draftId}/attachments/{attachmentId}`; storage: `local image database reference for new attachments`; platform: `camera for attachment (callbacks.onOpenAttachmentCamera)`, `file picker` · evidence `expense/src/main/java/com/visma/employee/expense/inbox/details/attachment/AttachmentHandler.kt:71-330; expense/src/main…`

**How they differ:**
- (platform parity) iOS stores new attachments locally on the draft and uploads them later (AttachmentsFeature.swift:242-336). On Android, adding attachments depends on being online (AttachmentHandler.kt:71-330).
- (platform parity) iOS validates attachments as jpeg, png or pdf with AttachmentValidator (AttachmentsFeature.swift). Android's allowed types for added attachments are not reported.
- (platform parity) Removing an attachment already on the server: on Android removeExistingAttachment returns early when offline, and existing attachments are marked removable only when isOnline (AttachmentHandler.kt:~95, buildAttachmentListItems). iOS has no online check before calling deleteDraftAt…
- (platform parity) The claim says Android needs to be online to add an attachment. The code does not show this. Android's addAttachment only appends to the local attachmentFiles state (AttachmentHandler.kt:79-81), and the Add more button is enabled by canAddAttachments and deletingAttachmentId, not…
- (platform parity) Minimum-one rule: iOS disables remove when the sheet has exactly one attachment in total (AttachmentsView.swift:134). On a saved draft, Android requires more than one server attachment to remove one, but a newly added file can always be removed (AttachmentHandler.kt buildAttachmen…
- (platform parity) Editability: iOS enables remove when the repository has a remove function (DraftAttachmentRepository.swift:10, ReceiptDetailViewController.swift:1300-1301). Android enables add and remove only when the draft screen is in the Edit state (ExpenseDraftDetailsViewModel.kt:952).
- (platform parity) iOS checks scanned or picked attachments with AttachmentValidator (AttachmentsFeature.swift:305-316). I found no matching check on Android's addAttachment path.

_Note: referee could not confirm: me-android AttachmentHandler.kt:71-330 does not show that adding attachments needs a connection. The online check guards only the removal of an attachment already on the server._

### CAP-249: View or download an expense attachment

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee opens a receipt image or PDF full screen (with zoom) and saves it to the device.

- **me-ios** (Employee): screens: `AttachmentsView`, `MediaPickerExportFeature`, `ImageViewController`, `QLPreviewController`, `UIDocumentPickerViewController (export)`; endpoints: `GET {attachment thumbnail/image URL}`, `GET {attachment file URL}`; storage: `temporary file for preview`, `Temporary file Preview.pdf (deleted on deinit)`, `temporary file Export.pdf`; platform: `QuickLook quickLookPreview`, `photo library add (photoLibrary.savePhoto)`, `UIDocumentPicker forExporting` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Attachments/AttachmentsFeature.swift:168-303; Modules/EmployeeExpense…`
- **me-android** (Employee): screens: `ExpenseDraftDetailsScreen`, `AttachmentsBottomSheet`, `DraftPhotoPreview`; endpoints: `GET {attachment fullImage/file href}`; storage: `MediaStore.Downloads (Environment.DIRECTORY_DOWNLOADS)`; platform: `MediaStore Downloads write (API 29+)`, `image/PDF preview`, `PDF thumbnail rendering` · evidence `expense/src/main/java/com/visma/employee/expense/inbox/details/ExpenseDraftDetailsViewModel.kt:1593-1671`

**How they differ:**
- (platform parity) iOS saves images to Photos, exports other files through the Files picker, and offers Settings when Photos permission fails (AttachmentsFeature.swift:220-303). Android writes a JPEG or PDF named {id or reference} to the Downloads folder through MediaStore (ExpenseDraftDetailsViewMo…
- (platform parity) iOS saves images to Photos and exports PDFs and other files through the Files export picker, and offers Settings when Photos permission fails (AttachmentsFeature.swift:220-237, 269-296, 446-485; MediaPickerCoordinator.swift ~109-115). Android writes a JPEG or PDF named {id or refe…
- (platform parity) iOS previews any attachment type, including PDFs, full screen with QuickLook (AttachmentsView.swift:21). Android previews only a decoded bitmap in a zoomable PhotoView (DraftPhotoPreview.kt:65-74), and I found no PDF preview in Android main code.
- (platform parity) Android saveFileViaMediaStore requires API 29 (@RequiresApi Q, ExpenseDraftDetailsViewModel.kt:1634) and has no fallback for older devices. Android also skips the save silently when external storage is not mounted (line 1594). iOS has no matching limit.

_Note: referee could not confirm: me-android 'PDF thumbnail rendering' platform claim: no PdfRenderer or PDF preview found in me-android/expense/src/main; me-ios ImageViewController.swift:20-105 is opened from ReceiptDetailViewController.swift:1546, not from the AttachmentsFeature flow (which uses QuickLook); it is part of this capability only through the older receipt detail screen; me-android storage…_

### CAP-250: Link a credit card transaction to a receipt (merge)

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee pairs one credit card transaction with one matching receipt, from the inbox merge mode or from an item's detail through a candidate list ranked as exact or possible match, and the two become one expense on the server.

- **me-ios** (Employee): screens: `ReceiptsMergeSelectionFeature`, `MergeListFeature`, `MergeListView`, `ReceiptsMergeSelectionView`, `ReceiptDetailViewController`; endpoints: `POST /employee/api/v2/expense/merge`, `POST /employee/api/v1/expense/upsert-draft (detail sheet saves edited item befo…`; events: `creditCardTransactionMerged`, `credit card transaction merged`, `toggle merge selection button tapped`, `merge receipts button tapped`; storage: `DatabaseService.deleteReceipt (originals)`, `DatabaseService.importReceipts (merged result)`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/Features/MergeSelection/ReceiptsMergeSelectionFeature.swift:…`
- **me-android** (Employee): screens: `ExpenseDraftsScreen (MergeDraftList)`, `MergeCandidatesBottomSheet`, `ExpenseDraftDetailsScreen`; endpoints: `POST api/v2/expense/merge`, `POST api/v1/expense/upsert-draft`, `GET api/v1/employees/{odpUserId}/expense/inbox`; events: `Receipts - credit card transaction merged`, `CREDIT_CARD_TRANSACTION_MERGED`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/inbox/ExpenseDraftsViewModel.kt:1028-1100; expense/src/main/java/com/v…`

**How they differ:**
- (platform parity) From the detail screen, Android merges only outside a claim context and reopens the merged draft in a new details screen (ExpenseDraftDetailsViewModel.kt:408-535). iOS imports the merged receipt into the local DB and shows a 'linked' message; no claim-context restriction is report…
- (platform parity) After a merge started from an item's detail screen, Android opens the merged draft in a new details screen (mNavigator.onDraftMerged, ExpenseDraftDetailsViewModel.kt around line 531). iOS closes the sheet and swaps the merged receipt into the detail screen that is already open (vi…
- (platform parity) Correction to the claim: both platforms block merge in a claim context. Android: supportsMerge requires editClaimDraftData == null and claimDetailsFlow == null (ExpenseDraftDetailsViewModel.kt:288-291). iOS: supportsMerge requires receiptEditingMode .update or .create (ReceiptDeta…
- (platform parity) iOS reads candidates from the local database and falls back to receipts still waiting for upload when offline (ReceiptsRepositoryClient.Live.swift makeMergeCandidates). The claim lists GET api/v1/employees/{odpUserId}/expense/inbox for Android, but I did not confirm that Android l…

_Note: The similarity rules (same day, 0.01% exact, 5% possible) match on both platforms. referee could not confirm: The claim's statement that iOS has 'no claim-context restriction' is contradicted by ReceiptDetailViewModel.swift:787-790, where supportsMerge requires inbox .update or .create mode._

### CAP-251: Delete an unsent expense

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee deletes a receipt, credit card transaction, mileage or allowance draft from the inbox or from its detail screen after confirming. It is deleted on the server, or only on the device if it was never uploaded.

- **me-ios** (Employee): screens: `ReceiptsListView (swipe action, delete confirmation alert, deleting overlay)`, `ReceiptDetailViewController`, `MileageView`, `TravelInfoFeature confirmationDialog`, `AllowanceInfoFeature confirmationDialog`; endpoints: `DELETE {receipt._links rel=delete href}`, `DELETE {draft delete link href}`, `DELETE {allowance _links rel=delete href}`; events: `delete receipt swipe action tapped`, `Delete receipt button tapped`, `deleteExpenseDraft`, `deleteMileage`, `deleteAllowance`, `deleteCreditCardTransaction`, `receipt deleted`, `mileages deleted` …; storage: `DatabaseService.deleteReceipt (local receipt DB)`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/Repository/ReceiptsRepositoryClient.Live.swift:503-536; Modu…`
- **me-android** (Employee): screens: `ExpenseDraftsScreen`, `ExpenseDraftDeleteModalBottomSheet`, `ExpenseDraftDetailsScreen`, `MileageScreen`, `DeleteConfirmation dialog`, `AllowancesStepOneScreen (top bar delete)`, `AllowancesStepTwoScreen top bar delete`; endpoints: `DELETE {draft delete link}`, `DELETE {draft link rel=DELETE_RECEIPT href}`; events: `Expense - Swipe to delete`, `Receipts - receipt deleted`, `Mileages - Mileages deleted`, `Receipts - credit card transaction deleted`, `RECEIPT_DELETED`, `CREDIT_CARD_TRANSACTION_DELETED`, `NEW_MILEAGE_DELETED (Mileages - Mileages deleted)`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/inbox/compose/ExpenseDraftsScreen.kt:352-364; expense/src/main/java/co…`

**How they differ:**
- (platform parity) iOS deletes from the inbox by swipe (ReceiptsListView.swift). Android uses a long-press that opens a delete bottom sheet, although its analytics event is named 'Swipe to delete' (ExpenseDraftsScreen.kt:352-364).
- (platform parity) iOS treats a 'cannot find resource' server error as already deleted and deletes drafts that were never uploaded only on the device (ReceiptsRepositoryClient.Live.swift:503-536). Neither rule is reported for Android, which only shows delete when a delete link exists (MileagesViewMo…
- (platform parity) iOS deletes from the inbox with a swipe action (ReceiptsListView.swift:143 -> ReceiptsListFeature.swift:350 deleteReceiptSwiped). Android opens a delete sheet on long-press (ExpenseDraftsScreen.kt:352-364 -> ExpenseDraftsViewModel.kt:986), even though its analytics constant is nam…
- (platform parity) iOS deletes a receipt that was never uploaded (state .created, no delete link) only on the device (ReceiptsRepositoryClient.Live.swift:512-516), and does the same for allowances through canOnlyBeDeletedLocally (DraftRepository.allowanceDatabase.swift:28-31). On Android, a missing…
- (platform parity) iOS treats a cannotFindResource API error as already deleted and removes the local copy (ReceiptsRepositoryClient.Live.swift:527-533, DraftRepository.allowanceDatabase.swift:37-41). Android shows a delete-failed error for any response other than Success (ExpenseDraftDetailsViewMod…
- (platform parity) iOS checks reachability before it deletes and stops with an offline error (ReceiptsRepositoryClient.Live.swift:518-520). The Android delete paths I read have no offline check. They call the service and show the generic delete-failed error.

_Note: referee could not confirm: me-ios Modules/EmployeeExpenses/Sources/EmployeeExpenses/Mileage/Coordinators/EditMileageCoordinator.swift:48-137 does not do the delete. It only dismisses the screen in viewModelDidDeleteMileageDraft once the view model has deleted. The delete logic is in MileageView.ViewModel, which the claim does not cite.; me-android: the second of the claimed Android delete-link ru…_

### CAP-252: Send selected expenses to a claim

**Fusion:** unique · **Personas:** employee · **Confidence:** High

In the inbox the employee selects several valid, synced drafts (one by one, per section or all), the app validates them, and the employee picks an existing editable claim or creates a new one. Before saving, the employee reviews the claim with previously added and to-be-added items.

- **me-ios** (Employee): screens: `ReceiptsListFeature`, `ReceiptsListView (selection checkboxes, Send button)`, `ClaimsTableViewController`, `SendClaimTableViewController`, `AddExpenseToClaimCoordinator`, `CreateClaimCoordinator`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/expense/claims?status=editable`, `GET /employee/api/v1/expense/currencies/{from}/exchangerate?to={to}&date={date}`, `POST {claim._links rel=addOrRemoveReceipts href}`, `POST {claim._links rel=addOrRemoveMileages href}`, `POST {claim._links rel=addOrRemoveAllowances href}`, `POST /employee/api/v1/employees/{odpUserId}/expense/claims/{claimId}/update-fro…`, `POST /employee/api/v1/employees/{odpUserId}/expense/claims/{claimId}/update-fro…`; events: `expensesSelectedForSending`, `select section checkbox tapped`, `receipt row checkbox selected`, `expensesAddedToExistingClaim`, `expensesAddedToNewClaim`, `Claim cell tapped`, `existingClaimSaved`; storage: `Local receipts database: sent source receipts deleted after save`; platform: `Reachability (send blocked offline)`, `Survicate survey thank-you toast after adding` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/Features/ReceiptsList/ReceiptsListFeature.swift:307-420; Mod…`
- **me-android** (Employee): screens: `ExpenseDraftsScreen`, `ClaimSelectionScreen`, `SelectedClaimScreen`, `SelectedClaimKey`; endpoints: `GET /api/v1/employees/{odpUserId}/expense/claims?status=editable`, `GET /api/v1/employees/{odpUserId}/expense/claims/template`, `POST (HATEOAS link update-from-drafts / update-from-mileage-drafts / update-fro…`, `PUT {claim link rel=update}`; events: `Expense - Amount of expenses selected`, `EXISTING_CLAIM_SAVED (Claims - existing claim saved)`, `EXPENSES_ADDED_TO_EXISTING_CLAIM`; platform: `connectivity observer reloads the claims when the connection returns` · evidence `expense/src/main/java/com/visma/employee/expense/inbox/compose/ExpenseDraftsScreen.kt:257-270; expense/src/main/java/co…`

**How they differ:**
- (platform parity) iOS caps the selection at 20 items (ReceiptsListFeature.selectedReceiptsLimit). Android caps it at MAX_DRAFTS_ALLOWED, whose value is not reported (ExpenseDraftsScreen.kt:257-270).
- (platform parity) iOS adds inbox items through claim links rel=addOrRemoveReceipts, addOrRemoveMileages and addOrRemoveAllowances (ReceiptsRepositoryClient.Live.swift:733-837). Android uses update-from-drafts, update-from-mileage-drafts and update-from-allowance-draft (SelectedClaimViewModel.kt:385…
- (platform parity) The Android review screen offers 'save for later' and 'send for approval' side by side (SelectedClaimLayout.kt:51-166). On iOS, SendClaimTableViewController shows previously added and to-be-added items with a save flow (SendClaimTableViewController.swift:283-392).
- (platform parity) Wrong in the claim: both platforms cap the selection at 20. iOS uses ReceiptsListFeature.selectedReceiptsLimit = 20 (ReceiptsListFeature.swift:14). Android uses MAX_DRAFTS_ALLOWED = 20 (me-android/expense/src/main/java/com/visma/employee/expense/ExpenseResultKeys.kt:23). There is…
- (platform parity) Wrong in the claim: the rel names are the same on the wire. iOS RelAction.addOrRemoveReceipts = "update_from_drafts" and addOrRemoveMileages = "update_from_mileage_drafts" (me-ios/EmployeeServices/EmployeeAPIInterface/Sources/EmployeeAPIInterface/Model/ResponseModel.swift:40-41).…
- (platform parity) Wrong in the claim: both review screens offer 'save for later' and 'send for approval'. iOS has saveForLater/sendForApproval (SendClaimTableViewController.swift:137-157, 428-432). Android shows expense_selected_claim_save_for_later_button and expense_selected_claim_send_for_approv…
- (platform parity) On iOS, sendTapped returns early when state.isOffline (ReceiptsListFeature.swift:~385). On Android, the claim reports a connectivity observer that reloads the claims when the connection returns. I did not verify an equivalent offline block on Android.
- (platform parity) Before posting, Android first updates the claim fields through the claim's update link (onUpdateClaim in SelectedClaimViewModel.kt:385-415) and, for EHRM companies, sets the cost units from the claim. iOS applies the cost-unit override and fills the purpose from the claim title (a…

_Note: referee could not confirm: Divergence line 1: 'Android caps at MAX_DRAFTS_ALLOWED, value not reported'. The value is 20, the same as iOS (ExpenseResultKeys.kt:23).; Divergence line 2: 'rel names differ'. The iOS enum raw values are update_from_drafts and update_from_mileage_drafts (ResponseModel.swift:40-41), the same as Android.; Divergence line 3 suggests Android alone offers 'save for later' a…_

### CAP-253: Create a new expense claim from selected expenses

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee bundles selected receipts, mileages, allowances and card transactions into a new claim. They fill in title, comment, cost units and project, review the totals (reimbursable and paid by company), save it for later, and see a confirmation.

- **me-ios** (Employee): screens: `CreateClaimViewController`, `SaveExpenseToNewClaimViewController`, `PostScreenViewController`, `CreateClaimCoordinator`, `SaveExpenseAndCreateClaimCoordinator`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/expense/claims/template`, `PUT /employee/api/v1/employees/{odpUserId}/expense/claims`, `POST /employee/api/v1/employees/{odpUserId}/expense/claims/{claimId}/update-fro…`, `POST /employee/api/v1/employees/{odpUserId}/expense/claims/{claimId}/update-fro…`, `POST {claim link rel addOrRemoveAllowances href}`; events: `Create new claim button tapped`, `Save for later button tapped`, `newClaimSaved`, `multipleExpensesInClaim`, `newAllowanceAddedToClaim`, `costUnitsSavedInClaim`; storage: `local drafts DB: databaseService.deleteReceipt after adding to claim`, `syncService.syncReceipts after save`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Claims/Create/CreateClaimViewController.swift:141-420; Modules/Employ…`
- **me-android** (Employee): screens: `NewClaimScreen`, `NewClaimLayout`, `CreateClaimKey`, `ClaimSelectionKey`; endpoints: `GET /api/v1/employees/{odpUserId}/expense/claims/template`, `GET /api/v1/employees/{odpUserId}/expense/currencies`, `PUT /api/v1/employees/{odpUserId}/expense/claims`, `POST {claim link rel=update_from_drafts / update_from_mileage_drafts / update_f…`, `POST /api/v1/expense/upsert-draft (via SaveReceiptDraftUseCase, not verified in…`; events: `Claims - expenses added to new claim`, `Claims - new claim saved`, `Cost Units - Assign CU clicked new Claims`, `Expense - multiple expenses in claim`; platform: `camera share mode: app exits after claim completes (ExpenseClaimEntries.kt:279-…` · evidence `expense/src/main/java/com/visma/employee/expense/inbox/claimselection/create/CreateClaimViewModel.kt:185-792; expense/s…`

**How they differ:**
- (platform parity) For eHRM companies, iOS copies the claim's cost units onto every receipt (CreateClaimViewController.swift:141-420). Android uses a separate eHRM save request and attaches organization unit and position to the drafts (CreateClaimViewModel.kt, ClaimSummaryViewModel.kt:484-690).
- (platform parity) iOS confirms with a full PostScreenViewController ('claim saved' or 'claim sent') (PostScreenViewController.swift:106-121). Android shows saved dialogs, and in camera share mode the app exits after the claim completes (ExpenseClaimEntries.kt:279-283).
- (platform parity) For eHRM companies, iOS copies the claim's cost units onto every receipt (CreateClaimViewController.swift:163-177, updateReceiptsWithEHrmUnitsIfNeeded). Android builds a separate eHRM save request instead (CreateClaimViewModel.kt:456-470, getSaveRequest with isEHRMCompany).
- (platform parity) iOS confirms through the delegate and a PostScreenViewController ('claim saved' or 'claim sent'). After a claim completes, Android either exits the app (camera share mode) or opens the inbox claim tab (ExpenseClaimEntries.kt:276-281).
- (platform parity) Android fetches currencies on the create flow (CreateClaimViewModel.kt:166 handleCurrenciesResponseResource; ExpenseTemplatesServiceImpl.kt:223). No currencies call is cited on the iOS create path.
- Scope note (not a fusion difference): both twins also offer 'Send for approval' from this create screen (iOS CreateClaimViewController.swift:153-161; Android CreateClaimViewModel.kt:589-670,751-792). The claim does not mention it.

_Note: referee could not confirm: The me-android implementation's 'platform' field says 'camera share mode: app exits after claim completes (ExpenseClaimEntries.kt:279-283)' instead of 'android-native'. The exit code is actually at ExpenseClaimEntries.kt:277-281._

### CAP-254: Send an expense claim for approval

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee sends a new or existing claim, with any newly added expenses, to the approver. The claim is saved first, and a server-defined confirmation may be shown.

- **me-ios** (Employee): screens: `ExpenseViewController`, `CreateClaimViewController`, `SendClaimTableViewController`, `PostScreenViewController`; endpoints: `POST {claim approval link href}`, `POST /employee/api/v1/employees/{odpUserId}/expense/claims/{claimId}/approvalRe…`; events: `Send for approval button tapped`, `newClaimSent`, `existingClaimSent`, `claimWithCommentSentForApproval`, `allowanceItemsInClaimSentForApproval`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Expense/ExpenseViewController.swift:559-623; Modules/EmployeeExpenses…`
- **me-android** (Employee): screens: `ExpenseRowsScreen`, `SelectedClaimScreen`, `NewClaimScreen`; endpoints: `PUT {claim link rel=update href}`, `POST {claim link rel=request_approval href}`, `POST /api/v1/employees/{odpUserId}/expense/claims/{claimId}/approvalRequest`; events: `EXISTING_CLAIM_SENT (Claims - existing claim sent)`, `Claims - new claim sent`, `claimWithCommentSentForApproval`, `allowanceItemsInClaimSentForApproval`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/details/ExpenseRowsViewModel.kt:548-660; expense/src/main/java/com/vis…`

**How they differ:**
- (platform parity) From the claim screen, iOS falls back to the fixed approvalRequest endpoint when the approval link has no href (ExpenseViewController.swift:559-623). Android requires a link with rel=request_approval (ExpenseServiceImpl.kt:65-104).
- (platform parity) iOS maps API errors to per-receipt messages (S.expenseSendClamReceiptsIncorrect) (CreateClaimViewController.swift:356-390). Android parses 4xx bodies into SendForApprovalError messages, and shows a generic failure dialog on the selected-claim path (SelectedClaimViewModel.kt:232-31…
- (platform parity) On the claim details screen, iOS posts to link.href and falls back to the fixed approvalRequest endpoint when href is nil (ExpenseService.swift:178-184). Android requires a link with rel=request_approval and shows a failure dialog if the link is missing (ExpenseServiceImpl.kt:65,…
- (platform parity) Android's add-drafts-to-existing-claim and new-claim paths use the fixed endpoint POST api/v1/employees/{odpUserId}/expense/claims/{claimId}/approvalRequest. It is declared in ExpensesInboxServiceImpl.kt:691, not in ExpenseServiceImpl.kt as the claim implies (called from SelectedC…
- (platform parity) iOS turns APIError into expenseClaimCreateError messages (CreateClaimViewController.swift:383-386) and shows a generic alert on the claim details path (ExpenseViewController.swift:600-605). Android parses 4xx error bodies into SendForApprovalError (ExpenseServiceImpl.kt:78-90) and…

_Note: referee could not confirm: me-android endpoint 'POST /api/v1/employees/{odpUserId}/expense/claims/{claimId}/approvalRequest' is cited under ExpenseServiceImpl.kt:65-104, but it is actually declared in expense/src/main/java/com/visma/employee/expense/inbox/data/ExpensesInboxServiceImpl.kt:691._

### CAP-255: Add new or existing expenses to a claim from the claim screen

**Fusion:** unique · **Personas:** employee · **Confidence:** High

From an open claim, the employee creates a new receipt, mileage or allowance that is saved straight into the claim, or picks existing inbox drafts to add to it.

- **me-ios** (Employee): screens: `ExpenseViewController`, `ReceiptsCoordinator (viewMode .addToClaim)`, `ReceiptScannerController`, `ReceiptDetailViewController`; endpoints: `POST {claim save-to-claim link href} (HATEOAS, via ReceiptDetailViewModel outsi…`; platform: `camera` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Expense/ExpenseViewController.swift:737-830; Modules/EmployeeExpenses…`
- **me-android** (Employee): screens: `ExpenseRowsScreen`, `add-expense bottom modal sheet`, `ExpenseInboxScreen (claim mode, single page)`; endpoints: `POST api/v1/employees/{odpUserId}/expense/claims/{id}/update-from-drafts`, `POST api/v1/employees/{odpUserId}/expense/claims/{id}/update-from-mileage-drafts`, `POST api/v1/employees/{odpUserId}/expense/claims/{id}/update-from-allowances`, `POST {claim update link}`; events: `existing allowance added to claim`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/details/ExpenseRowsViewModel.kt:124-128,183-199; expense/src/main/java…`

**How they differ:**
- (platform parity) iOS shows each option only when the matching addOrRemove* link exists, and allowance also needs canCreateAllowances and a connection (ExpenseViewController.swift:737-830). Android shows the add button when an update_from_drafts or update_from_allowance_drafts link exists, and allo…
- (platform parity) When drafts are added from the claim, Android overwrites their cost units with the claim's organization unit, positions and cost unit types (ExpenseDraftsViewModel.kt:454-525). iOS reports copying claim cost units only for eHrm companies (SaveExpenseToClaimCoordinator.swift).
- (platform parity) iOS shows each 'create new' option only when its own addOrRemoveReceipts, addOrRemoveMileages or addOrRemoveAllowances link exists. The allowance option also needs canCreateAllowances, and offline it is shown but disabled, not hidden (ExpenseViewController.swift:810-822). Android…
- (platform parity) When existing drafts are added, Android overwrites each draft's cost units with the claim's eHrmOrganizationUnit, eHrmPositions and costUnitTypes (ExpenseDraftsViewModel.kt:474-480). Android also pre-fills new receipts and mileages with the same values (ExpenseRowsEntries.kt:104-1…
- (platform parity) Android picks existing drafts in ExpenseInboxScreen claim mode and sends one POST per draft type, to update-from-drafts, update-from-mileage-drafts and update-from-allowances, in parallel. If the claim has no links it builds the claimId path itself (ExpensesInboxServiceImpl.kt:310…

_Note: referee could not confirm: The iOS side of the second divergence line is wrong. me-ios/Modules/EmployeeExpenses/Sources/EmployeeExpenses/Claims/AddExpense/SaveExpenseToClaimCoordinator.swift has no cost-unit, eHrm, position or organization-unit code, so it does not show claim cost units being copied only for eHrm companies.; The Android endpoint 'POST api/v1/employees/{odpUserId}/expense/claims/{…_

### CAP-256: Add a receipt, mileage or allowance to a claim from its form

**Fusion:** unique · **Personas:** employee · **Confidence:** High

From a receipt, mileage or allowance form, the employee saves the item and adds it to a claim they pick, or saves it straight into the claim the form was opened from ('Save to <claim>').

- **me-ios** (Employee): screens: `ReceiptDetailViewController`, `MileageView.MileageFormView`, `AllowanceInfoFeature`, `SaveExpenseToClaimCoordinator`; endpoints: `POST /employee/api/v1/expense/upsert-draft`, `POST {claim._links[rel=addOrRemoveReceipts].href}`, `POST /employee/api/v1/employees/{odpUserId}/expense/mileages`, `{claim addOrRemoveMileages link method} {link href} (SaveMileageClaim)`, `POST /employee/api/v1/expense/allowances`, `POST {claim update action href} (body: draft ids)`; events: `Save to claim button tapped`, `addMileage`, `newAllowanceSaved`; storage: `DatabaseService deleteReceipt (local draft removed after it is added to the cla…`; platform: `Reachability (disabled offline)` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/ReceiptDetailViewController.swift:2613-2639; Modules/Employe…`
- **me-android** (Employee): screens: `ExpenseDraftDetailsScreen`, `claim selection screen`, `MileageScreen`, `AllowancesStepTwoScreen (Add to claim button)`, `AllowancesStepTwoScreen (Save to claim button)`; endpoints: `POST api/v1/expense/upsert-draft`, `POST {claim link rel=update_from_drafts href}`, `POST api/v1/employees/{odpUserId}/expense/claims/{claimId}/update-from-mileage-…`, `POST api/v1/expense/allowances`, `POST {claim updateFromAllowanceDrafts link}`; events: `NEW_RECEIPT_ADD_TO_CLAIM_BUTTON_CLICKED`, `Mileages - new mileage add to claim clicked`, `Allowances - New allowance added to claim`, `Allowances - Existing allowance added to claim`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/inbox/details/ExpenseDraftDetailsViewModel.kt:1757-1823; expense/src/m…`

**How they differ:**
- (platform parity) Android shows 'Add to claim' on an allowance only when the allowance is not a claim item and has travels (AllowancesStepTwoViewModel.kt:925-938). iOS only requires the form to be valid first (DraftRepository.allowanceSaveToClaim.swift:17-34).
- (platform parity) iOS removes the local inbox copy after the item is added (DraftRepository.receiptSaveToClaim.swift:16-45). Android does not report removing a local copy (ExpenseDraftDetailsViewModel.kt:1757-1823).
- (platform parity) Android shows the allowance 'Add to claim' button only when the allowance has travels, and this is decided in the screen (AllowancesStepTwoScreen.kt:125-127). The cited ViewModel range only checks isDataValid (AllowancesStepTwoViewModel.kt:925-938). On iOS, DraftRepository.allowan…
- (platform parity) iOS deletes the local draft once it is in the claim, calling databaseService.deleteReceipt in all three repositories (DraftRepository.receiptSaveToClaim.swift:35, DraftRepository.mileageSaveToClaim.swift:37, DraftRepository.allowanceSaveToClaim.swift:33). No local delete was seen…
- (platform parity) When a receipt's purpose is empty, Android fills it with the claim title (preFillPurpose, ExpenseDraftDetailsViewModel.kt:1771-1780). iOS lets the receipt save without a purpose and relies on the purpose being filled in during the add-to-claim step (comment at ReceiptDetailViewCon…
- (platform parity) Android mileage validates at CLAIM_BOUND when editing an item already in a claim and at CLAIM_PENDING otherwise (MileagesViewModel.kt:1424-1425). iOS receipts validate at .claimPending (ReceiptDetailViewController.swift:2621).

_Note: referee could not confirm: The Android allowance visibility rule is cited at AllowancesStepTwoViewModel.kt:925-938, but it is actually in AllowancesStepTwoScreen.kt:125-127.; 'iOS only requires the form to be valid first' is cited to DraftRepository.allowanceSaveToClaim.swift:17-34, but that file has no validity check._

### CAP-257: Send a single expense straight for approval

**Fusion:** unique · **Personas:** employee · **Confidence:** High

From a receipt, mileage or allowance form, the employee sends that one item for approval without building a claim. A confirmation can be turned off with 'don't show again'. If the server rolls the item back, the returned draft is reopened.

- **me-ios** (Employee): screens: `ReceiptDetailViewController`, `MileageView`, `AllowanceInfoFeature`, `submitForApprovalAlert`, `PostScreenViewController`; endpoints: `POST /employee/api/v1/expense/send-draft-for-approval (multipart)`; events: `Submit for approval button tapped`, `directSendForApprovalSuccess`, `directSendForApprovalFailure`; storage: `UserDefaults Keys.expenseSubmitForApprovalDontShowAgain`, `Local receipts database (draft deleted on success, rolled-back draft imported)`; platform: `Reachability (button disabled offline)` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/ReceiptDetailViewController.swift:666-839; Modules/EmployeeE…`
- **me-android** (Employee): screens: `ExpenseDraftDetailsScreen`, `MileageScreen`, `AllowancesStepTwoScreen (Send for approval button)`, `SendForApprovalConfirmation dialog`, `SuccessDialog`; endpoints: `POST api/v1/expense/send-draft-for-approval`; events: `Expense - Direct send for approval success`, `Expense - Direct send for approval failure`; storage: `UserPreferencesRepository sendForApprovalDontShowAgain (per user email)`, `SharedPreferences:SEND_FOR_APPROVAL_DONT_SHOW_AGAIN`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/inbox/details/ExpenseDraftDetailsViewModel.kt:2022-2158; expense/src/m…`

**How they differ:**
- (platform parity) iOS keeps the 'don't show again' flag in UserDefaults key expenseSubmitForApprovalDontShowAgain, not scoped to a user (ReceiptDetailViewController.swift:666-839). Android keys it per user email (ExpenseDraftDetailsViewModel.kt:2022-2158), but one Android fragment says it is keyed…
- (platform parity) After success, iOS shows a post-submit screen and then opens the Claims tab (AllowanceInfoFeature.swift:315-351). Android shows a success dialog and opens the claims tab (AllowancesStepTwoViewModel.kt:1794-1926).
- (platform parity) iOS keeps the 'don't show again' flag as one global UserDefaults bool, Keys.expenseSubmitForApprovalDontShowAgain, which is not scoped to a user (AppUserPreferences.swift:140-145). Android keeps it per user in the Room UserPreferencesRepository (UserPreferencesRepositoryImpl.kt:11…
- (platform parity) After success, iOS shows PostScreenViewController(reason: .approval) and posts resetCalendar and reloadStartPage (ReceiptDetailViewController.swift:795-810). Android shows a success dialog with mNavigator.showSendForApprovalSuccessDialog (ExpenseDraftDetailsViewModel.kt:2124).
- (platform parity) On a rollback, iOS imports the returned draft into the local receipts database, databaseService.importDraft (ReceiptDetailViewController.swift:816, ExpenseMileageViewModel.swift:1882, AllowanceInfoFeature.swift:534). Android does not import it. For a new receipt it reopens the dra…
- (platform parity) iOS disables the send-for-approval button when offline (sendForApprovalButton.isEnabled = reachabilityService.isOnline, ReceiptDetailViewController.swift:943). The cited Android send path does not appear to check connectivity before sending (ExpenseDraftDetailsViewModel.kt:2054-20…

_Note: referee could not confirm: me-android storage 'SharedPreferences:SEND_FOR_APPROVAL_DONT_SHOW_AGAIN': the constant PREF_SEND_FOR_APPROVAL_DONT_SHOW_AGAIN is declared in SendApprovalPreferences.kt:15 and nothing uses it. The real storage is the Room UserPreferencesRepository (UserPreferencesRepositoryImpl.kt:118).; me-ios Services/SubmitExpenseForApprovalClient.swift is only a 25-line closure-type…_

### CAP-258: Review an expense claim's details

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee opens a claim and sees its status, any status-change reason, the receipts, mileages and allowances grouped by category, the total, the amount paid by the company, and the actions the server allows.

- **me-ios** (Employee): screens: `ExpenseViewController`, `PresentExpenseCoordinator`; endpoints: `GET {claim self link href} (claimRepository.fetchEditClaimData)`; events: `claimOpened`; storage: `UIPasteboard (claim ID copy)`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Expense/ExpenseViewController.swift:1015-1074; Employee/Expenses/Coor…`
- **me-android** (Employee): screens: `ExpenseRowsScreen`, `ExpenseRowsKey`; endpoints: `GET api/v1/employees/{odpUserId}/expenseclaims/{claimId}`, `GET api/v1/employees/{odpUserId}/expense/claims/template`; platform: `connectivity listener reloads the claim when the device comes back online` · evidence `expense/src/main/java/com/visma/employee/expense/details/ExpenseRowsViewModel.kt:314-417; expense/src/main/java/com/vis…`

**How they differ:**
- (platform parity) iOS shows the claim ID with tap-to-copy, who registered it, and approval status rows (ExpenseViewController.swift:1015-1074). Android fragments show claim totals and rows, but no copyable ID or 'registered by' is reported (ExpenseRowsViewModel.kt:314-417).
- (platform parity) Android reloads the claim automatically when the device comes back online (ExpenseRowsViewModel.kt). No such reload is reported on iOS.
- (platform parity) Both twins show the claim ID with tap-to-copy: iOS at ExpenseViewController.swift:330 (UIPasteboard plus claimIDCopied toast) and Android at ExpenseRequestStatusRow.kt:39-47 (LocalClipboard.setText, no toast string reported). The claim was wrong to say Android has no copyable ID.
- (platform parity) iOS shows a 'registered by' (secretaries) row (ExpenseViewController.swift:364, SecretariesRowView). No registered-by or secretaries code was found in the me-android expense module.
- (platform parity) Android reloads the whole claim when the connection comes back (ExpenseRowsViewModel.kt:270-279, observeConnectionRestored calls load()). iOS listens for reachability changes but only refreshes its buttons, with no reload (ExpenseViewController.swift:1231-1233, updateButtonsAfterR…
- (platform parity) Android shows a CO2 figure when the context has the sustainability permission (ExpenseRowsViewModel.kt, _co2) and project-accounting and cost-unit data on the details screen (ExpenseRowsScreen.kt:155-165). The claim does not mention this, and it was not verified on iOS.

_Note: referee could not confirm: me-android implementation 'platform' field holds a behaviour description ('connectivity listener reloads the claim...') instead of 'android-native'; Claim's first parity line states Android has no copyable claim ID; ExpenseRequestStatusRow.kt:39-47 implements copy-to-clipboard_

### CAP-259: Edit a claim's title and comment

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee changes an open claim's title (description) and comment and saves them back to the claim.

- **me-ios** (Employee): screens: `ExpenseViewController`, `SendClaimTableViewController`, `PresentExpenseCoordinator`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/expense/claims/template`, `GET /employee/api/v1/employees/{odpUserId}/expenseclaims/{claimId}`, `PUT {claim link rel update href} (method from link, default PUT)`; events: `existingClaimDescriptionEdited`, `claimDescriptionEdited`, `claimCommentsEdited`, `claimOpened`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Expense/EditExpenseViewModel.swift:115-265; Modules/EmployeeExpenses/…`
- **me-android** (Employee): screens: `ExpenseRowsScreen`, `SelectedClaimScreen`; endpoints: `PUT {claim link rel=update href}`, `POST/PUT (HATEOAS update link of the claim)`; events: `claimEdited`, `claimDescriptionEdited`, `Claims - Claim edited`, `Claims - Claim description edited`, `Claims - Claim with comment`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/details/ExpenseRowsViewModel.kt:789-907; expense/src/main/java/com/vis…`

**How they differ:**
- (platform parity) Android allows editing only while the claim status is Open, Cancelled or Rejected (ExpenseRowsViewModel.kt:789-907). iOS allows it whenever the claim has an 'update' link (EditExpenseViewModel.swift:115-265). These rules can disagree.
- (platform parity) Android fires the claim-edited event once per screen, and only when something changed (SnowplowEditClaimEventHandlerImpl.kt:12-98). iOS fires description and comment events per changed value (ExpenseViewController.swift:172-222).
- (platform parity) Android lets you edit only when the claim status is Open, Cancelled or Rejected (ExpenseRowsViewModel.kt:400-402, canEditClaim). It also fails the save if there is no update link (ExpenseRowsViewModel.kt:886-888). iOS decides editability only from whether the claim has an 'update'…
- (platform parity) Android sends claimEdited only once per screen, and only if something changed (SnowplowEditClaimEventHandlerImpl.kt:12-25). It sends claimDescriptionEdited only if the title changed (lines 27-38). iOS sends existingClaimDescriptionEdited plus claimDescriptionEdited when the descri…
- (platform parity) Both twins send cost units and project accounting in the same update request as the title and comment (EditExpenseViewModel.swift:237-246; ExpenseRowsViewModel.kt:866-878). The payloads match, so this is not a gap.
- (platform parity) After saving, Android shows a changes-saved dialog (UiEvent.ShowChangesSavedDialog) and a failure dialog that uses expense_claim_update_claim_description_and_comment_failed_default_text. iOS closes the screen through the delegate (savedClaimWith: .later) and shows a generic error…

_Note: referee could not confirm: The Android divergence line cites ExpenseRowsViewModel.kt:789-907 for the Open/Cancelled/Rejected rule. That rule is actually at ExpenseRowsViewModel.kt:400-402._

### CAP-260: Withdraw a claim from approval

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee cancels the approval request of a claim they already sent, after an optional server-defined confirmation. The claim then reloads.

- **me-ios** (Employee): screens: `ExpenseViewController (Cancel approval button)`; endpoints: `DELETE {claim cancel link href}`; events: `claimCancelled`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Expense/ExpenseViewController.swift:625-686`
- **me-android** (Employee): screens: `ExpenseRowsScreen`, `ExpenseRowsKey`; endpoints: `DELETE {claim link rel=cancel href}`; events: `CLAIM_CANCELED`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/details/ExpenseRowsViewModel.kt:662-708; expense/src/main/java/com/vis…`

**How they differ:**
- (platform parity) After cancelling, iOS also resets the calendar (ExpenseViewController.swift:625-686). Android only reloads the claim and parses user errors into CancelClaimError (ExpenseServiceImpl.kt:156-195).
- (platform parity) After a successful cancel, iOS reloads the claim and also posts AppMessage.resetCalendar (ExpenseViewController.swift:672-674). Android only calls load() (ExpenseRowsViewModel.kt:686-688).
- (platform parity) Android turns 4xx user errors into CancelClaimError with the server's messages and errors (ExpenseServiceImpl.kt:166-183). iOS shows AppCoreUtils.getDefaultResponseMessage in a generic error alert (ExpenseViewController.swift:655-660).
- (platform parity) Android logs CLAIM_CANCELED before the request, whether or not it succeeds (ExpenseRowsViewModel.kt:678). iOS logs claimCancelled only after the request succeeds (ExpenseViewController.swift:653).
- (platform parity) iOS shows the confirmation as an action sheet with a destructive confirm button (ExpenseViewController.swift:628-633). Android uses a generic confirmation dialog (ExpenseRowsViewModel.kt:669-674). Android also has a separate error for a missing cancel link (expense_claim_cancel_re…

### CAP-261: Delete an expense claim

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee confirms and deletes a claim they no longer need, and the claim screen closes.

- **me-ios** (Employee): screens: `ExpenseViewController (More actions sheet)`; endpoints: `DELETE {claim delete link href}`; events: `claimDeleted`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Expense/ExpenseViewController.swift:625-686`
- **me-android** (Employee): screens: `ExpenseRowsScreen`, `ExpenseRowsKey`; endpoints: `DELETE {claim link rel=delete href}`; events: `CLAIM_DELETED`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/details/ExpenseRowsViewModel.kt:710-748; expense/src/main/java/com/vis…`

**How they differ:**
- (platform parity) iOS places delete in a More actions sheet and runs a receipts sync after deleting (ExpenseViewController.swift:625-686). Android shows a delete button with a local confirmation dialog and closes with CLAIM_DELETE_OK (ExpenseRowsScreen.kt:341-353).
- (platform parity) iOS puts Delete in the More actions sheet (ExpenseViewController.swift:795-799) and confirms in an action sheet with S.Expense.Claim.deleteClaimConfirmationMessage (:723-735). Android confirms in a ConsentDialog with expense_delete_claim_dialog_title and expense_delete_claim_dialo…
- (platform parity) iOS may ask a second time: if the server sends link.confirmation, the delete path shows that confirmation too (ExpenseViewController.swift:627-633). Android shows only its local dialog.
- (platform parity) iOS closes the screen straight away through expenseViewControllerDidDeleteClaim and then runs syncService.syncReceipts() (ExpenseViewController.swift:653-658). Android first shows a success dialog (expense_delete_claim_deleted) and then closes with CLAIM_DELETE_OK (ExpenseRowsView…
- (platform parity) Android logs CLAIM_DELETED before the request, even if the delete then fails (ExpenseRowsViewModel.kt:712). iOS logs .claimDeleted only after the request succeeds (ExpenseViewController.swift:641-643).
- (platform parity) Error handling differs. iOS shows a generic alert with the default response message (ExpenseViewController.swift:645-651). Android parses a DeleteClaimError from the error body and shows a failure dialog, falling back to expense_delete_claim_failed (ExpenseServiceImpl.kt:124-141,…

### CAP-262: View, edit or delete an item inside a claim

**Fusion:** unique · **Personas:** employee · **Confidence:** High

From a claim, the employee opens a receipt, mileage or allowance. It is read-only when the claim cannot be changed, and can be edited, saved or deleted through the claim's links when it can.

- **me-ios** (Employee): screens: `ExpenseViewController`, `EditReceiptInClaimCoordinator`, `EditMileageInClaimCoordinator`, `EditAllowanceInClaimCoordinator`, `ReceiptDetailViewController (editInClaim)`, `MileageView.MileageFormView (previewFromClaim / updateFromClaim)`, `AllowanceView (previewFromClaim / updateFromClaim)`; endpoints: `GET {receipt load link href}`, `{receipt link rel update href}`, `{receipt link rel delete href}`, `POST {updateAction.href} (method from action, default POST, multipart)`, `GET {mileage self link href}`, `{update link method} {update link href}`, `GET {claim allowance load action href}`; events: `receiptPreviewInClaim`, `receiptEditedInClaim`, `receiptDeletedInClaim`, `mileagePreviewInClaim`, `mileageEditedInClaim`, `mileageDeletedInClaim`, `claimItemEdited`, `claimItemDeleted` …; storage: `syncService.sync after change`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Expense/ExpenseViewController.swift:498-551; Modules/EmployeeExpenses…`
- **me-android** (Employee): screens: `ExpenseRowsScreen`, `ExpenseDraftDetailsScreen`, `MileageScreen (preview/edit state)`, `AllowancesStepTwoScreen (preview mode)`; endpoints: `GET {EditClaimDraftData.getDraftLink href}`, `POST {draft update link href} (multipart)`, `POST {draft update-mileage link} (multipart draft)`; events: `editedMileageInClaim`, `deletedMileageInClaim`, `editedReceiptInClaim`, `deletedReceiptInClaim`, `Claims - Receipt preview in claim`, `Claims - Mileage preview in claim`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/details/ExpenseRowsViewModel.kt:237-268; expense/src/main/java/com/vis…`

**How they differ:**
- (platform parity) Android first shows a read-only preview with an Edit button when the item is editable (PreviewButtonLayout.kt:26-65). iOS opens straight into edit mode when an 'update' link exists, and into preview otherwise (EditMileageInClaimCoordinator.swift:50-143).
- (platform parity) Android shows a toast when the employee returns after editing or deleting (ExpenseRowsViewModel.kt:237-268). iOS shows the server's confirmation success message on delete (EditReceiptInClaimCoordinator.swift:55-140).
- (platform parity) Android opens an editable item as a read-only preview first, with an Edit button that switches to edit mode and then a 'Save changes' button (PreviewButtonLayout.kt:26-65). iOS opens straight into updateFromClaim when an update link exists (EditMileageInClaimCoordinator.swift:64,…
- (platform parity) Android shows a local toast string after an edit or delete (ExpenseRowsViewModel.kt:237-268). iOS shows the server's confirmation successMessage, and only on delete (EditReceiptInClaimCoordinator.swift:87-91, EditMileageInClaimCoordinator.swift:89-99).
- (platform parity) Android logs no edited or deleted analytics event for allowances, only toasts (ExpenseRowsViewModel.kt:254-256). It does log them for mileage and receipts. iOS tracks every item type through claimItemEdited and claimItemDeleted.

### CAP-263: Assign cost units to an expense or claim

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee picks cost-allocation dimension values for a receipt, mileage, allowance or claim from searchable, paged lists (for eHRM companies, organization unit and position with defaults), optionally splits the cost, and saves.

- **me-ios** (Employee): screens: `CostUnitsView`, `SplitCostUnitsView`, `CostUnitsFormView`, `AllowanceCostUnitsFeature`, `EditCostUnitsFeature`, `ReceiptDetailViewController`; endpoints: `GET {template costUnits link href per costUnitTypeId, paged via rel next}`, `GET {costUnits link href with search query param}`, `GET {link rel eHrmOrganizationUnits href}`, `GET {link rel eHrmPositions href}`, `GET /employee/api/v1/employees/expense/eHrmDefaults`, `PUT {claim link rel update href}`, `GET {cost unit link href from allowance template} (list/search cost units)`; events: `costUnitsSavedInClaim`, `costUnitsSavedInReceipt`, `costUnitsSavedInAllowance`, `costUnitsCleared`, `costUnitsEdited`, `assignSplitCostUnitsInEditClaimButtonTapped`, `Cost units type cell tapped`; storage: `realm-model:RealmFrequentlyUsedCostUnits`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/CostUnits/ViewModel/ClaimCostUnitsViewModel.swift:102-250; Modules/Em…`
- **me-android** (Employee): screens: `CostUnitSelectionScreen`, `CostUnitSelectionKey`, `DimensionSelectionScreen`, `ExpenseRowsScreen`, `ExpenseDraftDetailsScreen`; endpoints: `GET {cost unit dimension link}?query=&organizationUnitId=`, `GET /api/v1/employees/expense/eHrmDefaults?organizationUnitId=&positionId=`, `PUT {claim link rel=update href}`, `POST api/v1/expense/upsert-draft`; events: `ASSIGN_COST_UNITS_CLICKED_IN_EDIT_CLAIM_SCREEN`, `ASSIGN_SPLIT_COST_UNITS_CLICKED_IN_EDIT_CLAIM_SCREEN`, `COST_UNITS_SUCCESSFULLY_SAVED_IN_CLAIM_SCREEN`, `ASSIGN_COST_UNITS_CLICKED_IN_NEW_RECEIPT_SCREEN`, `Cost Units - Dimension cleared`; storage: `Room FrequentlyUsedCostUnitDbModel / FrequentlyUsedCostUnitTypeDbModel via Temp…`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/dimension/CostUnitSelectionViewModel.kt:99-591; expense/src/main/java/…`

**How they differ:**
- (platform parity) Android locks claim cost units when the claim is Sent, Paid or Approved, and turns the field off when offline (ExpenseRowsViewModel.kt:419-467). iOS decides by whether the claim is read-only (ClaimSaver.readOnly) (ClaimCostUnitsViewModel.swift:102-250).
- (platform parity) Android hides receipt cost units for eHRM companies unless the receipt is edited inside a claim (ExpenseDraftDetailsViewModel.kt:569-577). iOS uses EHrmDraftCostUnitsFormViewModel with the claim organization unit on the receipt (ReceiptDetailViewController.swift:2344-2392).
- (platform parity) Android recently used cost units are sorted by timesUsed and can be deleted (CostUnitSelectionViewModel.kt). iOS keeps frequently used cost units in Realm, and deletion is not reported (RealmService.swift:849-895). iOS searches remotely only when the link supports a query param an…
- (platform parity) Android turns the claim cost-unit field off based on costUnitsShouldBeEditable and connectionStateFlow (ExpenseRowsViewModel.kt:419-467). iOS turns the fields off when claimSaver.canSaveCostUnits is false (ClaimCostUnitsViewModel.swift:190-194).
- (platform parity) Android can delete frequently used cost units (CostUnitSelectionViewModel.kt:377) and sorts them by timesUsed (line 204). I found no deletion on iOS in the cited files, where frequently used cost units are kept in Realm (RealmFrequentlyUsedCostUnits.swift).
- (platform parity) Android waits searchTextDelayAmount before a remote search (CostUnitSelectionViewModel.kt:527). The iOS eHRM fetcher loads a single page and then sets fetchNextPageAction to nil, so it does no paging (CostUnitsFetcher.eHrm.swift:18-33).

_Note: Not merged with CAP-013 'Pick cost-unit dimension values for a registration': that one is about absence registrations, a different outcome._

### CAP-264: Assign project accounting to an expense or claim

**Fusion:** unique · **Personas:** employee at a project-accounting company · **Confidence:** High

In a company that uses project accounting, the employee picks a project, a dependent task and a reinvoice-on-project choice for a receipt, mileage, allowance or claim, using searchable paged pickers.

- **me-ios** (Employee): screens: `ProjectAccountingView`, `ProjectAccountingFormCellView`, `AllowanceProjectAccountingFeature`, `EditProjectAccountingFeature`, `CreateClaimViewController`; endpoints: `GET {template link rel=projects href}?query={search}`, `GET {template link rel=projectTasks href}?projectId={projectId}&query={search}`, `PUT {claim link rel update href}`; events: `assignProjectAccountingInNewReceiptButtonTapped`, `assignProjectAccountingInNewMileageButtonTapped`, `projectAccountingSavedInReceipt`, `projectAccountingSavedInAllowance`, `projectAccountingSavedInClaim`, `projectAccountingCleared`, `projectAccountingEdited`; storage: `Receipt projects/projectTasks links from local DB (receiptProjectsLink)`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/ProjectAccounting/ViewModel/ProjectAccountingFormViewModel.swift:1-21…`
- **me-android** (Employee): screens: `ProjectAccountingSelectionScreen`, `ProjectAccountingSelectionKey`, `ExpenseRowsScreen`, `ExpenseDraftDetailsScreen`; endpoints: `GET {projects link}?query=`, `GET {tasks link}?projectId=&query=`, `PUT {claim link rel=update href}`, `POST api/v1/expense/upsert-draft`; events: `Project Accounting - PA saved *`, `Project Accounting - Project allocation edited`, `Project Accounting - Project cleared`, `ASSIGN_PROJECT_ACCOUNTING_CLICKED_IN_EDIT_CLAIM_SCREEN`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/project_accounting/selection/ProjectAccountingSelectionViewModel.kt:21…`

**How they differ:**
- (platform parity) On Android, a claim's project accounting follows the same status lock as its cost units (not Sent, Paid or Approved) (ExpenseRowsViewModel.kt:469-546). On iOS, it is saved through ClaimSaver when canSaveProjectAccounting is true (ProjectAccountingFormViewModel.swift).
- (platform parity) iOS shows the fields only with the company feature companyUsesProjects and when the template has financialsproject or financialstask fields. Android uses isProjectAccountingCompany() (ProjectAccountingFieldViewModel.kt:64-136).
- (platform parity) On Android, a claim's project accounting field can be edited only when shouldBeEditable is true (status-driven, ExpenseRowsViewModel.kt:469-546). iOS ClaimSaver.updateExpenseClaim always sets canSaveProjectAccounting: true (ClaimSaver.UpdateExpenseClaim.swift:27-28).
- (platform parity) Android gates on mContextService.isProjectAccountingCompany() (ExpenseRowsViewModel.kt:476). iOS requires both userService.hasAccessForCompany(feature: .companyUsesProjects) and financials project/task fields in the template (ReceiptDetailViewModel.swift:872-874).
- (platform parity) Android finds the tasks link in the projects response links, matched on project id metadata (ProjectAccountingSelectionViewModel.kt:284-296). iOS takes the projectTasks link from the template or local DB (SyncReceiptTemplatesTask.swift:47-50, ExpenseProjectAccountingDataSource.swi…
- (platform parity) The Android project accounting field reads connection state through isOnlineStateFlow (ExpenseRowsViewModel.kt, mapProjectAccountingFieldsToOneField), and its own validation is handed to the picker (ProjectAccountingFieldViewModel.kt:135 isValid always true). iOS validates each fi…
- Not a shared capability with vmm: vmm's project/projectTask editing is for a manager on supplier invoice lines in approval tasks (ApprovalTaskEditFinancialsLinesScreen.tsx:153-178, financialsUtils.ts:178-230, 364-369). It is a separate capability.

_Note: referee could not confirm: ProjectAccountingSelectionKey was not checked as a screen; it is probably a navigation key, not a screen; The event names 'Project Accounting - PA saved *' etc. for Android were not checked; they are listed as reported_

### CAP-265: Log a business-trip mileage and save it as a draft

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee fills in or edits a mileage from the company mileage template (date, vehicle and fuel type, trip type, purpose, distance, passengers, cost units, project) and saves it as a draft. When offline it is kept locally and synced later.

- **me-ios** (Employee): screens: `MileageView.MileageFormView`, `AddMileageCoordinator`, `EditMileageCoordinator`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/expense/templates/mileage`, `POST /employee/api/v1/employees/{odpUserId}/expense/mileages`; events: `saveNewMileageTapped`, `addMileage`, `editMileage`, `costUnitsSavedInMileages`, `projectAccountingSavedInMileage`; storage: `Local receipts database (mileage draft stored via databaseService; the AppNetEr…`, `AppState mileage.isEditingPlaces`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Mileage/ViewModels/ExpenseMileageViewModel.swift:1707-1755; Modules/E…`
- **me-android** (Employee): screens: `MileageScreen`, `MileageContent (MileageHomeKey, route mileages)`, `Mileage draft details`; endpoints: `GET api/v1/employees/{odpUserId}/expense/templates/mileage`, `POST api/v1/employees/{odpUserId}/expense/mileages`, `POST {draft update-mileage link} (multipart draft)`; events: `show_mileage_screen`, `add_mileage`, `edit_mileage`, `COST_UNITS_SUCCESSFULLY_SAVED_IN_MILEAGE_SCREEN`, `Mileages - new mileages created`, `Mileages - passengers added`; storage: `Room databaseDao mileage template cache (MileageTemplateCacheModel)`, `Offline draft storage (saveMileageDraftUseCase saveOfflineOnError=true)`; platform: `offline queue on UnknownHostException`, `date picker dialog` · evidence `expense/src/main/java/com/visma/employee/expense/compose/MileageScreen.kt:109-385; expense/src/main/java/com/visma/empl…`

**How they differ:**
- (platform parity) On Android, switching the trip-type template copies matching fields, and the initial template comes from the last-used preference (MileagesViewModel.kt:386-446). On iOS the form comes from the active mileage type; template switching is not reported (ExpenseMileageViewModel.swift:1…
- (platform parity) iOS defaults passenger distance to the trip length. Android sets the first passenger's distance only when that field is hidden (RepeatableFieldViewModel.kt:36-271).
- (platform parity) Android number fields turn commas into dots and truncate to template precision (MileageScreen.kt:109-385). The equivalent is not reported on iOS.
- (platform parity) Android picks the initial trip-type template from the draft's tripType value or the saved mileage preferences (GET/POST api/v1/employees/{odpUserId}/expense/preferences, MileagesViewModel.kt:927-980, MileagesApi.kt:52-57) and writes the preferences back after a successful save (Sa…
- (platform parity) Offline editing: on Android, editing a draft that has an UPDATE_MILEAGE link goes through saveMileageFromLink, which catches only HttpException. There is no UnknownHostException offline fallback there (MileagesServiceImpl.kt:207-237), so offline edits of server drafts fail. On iOS…
- (platform parity) iOS defaults passenger distance to the trip length. Android sets the first passenger's distance only when that field is hidden (RepeatableFieldViewModel.kt:36-271). This is taken from the claim and was not re-verified.
- (platform parity) Android number fields turn commas into dots and truncate to template precision (MileageScreen.kt:109-385). No equivalent is reported on iOS. This is taken from the claim and was not re-verified.

_Note: referee could not confirm: me-android MileagesViewModel.kt:386-446 is the ViewModel init block, not the template-switching or last-used-preference logic; that logic is at MileagesViewModel.kt:927-980 (fetchTemplates/getSelectedTemplate); me-android implementation 'platform' field lists behaviours ('offline queue on UnknownHostException', 'date picker dialog') instead of android-native_

### CAP-266: Plan a mileage route and calculate its distance

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee sets a start point, destinations and waypoints by address search, map tap, current location or recent places. They can reorder stops and add a return trip, and the app fetches driving directions and fills in the distance.

- **me-ios** (Employee): screens: `CalculateDistanceInputFormView`, `Route overview`, `PlacePickerView`, `LocationPickerView`, `SelectWaypointView`, `RouteWaypointView`; endpoints: `POST /employee/api/v1/maps/directions`, `GET /employee/api/v1/maps/getPlace`; events: `editMileageRouteUsed`, `selectPlaceOnMapTapped`, `destinationSelectedOnMap`, `searchResultUsed`, `searchRequestsCountPerPlaceSearchSession`; storage: `Local places database (createPlace/updatePlace/deletePlace/allPlaces: recent or…`, `realm-model:RealmMEPlace`, `in-memory cache keyed by placeIDs`; platform: `CoreLocation when-in-use location (Employee/Info.plist:48)`, `Google Places autocomplete SDK (Modules/GoogleMapsProvider)`, `Google Maps SDK map picker` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Mileage/ViewModels/ExpenseMileageViewModel.swift:1259-1327; Modules/E…`
- **me-android** (Employee): screens: `MapScreen (mileages.map)`, `MileageDestinationScreen (mileages.destination)`, `MileageMapDestinationScreen (mileages.map.destination)`, `ExpenseRouteOverview`, `RenderMap`; endpoints: `POST /api/v1/maps/directions`, `GET /api/v1/maps/getPlace`; events: `Mileages - search requests`, `Mileages - search result used`, `Mileages - select on map clicked`, `MILEAGE_DESTINATION_SELECTED_ON_MAP (Mileages - destination selected on map)`, `returnTripUsed`, `mileageRouteEdited`, `destinationsPerMileage`; storage: `Room MileageLocationDbModel (recent searched places, max 4) via MileageLocation…`; platform: `ACCESS_FINE_LOCATION runtime permission`, `Google Maps Compose map`, `Google Places autocomplete (PlacesSearchManager)`, `FusedLocation current location` · evidence `expense/src/main/java/com/visma/employee/expense/destination/screens/MileagesDestinationScreen.kt:78-560; expense/src/m…`

**How they differ:**
- (platform parity) Android keeps at most 4 recent searched places (MAX_CACHED_LOCATIONS) (MileagesDestinationScreen.kt:78-560). iOS keeps frequently used places in a local places DB with no limit reported (PlacePickerViewModel.swift:70-166, RealmService.swift:808).
- (platform parity) Android requests alternative routes and lets the employee pick one on the map, with the first selected by default (MileageRouteManager.kt:148-350). iOS requests routes including alternatives, but route picking is not reported (GMDirectionsService.swift:24-89).
- (platform parity) When location permission is denied, Android shows a snackbar with an open-settings action (MileagesDestinationScreen.kt). iOS asks only when the status is notDetermined (PlacePickerViewModel.swift).
- (platform parity) Android keeps at most 4 recent searched places. MAX_CACHED_LOCATIONS = 4 is defined in CachingRepository.kt:125, enforced at CachingRepository.kt:70 and applied in MileagesDestinationScreen.kt:107. On iOS, frequently used places are stored in a Realm places database (RealmMEPlace)…
- (platform parity) Android lets the employee choose among alternative routes (MileageRouteManager.kt:321 selectRoute). iOS requests alternatives (MileageRoute.swift:259 alternatives: true) but only ever selects the first route (ExpenseMileageViewModel.swift:1294-1296). In the Mileage views I found n…
- (platform parity) When location permission is denied, Android shows a message with an open-settings action (MileageMapDestinationScreen.kt:92-94). The iOS LocationPickerViewModel.swift:56 only looks up the current location if it is enabled or permission has not been asked yet. The claim cites Milea…

_Note: referee could not confirm: The Android open-settings message for denied location permission is cited to MileagesDestinationScreen.kt. The strings are actually used in MileageMapDestinationScreen.kt:92-94.; The 4-place limit is cited as MileagesDestinationScreen.kt:78-560. The constant and its enforcement are in viewmodel/destination/CachingRepository.kt:70,125; the screen only applies it at line…_

### CAP-267: Calculate road tolls automatically for a mileage trip

**Fusion:** unique · **Personas:** employee · **Confidence:** High

With automatic road-toll calculation on, the app sends the route with fuel type, rush-hour and AutoPASS settings and fills in the road toll amount, which the employee can edit or delete. Saving waits until the calculation is done.

- **me-ios** (Employee): screens: `MileageView.MileageFormView`; endpoints: `POST /employee/api/v1/employees/expense/mileages/calculateRoadToll`; events: `valuesFromAutomaticCalculationsWasEdited`, `valuesFromAutomaticCalculationsWasDeleted`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Mileage/ViewModels/ExpenseMileageViewModel.swift:1342-1374`
- **me-android** (Employee): screens: `MileageDestinationScreen (road tolls switch)`, `MileageScreen`, `MileageKey`; endpoints: `POST api/v1/employees/expense/mileages/calculateRoadToll`; events: `Mileages - Calculate Automatic Road Tolls Toggled`, `Mileages - Calculate Automatic Road Tolls rush hour toggled`, `Mileages - Calculate Automatic Road Tolls auto pass toggled`, `Mileages - Calculate Automatic Road Tolls value was edited`, `Mileages - Calculate Automatic Road Tolls value was deleted`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/viewmodel/MileagesViewModel.kt:1773-1916; expense/src/main/java/com/vi…`

**How they differ:**
- (platform parity) Android puts the automatic road-toll toggle on the destination screen (MileageScreen.kt:617-625). iOS puts it in the mileage form (AutomaticRoadTollToggleViewModel.swift). Where the toggle value is stored also differs; see 'Remember my mileage defaults'.
- (platform parity) Toggle location: Android puts the switch on the destination screen, in AutomaticallyCalculateRoadTollSwitch at MileagesDestinationScreen.kt:267-290. iOS puts it in the mileage form as a form field (FormFieldID.automaticRoadTollToggle, AutomaticRoadTollToggleViewModel.swift).
- (platform parity) Failure handling: iOS shows the 'unable to calculate road toll' banner (ExpenseMileageViewModel.swift:1703-1705). On an error, Android calls navigator.onSaveButtonPressWhileCalculatingRoadToll(), which shows the 'still calculating' prompt (MileagesViewModel.kt:1875-1881). Android…
- (platform parity) Save while calculating: iOS shows an error banner with S.Expense.Mileage.calculatingRoadTollAmount (ExpenseMileageViewModel.swift:1693-1700). Android sends the user to a navigator callback (MileageScreenNav3.kt:231, called from MileageScreen.kt:454/494/577).
- (platform parity) Request shape: Android sends explicit route and returnRoute coordinate lists (CalculateRoadTollRequest.kt). iOS passes an isReturnTrip flag to RoadTollCalculator through RoadTollCalculationConfig (ExpenseMileageViewModel.swift:1360).

_Note: referee could not confirm: me-android MileageScreen.kt:617-625 is HandleRoadTollEvents, the handler that writes the calculated amount into the road-toll field. It is not the toggle. The toggle is at expense/src/main/java/com/visma/employee/expense/destination/screens/MileagesDestinationScreen.kt:267-290.; The iOS strings use the keys expense.mileage.calculatingRoadTollAmount and expense.mileage.u…_

### CAP-268: Remember my mileage defaults

**Fusion:** unique · **Personas:** employee · **Confidence:** High

New mileages start with the employee's last fuel type, vehicle or trip type, rush-hour, AutoPASS and automatic road-toll choices, saved locally and on the server.

- **me-ios** (Employee): screens: `MileageView.MileageFormView`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/expense/preferences`, `POST /employee/api/v1/employees/{odpUserId}/expense/preferences`; storage: `UserPreferences mileage preferences per company contextId (getMileagePreference…`, `UserDefaults:com.employee.vme.preferences.mileage`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Mileage/Utils/MileagePreferencesHandler.swift:61-156; Modules/Employe…`
- **me-android** (Employee): screens: `MileageScreen`, `MileageKey`; endpoints: `GET /api/v1/employees/{odpUserId}/expense/preferences`, `POST /api/v1/employees/{odpUserId}/expense/preferences`; storage: `MileagePreferencesRepository (vehicle type, fuel type, autoPass, rushHour, auto…`, `Mileage preference shouldAutomaticallyCalculateRoadToll`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/api/MileagesApi.kt:23-60; expense/src/main/java/com/visma/employee/exp…`

**How they differ:**
- (platform parity) iOS keeps tripTypeId and performAutomaticRoadTollCalculation only on the device and sends fuelTypeId, autoPass and rushHour to the server (MileagePreferencesHandler.swift:61-156). Android stores vehicle type and the automatic road-toll flag as server preferences too, with shouldAu…
- (platform parity) iOS lets server values override the local copy and syncs only for new mileages when fuelTypeId is an integer and both booleans are set. Android falls back to the local cache when the API fails (MileagesApi.kt:23-60).
- (platform parity) Both twins send only fuelTypeId, rushHour and autoPass to POST .../expense/preferences. iOS keeps tripTypeId and performAutomaticRoadTollCalculation on the device only (MileagePreferencesHandler.swift:140-156). Android keeps vehicleType and shouldAutoCalculateRoadToll in the local…
- (platform parity) The remembered choice differs: iOS remembers the trip type (tripTypeId) and Android remembers the vehicle type (vehicleType) (MileagePreferences.swift:11 vs domain/MileagePreferences.kt:6).
- (platform parity) The road-toll default differs: Android defaults shouldAutomaticallyCalculateRoadToll to true when nothing is cached (MileagePreferences.kt:10, MileagesServiceImpl.kt:296,333). iOS takes the value from the form field's default state when nothing is stored (MileagePreferencesHandler…
- (platform parity) The save order differs: iOS always saves locally first and then tries the server sync, which it skips unless fuelTypeId parses to an Int and both rushHour and autoPass are set (MileagePreferencesHandler.swift:132-156). Android writes the local cache only after the server POST succ…
- (platform parity) When nothing is cached, Android fills in the fallback values fuelTypeId=-1, autoPass=false and rushHour=false (MileagesServiceImpl.kt:323-334). iOS leaves missing values as nil (MileagePreferences.empty).

_Note: referee could not confirm: me-android expense/src/main/java/com/visma/employee/expense/inbox/details/extension/AnalyticsLoggerExtension.kt:44-63 only logs analytics events for the road-toll, rush-hour and AutoPASS toggles. It does not store any preference and does not show that vehicle type or road toll are sent to the server.; Divergence claim 'Android stores vehicle type and the automatic road-…_

### CAP-269: Register or edit a travel allowance (per diem)

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee enters purpose, regular-day travel and one or more travel segments (start and end date-time, destination country, allowance type), continues to the per-day step, and saves a new allowance draft or saves changes to an existing one.

- **me-ios** (Employee): screens: `AllowanceView`, `TravelInfoFeature`, `AllowanceInfoFeature`, `AllowanceFeature.Path`, `SearchListView`; endpoints: `GET /employee/api/v1/expense/templates/allowance/segments`, `GET {segment-types link href from template}?destinationId=`, `POST /employee/api/v1/expense/templates/allowance/periods`, `POST /employee/api/v1/expense/allowances`; events: `newAllowanceSaved`, `existingAllowanceEdited`, `travelSegmentsPerAllowance`; storage: `DatabaseService receipt (allowance draft, written on next sync)`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Allowance/Coordinator/AddAllowanceCoordinator.swift:40-129; Modules/E…`
- **me-android** (Employee): screens: `AllowancesStepOneScreen`, `AllowancesStepTwoScreen (Save changes button / top bar save)`, `AllowancesStepOneKey`, `AllowancesStepTwoKey`; endpoints: `GET /api/v1/expense/templates/allowance/segments`, `GET {segment-types link}?destinationId=`, `POST /api/v1/expense/templates/allowance/periods`, `POST api/v1/expense/allowances`, `POST {draft update link} (multipart part 'draft')`, `GET {draft link} (existing allowance in claim)`; events: `NEW_ALLOWANCE_SAVED (Allowances - New allowance saved)`, `EXISTING_ALLOWANCE_EDITED`, `Allowances - Travel segments per allowance`; storage: `SavedStateHandle ALLOWANCES_DATA (parcelable form state)`, `SavedStateHandle ExpenseArgKeys.ALLOWANCES_GET_DRAFT_LINK_KEY`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/allowances/data/AllowancesServiceImpl.kt:58-310; expense/src/main/java…`

**How they differ:**
- (platform parity) iOS rejects gaps between travel segments unless the template allows them (canSegmentsHaveGaps), and also checks overlap and start-after-end (AddAllowanceCoordinator.swift:40-129). Android fragments report only overlap and end-after-start checks (AllowancesStepOneViewModel.kt:220-2…
- (platform parity) Android defaults the allowance type to DailyAllowance and hides the cost unit and project field for eHRM companies unless the allowance is edited in a claim (AllowancesStepOneViewModel.kt). Neither rule is reported on iOS, where cost units and project are separate features (Allowa…
- (platform parity) iOS says the local DB copy of a saved allowance arrives only on the next sync, followed by a calendar and start-page reload (AddAllowanceCoordinator.swift). Android keeps the form state in SavedStateHandle and returns to the expense tab or claim (AllowancesStepTwoViewModel.kt:867-…
- (platform parity) Gap handling differs in how it works, not in whether it exists. iOS validates gaps when the template disallows them and shows S.Expense.Allowance.travelPeriodsGaps (TravelUtils.swift:91-120; TravelInfoFeature.swift:251, 566-580). Android prevents gaps by design: when canSegmentsHa…
- (platform parity) The two apps default differently when the template omits canSegmentsHaveGaps. iOS defaults to true, so gaps are allowed (TravelInfoFeature.swift:45). Android evaluates `canSegmentsHaveGaps == true`, so a missing value means gaps are not allowed (AllowancesStepOneViewModel.kt:418).
- (platform parity) Both apps check start-after-end and overlap. iOS uses findInvalidDateRanges and findOverlappingLegs (TravelUtils.swift:86-110). Android uses areValidationRulesMet and areTravelTimesOverlapping (AllowancesStepOneViewModel.kt:861-890).
- (platform parity) Android hides the cost unit and project fields for eHRM companies unless the allowance is edited in a claim (AllowancesStepOneViewModel.kt:616, 625). Android also falls back to the DailyAllowance ('ALLOW') type (AllowancesStepOneViewModel.kt:799). I found no equivalent eHRM rule o…
- (platform parity) After saving, iOS dismisses the screen, resets the calendar, reloads the start page and runs a sync; the local DB draft goes through the allowanceDatabase repository (AddAllowanceCoordinator.swift:176-190). Android publishes EventDataChanged and navigates to the claim or the expen…

_Note: referee could not confirm: me-ios AddAllowanceCoordinator.swift:40-129 is cited as the source of the gap, overlap and start-after-end validation, but that range contains no validation. It only wires up the store and flows. The validation is in Modules/EmployeeExpenses/Sources/EmployeeExpenses/Allowance/Utils/TravelUtils.swift:66-120 and TravelInfoFeature.swift:560-580.; me-android 'GET {draft lin…_

### CAP-270: Set meals and lodging per travel day and see the calculated allowance

**Fusion:** unique · **Personas:** employee · **Confidence:** High

On the second allowance step the employee sets breakfast, lunch, dinner or meal, lodging type and night allowance, either for all days or per day, and sees the server-calculated total, meal deduction and meal benefit.

- **me-ios** (Employee): screens: `AllowanceInfoFeature`, `AllowanceInfoView`; endpoints: `POST /employee/api/v1/expense/templates/allowance/periods`; events: `periodsSegmentChanged`, `periodsSegmentChange`, `allDaysMealAndLodgingType`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Allowance/Features/AllowanceInfo/AllowanceInfoFeature.swift:280-298`
- **me-android** (Employee): screens: `AllowancesStepTwoScreen`, `All days / Single days tabs`, `AllowanceAmountBreakdown bottom sheet`; endpoints: `POST api/v1/expense/templates/allowance/periods`; events: `Allowances - AllDays/singleDays segment switch per allowance`, `Allowances - All days meal and lodging type selection`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/allowances/presentation/step_two/AllowancesStepTwoViewModel.kt:661-825`

**How they differ:**
- (platform parity) Android debounces recalculation by 1000 ms and shows an amount breakdown bottom sheet with the meal deduction as a negative value (AllowancesStepTwoViewModel.kt:661-825). iOS debounces too, but the interval and a breakdown sheet are not reported (AllowanceInfoFeature.swift:280-298…
- (platform parity) Android shows the amount breakdown (AmountBreakdown, AllowancesStepTwoState.kt:84) in a bottom sheet on AllowancesStepTwoScreen.kt (ModalBottomSheet/BottomSheetScaffold). iOS shows the totals as inline rows in AllowanceInfoView.swift:172,219-231 (allowanceTotalsView), with no sepa…
- Correction to the claim: both platforms debounce recalculation by 1 second: iOS at AllowanceInfoFeature.swift:56 (.seconds(1)) and line 298, Android at AllowancesStepTwoViewModel.kt:778 (delay(1000)). Both show the meal deduction as a negative value: iOS at AllowanceAmounts.swift:73, Android throug…

_Note: referee could not confirm: Divergence line claim 'iOS interval not reported': the interval is explicit, 1 second, at AllowanceInfoFeature.swift:56; iOS event 'periodsSegmentChange' / 'allDaysMealAndLodgingType' are not confirmed as analytics event names; only periodsSegmentChanged exists (AllowanceInfoFeature.swift:162,591)_

### CAP-271: Record hotel stays for an allowance and find the hotel

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee adds hotel stays to the allowance, which must be continuous and inside the server's lodging periods. They fill in each hotel by search or pick from recently used hotels, which they can remove.

- **me-ios** (Employee): screens: `AllowanceInfoView hotel search list`, `HotelSearchActionView sheet (SearchListView)`; events: `allowanceHotelSearchFeatureUsed`, `allowanceHotelSearchHistoryUsed`, `allowanceContainsHotelNameAndAddress`; storage: `UserPreferences key com.visma.employee.expense.allowance.hotelName (recent hote…`; platform: `MapKit MKLocalSearchCompleter (query + pointOfInterest, world region)`, `Google Places SDK autocomplete (placeProvider dependency)` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Allowance/Features/AllowanceForm/AllowanceFormViewFactory.swift:135-1…`
- **me-android** (Employee): screens: `AllowancesStepTwoScreen (hotels repeatable group)`, `HotelSearchLayout modal bottom sheet`; endpoints: `GET api/v1/maps/hotels?query={query}`; events: `Allowances - Allowance hotel search feature used`, `Allowances - Allowance hotel search history used`, `Allowances - Allowance contains hotel name and address`; storage: `Room table frequently_used_hotels (FrequentlyUsedHotelDbModel)`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/allowances/presentation/step_two/AllowancesStepTwoViewModel.kt:572-653…`

**How they differ:**
- (platform parity) Android searches hotels through the backend GET api/v1/maps/hotels?query= (AllowancesStepTwoViewModel.kt:1272-1425). iOS searches on the device, with Apple MapKit in one fragment (AllowanceFormViewFactory.swift:135-152) and Google Places autocomplete in another (SearchListReposito…
- (platform parity) iOS keeps at most 4 recent hotels in UserPreferences and records them when the allowance is added to a claim (AllowanceFormViewFactory.swift). Android caches the hotel in a Room table as soon as it is selected, with no limit reported (AllowancesStepTwoViewModel.kt).
- (platform parity) iOS offers hotel search only when the template field has the 'hotelsearch' rendering hint. Android also drops draft hotels outside new travel dates or on the last travel day (AllowancesStepTwoViewModel.kt:572-653).
- (platform parity) Android searches hotels through the backend GET api/v1/maps/hotels?query= (AllowancesServiceImpl.kt:290, called by queryHotels at AllowancesStepTwoViewModel.kt:1272). iOS searches only on the device with Apple MapKit MKLocalSearchCompleter (SearchListSearchDataRepository.hotelSear…
- (platform parity) iOS keeps at most 4 recent hotels as plain strings in UserPreferences under com.visma.employee.expense.allowance.hotelName (SuggesionsRepository.userPreferences.swift:13). Android saves the full hotel object in the Room table frequently_used_hotels as soon as it is selected (onHot…
- (platform parity) On Android a selected hotel is formatted as 'name, address' from the backend result (AllowancesStepTwoViewModel.kt:1341-1357). On iOS it is the MapKit completion text 'title, subtitle' (MapKitSearchService.swift).
- (platform parity) iOS offers hotel search only when the template field has the 'hotelsearch' rendering hint (AllowanceFormViewFactory.swift:134). Android removes draft hotels that fall outside new travel dates (removeOutdatedHotelsAfterChangingTravelDates, AllowancesStepTwoViewModel.kt:397,471). Wh…

_Note: referee could not confirm: me-ios Modules/EmployeeExpenses/Sources/EmployeeExpenses/Receipts/Repository/SearchList.Places/SearchListRepository.places.swift:13-108 is not hotel search. The googlePlaces repositories are used only by PlaceSelectionFormRow.swift:50-54 for place selection in the mileage and calculate-distance flow: they use calculateDistanceSuggestions and the string S.Expense.Mileage…_

### CAP-272: Read what allowances are and the company policy

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee opens a help sheet from an allowance field label that explains the allowance and period definitions, with a link to more documentation.

- **me-ios** (Employee): screens: `DefinedLabel explanation sheet`; events: `allowancesDefinitionSheetOpened`; platform: `ios-native` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Allowance/Features/AllowanceForm/Extensions/DefinedExplanation.Allowa…`
- **me-android** (Employee): screens: `DefinedLabelExplanationLayout bottom sheet`; events: `Allowances - Allowances definition sheet opened`; platform: `external browser link` · evidence `expense/src/main/java/com/visma/employee/expense/allowances/presentation/step_two/AllowancesStepTwoViewModel.kt:200-218`

**How they differ:**
- (platform parity) The iOS sheet explains what an allowance is, the company policy and regular-day travel (DefinedExplanation.Allowances.swift:12-40). The Android sheet explains the period definitions and picks a docs URL by language (nb-NO, sv-SE, otherwise English) (AllowancesStepTwoViewModel.kt:2…
- (platform parity) Both twins show the same two sections, 'What is allowance' and 'Company policy' (iOS DefinedExplanation.Allowances.swift:15-24; Android values/strings.xml:849-852 read at AllowancesStepTwoViewModel.kt:200-210). The claim says the Android sheet explains 'period definitions'; the co…
- (platform parity) Both pick the read-more docs URL by language and point to the same three URLs for Norwegian, Swedish and everything else (iOS AllowanceConstants.swift:32-41; Android AllowancesStepTwoViewModel.kt:1928-1934, 1969-1974). iOS lists Finnish and Danish explicitly as English; Android fa…
- (platform parity) Where the sheet opens: on Android it opens from the allowance-period field-group label on step two (AllowancesStepTwoScreen.kt:271-275, BottomSheetContentType.ALLOWANCE_PERIOD_GROUP_EXPLANATION). On iOS it opens from DefinedLabels on the allowance form (AllowanceFormViewFactory.sw…
- (platform parity) Regular-day travel has its own explanation on both platforms, not inside this sheet (iOS DefinedExplanation.regularDayTravel at DefinedExplanation.Allowances.swift:35-45, used at AllowanceFormViewFactory.swift:193; Android regularDayTravelExplanationData at AllowancesStepOneScreen…

_Note: referee could not confirm: me-android platform is given as 'external browser link'; it should be android-native. The sheet is a Compose bottom sheet (DefinedLabelExplanationLayout.kt:36).; iOS evidence range DefinedExplanation.Allowances.swift:12-40 includes the separate regularDayTravel explanation (lines 35-45); the allowance/company-policy sheet itself is lines 13-33.; The iOS string key S.Exp…_

### CAP-273: View my travel emissions summary

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee sees this year's CO2 emissions from their expenses as a donut chart of top expense types with the change from the previous period, and can read how emissions are calculated and their limits, with links to sources.

- **me-ios** (Employee): screens: `EmissionReportsView`, `HowDoWeCalculateEmissionsView`, `EmptyReportView`, `ClimateReportsCoordinator`, `ClimateReportsModalCoordinator`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/expense/climateReport?reportPeriod=T…`; events: `viewEmissionsSummary`; platform: `in-app browser for external links (openURLInApp)` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/ClimateReports/Views/EmissionReports/EmissionReportsViewModel.swift:5…`
- **me-android** (Employee): screens: `EmissionsSummaryScreen`, `EmissionSummaryKey`, `HowWeCalculateEmissionsKey`, `HowDoWeCalculateEmissionsScreen`; endpoints: `GET /api/v1/employees/{odpUserId}/expense/climateReport?ReportPeriod=THIS_YEAR`, `GET /api/v1/employees/{odpUserId}/expense/climateReport?ReportPeriod=`; events: `logEmissionSummaryScreenOpened`, `VIEW_EMISSIONS_SUMMARY (Expense - View Emissions Summary)`; storage: `DataStorageService.getHowDoWeCalculateEmissionsUrls`, `res/xml/urls how-do-we-calculate-emissions-urls`; platform: `external browser via LocalUriHandler` · evidence `expense/src/main/java/com/visma/employee/expense/sustainability/presentation/emissions_summary/EmissionsSummaryViewMode…`

**How they differ:**
- (platform parity) iOS hard-codes the period to ThisYear (EmissionReportsViewModel.swift:54-146). The Android service supports Last7Days, Last30Days, ThisMonth, ThisYear and LastYear (SustainabilityServiceImpl.kt:26-49), but its summary screen requests THIS_YEAR (EmissionsSummaryViewModel.kt).
- (platform parity) iOS merges types below a minimum value, or beyond the top count, into 'Other', shown only if it meets the minimum. Android shows 'Other' only if it is above 0% (EmissionsSummaryViewModel.kt:45-200).
- (platform parity) iOS opens external links in an in-app browser. Android opens them in the external browser (HowDoWeCalculateEmissionsScreen.kt:41-138).
- (platform parity) iOS shows the entry in the profile menu only with the expenseApiShowEmissionDetails permission (UserProfileCoordinator.swift:132-142). The Android entry point and its permission gate are not reported.
- (platform parity) Correction to the claim: both twins support the same five periods (Last7Days, Last30Days, ThisMonth, ThisYear, LastYear), and both summaries request ThisYear. On iOS this is the ReportPeriod enum in GetClimateReport.swift, called through loadYearToDateReports. On Android it is Sus…
- (platform parity) Top-category filter: iOS moves a type to 'Other' when min(percent, co2) < minimumValueToDisplay, or when it is beyond topCategoriesCount (EmissionReportsViewModel.swift group()). Android keeps a type only if its rounded percentage and rounded CO2 are both above 0, then takes AMOUN…
- (platform parity) The 'Other' row's change value: iOS sets co2Change to nil for 'Other' (reduceOtherTypes). Android adds up co2Change and previousCo2 across the merged categories (calculateOtherEmissionCategory).
- (platform parity) When 'Other' is shown: iOS shows it only if min(percent, co2) >= minimumValueToDisplay. Android shows it only if the rounded percentage and rounded CO2 are both above 0.
- (platform parity) External links: iOS opens them in an in-app browser (openURLInApp, as the claim says). Android opens them in the external browser with LocalUriHandler.openUri (HowDoWeCalculateEmissionsScreen.kt:131).
- (platform parity) Entry point and permission gate: on iOS, the profile menu adds .emissionsSummary only when the user has expenseApiShowEmissionDetails (UserProfileFeature.swift:103-104). Android also has a permission gate, Feature.ExpenseSpecificFeature.ShowEmissionDetails = 'meapi:expense:show-em…
- (platform parity) Endpoint path: iOS uses resourceName '/employee/api/v1/...' with the parameter reportPeriod. Android uses 'api/v1/...' with the parameter ReportPeriod, so the /employee prefix probably sits in Android's base URL. This only matters for the backend contract.

_Note: referee could not confirm: UserProfileCoordinator.swift:132-142 does not contain the expenseApiShowEmissionDetails permission check. The check is at Employee/Accounts/Feature/UserProfile/UserProfileFeature.swift:103-104.; The divergence line saying iOS 'hard-codes the period to ThisYear' while Android 'supports' five periods is misleading. EmployeeServices/Expense/Sources/Expense/Request/GetClima…_

### CAP-274: See the CO2e emissions of an expense or claim

**Fusion:** unique · **Personas:** employee · **Confidence:** Medium

On a receipt, mileage or claim, the employee sees the calculated CO2e emissions, when the company has emission details turned on.

- **me-ios** (Employee): screens: `CO2EmissionsView (ReceiptDetail)`, `ExpenseViewController`, `MileageView.MileageFormView`; platform: `ios-native` · evidence `Modules/EmployeeUIComponents/Sources/EmployeeUIComponents/CO2EmissionsView/CO2EmissionsView.swift:53-58; Modules/Employ…`
- **me-android** (Employee): screens: `ExpenseRowsScreen`, `ExpenseDraftDetailsScreen`, `Mileage screen (MileagesViewModel)`; platform: `android-native` · evidence `expense/src/main/java/com/visma/employee/expense/details/ExpenseRowsViewModel.kt:314-417; expense/src/main/java/com/vis…`

**How they differ:**
- (platform parity) iOS gates CO2 display on the company feature expenseApiShowEmissionDetails (EditExpenseViewModel.swift:115-265). Android gates it on a 'sustainability permission' (ExpenseRowsViewModel.kt:314-417). The two may be the same flag, but this is not confirmed.
- (platform parity) Both twins use the same gate. iOS checks UserPermission.expenseApiShowEmissionDetails = "meapi:expense:show-emission-details" (UserService.swift:44, used at EditExpenseViewModel.swift:138, ReceiptDetailViewModel.swift:255, ExpenseMileageViewModel.swift:509). Android checks Feature…
- (platform parity) Android also shows CO2e on the selected-claim screen (SelectedClaimViewModel.kt:177-178), which the claim does not list. iOS shows claim-level CO2 through EditExpenseViewModel/ExpenseViewController (ExpenseViewController.swift:910-920).
- (platform parity) Formatting matches: both round to whole numbers and add 'kg CO2e'. iOS uses ExpenseUtils.localizedCO2Amount with 0 fraction digits (ExpenseConstants.swift:14-15). Android uses String.roundToIntAndFormat (BaseExtensions.kt:32-34) with expense_sustainability_co2_emissions_body '%1$s…
- (platform parity) Hiding is slightly different. iOS hides the row when co2 == nil. Android hides it when the formatted string is null or blank (MileageScreen.kt:404-405), so a co2 value that is not a number would also hide the row.

_Note: Medium confidence: the fragments mention CO2 only in passing, inside larger receipt, mileage and claim fragments. referee could not confirm: The Android string key expense_sustainability_co2_emissions_label is used in Co2EmissionRow.kt:28 (expense/.../sustainability/presentation/emissions_summary/components/), which is not in the cited files.; The iOS files list leaves out the files that do the r…_

### CAP-275: Keep expenses in sync and upload offline drafts automatically

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The app downloads the inbox, currencies and templates and uploads receipts and mileages saved locally while offline. It runs in the background when the connection returns, shows each item's upload state, and explains failures.

- **me-ios** (Employee): screens: `ReceiptsListView (sync progress, row upload state)`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/expense/inbox`, `GET /employee/api/v1/employees/{odpUserId}/expense/currencies`, `GET /employee/api/v1/employees/{odpUserId}/expense/templates/expense`, `GET /employee/api/v1/employees/{odpUserId}/expense/templates/mileage`, `POST /employee/api/v1/expense/upsert-draft`, `POST /employee/api/v1/employees/{odpUserId}/expense/mileages`; storage: `DatabaseService.syncDrafts`, `DatabaseService.allReceiptsForUpload`, `realm-model:RealmReceipt`, `realm-model:RealmReceiptAttachment`, `realm-model:RealmReceiptTemplate`, `realm-model:RealmMileageTemplates`, `keychain:kSecClassGenericPassword (Realm encryption key)`; platform: `reachability-triggered sync (ReachabilityListener)`, `background-QoS OperationQueue`, `app group shared container (sharedRealmURL/userRealmURL)` · evidence `Modules/EmployeeExpenses/Sources/EmployeeExpenses/Services/SyncService.swift:120-219; EmployeeServices/EmployeeDatabase…`
- **me-android** (Employee): screens: `ExpenseDraftsScreen`, `Expense inbox (triggers sync)`; endpoints: `POST /api/v1/expense/upsert-draft`, `POST /api/v1/employees/{odpUserId}/expense/mileages`; storage: `local offline drafts DB (SyncManagerImpl syncObject dbId)`, `ExpenseServiceModelMapper local receipts and attachments (deleted after upload)`; platform: `WorkManager background task` · evidence `expense/src/main/java/com/visma/employee/expense/core/storage/sync/SyncManagerImpl.kt:46-129; expense/src/main/java/com…`

**How they differ:**
- (platform parity) iOS keeps drafts in an encrypted per-user Realm, with a 64-byte key in the keychain, and rebuilds the database on errors (RealmService.swift:379-400). Android keeps them in a local offline drafts DB; encryption is not reported (SyncManagerImpl.kt:46-129).
- (platform parity) iOS syncs only when authenticated, the DB belongs to the current user, and the user has expenseApiRead, expenseApiWrite and expenseClaims access (SyncService.swift:120-219). Android runs a WorkManager upload worker when the inbox syncs, and a permission gate is not reported.
- (platform parity) Android shows a failure dialog explaining invalid documents, connection issues or a business error (ExpenseDraftsScreen.kt:583-648). iOS shows an upload-failed alert only after the initial sync (ReceiptsListFeature.swift:194-305). Both delete the local draft when the server says t…
- (platform parity) iOS sync() also downloads currencies, receipt templates and mileage templates, and syncs the inbox (SyncService.swift:147-181). Android SyncManagerImpl.sync() only uploads local drafts, one ExpenseUploadWorker each (SyncManagerImpl.kt:51-68). Downloading the inbox is not part of A…
- (platform parity) Both start a sync when the connection comes back: iOS in onReachabilityStatusChange(.reachable) (SyncService.swift:324-330), Android in ConnectionManagerImpl.invalidateNetworkState (core/network/ConnectionManagerImpl.kt:34-38). Android also syncs when the inbox opens (ExpenseInbox…
- (platform parity) iOS sync() checks authentication, that the database belongs to the current user, and expenseApiRead+expenseApiWrite (SyncService.swift:121-138). The expenseClaims check applies inside the per-task sync (see SyncCurrenciesTaskTests/SyncMileageTemplatesTaskTests), not in sync() itse…
- (platform parity) Android maps failures to ATTACHMENT_VALIDATION, NETWORK_ISSUES, BUSINESS_ERROR or UNKNOWN and shows a specific message for each. On BUSINESS_ERROR it also deletes the draft (ExpenseDraftsScreen.kt:622-641). iOS shows a generic upload-failed alert (ReceiptsListFeature.swift:247) an…
- (platform parity) Both delete the local draft when the server reports the attachment is already used. Android does this at ExpenseUploadWorker.kt:71-77.
- (platform parity) iOS stores drafts in an encrypted Realm (RealmService.swift:67-79 encryptionKey). I did not verify Android's storage encryption; a grep for SQLCipher and EncryptedFile found nothing.

_Note: referee could not confirm: me-android evidence path expense/src/main/java/com/visma/employee/expense/core/storage/sync/SyncManagerImpl.kt does not exist. The real file is expense/src/main/java/com/visma/employee/core/storage/sync/SyncManagerImpl.kt (the files list has it right).; EmployeeServices/EmployeeDatabase/Sources/EmployeeDatabase/RealmService.swift:379-400 is syncDrafts: it merges remote…_

## Time and absence

Calendar, absence and time registration, check-in and check-out, confirming time, balances, and the calendar assistant

### CAP-001: View a calendar month by month

**Fusion:** shared-diverged · **Personas:** Manager, Employee · **Confidence:** High

Open a month grid of calendar entries (attendance, absence, supplement and, in Employee, roster shifts and special days) and move between months with arrows, swipes or a month/year picker. The Manager opens it for one employee from the HRM employee detail; the Employee sees their own calendar.

- **vmm** (Manager): screens: `HrmEmployeeDetailScreen`, `EmployeeCalendarScreen (SCREEN_NAME_EMPLOYEE_CALENDAR)`, `WeekdayCalendarGrid`, `CalendarMonthYearPicker`; endpoints: `GET {ME_BASE_URL}employee/api/v2/calendar/my-employees/feed?From={from}&Offset=…`; storage: `redux features.isEmployeeCalendarEnabled (persisted)`, `RTK Query cache tag CALENDAR`, `redux settings.calendar* (persisted)` · evidence `src/screens/EmployeeCalendarScreen/EmployeeCalendarScreen.tsx:76-200; src/components/hrm/HrmEmployeeDetailAccordeon/Hrm…`
- **me-ios** (Employee): screens: `CalendarGridView`, `CalendarMonthYearNavigationView`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar/workshift`, `GET /employee/api/v2/Calendar/specialdays`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/CalendarGridFeature.swift:185-491; Em…`
- **me-android** (Employee): screens: `CalendarView`, `AbsenceFeedScreen`, `AbsenceFeedKey`; endpoints: `GET /api/v1/employees/{odpUserId}/calendar?FromDate&ToDate`, `GET /api/v1/employees/{odpUserId}/calendar/workshift?fromDate&toDate`, `GET /api/v2/Calendar/specialdays?fromDate&toDate`, `GET /api/v1/employees/{odpUserId}/calendar/confirm`; events: `Calendar - View mode`; platform: `android-native` · evidence `absence/src/main/java/com/visma/employee/absence/feed/calendar_view/components/calendar/CalendarView.kt:54-245; absence…`

**How they differ:**
- Whose calendar: vmm shows a managed employee's calendar via GET {ME_BASE_URL}employee/api/v2/calendar/my-employees/feed (EmployeeCalendarScreen.tsx:76-200); Employee shows the user's own calendar via /employee/api/v1/employees/{odpUserId}/calendar[/feed] (CalendarService.swift:28-55, AbsenceFeedVie…
- Live data: vmm grid and agenda currently serve createMockCalendarFeedResponse because the live feed returns 403 (queryEndpointsCalendar.ts:71-75,158-164); Employee loads live data
- Content: Employee adds roster shifts (calendar/workshift) and special days (v2/Calendar/specialdays) to the grid (CalendarService.swift:76-100, CalendarView.kt:54-245); vmm shows only attendance, absence and supplement events
- Access: vmm shows the entry row only when features.isEmployeeCalendarEnabled and a companyId is resolved (HrmEmployeeDetailAccordion.tsx:268-273); Employee needs calendar permissions
- Registration from the grid: Employee month view creates a registration from an empty-day tap or a dragged range (CalendarGridFeature.swift:217-220, AbsenceFeedScreen.kt:366-440); vmm grid is read-only
- (platform parity) iOS month data goes through CalendarGridRepository (endpoint not resolved in the fragment); Android calls GET /api/v1/employees/{odpUserId}/calendar?FromDate&ToDate and reloads only when cached coverage is missing (CalendarView.kt, AbsenceFeedViewModel.kt:339-440)
- (platform parity) Android grid shows request status strings status_approved/status_awaiting_approval/status_declined (CalendarView.kt:54-245); iOS grid fragment reports no status labels
- (platform parity) iOS offers a month/year picker (calendar.selectMonthAndYear, CalendarMonthYearNavigationFeature.swift); Android fragment reports only swiping between months
- Whose calendar: vmm shows a managed employee's calendar. The commented-out live queryFn calls GET {ME_BASE_URL}employee/api/v2/calendar/my-employees/feed and filters to one employeeId on the client (queryEndpointsCalendar.ts:74-130). Employee shows the user's own calendar via /employee/api/v1/emplo…
- Live data: the vmm grid and the agenda both return createMockCalendarFeedResponse(from); the live implementation is commented out because of a 403 (queryEndpointsCalendar.ts:69-72, 160-166). The Employee app loads live data.
- Content: the Employee grid adds roster shifts (calendar/workshift) and special days (v2/Calendar/specialdays) (CalendarService.swift:76-100; CalendarServiceImpl.kt:460,466), plus confirm-time items (CalendarFeedRepositoryAdapter.swift:81-100; AbsenceFeedViewModel.kt:357-367). vmm filters only atten…
- Access: in vmm the calendar section has details only when features.isEmployeeCalendarEnabled is on (HrmEmployeeDetailAccordion.tsx:52,83-86). That flag is toggled from SettingsDevToolsScreen.tsx:406. The Employee app gates writing and confirm time by permissions (CalendarGridFeature.swift isWriteAv…
- Registration from the grid: tapping an empty day in the Employee grid starts a new registration when write is available, and dragging selects a date range (CalendarGridFeature.swift:217-220, 237-240). In vmm, onDayPress only opens a read-only day detail sheet (EmployeeCalendarScreen.tsx onDayPress).
- Extra view mode: vmm has a grid/agenda toggle (settings.calendarViewMode), and its agenda is an infinite list going back in time (queryEndpointsCalendar.ts:155-170). The Employee grid is a month-only feature, with the feed list as a separate view.
- (platform parity) iOS loads the month through CalendarFeedRepositoryAdapter.fetchMonth, which fetches feed pages until they cover the interval (CalendarFeedRepositoryAdapter.swift:81). Android reloads around a center date with feed batches and ensureCalendarMonthCoverage (AbsenceFeedViewModel.kt:33…
- Correction to the claim: Android also has month/year selection (CalendarView.kt:65,162-163, onMonthSelected/onYearSelected), so the parity line 'Android only swipes' is false.
- Correction to the claim: the Android status_approved/status_declined strings are in CalendarViewMonthDayDetailsBottomSheetLayout.kt:120-157 (the day sheet), not in the CalendarView.kt grid. vmm also shows request status in its day sheet (EmployeeCalendarDayDetail.tsx:98, employee_calendar_status_*).

_Note: Fragment 76 (entry row on the HRM detail) is folded in as the Manager's entry point. Roster (258) and special days (259) service fragments are data sources for this grid and the day sheet. referee could not confirm: The claim says the iOS month endpoint is not resolved. It is: CalendarGridRepository resolves to CalendarFeedRepositoryAdapter.fetchMonth (Modules/CalendarFeature/.../Repository/Calen…_

### CAP-002: Browse the calendar as a scrolling list

**Fusion:** shared-diverged · **Personas:** Manager, Employee · **Confidence:** High

Scroll a chronological list of calendar entries that loads more entries while scrolling. In Employee the list also lets you jump to a date, open an item and confirm time from a feed item.

- **vmm** (Manager): screens: `EmployeeCalendarScreen (SCREEN_NAME_EMPLOYEE_CALENDAR)`, `EmployeeCalendarAgendaView`; endpoints: `GET {ME_BASE_URL}employee/api/v2/calendar/my-employees/feed?From={from}&Offset=…`; storage: `RTK Query cache tag CALENDAR` · evidence `src/screens/EmployeeCalendarScreen/EmployeeCalendarScreen.tsx:76-200`
- **me-ios** (Employee): screens: `CalendarViewController (list mode)`, `CalendarHeaderView`, `DatePicker`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar`, `GET /employee/api/v1/employees/{odpUserId}/calendar/feed?From={date}&Offset={of…`, `GET /employee/api/v1/employees/{odpUserId}/calendar/confirm`; events: `Calendar item tapped (log breadcrumb)`, `Date header tapped (log)`, `Date nav bar item tapped (log)`; platform: `ios-native`, `reachability-driven offline placeholder`, `NotificationCenter AppMessage.resetCalendar / resetCalendarBackground reload` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarViewController.swift:208-280; Modules/CalendarFeature/…`
- **me-android** (Employee): screens: `AbsenceFeedScreen`, `AbsenceFeedKey`; endpoints: `GET /api/v1/employees/{odpUserId}/calendar/feed`, `GET /api/v1/employees/{odpUserId}/calendar/feed?from&direction&offset`, `GET {nextLink/previousLink} (calendar paging)`; platform: `android-native` · evidence `absence/src/main/java/com/visma/employee/absence/feed/AbsenceFeedViewModel.kt:339-440`

**How they differ:**
- Paging: vmm agenda pages back one month at a time up to AGENDA_MONTHS_CAP (EmployeeCalendarScreen.tsx:76-200); Employee pages both directions with From/Offset/Direction and follows server next/previous links (CalendarService.swift:103-111, AbsenceFeedViewModel.kt)
- Jump to date: Employee has a date picker from the section header or nav bar that reloads the feed from the picked date (CalendarHeaderView.swift:64-83); vmm fragment reports none
- Feed content: Employee inserts confirm-time items and shows approval statuses canceled/rejected/denied/pending/sent (CalendarFeedViewModel.swift:89-92, AbsenceService.swift:39-49); vmm agenda shows attendance/absence/supplement events only, from mock data
- Offline: Employee shows a reachability-driven offline placeholder (calendarOfflineText / calendar_offline); vmm fragment reports only a load error (employee_calendar_load_error)
- (platform parity) iOS reuses the same list controller for expense claims when permissions say so (CalendarViewController.swift:56-72); Android fragment reports no such reuse
- (platform parity) Jump to a date is evidenced in detail on iOS (GMT picker, CalendarViewController.swift:329-336); Android fragment only states 'jumping to a date' (AbsenceFeedViewModel.kt:339-440)
- Whose calendar: vmm shows the calendar of a managed employee picked through route params (employeeId, companyId), with the employee's name as the screen title; companyTenantId is looked up from the employees list, and the live version would filter the aggregate my-employees/feed down to that one em…
- Paging: vmm starts at the current month and only goes back in time, one month per page, stopping at AGENDA_MONTHS_CAP = 24 (queryEndpointsCalendar.ts:17, 144-157). Employee pages both past and future and follows the server's previous/next links (CalendarFeedPagingControllerDataSource.swift:40-44; A…
- Data source: vmm agenda and grid both serve mock data (queryEndpointsCalendar.ts:75, 168-171), with the live v2 my-employees/feed call commented out. Employee calls the live v1 employees/{odpUserId}/calendar/feed
- Jump to a date: Employee has one: on iOS a date picker from the section header (CalendarHeaderView.swift:64-83), on Android selectedDate triggers reloadByCustomCenterDate plus scrollToNearestDate (AbsenceFeedViewModel.kt:~605-620). vmm's agenda has no date picker; its CalendarMonthYearPicker and mo…
- Tapping an item: in vmm, tapping an agenda row opens that day's bottom sheet (EmployeeCalendarAgendaView.tsx:97, onDayPress to setSelectedDay). In Employee, tapping opens the item itself through the delegate (CalendarViewController.swift:317-322, 'Calendar item tapped' log)
- Feed content: Employee merges confirm-time items into the feed when the user has permission (CalendarFeedViewModel.swift:89-95; AbsenceFeedViewModel.kt:356-368, 415-418) and keeps approval statuses canceled/rejected/denied/pending/sent (AbsenceService.swift:39-49). vmm shows only attendance, absenc…
- Type filters: vmm settings toggles showAttendance, showAbsence and showSupplement filter the grid only (eventsByDate). The agenda list does not apply them (agendaItems, EmployeeCalendarScreen.tsx:181-183). Employee has no such toggles in the cited code
- Offline: Employee uses reachability to show an offline placeholder (calendarOfflineText at CalendarViewController.swift:54-75, 229-233; calendar_offline at AbsenceFeedScreen.kt:211). vmm shows only a generic employee_calendar_load_error (EmployeeCalendarScreen.tsx:318), and when a later page fails…
- (platform parity) iOS reuses the same list controller for expense claims when the user's features include expenseClaims, with claimsOfflineText (CalendarViewController.swift:56-62). No such reuse was found in the Android feed
- (platform parity) Both twins support jumping to a date, but differently: iOS reloads the feed through loadFeed(from:) with a GMT DatePicker; Android reloads only when the chosen date is outside the loaded range and otherwise just scrolls to it (AbsenceFeedViewModel.kt:~605-620). The claim's line th…

_Note: referee could not confirm: The vmm endpoint GET employee/api/v2/calendar/my-employees/feed is commented out for this screen (queryEndpointsCalendar.ts:77-135). The agenda queryFn returns mock data (line 168), so the endpoint is not actually called for this capability.; The claim's '(platform parity)' line saying Android only mentions jumping to a date is inaccurate: AbsenceFeedViewModel.kt has wo…_

### CAP-003: Switch between list and month view of the calendar

**Fusion:** shared-diverged · **Personas:** Manager, Employee · **Confidence:** High

Switch the calendar between a list/agenda view and a month grid. The app remembers the chosen view.

- **vmm** (Manager): screens: `CalendarOptionsMenu (EmployeeCalendarScreen header right)`; storage: `redux settings.calendarViewMode` · evidence `src/screens/EmployeeCalendarScreen/components/CalendarOptionsMenu/CalendarOptionsMenu.tsx:53-130`
- **me-ios** (Employee): screens: `CalendarContainerViewController`; events: `View mode`; storage: `UserDefaults calendarViewMode`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarContainerViewController.swift:70-170`
- **me-android** (Employee): screens: `AbsenceFeedScreen`; events: `Calendar - View mode`; storage: `Room UserPreferenceDbModel.preferred_calendar_ui_mode`, `room-entity:user_preferences`; platform: `android-native` · evidence `absence/src/main/java/com/visma/employee/absence/feed/AbsenceFeedViewModel.kt:857-1004; core/src/main/java/com/visma/em…`

**How they differ:**
- Control: vmm switches grid/agenda inside the header options menu (calendar_view_mode, CalendarOptionsMenu.tsx:53-130); Employee uses nav-bar toggle buttons (CALENDAR_SWITCH_TO_MONTH_VIEW / CALENDAR_SWITCH_TO_LIST_VIEW, CalendarContainerViewController.swift:70-170)
- Storage: vmm persists redux settings.calendarViewMode; Employee iOS uses UserDefaults calendarViewMode, Android Room UserPreferenceDbModel.preferred_calendar_ui_mode keyed by user email
- Analytics: Employee logs 'View mode' (Android once per session); vmm fragment reports no event
- (platform parity) iOS restores the view and shows nav buttons only with calendar permissions; Android keys the preference by last logged-in user email (AbsenceFeedViewModel.kt:857-1004)
- Control: vmm picks Grid or Agenda with radio rows under a 'calendar_view_mode' section inside the header options menu (CalendarOptionsMenu.tsx:94-102). Employee uses a single nav-bar or top-bar icon that toggles between the two views (iOS CalendarContainerViewController.swift:132-156; Android Absen…
- Default view: vmm opens in grid (month) by default (settingsReducer.ts:119 calendarViewMode: 'grid'). Employee opens in list by default (iOS CalendarContainerViewController.swift:52 currentViewMode = .list; Android AbsenceFeedViewModel.kt:142-143 falls back to UiMode.List).
- Storage and sync: vmm puts calendarViewMode into the payload sent to the backend by saveUserSettings, so the choice roams across devices (apiUserSetting.ts:81, validated in userSettingsValidator.ts:77), even though a comment in settingsReducer.ts:81 says 'local-only'. Employee keeps it on the devic…
- Analytics: Employee logs the 'View mode' event (iOS Events.swift:192-193, fired at setup in CalendarContainerViewController.swift:89-95; Android calendarViewAnalyticsService.logCalendarViewMode in AbsenceFeedViewModel.kt:202-212). No view-mode analytics call was seen in the vmm menu or screen.
- Switch behaviour: when moving from agenda back to grid, vmm moves the grid to the month the agenda was showing (EmployeeCalendarScreen.tsx:152-158). Android syncs the date in both directions and reloads data if needed (syncListToCalendarView / syncCalendarToListView, AbsenceFeedViewModel.kt:923-985…
- (platform parity) iOS restores the saved mode and shows the switch button only when the user has calendar permissions (CalendarContainerViewController.swift:70-76,110-112). Android always shows the switch button and keys the stored preference by user email.
- (platform parity) iOS logs the view-mode event every time the calendar is set up, including the default mode (CalendarContainerViewController.swift:89-95). Android logs it only on ViewModel init and only when a preference has already been saved (AbsenceFeedViewModel.kt:202-212). iOS also logs a sep…

_Note: referee could not confirm: The claimed detail 'Android once per session' is imprecise: Android logs the view mode only in AbsenceFeedViewModel init (kt:202-212) and only when a saved preference exists. The cited range 857-1004 covers the toggle, not the analytics call.; The storage line 'vmm persists redux settings.calendarViewMode' is incomplete: vmm also sends the value to the backend through s…_

### CAP-004: See the details of a calendar day

**Fusion:** shared-diverged · **Personas:** Manager, Employee · **Confidence:** High

Tap a day to open a sheet listing that day's entries with time or full-day label, title and status. In Employee the sheet also shows the special day and the scheduled roster hours, entries can be opened, and the sheet offers register and confirm-time actions.

- **vmm** (Manager): screens: `EmployeeCalendarDayDetail` · evidence `src/screens/EmployeeCalendarScreen/EmployeeCalendarScreen.tsx:76-200`
- **me-ios** (Employee): screens: `DayDetailFeature`, `DayDetailView`, `ViewAbsenceRegistrationFeature (sheet)`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar/feed?From={date}&Offset={of…`, `GET /employee/api/v1/employees/{odpUserId}/calendar/workshift`, `GET /employee/api/v2/Calendar/specialdays`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/DayDetailView.swift:40-125`
- **me-android** (Employee): screens: `CalendarViewMonthDayDetailsBottomSheetLayout`; platform: `android-native` · evidence `absence/src/main/java/com/visma/employee/absence/feed/calendar_view/components/calendar/CalendarView.kt:54-245`

**How they differ:**
- Content: Employee sheet lists special day and roster scheduled hours first (Calendar.specialDay, Calendar.scheduledHours, DayDetailFeature.swift:30-31); vmm EmployeeCalendarDayDetail lists events only (employee_calendar_empty_day_message)
- Actions: Employee entries open their detail and the sheet offers Register and Confirm time (DayDetailView.swift:40-125, DayDetailFeature.swift:66-116); vmm day detail is read-only
- Empty day: Employee skips the sheet and opens registration when write permission exists (CalendarGridFeature.swift:217-220); vmm shows an empty-day message
- (platform parity) Android sheet is CalendarViewMonthDayDetailsBottomSheetLayout; iOS is DayDetailFeature sheet; roster not tappable on iOS (CalendarGridFeature.swift:318-324), Android behaviour not reported
- Content: Employee lists the special day first (DayDetailView.swift:55-70; CalendarViewMonthDayDetailsBottomSheetLayout.kt:63-65, 196-224) and a roster 'scheduled hours' row (DayDetailView.swift:72-76; Android RosterListItem :186-193). vmm EmployeeCalendarDayDetail.tsx lists feed events only.
- Status tags: vmm shows a tag only for requestStatus === 'pending' (EmployeeCalendarDayDetail.tsx:78-81). Employee shows approved (green), rejected (red) and pending/awaiting approval (blue) (DayDetailView.swift:18-34; Android EventListItem :145-171).
- Actions: in Employee, tapping an entry opens its detail (CalendarGridFeature eventTapped -> viewEvent; Android onAbsenceItemClicked). The sheet also offers Register (only with write permission) and Confirm time, with a warning alert and a forced retry (DayDetailFeature.swift:73-118; AbsenceFeedScre…
- Empty day: Employee skips the sheet and opens registration when write permission exists, and does nothing otherwise (CalendarGridFeature.swift dayTapped isEmptyDay guard; AbsenceFeedScreen.kt:384-392). vmm always opens the sheet and shows employee_calendar_empty_day_message (EmployeeCalendarDayDeta…
- Data scope: vmm filters the day's items by the attendance/absence/supplement settings for another employee, identified by companyId, companyTenantId and employeeId (EmployeeCalendarScreen.tsx eventsByDate). Employee shows the signed-in user's own feed plus workshift and special days.
- Date title: vmm uses a capitalised locale long date (formatLocaleLongDate). iOS uses a numeric date (DayDetailFeature.swift:33). Android uses DateFormatters.absence.
- (platform parity) Android adds a timesheet confirmation status row (Approved / Awaiting approval) to the sheet (CalendarViewMonthDayDetailsBottomSheetLayout.kt:66-68, 110-131). iOS DayDetailView has no such row.
- (platform parity) Android opens the sheet when the day has events, a time confirmation or a special day (AbsenceFeedScreen.kt:348-352). iOS opens it only when dayData.events is not empty (CalendarGridFeature dayTapped).
- (platform parity) Android disables the Add event and Confirm time buttons when offline (enabled = isNetworkAvailable, AbsenceFeedScreen.kt:379, 401). iOS DayDetailView has no network gating.
- (platform parity) The roster row cannot be tapped on either platform: iOS DayDetailView.swift:72-76 plus the CalendarGridFeature isRosterType guard, and Android RosterListItem has no onClickAction. The claim said the Android behaviour was not reported.

_Note: referee could not confirm: vmm evidence src/screens/EmployeeCalendarScreen/EmployeeCalendarScreen.tsx:76-200 covers only the onDayPress/selectedDay state. The sheet is rendered at EmployeeCalendarScreen.tsx:448-452.; me-android evidence CalendarView.kt:54-245 only passes the onDayClick callback. The sheet decision and buttons are in absence/src/main/java/com/visma/employee/absence/feed/AbsenceFee…_

### CAP-005: Customize what the calendar shows

**Fusion:** shared-diverged · **Personas:** Manager, Employee · **Confidence:** High

Hide weekends, show week numbers, filter entry types and choose icon or text style for events. The choices are saved across sessions.

- **vmm** (Manager): screens: `CalendarOptionsMenu (EmployeeCalendarScreen header right)`; storage: `settings.calendarHideWeekends`, `settings.calendarShowWeekNumbers`, `settings.calendarShowAttendance`, `settings.calendarShowAbsence`, `settings.calendarShowSupplement`, `settings.calendarDisplayMode` · evidence `src/screens/EmployeeCalendarScreen/components/CalendarOptionsMenu/CalendarOptionsMenu.tsx:53-130`
- **me-ios** (Employee): screens: `CalendarViewFilterFeature`, `CalendarViewFilterView`, `CalendarGridView (filter view)`; storage: `com.employee.vme.calendar.hideWeekends`, `com.employee.vme.calendar.showLabels`, `com.employee.vme.calendar.hideAbsence`, `com.employee.vme.calendar.hideAttendance`, `com.employee.vme.calendar.hideSupplement`, `com.employee.vme.calendar.hideRoster`, `com.employee.vme.calendar.showWeekNumbers`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarFeature/Features/Components/CalendarViewFilterFeature.…`
- **me-android** (Employee): screens: `CalendarViewFilterMenu`, `AbsenceFeedScreen`; storage: `hide_weekends`, `event_display_style`, `show_attendance`, `show_absence`, `show_supplement`, `show_roster`, `show_week_numbers`, `room-entity:user_preferences`; platform: `android-native` · evidence `absence/src/main/java/com/visma/employee/absence/feed/calendar_view/components/calendar/CalendarViewFilterMenu.kt:45-21…`

**How they differ:**
- Layers: Employee can also hide/show roster (calendarHideRoster / show_roster, Calendar.roster); vmm filters only attendance, absence and supplement (CalendarOptionsMenu.tsx:53-130)
- Storage: vmm redux settings.calendar* (persisted); Employee iOS UserDefaults com.employee.vme.calendar.*; Android Room user_preferences keyed by user email
- Filtering: vmm filters client-side on filterableType; iOS hide weekends also drops other-month rows (CalendarGridFeature.swift:284-310)
- (platform parity) iOS stores negative flags (hideAbsence, hideAttendance...) while Android stores show_* flags with show_week_numbers defaulting to 0 and others 1 (AbsenceFeedViewModel.kt:857-1004)
- Layers: Employee can also show or hide roster events (iOS CalendarViewFilterFeature.swift ItemID.showRoster -> hideRoster, CalendarGridFeature.swift:305-307 and monthLoaded filter isRosterType; Android CalendarViewFilterMenu.kt:203-213 show_roster). vmm filters only attendance, absence and suppleme…
- Storage and sync: vmm keeps the choices in redux settings.calendar* (persisted) and also includes them in the backend user-settings payload PUT users/{id}/settings (apiUserSetting.ts:79-86, 96-104). The backend value is loaded on login (useSettingsPersistence.ts:46-50), but a calendar-menu change t…
- Hide weekends: iOS drops weekend days and also removes other-month week rows and weekend day names (CalendarGridFeature.swift:385-389, 428-431). vmm switches to weekday-only rows through getWeekdayRowsInMonth (EmployeeCalendarScreen.tsx:252, 336).
- vmm's same options menu also carries a grid/agenda view-mode radio (CalendarOptionsMenu.tsx:94-102). In Employee the view mode is a separate control: Android has a top-bar toggle (AbsenceFeedViewModel.kt:862-890), and iOS uses a separate calendarViewMode key. This belongs to a different capability,…
- Filter semantics: vmm and Android store positive show_* flags. iOS stores negative hide* flags and inverts them in the filter view (CalendarViewFilterFeature.swift:96-101, CalendarFilterPreferences.swift:5-11).
- (platform parity) iOS stores hide* flags with every default false (showWeekNumbers false, showLabels false). Android stores show_* columns: show_week_numbers defaults to 0, show_roster to 1, hide_weekends to 0 (UserDatabase.kt:77,135,159). Android keys preferences by user email, while iOS uses glob…
- (platform parity) Android's filter lives in AbsenceFeedScreen and is shared with the list/month toggle. iOS's lives in CalendarGridFeature and regenerates the grid on each change. Both offer the same six toggles plus the icons/text radio.

_Note: referee could not confirm: me-android AbsenceFeedViewModel.kt:857-1004: most of this range is unrelated top-bar and list/calendar sync code; the filter setters are at about lines 978-1004; me-android CalendarViewFilterMenu.kt:45-210: the menu runs to about line 280, and the roster row (203-213) and events-style section (225-276) sit at or past the end of the cited range; vmm 'settings.calendar* (…_

### CAP-006: Start a time or absence registration from the calendar

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

From the calendar list add button, a day detail, a tapped empty day or a dragged day range, start registering new time or absence for yourself with the dates prefilled.

- **me-ios** (Employee): screens: `CalendarViewController new event button`, `DayDetailView register button`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/CalendarViewController.swift:526-541`
- **me-android** (Employee): screens: `AbsenceFeedScreen`, `EventSelectionKey`; events: `Calendar - Month view single day registration`, `Calendar - Month view period registration`; platform: `android-native` · evidence `absence/src/main/java/com/visma/employee/absence/feed/AbsenceFeedScreen.kt:366-440`

**How they differ:**
- (platform parity) Android disables the add button offline (AbsenceFeedScreen.kt:366-440); iOS fragment reports only the write-permission gate (CalendarViewController.swift:526-541)
- (platform parity) Offline, iOS hides the list's new-event button and turns off calendar buttons (CalendarViewController.swift:915-918, 937-943: newEventButtonContainer.isHidden = true, calendarButtonsAreEnabled = false). Android keeps the day-sheet add button visible but disabled (AbsenceFeedScreen…
- (platform parity) Android opens registration straight away when a day is tapped and the day sheet is not shown (AbsenceFeedScreen.kt:423-430). iOS goes through the DayDetailView register button (DayDetailView.swift:116-117).
- (platform parity) Android logs analytics events 'Calendar - Month view single day registration' and 'Calendar - Month view period registration' (AbsenceFeedScreen.kt:371, 609). I saw no equivalent events in the cited iOS registration code.

_Note: referee could not confirm: The claim's divergence line says iOS reports only the write-permission gate (CalendarViewController.swift:526-541). In fact iOS also handles offline (CalendarViewController.swift:915-918, 937-943)._

### CAP-009: View an employee's absence balances

**Fusion:** unique · **Personas:** Manager · **Confidence:** High

A manager expands Balances on an employee's HRM detail to see this year's vacation balance (normal, additional, transferred, transferred additional) plus self-certification sickness over 12 months and sick-child occasions this year.

- **vmm** (Manager): screens: `HrmEmployeeDetailScreen`; endpoints: `GET {calendarBaseUrl}/org/{orgId}/balances/employee/{employeeId}/total`, `GET {calendarBaseUrl}/org/{orgId}/employee/{employeeId}/summary/template/sickch…`, `GET {calendarBaseUrl}/org/{orgId}/employee/{employeeId}/summary/template/sickne…` · evidence `src/components/hrm/HrmEmployeeBalances/HrmEmployeeBalances.tsx:24-124`

_Note: Uses legacyEmployeeId and odpCompanyId; target date Dec 31 of the current year; 'days' suffix hard-coded. referee could not confirm: Description overstates what is shown: the vacation breakdown (normal, additional, transferred, transferred additional) in HrmEmployeeBalances.tsx:70-104 never renders, because useEmployeeBalanceDataClean.ts:133-166 never sets vacationDetails; Minor wording: the sick…_

### CAP-010: See my time and absence balances for a month

**Fusion:** unique · **Personas:** Employee · **Confidence:** Medium

An employee opens a balances summary (vacation, attendance/flex, sickness, sick child) from the calendar, expands rows and adjusts period or future-registration options, which the app remembers.

- **me-ios** (Employee): screens: `BalancesOverviewView`, `BalancesOverviewModalView`, `BalancesOverviewHostingController`; endpoints: `GET /employee/api/v2/calendar/time-balance-summary?fromDate={yyyy-MM-dd}&toDate…`; events: `Summary`, `show summary show more`; storage: `UserDefaults calendarBalancesControl (per-user dictionary controlId->option)`; platform: `ios-native`, `Survicate in-app survey on leave` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/BalancesOverview/Features/BalancesOverviewFeature.swift:47-115…`
- **me-android** (Employee): screens: `AbsenceSummaryScreen`, `AbsenceSummaryKey`, `SummaryCard`; endpoints: `GET /api/v1/employees/{odpUserId}/calendar/balances/combined`; storage: `Room UserPreferenceDbModel.include_future_registrations`; platform: `android-native`, `Survicate NPS survey trigger` · evidence `absence/src/main/java/com/visma/employee/absence/summary/AbsenceSummaryViewModel.kt:66-150; absence/src/main/java/com/v…`

**How they differ:**
- (platform parity) Data source: iOS loads GET /employee/api/v2/calendar/time-balance-summary for first..last day of the viewed month (BalancesOverviewFeature.swift:47-115); Android loads GET /api/v1/employees/{odpUserId}/calendar/balances/combined with no month range (BalancesServiceImpl.kt:24-60)
- (platform parity) Controls: iOS offers per-section period options stored in UserDefaults calendarBalancesControl; Android offers one 'include future registrations' toggle stored in Room include_future_registrations, shown only if attendance balances exist (AbsenceSummaryViewModel.kt:66-150)
- (platform parity) Android auto-reloads on reconnect; iOS shows COMMON_CONNECT_AND_RETRY
- (platform parity) Data source: iOS loads GET {employeeApiV2}/calendar/time-balance-summary for the first to last day of the month being viewed (GetTimeBalanceOverview.swift, LoadBalancesOverviewUseCase.repository.swift, CalendarService.swift:66-74). Android loads GET api/v1/employees/{odpUserId}/ca…
- (platform parity) Controls: iOS has period options for each section, saved through UserPreferences.setCalendarBalancesControlOption (BalancesControlPreferences.userPreferences.swift). Android has a single 'include future registrations' toggle, saved for each user email through UserPreferencesReposi…
- (platform parity) Offline: Android reloads by itself when the connection is restored (AbsenceSummaryViewModel.kt observeConnectionRestored). iOS shows COMMON_CONNECT_AND_RETRY on a noInternet error and waits for the user to tap retry (LoadBalancesOverviewUseCase.swift:15-16, BalancesOverviewFeature…
- (platform parity) Entry point: iOS opens the summary from the calendar container for the month on screen (CalendarContainerViewController.swift:389-406). Android opens it from the absence feed through onOpenSummary (AbsenceEntries.kt:210), with no month context.
- (platform parity) Android treats a response with an empty current balance list as an error (BalancesServiceImpl.kt hasCurrentBalances check); iOS has no matching check in the cited code.

_Note: Medium: Android's summary uses the combined-balances endpoint that iOS uses for start-page cards (CAP-011); a person should confirm the Android summary screen is the twin of the iOS month summary rather than of the start-page cards. referee could not confirm: The claim puts CalendarService.swift:57-74 as the time-balance-summary call. Lines 57-64 are actually getVacationBalances (GetCalendarBalan…_

### CAP-012: Register an absence or time event

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

The employee chooses an absence or time type from a grouped, searchable list of calendar templates (recently used first), fills the server-driven form (dates, full/partial day or definite time, hours/percent, comment, cost-unit dimensions, medical certificate, compensation level, vacation balance hint) and saves it, confirming a future-registration warning when the server requires, then sees a co…

- **me-ios** (Employee): screens: `ItemSelectorView (select type, ABSENCE_SELECTOR_TITLE)`, `AbsenceRegistrationTableViewController`, `PostScreenViewController`, `AddAbsenceView / AddAbsenceFeature (month view sheet)`, `AddAbsenceCoordinator (source .startPage)`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar/templates`, `GET {absenceTemplate._self.href} (absence type details, server-provided link)`, `POST /employee/api/v1/employees/{odpUserId}/absenceregistration`, `GET /employee/api/v1/employees/{odpUserId}/calendar/confirm/template`, `GET /employee/api/v1/employees/{odpUserId}/time/templates`; events: `new event created`, `Month view single day registration`, `Month view period registration`, `quickSelection(registerTimeOrAbsence)`, `quickSelection(registerAbsence)`, `quickSelection(reportTime)`; platform: `ios-native`, `Survicate in-app survey after save`, `NotificationCenter AppMessage.reloadStartPage` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrationTableViewController.swift:366-41…`
- **me-android** (Employee): screens: `EventSelectionScreen`, `EventSelectionKey`, `CreateEventSelectionLayout`, `AddEditEventScreen`, `AddEventKey`, `AddEditEventKey`, `AdditionalInfoBottomSheet`; endpoints: `GET /api/v1/employees/{odpUserId}/calendar/templates`, `GET /api/v1/employees/{odpUserId}/calendar/confirm/template`, `GET {template self link}?fromDate&toDate`, `POST /api/v1/employees/{odpUserId}/absenceregistration`; events: `Calendar - new event created`, `Calendar - new event created input type`, `Calendar - new event created with comment`; storage: `in-memory field cache mCachedFields (DateFrom, DateTo, Comment, InputType, Dime…`; platform: `android-native`, `Survicate NPS survey trigger after save` · evidence `absence/src/main/java/com/visma/employee/absence/add_event/AddEventViewModel.kt:85-243; absence/src/main/java/com/visma…`

**How they differ:**
- (platform parity) After save iOS shows a full-screen PostScreenViewController with a type-specific headline and illustration (PostScreenService.swift:20-60); Android shows a success dialog/message (absence_saved_messsage, dialog_success_title) and lands on the calendar at that date (AddEventViewMod…
- (platform parity) Android caches entered fields (dates, comment, dimensions, certificate) across type switches (mCachedFields); iOS re-fetches templates when dates change (AbsenceRegistrationTableViewController.swift:366-417)
- (platform parity) Android has an additional-info bottom sheet gated by AdditionalInfoLocalRuleHelper and a compensation-level field; iOS fragments report neither
- (platform parity) iOS offers a start-page quick action 'Register time or absence / Register absence / Report time' (StartPageService.swift:128-177); no Android start-page entry reported
- (platform parity) iOS service also loads GET /employee/api/v1/employees/{odpUserId}/time/templates (TimeService.swift:79-101); no Android equivalent reported
- (platform parity) Android type search matches display name, type code, type display name and group and excludes the recently-used group (EventSelectionLayout.kt:28-90); iOS ItemSelectorView search rules not reported
- (platform parity) After saving, iOS shows a full-screen post screen whose headline and illustration depend on the absence type (PostScreenService.swift:20-60). Android shows a success dialog and goes to the calendar unless the flow came from the chatbot (AddEventViewModel.kt onSaved, shouldNavigate…
- (platform parity) Android keeps entered field values when the user switches type (mCachedFields in AddEditEventViewModel.kt:64 and 386-392). The claim cites the iOS template re-fetch at AbsenceRegistrationTableViewController.swift:366-417, but that range is submitAbsenceAsync, so the iOS side is no…
- (platform parity) Android checks additional-info rules locally with AdditionalInfoLocalRuleHelper.validate (AddEditEventViewModel.kt:315). No iOS equivalent was confirmed.
- (platform parity) iOS also calls GET /employee/api/v1/employees/{odpUserId}/time/templates (GetTimeTemplates.swift:33). Android does not call this endpoint directly; it follows the template self link instead.
- (platform parity) The claimed start-page gap is wrong. Android has quick actions QC_ABSENCE, QC_TIME and QC_ABSENCE_AND_TIME that open EventSelectionKey (app/.../RootNavDisplay.kt:534-537), matching iOS StartPageService.swift:128-177.
- (platform parity) The claimed compensation-level gap is wrong. iOS handles a CompensationLevel field in AbsenceRegistrationViewModel.swift:77, and Android has CompensationLevelCalendarFieldViewModel.

_Note: referee could not confirm: The divergence line saying no Android start-page entry exists is wrong. The entry is at me-android/app/src/main/java/com/visma/employee/navigation/RootNavDisplay.kt:534-537.; The divergence line saying iOS fragments report no compensation-level field is wrong. iOS handles it at me-ios/Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/ViewModel/AbsenceR…_

### CAP-013: Pick cost-unit dimension values for a registration

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

While registering or editing, the employee picks dimension (cost unit/project) values from a paged, searchable list with recently used values first.

- **me-ios** (Employee): endpoints: `GET {dimension values action href} (cost-unit dimension values, paged/search)`, `GET /employee/api/v1/org/{orgId}/accounting/dimensions/{dimensionId}/values`; events: `cost units edited`; platform: `ios-native` · evidence `EmployeeServices/Calendar/Sources/Calendar/Service/AbsenceRegistrationService.swift:31-80`
- **me-android** (Employee): screens: `AbsenceDimensionModalBottomSheetLayout`; endpoints: `GET {dimension_values link}?query={search}`, `GET {dimensionListLink}`; events: `Calendar - cost units edited`; platform: `android-native` · evidence `absence/src/main/java/com/visma/employee/absence/addedit/AddEditEventViewModel.kt:637-880`

**How they differ:**
- (platform parity) iOS service calls GET /employee/api/v1/org/{orgId}/accounting/dimensions/{dimensionId}/values with searchTerm (AbsenceRegistrationService.swift:136); Android follows the template link rel 'dimension_values' with ?query= and 300 ms debounce (AddEditEventViewModel.kt:637-880)
- (platform parity) The search debounce differs: iOS waits 0.5 s (DimensionValueItemSelectorViewModel.swift, viewDidLoad debounce .seconds(0.5)), Android waits 300 ms (AddEditEventViewModel.kt:915 DEBOUNCE_DELAY = 300L).
- (platform parity) Android puts an 'empty dimension' option first so the user can clear the value (createEmptyDimensionOption, R.string.expense_draft_cost_unit_empty_dimension, AddEditEventViewModel.kt about line 813). The iOS selector adds no such option.
- (platform parity) iOS sorts recently used values by id (DimensionValueItemSelectorViewModel.swift init) and shows them in their own 'recently used' section, which hides while filtering. Android passes them unsorted as frequentlyUsedOptions and hides them when the search text is not blank.
- (platform parity) The endpoints are the same, not different: both follow the template's dimension-values link with search param 'q' (iOS DimensionValue.swift:53 searchParam = "q"; Android core Link.kt:69 QUERY_PARAM = "q", AbsenceServiceImpl.kt:158-165).

_Note: referee could not confirm: me-ios EmployeeServices/Calendar/Sources/Calendar/Service/AbsenceRegistrationService.swift:31-80: these lines are getCalendarTemplates, getAbsenceTypeDetails and registerAbsence. The dimension-value methods are at lines 115-135.; me-ios endpoint 'GET /employee/api/v1/org/{orgId}/accounting/dimensions/{dimensionId}/values' (GetDimensionValues.swift): the request struct i…_

### CAP-014: View details of a registered absence

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

The employee opens a registered absence or time entry to see its type, fields, comment, dates, certificate, dimensions and approval status, with edit/delete offered when the server allows.

- **me-ios** (Employee): screens: `AbsenceViewTableViewController`; endpoints: `GET {calendarItem link rel=details/self href}`, `GET {absence details href}`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Absence/AbsenceViewTableViewController.swift:213-275`
- **me-android** (Employee): screens: `EventDetailsScreen`, `EventDetailsKey`; endpoints: `GET {detailsLink}`; platform: `android-native` · evidence `absence/src/main/java/com/visma/employee/absence/details/AbsenceDetailsViewModel.kt:107-170`

**How they differ:**
- (platform parity) Android details screen offers both Edit and Remove (action_edit, action_remove, AbsenceDetailsViewModel.kt:107-170); iOS detail offers only Edit, with delete inside the edit form (AbsenceViewTableViewController.swift:213-275)
- (platform parity) Android details screen offers Edit and Remove in the top bar, each shown only when the 'update' or 'delete' link exists (EventDetailsScreen.kt:132-155, AbsenceDetailsViewModel.kt:80-101,123-128). The iOS detail view has only an Edit button and no delete action of its own; delete c…
- (platform parity) iOS shows Edit whenever the details response has any links (!linksForEdit.isEmpty). Before opening the editor it also checks the calendar write permission and loads calendar templates, and it opens nothing if no templates come back (AbsenceViewTableViewController.swift editEvent/g…
- (platform parity) iOS hides the InputType field when it equals full day, and drops empty fields from the groups. Android shows every field through read-only field view models (prepareFieldViewModels, fieldsShouldBeReadOnly=true).

### CAP-015: Edit a registered absence

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

From the absence detail, the employee edits a registered absence or time entry, including its type and cost units, and saves it through the entry's update link, confirming a future-registration warning when the server requires.

- **me-ios** (Employee): screens: `AbsenceViewTableViewController`, `AbsenceRegistrationTableViewController`, `PostScreenViewController`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar/templates`, `GET {absenceTemplate._self.href}`, `PUT {absence link rel=update href}`; events: `event edited`, `cost units edited`; platform: `ios-native`, `Survicate in-app survey after save` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrationCoordinator/EditAbsenceRegistrat…`
- **me-android** (Employee): screens: `AddEditEventScreen`, `AddEditEventKey`, `EventSelectionEditKey`; endpoints: `GET {detailsLink}`, `PUT {updateLink}`, `PUT {update link}`; events: `Calendar - event edited`, `Calendar - cost units edited`; platform: `android-native` · evidence `absence/src/main/java/com/visma/employee/absence/edit_event/EditEventViewModel.kt:191-238; absence/src/main/java/com/vi…`

**How they differ:**
- (platform parity) iOS confirms via PUT to the returned updateUrl and shows the PostScreen 'saved' variant; Android re-prompts and shows absence_updated_messsage (EditEventViewModel.kt:191-238)
- (platform parity) iOS sends the edit via UpdateAbsence PUT to the link href (AbsenceRegistrationService.swift:90) and then shows PostScreenViewController with isAbsenceUpdated (EditAbsenceRegistrationCoordinator.swift:96-115). Android sends absenceService.update(updateLink, template) and replaces t…
- (platform parity) iOS asks for the future-registration confirmation with a UIAlert titled calendar.time.futureRegistration (AbsenceRegistrationTableViewController.swift:510). Android handles it through FutureAbsenceConfirmationController, which calls updateEvent again with dimensionsWereEdited=fals…
- (platform parity) iOS asks for a Survicate survey after a successful save (EditAbsenceRegistrationCoordinator.swift:126-128). Android has no such step.
- (platform parity) iOS can also start an edit from the chatbot: the editFromChatbot and editPredictionFromChatbot initialisers (EditAbsenceRegistrationCoordinator.swift:58-80). Android can open the edit screen either from initial data or from a template link (EditEventViewModel.kt:78-81).
- (platform parity) Android can also edit a failed check-out via updateCheckoutEvent (EditEventViewModel.kt:241-260) and offers a delete check-in action in the edit top bar (AddEditEventScreen.kt:368-370). The claim does not mention this.
- (platform parity) When no certificate is selected, Android removes the CertificateDate and CertificatePercentage fields before the PUT and puts them back if it fails (EditEventViewModel.kt:206-212,231-234). No equivalent was seen in the cited iOS edit path.

_Note: referee could not confirm: me-android AddEditEventScreen.kt:340-372 is only the Scaffold and top bar (edit_absence_title), not the save logic, so it is weak evidence for saving.; Android endpoint 'PUT {update link}' is listed twice: it repeats 'PUT {updateLink}'._

### CAP-016: Delete a registered absence

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

The employee deletes a registered absence after a confirmation prompt, using the entry's delete link.

- **me-ios** (Employee): screens: `AbsenceRegistrationTableViewController`, `PostScreenViewController`; endpoints: `DELETE {absence link rel=delete href}`; events: `event deleted`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrationTableViewController.swift:423-465`
- **me-android** (Employee): screens: `EventDetailsScreen`; endpoints: `DELETE {deleteLink}`; events: `Calendar - event deleted`; platform: `android-native` · evidence `absence/src/main/java/com/visma/employee/absence/details/AbsenceDetailsViewModel.kt:80-105`

**How they differ:**
- (platform parity) iOS deletes from the edit form (AbsenceRegistrationTableViewController.swift:423-465) with Delete/Cancel; Android deletes from the details screen (AbsenceDetailsViewModel.kt:80-105) with Delete/Keep
- (platform parity) Where delete starts: iOS deletes from the absence edit form (AbsenceRegistrationTableViewController.swift:422-428) with a Delete/Cancel option menu. Android deletes from a top-bar button on the details screen (EventDetailsScreen.kt:143-155) with a Delete/Keep ConsentDialog (EventD…
- (platform parity) What happens after success: iOS dismisses and opens the post-registration screen with isDeleted: true (AbsenceRegistrationTableViewController.swift:453-455). Android shows a SuccessDialog (dialog_success_title, absence_delete_success) and then goes back (EventDetailsScreen.kt:262-…
- (platform parity) When delete is offered: Android hides the delete button unless a delete link is present (EventDetailsScreen.kt:155). iOS offers delete and only throws unexpectedError at call time if no rel=delete link exists (AbsenceRegistrationService.swift:94-99).
- (platform parity) Waiting message: iOS shows a generic PLEASE_WAIT spinner. Android shows a delete-specific absence_delete_deleting loading dialog.

### CAP-018: Check in and check out for the workday

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

The employee checks in from a start-page/home card at the current local time, sees elapsed time since check-in, and later checks out. A too-short or failed/cross-day checkout routes to editing the registration from the checkout template.

- **me-ios** (Employee): screens: `CheckinCardView`, `PostScreenViewController`, `EditCheckoutRegistrationCoordinator`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar/checkin`, `PUT /employee/api/v1/employees/{odpUserId}/calendar/checkin`, `PUT {checkin.updateUrl (HAL link from checkin response)}`, `GET {checkin.checkoutTemplateUrl (HAL link rel checkoutTemplate)}`, `PUT {checkout href}`; events: `checkIn`, `checkOut`, `checkedOutOnDifferentDay`, `checkoutForLunchBreak`, `openHighlight`; storage: `UserDefaults com.employee.vme.payslip.lastCheckoutDate`; platform: `ios-native`, `NotificationCenter AppMessage.resetCalendar post` · evidence `Employee/StartPage/ViewControllerCheckinWrapper.swift:43-136; EmployeeServices/Calendar/Sources/Calendar/Service/TimeSe…`
- **me-android** (Employee): screens: `HomeScreen (CheckInHighlight card)`, `HomeScreen (CheckOutHighlight card)`, `HighlightCard`, `HomeUiEventEffect`, `Edit checkout screen (OpenEditCheckoutScreen)`; endpoints: `GET api/v1/employees/{odpUserId}/calendar/checkin`, `PUT api/v1/employees/{odpUserId}/calendar/checkin`, `PUT {checkout link href}?localTime=`, `GET {checkout template link href}`; events: `Calendar - check in`, `Calendar - check out lunch break`, `Calendar - check out`, `Calendar - check out on other day`; storage: `UserPreferences.lastCheckoutTime (encrypted, per user email)`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/home/HomeViewModel.kt:803-1162; app/src/main/java/com/visma/employee/home/presenta…`

**How they differ:**
- (platform parity) Lunch-break analytics: iOS fires when previous checkout and check-in fall in 'today's lunch break' (ViewControllerCheckinWrapper.swift:43-136); Android uses a fixed 10:30-14:00 window (HomeViewModel.kt:828-857)
- (platform parity) Last checkout storage: iOS UserDefaults com.employee.vme.payslip.lastCheckoutDate; Android encrypted UserPreferences.lastCheckoutTime per user email
- (platform parity) Checkout request: Android PUT {checkout link href}?localTime=; iOS PUT {checkin.updateUrl} with device local time ISO8601 (PutCheckout.swift:37-40)
- (platform parity) Under one minute: iOS shows 'event not saved' (savedLessThanOneMinuteCheckinDuration); Android shows a less-than-one-minute info dialog instead of success
- (platform parity) Lunch-break analytics: the claim is wrong that the windows differ. Both use 10:30-14:00: iOS in Date.isInTodayLunchBreak (EmployeeCore/.../DateExtensions.swift:80-85) and Android in LUNCH_TIME_* constants (HomeViewModel.kt:1562-1565). The real difference is storage: iOS saves the…
- (platform parity) Last checkout storage: iOS keeps it in UserPreferences.setLastCheckoutDate (UserDefaults). Android keeps it in userPreferencesRepository.saveLastCheckoutTime(userEmail).
- (platform parity) Checkout request: Android sends PUT {checkout link href} with localTime as a query parameter (@Query, CalendarServiceImpl.kt:449-453). iOS sends PUT {updateUrl} with localTime in a JSON body (PutCheckout.swift:37-44, PutCheckinParams).
- (platform parity) Cross-day checkout: Android checks for a different day on the device before calling checkout. If the current status already has a checkout template link, it opens the edit dialog without calling the server (HomeViewModel.kt:883-910). iOS always calls PUT checkout first and treats…
- (platform parity) Under one minute: both platforms save the checkout on the server first. iOS then shows an 'event not saved' alert (savedLessThanOneMinuteCheckinDuration), which contradicts the saved state. Android shows an info dialog with the less_than_one_minute_passed title and body (HomeViewM…
- (platform parity) Checkout success confirmation: iOS shows a full-screen PostScreenViewController (absencePostScreenHeadline). Android shows a success dialog with the check-in and check-out dates (absence_saved_messsage, HomeViewModel.kt:971-980).

_Note: referee could not confirm: The iOS lunch-break analytics lines cite ViewControllerCheckinWrapper.swift:43-136, but that range has no lunch logic. It lives in Employee/StartPage/Time/CheckinHandler.swift:140-165, with the window defined in EmployeeCore/.../DateExtensions.swift:80-85.; The divergence line saying Android uses 'a fixed 10:30-14:00 window' as opposed to iOS is misleading: the iOS 'tod…_

### CAP-019: Edit or delete a check-in/check-out registration

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

The employee corrects the fields of a check-in/check-out time registration (including a failed checkout), or deletes it, in the shared registration form.

- **me-ios** (Employee): screens: `AbsenceRegistrationTableViewController (checkin editor)`, `PostScreenViewController`; endpoints: `GET {checkoutTemplate._self.href}?{fromDate}&{toDate}`, `POST {checkout link rel=update href}`, `{link.method} {checkin link rel=delete href} (method taken from server link)`; events: `checkin edited`, `checkin deleted`; platform: `ios-native`, `Survicate in-app survey after save` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AbsenceRegistrationCoordinator/EditCheckoutRegistra…`
- **me-android** (Employee): screens: `AddEditEventScreen`; endpoints: `GET {editCheckoutTemplateLink}`, `POST {checkoutSaveUrl}`, `DELETE {deleteCheckinUrl}`; events: `Calendar - check in edited`, `Calendar - check in deleted`; platform: `android-native` · evidence `absence/src/main/java/com/visma/employee/absence/edit_event/EditEventViewModel.kt:241-305`

**How they differ:**
- (platform parity) iOS requires both update and delete links and refreshes the template on date change only with addTime/timeWrite (EditCheckoutRegistrationCoordinator.swift:31-120); Android shows the delete action only when editing a failed checkout with a delete-checkin URL (AddEditEventScreen.kt:…
- (platform parity) iOS delete method comes from the server link ({link.method}); Android always uses DELETE (EditEventViewModel.kt:241-305)
- (platform parity) iOS refuses to open the editor unless the checkout template has both an update link and a delete link (EditCheckoutRegistrationCoordinator.swift:57-64). Android shows the delete action only when editingFailedCheckout is set and deleteCheckinUrl is not null (AddEditEventScreen.kt:3…
- (platform parity) iOS sends the delete with the HTTP method the server link names (TimeService.swift:204-212). Android always sends a DELETE through Retrofit @DELETE @Url (CalendarServiceImpl.kt:455-458).
- (platform parity) Android asks for confirmation before deleting (requestDeleteCheckin/confirmDeleteCheckin, EditEventViewModel.kt:276-288). It also only counts the delete as done when the returned check-in status is IDLE, otherwise it shows absence_delete_failed (EditEventViewModel.kt:296-303). On…
- (platform parity) iOS shows PostScreenViewController after an edit or delete, then a Survicate survey with a thank-you toast (EditCheckoutRegistrationCoordinator.swift:88-110). Android shows a success dialog (EventUpdated or CheckinDeleted) and has no survey (EditEventViewModel.kt:260, 301).
- (platform parity) Android hides the type selector when editing a failed checkout (AddEditEventScreen.kt:486-487).

_Note: referee could not confirm: The claim that iOS reloads the template on a date change only with addTime/timeWrite is not in the cited EditCheckoutRegistrationCoordinator.swift:31-120, and I did not find it. The editCheckout templates repository (AbsenceRegistrationTemplatesRepository.editCheckout.swift:13-19) returns a fixed template and an empty CalendarTemplates, so this detail is unconfirmed.; T…_

### CAP-020: Confirm worked time up to a date

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

The employee sends the timesheet for confirmation up to the suggested date or a chosen date, from the calendar list/feed, the month day detail or the event-type selector. Error-level validation blocks; warning-level validation can be accepted and force-confirmed.

- **me-ios** (Employee): screens: `UIAlertController action sheet (confirm period)`, `DatePicker`, `PostScreenViewController (period sent)`, `DayDetailFeature`, `DayDetailView`, `CalendarViewController confirm time button`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar/confirm`, `GET /employee/api/v1/employees/{odpUserId}/calendar/confirm/template?targetDate…`, `PUT {confirm template link rel=update href}`; events: `confirm time clicked`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/AbsenceRegistration/AddAbsenceCoordinator/AddAbsenceCoordinator.swift:1…`
- **me-android** (Employee): screens: `AbsenceFeedScreen`, `EventSelectionScreen`, `ConfirmTimeDialog`, `ConfirmTimeDialogs`; endpoints: `GET /api/v1/employees/{odpUserId}/calendar/confirm`, `GET /api/v1/employees/{odpUserId}/calendar/confirm/template?targetDate`, `PUT {confirm update link} body {date}`, `PUT {confirmLink}`; events: `Calendar - confirm time clicked`; platform: `android-native`, `Survicate NPS survey on dismiss of confirmation dialog` · evidence `absence/src/main/java/com/visma/employee/absence/confirmtime/ConfirmTimeDialogController.kt:13-98; absence/src/main/jav…`

**How they differ:**
- (platform parity) Android validates the date locally against the template date field (GreaterThan/GreaterThanOrEqual, ConfirmTimeDateValidator.kt) and warns for future dates; iOS relies on template validations (ConfirmTimeUseCase.timeService.swift:41-58)
- (platform parity) iOS shows a PostScreen 'period sent' after success; Android shows a success dialog then triggers a Survicate survey on dismiss (ConfirmTimeUseCase.kt:31-80)
- (platform parity) Both twins check the date on the device against the template's date-field validations. iOS uses firstFailingValidation (ConfirmTimeTemplate.swift:275-281, called from ConfirmTimeUseCase.timeService.swift:44-47). Android uses FieldInfoValidator (ConfirmTimeUseCase.kt:54-71). The cl…
- (platform parity) Android also checks the date as soon as the user picks it, using the template field already loaded (ConfirmTimeDateValidator.kt:36-53). It also sets the picker's earliest date from an Error-level GreaterThan or GreaterThanOrEqual rule (ConfirmTimeDateValidator.kt:22-34). iOS only…
- (platform parity) Android checks date.asDateOneMonthAheadString() instead of the chosen date (ConfirmTimeDateValidator.kt:39, ConfirmTimeUseCase.kt:57). iOS checks the chosen date as a plain string (ConfirmTimeTemplate.swift:279). This may be a bug.
- (platform parity) The code does not show that Android warns about future dates. Its warnings come only from the template's validation rules.
- (platform parity) After success, iOS shows a PostScreenViewController with PERIOD_SENT (AddAbsenceCoordinator.swift:226-229). Android sends ConfirmTimeSucceeded, reloads the feed, and triggers the Survicate NPS survey when the dialog is dismissed. That code is in EventSelectionViewModel.kt:202-230,…
- (platform parity) The analytics event fires at different moments. iOS logs confirmTime only after a successful PUT (ConfirmTimeUseCase.timeService.swift:35). Android logs CALENDAR_CONFIRM_TIME_CLICKED at the start of every attempt (ConfirmTimeUseCase.kt:32).
- (platform parity) On a forced confirm, iOS fetches the template again to get the update link (ConfirmTimeUseCase.timeService.swift:55-57). Android skips the template and sends the PUT to the item's confirmLink (ConfirmTimeUseCase.kt:34-46).

_Note: referee could not confirm: Survicate survey on dismiss is attributed to me-android ConfirmTimeUseCase.kt:31-80, but it is in EventSelectionViewModel.kt:228-230; The me-android 'platform' field lists 'Survicate NPS survey on dismiss of confirmation dialog', which is behaviour, not a platform; The divergence line says iOS relies on template validations while Android validates locally. In fact both…_

### CAP-021: Register time or absence by chatting with the Employee Agent

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

The employee opens the Employee Agent, types or dictates a request such as 'sick tomorrow', reviews the predicted events and confirms to create them (in parallel), handling extra warning confirmations; sickness needing a certificate must be edited first.

- **me-ios** (Employee): screens: `CalendarContainerViewController`, `CalendarChatBotCoordinator`, `CalendarChatBotView`, `CalendarChatBotFeature`, `ChatFeature`, `CalendarChatBotMessageView`; endpoints: `POST /employee/api/v1/employees/{odpUserId}/chatbot/predictCalendarRegistration`, `POST /employee/api/v1/employees/{odpUserId}/absenceregistration`; events: `Prediction request`, `Event Created`, `Amount of Events Created`, `Chatbot button tapped (log)`, `Voice input used in message`; platform: `ios-native`, `modal SwiftUI hosting controller`, `NotificationCenter AppMessage.reloadStartPage / resetCalendar`, `speech recognition`, `microphone`, `open app Settings on permission error` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:231-325;…`
- **me-android** (Employee): screens: `CalendarBotChatScreen`, `CalendarBotChatKey`; endpoints: `POST /api/v1/employees/{odpUserId}/chatbot/predictCalendarRegistration`, `POST /api/v1/employees/{odpUserId}/absenceregistration`; events: `CalendarBot - Prediction request`, `CalendarBot - Event Created`, `CalendarBot - Amount of Events Created`, `CalendarBot - Voice input used in message`; platform: `android-native`, `speech recognition voice input with RECORD_AUDIO runtime permission` · evidence `absence/src/main/java/com/visma/employee/calendar/calendar_bot/presentation/chat/CalendarBotChatViewModel.kt:247-612; a…`

**How they differ:**
- (platform parity) iOS entry is a sparkles button in the calendar nav bar gated by calendar permissions (CalendarContainerViewController.swift:410-422); Android entry point not reported in the fragments
- (platform parity) iOS reloads start page and calendar on close via NotificationCenter (CalendarChatBotCoordinator.swift:71-82); Android behaviour not reported
- (platform parity) Android offers copying a bot message (action_copy); iOS fragment reports none
- (platform parity) iOS entry is a nav-bar button in CalendarContainerViewController (showChatbot/openCalendarBot, ~lines 410-422, logs 'Chatbot button tapped'). On Android, CalendarBotChatKey is registered at AbsenceEntries.kt:167, is pushed from Learn More (AbsenceEntries.kt:225), and has an info b…
- (platform parity) iOS reloads the start page and calendar on close through NotificationCenter (CalendarChatBotCoordinator.swift:71-82, not re-opened). Android sets AbsenceResult FEED_RELOAD after each confirm through absenceResultHolder (CalendarBotChatViewModel.kt confirm handlers).
- (platform parity) Android's action_copy is not a copy action on bot messages. It is only the icon contentDescription on example prompts in Learn More (PromptView.kt:48), with no clipboard code in calendar_bot. The claim's copy divergence is unfounded.
- (platform parity) Android strips sickness-certificate info with removeSicknessCertificateInfoIfNeeded before showing predictions (CalendarBotChatViewModel.kt, onSendMessage). iOS instead marks such events as needing edits before confirmation (EventDataType.swift:79-82).

_Note: referee could not confirm: me-android string action_copy: it is not a copy action on bot messages. It is only a contentDescription on Learn More example prompts (absence/src/main/java/com/visma/employee/calendar/calendar_bot/presentation/learn_more/components/PromptView.kt:48)_

### CAP-022: Confirm the time sheet through the Employee Agent

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

When the agent reads the prompt as a time-confirmation request, it shows a confirm-time event; on confirm, the time sheet for that date is sent for approval.

- **me-ios** (Employee): screens: `CalendarChatBotView`; endpoints: `POST /employee/api/v1/employees/{odpUserId}/chatbot/predictCalendarRegistration`, `PUT {confirmTime template update action href}`; events: `Event Created`, `Amount of Events Created`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Message/QuickResponseAction/QuickResponseAction.confir…`
- **me-android** (Employee): screens: `CalendarBotChatScreen`; endpoints: `PUT {confirm update link}`; platform: `android-native` · evidence `absence/src/main/java/com/visma/employee/calendar/calendar_bot/presentation/chat/CalendarBotChatViewModel.kt:247-612`

**How they differ:**
- (platform parity) Analytics timing: Android logs chatBotEventCreated(CONFIRM_TIME_EVENT_TYPE) before the PUT, so it fires even if the call later fails (CalendarBotChatViewModel.kt:358-362). iOS sends eventConfirmed and eventsConfirmed(count:1) after the PUT, whether it succeeded or failed (QuickRes…
- (platform parity) Error display: Android shows the formatted ConfirmTimeError text plus a summary line with the date (confirm_time_event_selection_title_with_date) (CalendarBotChatViewModel.kt:428-455). iOS sends .failed(event, error) and leaves the display to the view model.
- (platform parity) Feed reload: Android sets AbsenceResultKeys.FEED_RELOAD after the attempt (CalendarBotChatViewModel.kt:460). No matching reload was seen in the iOS action.
- (platform parity) Follow-up: after success, Android adds a follow-up bot message (CalendarBotMessageHandler.getAdditionalCalendarBotMessageOrNull, :414-418).
- (platform parity) Android adds a user chat bubble (confirm_time_event_selection_title, :366-372) before the call. iOS uses message: .userConfirmationMessage() (:30).

_Note: referee could not confirm: The iOS evidence range 1-45 cuts off the analytics publish at lines 48-50. The file runs to line 53.; The iOS string keys registerEventsQuestion and timeSheetSentForApproval are not in the cited action file. Only confirmRegistration is (line 28). timeSheetSentForApproval was found only as a CalendarChatBotMessageViewModel factory in tests (CalendarChatBotMessageViewMode…_

### CAP-023: Ask the Employee Agent about leave balances

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

The employee asks the agent about balances and it replies with the balance text returned by the prediction service.

- **me-ios** (Employee): screens: `CalendarChatBotView`; endpoints: `POST /employee/api/v1/employees/{odpUserId}/chatbot/predictCalendarRegistration`; events: `Prediction request`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:346-352`

**How they differ:**
- (platform parity) Only iOS reports handling balancesQueryResult (CalendarChatBotViewModel.swift:346-352); no Android fragment reports it
- No platform parity gap: me-android also shows balancesQueryResult (absence/src/main/java/com/visma/employee/calendar/calendar_bot/presentation/chat/util/handlers/CalendarBotMessageHandler.kt:73-77; domain/CalendarBotChatResponse.kt:31-32) in the same order as iOS (CalendarChatBotViewModel.swift:277…

_Note: referee could not confirm: Divergence line 'Only iOS reports handling balancesQueryResult; no Android fragment reports it' is false: Android handles it in CalendarBotMessageHandler.kt:73-77_

### CAP-024: Edit a predicted registration before saving it

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

From the agent's suggestion, the employee opens the registration form pre-filled with the prediction (for example to add a required medical certificate for sickness), adjusts it and saves it as a real registration.

- **me-ios** (Employee): screens: `EditPredictedAbsenceRegistrationFeature`, `EditPredictedAbsenceRegistrationView (wraps EditAbsenceRegistrationCoordinator)`; endpoints: `POST /employee/api/v1/employees/{odpUserId}/absenceregistration`; events: `Edit registration button clicked`, `Edit registration event created`, `Amount of Events Created`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/EditAbsenceRegistration/EditPredictedAbsenceRegi…`
- **me-android** (Employee): screens: `CalendarBotChatScreen`, `AddEditEventScreen`; events: `CalendarBot - Edit registration button clicked`, `CalendarBot - Edit registration event created`; platform: `android-native` · evidence `absence/src/main/java/com/visma/employee/navigation/entries/AbsenceEntries.kt:373-455`

**How they differ:**
- (platform parity) iOS offers edit only when exactly one event is predicted (CalendarChatBotViewModel.swift:306-308); Android blocks multi-event registration when a certificate is mandatory and shows an error message (calendar_bot_chat_error_mandatory_sickness_certificate_in_multiple_events_message)
- (platform parity) Both twins offer 'Edit registration' only when exactly one event is predicted: iOS CalendarChatBotViewModel.swift:308 (messageEvents.count == 1), Android CalendarBotAdditionalActionHandler.kt:37 (calendarRegistrations.size == 1). This is not a difference between them.
- (platform parity) Android hides Confirm and makes Edit the primary action when the single prediction needs a mandatory sickness certificate (CalendarBotAdditionalActionHandler.kt:24, 46-50). iOS always shows confirm for events that are ready (CalendarChatBotViewModel.swift:303-306) and builds the c…
- (platform parity) When several events are confirmed at once, Android holds back the ones that need a certificate, shows calendar_bot_chat_error_mandatory_sickness_certificate_in_multiple_events_message and offers edit for them (CalendarBotChatViewModel.kt:496-500, 552-571; CalendarBotMessageHandler…

_Note: referee could not confirm: me-android screen 'AddEditEventScreen' is not what AbsenceEntries.kt:439-444 cites; the navigation there goes to AddEventKey (the add-event entry); The claim's divergence line suggests only iOS limits edit to one event; Android limits it the same way (CalendarBotAdditionalActionHandler.kt:37)_

### CAP-025: View, edit or delete an absence created in the agent chat

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

The employee taps an event the agent has just registered to open its detail, where they can edit or delete it; a deletion shows in the chat.

- **me-ios** (Employee): screens: `ViewAbsenceRegistrationFeature`, `AbsenceRegistrationView (wraps AbsenceCoordinator)`; endpoints: `GET {registration retrievalLink href}`, `PUT {absence _links rel=update href}`, `DELETE {absence _links rel=delete href}`; events: `Created event link clicked`, `Edit registration from preview`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/Chatbot/CalendarChatBotViewModel.swift:568-604`
- **me-android** (Employee): screens: `CalendarBotChatScreen`, `EventDetailsScreen`; events: `CalendarBot - Created event link clicked`, `CalendarBot - Edit registration from preview`; platform: `android-native` · evidence `absence/src/main/java/com/visma/employee/navigation/entries/AbsenceEntries.kt:373-455; absence/src/main/java/com/visma/…`

**How they differ:**
- (platform parity) After a deletion, iOS sends an absenceTypeDeleted message and also replaces the earlier registeredEventsSummary message in place with a registeredAbsenceDeleted version (CalendarChatBotViewModel.swift:568-589). Android only appends a generic 'Registration deleted!' message (absenc…
- (platform parity) Android opens the shared EventDetailsScreen with isOpenedFromChatBot=true, using absenceType.links.firstOrNull() (AbsenceEntries.kt:434-445). iOS opens a chatbot-specific ViewAbsenceRegistrationFeature and AbsenceRegistrationView using registeredAbsenceRetrievalLink (CalendarChatB…
- (platform parity) Android returns separate Edited and Updated results to the chat (onRegistrationEdited and onRegistrationUpdated in AbsenceEntries.kt:379-387). The cited iOS view-model lines only show how a deletion is sent back to the chat.

### CAP-026: Learn how to use the Employee Agent and try example prompts

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

The employee opens the info page to read about the agent and see example prompts from the server; tapping an example puts it in the chat input.

- **me-ios** (Employee): screens: `LearnMoreFeature`, `LearnMoreView`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/chatbot/examplePrompts`; platform: `ios-native` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/LearnMore/LearnMoreReducer.swift:34-66`
- **me-android** (Employee): screens: `CalendarBotLearnMoreScreen`, `CalendarBotLearnMoreKey`; endpoints: `GET /api/v1/employees/{odpUserId}/chatbot/examplePrompts`; platform: `android-native` · evidence `absence/src/main/java/com/visma/employee/calendar/calendar_bot/presentation/learn_more/CalendarBotLearnMoreViewModel.kt…`

**How they differ:**
- (platform parity) Load errors: iOS hides them. LearnMoreReducer.swift:47-48 treats a failure as an empty list. Android builds an error text from error_no_internet_connection or error_unexpected (CalendarBotLearnMoreViewModel.kt:63-73), but CalendarBotLearnMoreScreen.kt never reads state.error, so t…
- (platform parity) Caching: iOS keeps prompts it already loaded and skips a new fetch (LearnMoreReducer.swift:39-41). Android fetches again each time the ViewModel is created (CalendarBotLearnMoreViewModel.kt:28-32).
- (platform parity) Examples heading: iOS shows it as a section header only when there are prompts (LearnMoreView.swift:46-49). Android always shows calendar_bot_learn_more_examples inside HowToUse (components/HowToUse.kt:22).
- (platform parity) Feedback form: iOS opens it in an in-app SFSafariView sheet (LearnMoreView.swift:62-70). Android opens it in an external browser with an ACTION_VIEW intent (CalendarBotLearnMoreViewModel.kt:76-84).

### CAP-027: Send feedback about the Employee Agent

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

From the Learn More page, the employee opens an external feedback form (Google Forms) about the agent.

- **me-ios** (Employee): screens: `LearnMoreView`; platform: `ios-native`, `in-app web view for external feedback form` · evidence `Modules/CalendarFeature/Sources/CalendarFeature/Calendar/Chatbot/Views/LearnMore/LearnMoreReducer.swift:34-66`
- **me-android** (Employee): screens: `CalendarBotLearnMoreScreen`; platform: `android-native`, `external browser intent (Google Forms)` · evidence `absence/src/main/java/com/visma/employee/calendar/calendar_bot/presentation/learn_more/CalendarBotLearnMoreViewModel.kt…`

**How they differ:**
- (platform parity) iOS opens the form in an in-app web view (LearnMoreConstants.swift:4); Android opens an external browser intent (CalendarBotLearnMoreViewModel.kt:17-80)
- (platform parity) iOS opens the form in an in-app SFSafariView sheet (LearnMoreView.swift:63-68, LearnMoreReducer.swift:58-63 with dismissFeedbackForm); Android sends an ACTION_VIEW intent with FLAG_ACTIVITY_NEW_TASK to an external browser (CalendarBotLearnMoreViewModel.kt:76-84)
- (platform parity) Button label comes from different string sources: iOS uses the shared settings key S.Settings.sendFeedback (LearnMoreView.swift:58); Android uses calendar_bot_learn_more_feedback_button_title (CalendarBotLearnMoreScreen.kt:115)
- (platform parity) The form URL is defined twice: LearnMoreConstants.swift:12 and the FORM_URL companion constant at CalendarBotLearnMoreViewModel.kt:93 (the values are the same today)

_Note: referee could not confirm: Divergence cites LearnMoreConstants.swift:4, but the form URL constant is at line 12; Android evidence range CalendarBotLearnMoreViewModel.kt:17-80 is mostly prompt loading; the feedback intent is at lines 76-84 (URL at :93); iOS screen LearnMoreView is not in the files list; the button and SFSafariView code are in LearnMoreView.swift:58-68_

### CAP-211: See my vacation balances on the start page

**Fusion:** unique · **Personas:** Employee · **Confidence:** Medium

An employee sees their combined vacation and leave balances grouped with units.

- **me-ios** (Employee): screens: `not found in this shard`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar/balances/combined`; platform: `ios-native` · evidence `EmployeeServices/Calendar/Sources/Calendar/Service/CalendarService.swift:57-74`

**How they differ:**
- (platform parity) Android fragments report no start-page balance cards; the same combined endpoint feeds Android's summary screen instead (BalancesServiceImpl.kt:24-60)
- (platform parity) Both twins show a remaining-vacation card on the start or home page from the same combined endpoint. iOS uses RemainingVacationCardViewModel via GetVacationBalancesTask.swift:27-34; Android uses VacationDaysHighlightViewModel via BalancesHighlightViewModelMapper.kt:19-26 and HomeV…
- (platform parity) Permission gating differs. iOS loads balances when the user has any of addAbsence, addTime, absenceReadOnly, timeReadOnly, absenceWrite or timeWrite (StartPageViewModel.swift:236-247). Android gates on CalendarPermissions.visibility (HomeViewModel.kt:1334-1336).
- (platform parity) Empty or failed responses are handled differently. Android treats a non-success provider status or an empty 'current' list as an error, BalancesErrorResponse (BalancesServiceImpl.kt:30-41). iOS returns an empty card list when there is no vacation group and only reports an error on…
- Scope: both platforms show only the 'vacation' category on the start page. Other balance groups are dropped (iOS GetVacationBalancesTask.swift:28; Android BalancesHighlightViewModelMapper.kt:21-26 maps other categories to UnknownHighlightViewModel), so 'combined vacation and leave balances' oversta…

_Note: Service-layer fragment only; the screen was not found in this shard. referee could not confirm: screens: 'not found in this shard'. The screen exists: the iOS start page card (Employee/StartPage/StartPageViewModel.swift:246, Employee/StartPage/Cards/ViewModels/Absence/RemainingVacationCardViewModel.swift); divergence line 'Android fragments report no start-page balance cards'. Android's home feed…_

### CAP-212: Preview a day timeline (prototype)

**Fusion:** unique · **Personas:** Developer / internal · **Confidence:** Low

An internal prototype screen shows an expandable week calendar with a day timeline of hardcoded sample events. It does not appear to be reachable by users.

- **vmm** (Manager): screens: `TimelineScreen (SCREEN_NAME_TIMELINE)` · evidence `src/screens/TimelineScreen/TimelineScreen.tsx:17-184`

_Note: All events hardcoded (lines 17-130); registered at configs/navConfig/common/CommonScreensNavConfig.tsx:269-271 with no navigate() call found. Likely drop rather than carry over._

### CAP-213: Fill in and edit a server-defined form

**Fusion:** unique · **Personas:** Employee · **Confidence:** Low

The employee edits server-driven forms with typed fields, repeatable groups, validation and reveal/hide of sensitive values. The fragment says it is used by the Dottie employee-info feature.

- **me-ios** (Employee): screens: `DynamicFormView`, `DynamicFormEditSheet`, `DottieEmployeeInfoView (consumer, outside shard)`; platform: `ios-native` · evidence `Modules/DynamicForms/Sources/DynamicFormsUI/Views/DynamicFormEditSheet.swift:34-124`

**How they differ:**
- (platform parity) me-android implements the same Dottie employee-info form in its own dynamic-form engine (templates/.../dynamicform/model/DynamicFormField.kt, dottie/.../employee_info/EmployeeInfoViewModel.kt:262-272 for repeatable add and edit, form/components/DottieRedactedField.kt for masked va…
- (platform parity) Android loads the form from GET api/v2/dottie/employee/me/template and saves with PUT api/v2/dottie/employee/me (DottieServiceImpl.kt:518-521). The claim names no endpoint for iOS. Check that iOS uses the same pair.
- The domain is wrong: this is employee self-service personal data (Dottie employee info), not Time and absence.
- vmm only reads a manager's view of an employee with GET api/v2/dottie/employee/{id} (queryEndpointsDottie.ts:139-140). That is a different, read-only outcome and does not make this capability shared.

_Note: Probably belongs to an employee-info domain rather than Time and absence; it is a shared UI building block, not a time/absence outcome. A person should re-home it._

## AI assistant

Gaia and payslip chat assistants: asking questions, conversations, rating answers, suggested questions, assistant actions

### CAP-047: Ask the AI assistant a question

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** Medium

A person types or taps a question in the assistant chat and reads the AI answer. Manager: Gaia, a general assistant with streamed answers, tool progress, rich text and follow-up reply buttons. Employee: a beta payslip assistant that replies in a chat and keeps one server session per conversation.

- **vmm** (Manager): screens: `GaiaChatModal (SCREEN_NAME_GAIA_CHAT_MODAL)`, `GaiaChatContent`, `GaiaActionButton`, `GaiaToolStatus`; endpoints: `POST {gaiaBaseUrl}/api/v1/agent/{profileId}`, `GET {gaiaBaseUrl}/api/v1/bootstrap?profileId={profileId}`; events: `chat_opened`, `chat_closed`, `speech_started`, `action_button_tapped`, `message_sent`; storage: `redux gaiaChat state (messages, visible thread)`; platform: `Android soft input adjustResize via react-native-keyboard-controller` · evidence `src/components/modals/GaiaChatModal/GaiaChatModal.tsx:172-362`
- **me-ios** (Employee): screens: `EmployeeChatBotFeature`, `EmployeeChatBotView`, `PromptBar`; endpoints: `POST /employee/api/v1/employeeassistant/chat`; events: `Payslip bot screen opened`, `Payslip bot message sent`, `Voice input used in message`; storage: `in-memory sessionId (LockIsolated) reset on each new conversation` · evidence `Modules/EmployeeChatBot/Sources/EmployeeChatBot/EmployeeChatBotFeature/Features/EmployeeChatBotFeature.swift:104-200`
- **me-android** (Employee): screens: `PayslipBotChatScreen`, `PayslipBotChatKey`, `BotChatBubble`, `UserChatBubble`, `UserChatMessageView`, `ChatInputBar`, `TextInputBar`; endpoints: `POST /api/v1/employeeAssistant/chat`; events: `Payslip - Payslip bot screen opened`, `Payslip - Payslip bot message sent`, `Payslip - Voice input used in message` · evidence `payslip/src/main/java/com/visma/employee/payslip/payslip_bot/presentation/chat_screen/PayslipBotChatViewModel.kt:55-229…`

**How they differ:**
- Scope: vmm Gaia is a general assistant bound to a module, task, employee or home context (GaiaChatModal.tsx:172-362); me-ios/me-android answer only payslip questions (EmployeeChatBotFeature.swift:104-200, PayslipBotChatViewModel.kt:55-229)
- Endpoint: vmm POST {gaiaBaseUrl}/api/v1/agent/{profileId} plus GET bootstrap; Employee POST /employee/api/v1/employeeassistant/chat with body {sessionId,message}
- Answer delivery: vmm streams the answer with tool status rows (gaia_tool_calls_processing) and [[q:...]] follow-up reply buttons; me-ios gets one reply per message, sanitized of markdown images, links and HTML
- Input rules: vmm caps input at the bootstrap maxInputLength and disables send while loading or listening; me-ios trims the text and ignores it when empty or while a reply is loading, with no length cap reported
- Persistence: vmm keeps messages in persisted redux gaiaChat; me-ios keeps only an in-memory sessionId that resets on each new conversation
- Pre-filled question: vmm auto-sends initialMessage once or only seeds draftMessage into the composer; Employee auto-sends initialQuery/initialQuestionRes after the greeting
- (platform parity) The chat endpoint path differs between twins: me-ios /employee/api/v1/employeeassistant/chat, me-android /api/v1/employeeAssistant/chat (base path and casing)
- (platform parity) me-android reports an error_no_internet_connection state; no offline message was reported for me-ios
- Scope: vmm Gaia is a general manager assistant with conversation threads, a history screen and a question catalogue (GaiaChatModal.tsx:268-330). me-ios and me-android answer only payslip questions (EmployeeChatBotFeature.swift, PayslipBotChatViewModel.kt).
- Endpoint: vmm streams over SSE from POST {gaiaBaseUrl}/api/v1/agent/{profileId} (aguiService.ts:270, 297). The Employee app posts to /employee/api/v1/employeeassistant/chat and gets one reply per request (PostEmployeeAssistantChat.swift:13).
- Answer delivery: vmm shows streamed text and tool-call progress (aguiService.ts:377-395). The Employee app shows a loading bubble and then one reply with markdown removed (EmployeeChatBotFeature.swift:155-168; PayslipBotChatViewModel.kt, markdownSanitizer.sanitize).
- Input rules: vmm caps input at the bootstrap maxInputLength (GaiaChatModal.tsx:545). The Employee app trims the text and ignores it when empty or loading, with no length cap (EmployeeChatBotFeature.swift:141-145; PayslipBotChatViewModel.kt:onSendMessage).
- Conversation state: vmm keeps its threads in redux, can reopen a thread from a notification (openThread at GaiaChatModal.tsx:262) and has a history screen. The Employee app keeps only an in-memory sessionId that resets on each new conversation (ChatBotRepository.payslips.swift:15-28).
- Pre-filled question: vmm auto-sends initialMessage once or puts draftMessage in the input box without sending it (GaiaChatModal.tsx:338-362). The Employee app auto-sends initialQuery after the greeting (EmployeeChatBotFeature.swift:180-185) or through fireInitialQuestion on Android.
- Missed by the claim: the Employee app shows server-suggested questions, loaded from GET employeeassistant/suggestedQuestions and hidden once a message is sent (EmployeeChatBotFeature.swift:113-123; PayslipBotServiceImpl.kt:148). vmm shows bootstrap suggestedQuestions plus a question catalogue.
- Missed by the claim: Employee answer feedback (thumbs up/down) is sent to the server, keyed by sessionId (ChatBotRepository.payslips.swift:48-52; Android POST api/v2/EmployeeAssistant/feedback at PayslipBotServiceImpl.kt:152). vmm stores feedback in redux through gaiaChatSetMessageFeedback (GaiaCha…
- Greeting: Employee shows a fixed local greeting ('how can I help' on iOS via ChatMessage.howCanIHelp; payslip_bot_chat_first_message on Android). vmm shows welcomeMessage from the bootstrap response.
- (platform parity) The chat endpoint path differs between twins: me-ios /employee/api/v1/employeeassistant/chat, me-android api/v1/employeeAssistant/chat (base path and casing; PayslipBotServiceImpl.kt:143).
- (platform parity) me-android also sends a localTime field in the chat request (PayslipBotChatRequest.kt:11-12). The me-ios body has only sessionId and message (PostEmployeeAssistantChat.swift:7-10).
- (platform parity) me-android maps UnknownHostException to error_no_internet_connection (PayslipBotChatViewModel.kt:241). me-ios adds a generic botErrorMessage(error) (EmployeeChatBotFeature.swift:187-190).
- (platform parity) me-ios starts a conversation through the repository's startNewConversation, which clears the sessionId. me-android builds the first message locally in loadInitialMessages.

_Note: Merged as one outcome (ask the assistant) because both products offer a chat with an AI assistant, but the scope differs a lot (general Gaia versus payslip-only bot). A person should decide whether the new app has one assistant or two. Fragment 557 covers the shared chat-bubble components that the Employee calendar agent (CAP-021) also uses. referee could not confirm: The claimed vmm endpoint GET…_

### CAP-048: Open the assistant for the current screen from the header

**Fusion:** shared-diverged · **Personas:** manager · **Confidence:** High

From the sparkles header button the manager opens the Gaia chat scoped to the current task, or to the current module when no task is passed. A status dot shows when a chat is still running, has an unread answer or needs approval.

- **vmm** (Manager): screens: `ChatButton (header)`, `SCREEN_NAME_GAIA_CHAT_MODAL (nested in the current tab stack)`; storage: `GaiaChatContext (openForContext)` · evidence `src/components/navigation/ChatButton/ChatButton.tsx:24-52`

**How they differ:**
- Status indicator: vmm shows a StatusDot on the header icon for a running, unread or approval-waiting run in any chat (ChatButton.tsx:47-49, useGaiaRunIndicators.ts:26-39). The me-ios and me-android sparkles buttons have no dot or badge (MainPayslipView.swift:105-113, PayslipDetailsScreen.kt:155-160…
- Context scoping: vmm passes a per-task or per-module GaiaConversationContext through openForContext, so each surface keeps its own conversation (ChatButton.tsx:40). Employee sends openChatbotTapped with no context: the payslip detail and year-end report send it with no payload and open .assistant(.…
- Assistant behind the button: vmm opens one shared Gaia chat modal in whatever tab stack the user is in (ChatButton.tsx:42). Employee opens a separate bot per module: CalendarChatBotCoordinator for the calendar (CalendarContainerViewController.swift:415-422) and an .assistant destination for payslip…
- Coverage: vmm puts the button on nearly every module header (Start, Approval, ApprovalTask, ApprovalProcess, HRM, OSR, Autopay). Employee puts it only on the Calendar and Payslip headers (payslip list, payslip detail, year-end report).
- Permission gating: the iOS calendar button appears only when possibleFeatures.hasCalendarPermissions() is true (CalendarContainerViewController.swift:111). The vmm ChatButton has no such gate.
- (platform parity) Android payslip: the sparkles button was confirmed only on PayslipDetailsScreen.kt:155 (onOpenPayslipBot). On iOS it is also on the main payslip list (MainPayslipView.swift:107); whether Android has it on the salary feed is still unconfirmed (SalaryFeedViewModel.kt references a ch…

_Note: The context defaults to {type:'module', id: tab route name}. The dot uses needsAttention styling when a run needs approval._

### CAP-049: Ask the assistant about an approval task or past approval

**Fusion:** unique · **Personas:** manager, approver · **Confidence:** High

From a task, process, voucher-lines view or the approval list, the manager opens Gaia scoped to that document, or taps a suggested question chip (safe to approve?, approvers, comments, supplier history and more).

- **vmm** (Manager): screens: `ApprovalTaskScreen`, `ApprovalProcessDetailsScreen`, `ApprovalProcessTaskScreen`, `ApprovalTaskVoucherlinesScreen`, `ApprovalScreen`, `GaiaAssistBand on ApprovalTaskBXNLineEditScreen`, `GaiaChatModal`, `Approval header (chat button / assist toggle)`; events: `task_hint_tapped`, `history_hint_tapped`; storage: `redux features.showAiChat` · evidence `src/components/approval/GaiaTaskHints/GaiaTaskHints.tsx:28-80; src/screens/manager/ApprovalProcessDetailsScreen/compone…`

**How they differ:**
- Correction to the notes: the hint chips are gated by redux features.showGaiaHints (hooks/useGaiaHintsEnabled, off by default). features.showAiChat only gets the approval-list chat ready (ApprovalScreenProvider.tsx:57-63).
- Correction to the notes: GaiaTaskHints renders only when assistStyle === 'legacy' (ApprovalTaskScreen.tsx:437-444). Otherwise the task uses GaiaAssistBand with TASK_PROMPT_MODULE.
- Correction to the notes: GaiaProcessHints does not require processId (GaiaProcessHints.tsx:27-30 sends String(processId) even when it is undefined). Only GaiaTaskHints hides without a task uid (GaiaTaskHints.tsx:47).
- Not in the Employee twins: me-ios/me-android have no approval-task assistant. Their only chatbot is for calendar registration (me-ios Calendar/Request/Chatbot/GetExamplePrompts.swift, PostPredictCalendarRegistration.swift).

_Note: Hints stay hidden unless GAiA hints are enabled (useGaiaHintsEnabled dev flag) and the task uid is present. Hints are filtered by the task data and rotate on each mount. The context type is task, history or module._

### CAP-050: Ask the assistant about an employee

**Fusion:** unique · **Personas:** manager · **Confidence:** High

On the employee detail screen the manager taps a hint chip (pending tasks for this employee, vacation days) or the header assist button to ask Gaia about that employee.

- **vmm** (Manager): screens: `HrmEmployeeDetailScreen`, `HRM employee list header`; events: `employee_hint_tapped` · evidence `src/components/hrm/GaiaEmployeeHints/GaiaEmployeeHints.tsx:28-67`

**How they differ:**
- Within vmm, the chip card (GaiaEmployeeHints) only shows when assistStyle === 'legacy' (HrmEmployeeDetailScreen.tsx:145). Under 'toggle', the header button opens GaiaAssistBand instead (HrmDetailScreenHeaderRight.tsx:28-34, HrmEmployeeDetailScreen.tsx:114-128).
- The claim misses the toggle band's free-text question box (gaia_employee_ask_placeholder, HRM.DETAIL.GAIA_ASK_INPUT) at HrmEmployeeDetailScreen.tsx:120-127.
- The claim misses the band's prompt set: vacation_left, time_registration and pending_tasks, with one pinned and the others rotating (employeePrompts.ts:17-50). The legacy chips offer pending_tasks and vacation_days instead (GaiaEmployeeHints.tsx:41-48).
- Under the legacy style, the header shows a ChatButton that opens the general chat rather than asking about this employee (HrmDetailScreenHeaderRight.tsx:36).

_Note: The employee name is sanitized and embedded in the question. The conversation is keyed by employeeId or name. referee could not confirm: The claim lists 'HRM employee list header' (HrmEmployeeListScreenHeaderRight.tsx) as a screen for this capability. That header toggles the band or opens the chat without any employee context, so it is not asking about an employee.; The evidence range GaiaEmploye…_

### CAP-051: Ask the assistant from Home, Home search or a list's search band

**Fusion:** unique · **Personas:** manager · **Confidence:** High

The manager types a question, or taps a suggested question or prompt card, in the Home hero panel, the Home search (when nothing is found) or the combined search/ask band on list screens. This opens Gaia, or streams the answer inline, for that context.

- **vmm** (Manager): screens: `GaiaHeroPanel`, `GaiaAssistBand`, `StartScreenHeaderRight`, `HomeSearchScreen`, `StartHub`, `BnxtOrdersPane`, `BnxtInvoicesPane`, `BnxtRegistersPane` …; events: `assist_ask_tapped`, `promptModule.trackEventName (per-module hint event, not resolved)`; storage: `redux gaiaChat (persisted)`, `redux gaiaRuns (persisted)` · evidence `src/screens/StartScreen/components/StartHub/StartHub.tsx:249-260; src/screens/common/HomeSearchScreen/HomeSearchScreen.…`

**How they differ:**
- No cross-product divergence: the Employee product (me-ios/me-android) only has a calendar-registration chatbot (EmployeeCalendarBotService.swift, CalendarBotChatViewModel), a separate capability, and no ask from Home or search.

_Note: Two distinct questions are picked from a pool of 8 on each mount. The hero panel appears only in the 'legacy' assist style (A/B) and the band only in the 'toggle' style. Search text is debounced 600 ms. Home search asks only when there are no results (source 'home_search'). referee could not confirm: The note says the band shows 'only in the toggle style'. That is wrong: GaiaAssistBand.tsx return…_

### CAP-052: Ask the payslip assistant about a payslip or year-end report

**Fusion:** unique · **Personas:** employee · **Confidence:** High

From the payslips screen, a single payslip, a year-end report or a new-feature card, the employee opens the payslip AI assistant, optionally with a pre-filled question.

- **me-ios** (Employee): screens: `EmployeeChatBotView (sheet)`, `MainPayslipFeature.Destination.assistant`, `MainPayslipDetailFeature.assistant`, `MainYearEndReportFeature.assistant`, `MainPayslipFeature (openChatbotTapped)`; events: `newFeatureAction(payslip_bot)`; platform: `coordinator action showPayslipsBot(initialQuery) routes into the tab (PayslipsL…` · evidence `Modules/PayslipsFeature/Sources/PayslipFeature/Features/Main/MainPayslipFeature.swift:274-299; Employee/NewFeatures/New…`
- **me-android** (Employee): screens: `PayslipBotChatKey` · evidence `payslip/src/main/java/com/visma/employee/payslip/payslip_bot/presentation/chat_screen/PayslipBotChatViewModel.kt:55-229`

**How they differ:**
- (platform parity) me-ios opens it from MainPayslipFeature, MainPayslipDetailFeature, MainYearEndReportFeature and a new-feature card (NewFeatureCoordinator.swift:28-33); me-android always adds the entry button to the salary feed top bar and can pre-fire a question via PayslipBotChatKey.initialQuest…
- (platform parity) Both twins open the assistant from the same places. The claim says Android has no card entry, but on Android a home highlight card (HighlightCardAction.NavigateToPayslipBot, HomeEntries.kt:90-91) opens the bot with a pre-filled R.string.payslip_bot_holiday_pay_prompt (RootNavDispl…
- (platform parity) me-android also opens the bot from payslip details (PayslipDetailsScreen.kt:155, PayslipEntries.kt:126) and report details (ReportDetailsScreen.kt:82, PayslipEntries.kt:153), as well as the salary feed (SalaryFeedScreen.kt:145-153, PayslipEntries.kt:83). This matches the iOS entry…
- (platform parity) Presentation differs: iOS shows EmployeeChatBotView as a sheet (MainPayslipView.swift:30-31), while Android pushes PayslipBotChatKey as a full navigation destination (PayslipEntries.kt:93).

_Note: referee could not confirm: Divergence line claim 'no new-feature card entry was reported' for me-android: wrong, because HomeEntries.kt:90-91 opens the bot from a highlight card with a pre-filled question; The me-android implementation leaves out the detail and report entry points (PayslipDetailsScreen.kt, ReportDetailsScreen.kt, PayslipEntries.kt:126,153)_

### CAP-053: Start from a suggested question

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** Medium

When a conversation is empty, the assistant shows example questions that the person can tap to send.

- **vmm** (Manager): screens: `GaiaChatModal (SCREEN_NAME_GAIA_CHAT_MODAL)`; events: `message_sent` · evidence `src/components/modals/GaiaChatModal/GaiaChatModal.tsx:172-362`
- **me-ios** (Employee): screens: `EmployeeChatBotView`, `SuggestedPromptsView`; endpoints: `GET /employee/api/v1/employeeassistant/suggestedQuestions`; events: `Suggested prompt used` · evidence `Modules/EmployeeChatBot/Sources/EmployeeChatBot/EmployeeChatBotFeature/Features/EmployeeChatBotFeature.swift:114-125`
- **me-android** (Employee): screens: `PayslipBotChatScreen`; endpoints: `GET /api/v1/employeeassistant/suggestedQuestions`; events: `Payslip - Suggested prompt used` · evidence `payslip/src/main/java/com/visma/employee/payslip/payslip_bot/presentation/chat_screen/PayslipBotChatViewModel.kt:55-229`

**How they differ:**
- Source: Employee loads the questions from the server with GET /employee/api/v1/employeeassistant/suggestedQuestions; vmm shows suggested questions in the chat modal and the fragment reports no dedicated endpoint (they may come from the bootstrap call)
- When shown: vmm shows them only on an empty conversation; me-ios loads them only when there is no initialQuery and clears them once any message is sent
- Analytics: me-ios sends the prompt text in 'Suggested prompt used'; vmm sends message_sent with no suggestion-specific event reported
- (platform parity) me-android GET /api/v1/employeeassistant/suggestedQuestions versus me-ios /employee/api/v1/... path; me-ios shows an empty list on load failure, and this behaviour was not reported for me-android
- Source: vmm gets the suggestions from the Gaia bootstrap call GET ${baseUrl}/api/v1/bootstrap?profileId= (queryEndpointsGaia.ts:490), and only when the bootstrap flag is on (useGaiaChat.ts:1309-1312). Employee has its own endpoint, employeeassistant/suggestedQuestions (me-ios GetSuggestedQuestions.…
- Language and count: vmm picks the list for the user's language, falls back to English and caps it at 3 (useGaiaChat.ts:1311). Employee shows whatever the server returns, with no cap on the client.
- When shown: vmm shows them only when messages.length===0 and it is not loading (GaiaChatModal.tsx:364). me-ios fetches them only when initialQuery==nil and clears them on any send (EmployeeChatBotFeature.swift:114, sendMessage sets suggestedPrompts=[]).
- Analytics: vmm sends action_button_tapped with source suggested_question and the 1-based position as the label, never the question text (GaiaActionButton.tsx:25, gaiaEvents.ts:140-145). me-ios sends 'Suggested prompt used' with the prompt text (Events.swift:211). me-android sends 'Payslip - Suggest…
- vmm also shows a link to the capabilities catalog on an empty conversation (behind a dev flag), even when there are no suggestions (GaiaChatModal.tsx:507-515). Employee has no equivalent.
- (platform parity) me-android always fetches the suggestions but drops them if an initial question has already been sent (initialQuestionFired check, PayslipBotChatViewModel.kt:85). me-ios skips the fetch entirely when there is an initialQuery.
- (platform parity) The endpoint path is written as a relative 'api/v1/employeeassistant/suggestedQuestions' on me-android and as APIConstants.URL.employeeApiV1 + '/employeeassistant/suggestedQuestions' on me-ios. It is probably the same resource once the base URLs are resolved; I did not verify this.
- (platform parity) On load failure me-ios sends suggestedPromptsLoadFailed, and me-android ignores the error and keeps its empty default list. The user sees the same thing on both (no suggestions).

_Note: referee could not confirm: The vmm claim that there is 'no suggestion-specific event' is wrong: GaiaActionButton.tsx:25 sends GAIA_EVENTS.ACTION_BUTTON_TAPPED ('action_button_tapped') with source 'suggested_question'.; vmm evidence range GaiaChatModal.tsx:172-362 misses the rendering, which is at :364 and :495-505._

### CAP-054: Browse the catalog of questions the assistant can answer

**Fusion:** shared-diverged · **Personas:** manager · **Confidence:** High

From the chat header or the empty-chat link, the manager opens a catalog of example questions grouped by the integrations they can access, and taps one to send it to Gaia.

- **vmm** (Manager): screens: `GaiaCapabilitiesScreen (SCREEN_NAME_GAIA_CAPABILITIES)`, `GaiaChatModal`; events: `capability_question_tapped`, `capabilities_opened` · evidence `src/screens/gaia/GaiaCapabilitiesScreen/GaiaCapabilitiesScreen.tsx:30-67; src/components/modals/GaiaChatModal/GaiaChatM…`

**How they differ:**
- Source of questions: vmm builds the catalog on the device from its own list (utils/gaiaCapabilityCatalog via useGaiaCapabilitySections) with localized strings. Employee fetches a flat list of strings from GET /employee/api/v1/employees/{odpUserId}/chatbot/examplePrompts (me-ios EmployeeServices/Cal…
- Grouping and filtering: vmm groups questions by integration and shows only the sections for integrations the user can access (approval, HRM, autopay). It drops the working-time section when the user's country is unknown and puts the country name into those questions. Employee shows one ungrouped li…
- Scope of the assistant: vmm's catalog covers the whole Gaia assistant, across modules. Employee's covers only the calendar registration bot, inside the absence/calendar flow.
- What a tap does: vmm sends the question at once and continues the thread for that module (type 'module', id sectionKey), logging capability_question_tapped. On Android a tap stores the prompt as a pending chat prompt and closes the screen (AbsenceEntries.kt:478-484, absenceResultHolder.setPendingCh…
- Entry points and gating: vmm opens the catalog from the chat header's question-mark button or from a link on an empty chat, both behind the showGaiaCapabilities dev flag. Employee opens it from the calendar bot's 'Learn more' screen, which also offers a feedback button (CalendarBotLearnMoreScreen.k…
- Twin check: me-ios loads the prompts in Modules/CalendarFeature/.../Chatbot/Views/LearnMore/LearnMoreReducer.swift:45 and me-android in CalendarBotLearnMoreViewModel.kt:42. I did not confirm iOS's tap behaviour line by line, so there may be a (platform parity) gap if iOS sends the prompt instead of…

_Note: The entry points are gated by the useGaiaCapabilitiesEnabled dev flag. A tapped question continues the thread for that module context (type 'module', id sectionKey). referee could not confirm: The empty-chat link (gaia_capability_link) is at src/components/modals/GaiaChatModal/GaiaChatModal.tsx:510-517, outside the cited range 296-337. That range covers only the header button and its handler._

### CAP-055: Start a new assistant conversation

**Fusion:** unique · **Personas:** manager · **Confidence:** High

The manager clears the current chat and starts a fresh thread from the chat header or the conversation list.

- **vmm** (Manager): screens: `GaiaChatModal`, `GaiaConversationsScreen (SCREEN_NAME_GAIA_CONVERSATIONS)`; events: `new_chat_started` · evidence `src/components/modals/GaiaChatModal/GaiaChatModal.tsx:289-294`

**How they differ:**
- me-ios resets the payslip bot session only when the screen opens (EmployeeChatBotFeature.swift:104-108 calls ChatBotRepository.payslips.swift:20-21), and there is no button for it. This is noted for context only; the user outcome does not exist in the Employee product.
- vmm lets the user start a new chat from two places: the chat header button (GaiaChatModal.tsx:328-333) and the empty state of the conversation list (GaiaConversationsScreen.tsx:200-202). The history thread the user leaves is kept, and its run keeps going (useGaiaChat.ts:510-511).

_Note: Employee has no explicit action. me-ios starts a new server session (sessionId reset) each time the assistant opens._

### CAP-056: Find and resume a past assistant conversation

**Fusion:** unique · **Personas:** manager · **Confidence:** High

The manager opens the conversation history from the chat header, searches past conversations by title and reopens one. Threads still running or with unseen answers are raised to the top.

- **vmm** (Manager): screens: `GaiaConversationsScreen (SCREEN_NAME_GAIA_CONVERSATIONS)`, `GaiaChatModal`; endpoints: `GET https://api.assistant.vsn.dev/api/v1/conversations?profileId={profileId}&li…`; events: `conversation_selected`, `conversation_searched`, `conversation_history_opened`; storage: `redux gaiaChat (persisted; context-thread map)`, `redux gaiaRuns (persisted)` · evidence `src/screens/gaia/GaiaConversationsScreen/GaiaConversationsScreen.tsx:41-104`

_Note: The list is paged by GAIA_CONVERSATIONS_PAGE_SIZE. The context-thread map is rebuilt from server summaries so it survives a reinstall. Employee keeps no conversation history._

### CAP-057: Rename, pin or delete an assistant conversation

**Fusion:** unique · **Personas:** manager · **Confidence:** High

The manager long-presses a conversation in the list to rename it, pin or unpin it, or delete it after confirmation. Each row shows its title, last update, company and whether it is running or unread.

- **vmm** (Manager): screens: `GaiaConversationsScreen`, `GaiaConversationActionsSheet (bottom sheet)`, `GaiaConversationRow`; endpoints: `PATCH https://api.assistant.vsn.dev/api/v1/conversations/{id}`, `DELETE https://api.assistant.vsn.dev/api/v1/conversations/{id}`; events: `conversation_renamed`, `conversation_pinned`, `conversation_deleted`; storage: `redux gaiaChat (forget thread)` · evidence `src/screens/gaia/GaiaConversationsScreen/GaiaConversationsScreen.tsx:106-131; src/components/gaia/GaiaConversationActio…`

_Note: A title that is empty after trimming cannot be saved, and titles are capped at GAIA_CONVERSATION_TITLE_MAX_LENGTH. Delete first aborts any run streaming into that thread. The local thread reference is dropped only after the server delete succeeds._

### CAP-058: Resume the conversation an answer-ready notification announced

**Fusion:** unique · **Personas:** manager · **Confidence:** High

Tapping an 'answer ready' push notification or toast opens the chat directly in the named thread and marks it as read.

- **vmm** (Manager): screens: `GaiaChatModal`; endpoints: `GET {gaiaBaseUrl}/api/v1/agent/threads/{threadId}`; storage: `redux gaiaChat visibleThread (gaiaChatSetVisibleThread)`; platform: `push notification payload threadId (data/userInfo)` · evidence `src/components/modals/GaiaChatModal/GaiaChatModal.tsx:232-264`

_Note: The route threadId is handled once per params object. The visible thread is not published while the route thread is still opening, so the wrong thread is not marked read. referee could not confirm: platform 'push notification payload' is imprecise: the answer-ready notification is posted on the device by the app through notifee (legacy/vmm/src/utils/notifications/displayGaiaRunFinished.ts:59-82),…_

### CAP-059: Rate an assistant answer

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** High

The person gives an assistant answer a thumbs up or thumbs down, or undoes it. In Employee, a thumbs down opens a sheet to pick an issue category and add details, and the rating is sent to the server.

- **vmm** (Manager): screens: `GaiaChatItem`; events: `chat_feedback`; storage: `redux gaiaChat message feedback (gaiaChatSetMessageFeedback)` · evidence `src/components/modals/GaiaChatModal/GaiaChatItem.tsx:141-153`
- **me-ios** (Employee): screens: `EmployeeChatBotView`, `FeedbackThumbsView`, `ThumbButton`, `EmployeeChatBotFeedbackFeature`, `EmployeeChatBotFeedbackView`; endpoints: `POST /employee/api/v2/EmployeeAssistant/feedback` · evidence `Modules/EmployeeChatBot/Sources/EmployeeChatBot/EmployeeChatBotFeature/Features/EmployeeChatBotFeature.swift:210-223; M…`
- **me-android** (Employee): screens: `PayslipBotChatScreen (FeedbackBottomSheet)`; endpoints: `POST /api/v2/EmployeeAssistant/feedback` · evidence `payslip/src/main/java/com/visma/employee/payslip/payslip_bot/presentation/chat_screen/PayslipBotChatViewModel.kt:251-340`

**How they differ:**
- Backend: vmm stores feedback only in redux (gaiaChatSetMessageFeedback), with no backend call found (GaiaChatItem.tsx:141-153); Employee sends POST /employee/api/v2/EmployeeAssistant/feedback with {sessionId, rating, issueCategory?, details?}
- Negative feedback: vmm thumbs down is a single tap; Employee opens a sheet with issue categories Incorrect/Incomplete/NotWhatIAskedFor/Other and details capped at 1000 characters, and send is enabled only when a category is chosen or details are entered (EmployeeChatBotFeedbackFeature.swift:41-76)
- Eligibility: vmm hides feedback on user, error, streaming, first/welcome messages and messages without messageId; me-ios shows it only when isFeedbackEligible and sends nothing without a sessionId
- Confirmation: me-ios shows a thank-you toast after a thumbs up; vmm fires only the chat_feedback analytics event (label = answer shape)
- Undo: both let a repeat tap clear the rating, but me-ios sends positive feedback at most once per message, so the undo is local only
- (platform parity) me-android feedback endpoint POST /api/v2/EmployeeAssistant/feedback versus me-ios /employee/api/v2/...; me-android shows a character counter (payslip_bot_feedback_char_counter), and the 1000 limit is reported for me-ios only
- Backend: vmm keeps the rating only in redux (gaiaChatSetMessageFeedback, gaiaChatReducer.ts:197-202; GaiaChatItem.tsx:141-153) and never sends it to a server. Employee sends POST .../EmployeeAssistant/feedback with {sessionId, rating, issueCategory?, details?} (PostEmployeeAssistantFeedback.swift).
- Negative feedback: in vmm a thumbs down is one tap. In Employee it opens a sheet with issue categories Incorrect/Incomplete/NotWhatIAskedFor/Other and a details field capped at 1000 characters. Send is enabled only when a category is picked or the details are not blank (EmployeeChatBotFeedbackFeatu…
- Undo of a thumbs down: in vmm a second tap on the same thumb clears either rating (GaiaChatItem.tsx:144). In Employee a thumbs down cannot be undone: me-ios ignores the tap once the message is negative (EmployeeChatBotFeature.swift:227-229), and me-android swaps the button for a static icon and hid…
- Resend: Employee sends positive feedback at most once per message (sentPositiveFeedbackMessageIds / hasPositiveFeedbackBeenSent). vmm has no server send, so this does not apply there.
- Eligibility: vmm hides feedback on user messages, errors, streaming answers, the first/welcome message, empty messages and messages without a messageId (GaiaChatItem.tsx:154-155). me-ios shows it only when message.isFeedbackEligible (EmployeeChatBotView.swift:153), and nothing is sent without a ses…
- Confirmation: Employee shows a thank-you toast or snackbar. vmm has no confirmation beyond a shake animation and the chat_feedback analytics event, whose label is the answer shape (sources/tools/plain).
- (platform parity) Endpoint path: me-android posts to api/v2/EmployeeAssistant/feedback (PayslipBotServiceImpl.kt:153). me-ios posts to employeeApiV2/EmployeeAssistant/feedback.
- (platform parity) Thank-you message: me-ios shows the thank-you toast on every thumbs up, before and apart from the send, and shows none after a negative submit. me-android shows the snackbar only after the first positive send, and also after a negative submit.
- (platform parity) Failed send: when the negative send fails, me-ios still marks the message as negative (feedbackSubmissionFailed is handled the same way). me-android marks it negative before sending and ignores the result.
- (platform parity) Both platforms enforce the 1000-character details limit. me-android shows a counter string, payslip_bot_feedback_char_counter. me-ios exposes characterCount.

_Note: referee could not confirm: The claim reports the 1000-character limit for me-ios only. me-android enforces it too (FeedbackBottomSheet.kt:184).; The claim's undo line says both products let a repeat tap clear the rating. In Employee (both platforms) that is true only for a thumbs up; a thumbs down cannot be cleared._

### CAP-060: Copy an assistant answer

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee copies the text of a bot reply to the clipboard.

- **me-ios** (Employee): screens: `EmployeeChatBotView`; platform: `UIPasteboard.general` · evidence `Modules/EmployeeChatBot/Sources/EmployeeChatBot/EmployeeChatBotFeature/Features/EmployeeChatBotView.swift:231-239`
- **me-android** (Employee): screens: `PayslipBotChatScreen`; platform: `clipboard copy` · evidence `payslip/src/main/java/com/visma/employee/payslip/payslip_bot/presentation/chat_screen/PayslipBotChatViewModel.kt:55-229`

**How they differ:**
- (platform parity) me-ios copies from a long-press context menu, only on bot messages (EmployeeChatBotView.swift:231-239); me-android exposes action_copy, and its trigger was not reported
- (platform parity) The trigger matches: iOS uses a long-press .contextMenu shown only on bot messages (EmployeeChatBotView.swift:230-239); Android uses a long-press DropdownMenu shown only in the PayslipBotChatMessage branch (PayslipBotChatScreen.kt:291-345; onLongClickAction at 305, clipboard.setTe…
- (platform parity) The assistant is scoped differently: iOS copies from the general EmployeeChatBot module, while Android copies from the payslip-specific PayslipBotChatScreen (payslip module). The chatbots may cover different subjects.

_Note: referee could not confirm: me-android PayslipBotChatViewModel.kt:55-229 does not copy anything; its 'copy' matches are Kotlin data-class .copy() state updates. The real code is PayslipBotChatScreen.kt:305-345.; me-android PayslipBotChatMessageView.kt only passes onLongClickAction through (lines 21, 28); it does not copy to the clipboard itself.; me-ios EmployeeChatBotView.swift: the context menu…_

### CAP-061: Open a source cited in an assistant answer

**Fusion:** unique · **Personas:** manager · **Confidence:** High

The manager taps a knowledge source cited under a Gaia answer to open it in the external browser.

- **vmm** (Manager): screens: `GaiaChatItem`; events: `source_link_tapped`; platform: `Linking.openURL external browser` · evidence `src/components/modals/GaiaChatModal/GaiaChatItem.tsx:85-95`

**How they differ:**
- Employee (me-ios EmployeeChatBotView.swift:228) discards every URL tap in chatbot messages and shows no cited-sources list; vmm GaiaChatItem.tsx:221-230 lists sources and opens them with Linking.openURL. This only supports the unique class and is not a shared divergence.
- The claim's note says Employee 'strips links'. In fact me-ios still renders the links through LocalizedStringKey and discards the tap.

_Note: Only the link host is tracked, never the path. By contrast, Employee strips links from bot replies and makes them not openable._

### CAP-062: Approve or decline an action the assistant asks permission for

**Fusion:** unique · **Personas:** manager · **Confidence:** High

When Gaia wants to run a gated tool, it shows a confirmation card and the manager approves or declines it.

- **vmm** (Manager): screens: `GaiaApprovalRequestCard`; endpoints: `POST {gaiaBaseUrl}/api/v1/agent/{profileId}`; events: `approval_request_shown`, `approval_request_answered` · evidence `src/components/modals/GaiaChatModal/GaiaApprovalRequestCard/GaiaApprovalRequestCard.tsx:29-99`

_Note: The buttons are disabled while loading. Once resolved, the card shows the outcome (approved, declined, or auto_declined by a newer message). An unparseable requestApproval payload falls back to a status row._

### CAP-063: Approve or reject an approval task from within the assistant chat

**Fusion:** unique · **Personas:** manager, approver · **Confidence:** High

An approval task linked in a Gaia answer renders as a card with amount, due date, attachments or comments, and the manager approves or rejects it without leaving the chat.

- **vmm** (Manager): screens: `ApprovalTaskLinkCard`; endpoints: `GET approval/rest/tasks/{taskUid}`, `POST approval/rest/tasks/{taskId}/approve`, `POST approval/rest/tasks/{taskId}/reject`; events: `chat_task_card_action` · evidence `src/components/modals/GaiaChatModal/ApprovalTaskLinkCard/ApprovalTaskLinkCard.tsx:147-177`

**How they differ:**
- Within vmm, compared with the main approval flow: the chat card always sends an empty comment (ApprovalTaskLinkCard.tsx:166). On reject this posts {comment: ''}, even though queryEndpointsApproval.ts:312-313 says the API contract always requires the comment field for reject. This is a different com…
- The chat card offers only approve and reject (lines 300-313). The review, complete-review and forward actions that closeTask supports (queryEndpointsApproval.ts:325-340) are available only after tapping through to SCREEN_NAME_APPROVAL_TASK.

_Note: Buttons are shown only for actions in task.actions. The comment is sent empty. A 404 means the task was already processed. An overdue due date is highlighted, and the attachments variant shows at most 3. This overlaps the approval domain's approve/reject capability, with a different comment rule._

### CAP-064: Open an approval task linked in an assistant answer

**Fusion:** unique · **Personas:** manager, approver · **Confidence:** High

Tapping the task card in a Gaia answer opens the approval task detail screen, or the original link in the browser if the task cannot be loaded.

- **vmm** (Manager): screens: `ApprovalTaskLinkCard`, `SCREEN_NAME_APPROVAL_TASK (Approval tab)`; endpoints: `GET approval/rest/tasks/{taskUid}`; platform: `Linking.openURL fallback` · evidence `src/components/modals/GaiaChatModal/ApprovalTaskLinkCard/ApprovalTaskLinkCard.tsx:122-145`

**How they differ:**
- Refinement of the claim (not a cross-app divergence): the browser fallback appears only when fetching the task fails for a reason other than 404. A 404 shows a disabled 'already processed' card with no link (ApprovalTaskLinkCard.tsx:196-226).
- Refinement: once the task is approved or rejected from the card, the card is disabled and tapping it no longer opens the task detail (ApprovalTaskLinkCard.tsx:123, 320-321).

### CAP-065: Let the assistant navigate the app

**Fusion:** unique · **Personas:** manager · **Confidence:** High

Gaia can open an approval task, the approval list (to-do or history, with a search), an employee's detail, or the start, conversation-history and settings screens, and reports the result back into the chat.

- **vmm** (Manager): screens: `GaiaChatModal`, `SCREEN_NAME_APPROVAL_TASK`, `SCREEN_NAME_APPROVAL`, `SCREEN_NAME_HRM_EMPLOYEE_DETAIL`, `SCREEN_NAME_GAIA_CONVERSATIONS`, `SCREEN_NAME_SETTINGS`, `TAB_ROUTE_NAME_START_SCREEN`; endpoints: `GET approval/rest/tasks/{taskUid}`, `GET employee/companies/employees`, `POST {gaiaBaseUrl}/api/v1/agent/{profileId}`; events: `frontend_tool_executed`; storage: `redux approval active tab / search text / search bar` · evidence `src/components/modals/GaiaChatModal/useGaiaFrontendToolExecutor.ts:66-260`

_Note: Gated by the useGaiaFrontendToolsEnabled dev flag. Only the focused instance executes tool calls, and history or restored calls are never re-executed. Opening an employee requires hasAccessHRM and the id in the employee list._

### CAP-066: Dictate a message to the assistant by voice

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** Medium

The person taps the microphone in the assistant's message field, grants permission and speaks. The transcript is added to what was already typed.

- **vmm** (Manager): screens: `GaiaChatModal (SCREEN_NAME_GAIA_CHAT_MODAL)`; events: `speech_started`; platform: `speech recognition (@react-native-voice/voice, microphone permission)` · evidence `src/components/modals/GaiaChatModal/GaiaChatModal.tsx:172-362`
- **me-ios** (Employee): screens: `TextFieldWithVoiceInputView (hosted by EmployeeChatBot PromptBar and CalendarFe…`; events: `Voice input used in message`; platform: `Speech framework (SFSpeechRecognizer) on-device transcription`, `microphone (AVFoundation)`, `NSMicrophoneUsageDescription and NSSpeechRecognitionUsageDescription (Employee/…` · evidence `Modules/EmployeeUIComponents/Sources/EmployeeUIComponents/SwiftUI/METextFieldWithVoiceInput/TextFieldWithVoiceInputView…`
- **me-android** (Employee): screens: `ScreenOverlay (voice input overlay)`; events: `Payslip - Voice input used in message`; platform: `RECORD_AUDIO runtime permission with settings rationale`, `Android SpeechRecognizer (free-form, partial results, 3s silence)`, `open app settings` · evidence `core/src/main/java/com/visma/employee/core/employee_assistant/presentation/util/voice_input/VoiceInputHandler.kt:18-150…`

**How they differ:**
- Sending: vmm auto-sends the final speech transcript, appended to the existing text (GaiaChatModal.tsx:172-362); me-ios only appends the transcript and the person submits with Return (TextFieldWithVoiceInputViewModel.swift:35-71)
- Engine: vmm uses @react-native-voice/voice; me-ios uses on-device SFSpeechRecognizer; me-android uses Android SpeechRecognizer with partial results and a 3 s silence stop
- Reuse: the Employee dictation field is shared with the calendar agent chat (CalendarChatBotView, see CAP-021); vmm dictation lives only in the Gaia chat
- (platform parity) me-android shows a permission rationale with an open-settings link (voice_input_permissions_rationale_open_settings) and maps errors to InsufficientPermissions/NoMatch/Other; me-ios starts only when both speech and microphone permission are granted, and no settings rationale was r…
- (platform parity) me-ios limits the field to 3 lines and treats a typed newline as submit; me-android shows a voice input overlay (ScreenOverlay) and takes the recognition language from LanguageService
- Sending: vmm sends the final transcript automatically, joined to the text typed before recording (GaiaChatModal.tsx:185-194, 455); Employee only adds it to the field: iOS sends on Return or newline (TextFieldWithVoiceInputView.swift:63-76), Android sends through the view model's sendMessage (Paysli…
- Stopping: vmm stops after 1.5 s of silence once at least 2 s have been recorded, using its own silence check on iOS (useSpeech.ts:9-13); me-android stops after 3 s of silence (SpeechRecognitionHelperImpl.kt EXTRA_SPEECH_INPUT_COMPLETE_SILENCE_LENGTH_MILLIS=3000); me-ios stops when the recognizer fi…
- Engine: vmm uses @react-native-voice/voice with the app locale (useSpeech.ts:1-17); me-ios uses SFSpeechRecognizer() with partial results (SpeechRecognizerService.speechFramework.swift:29-30,139). It is not set to on-device recognition, so the claim's 'on-device' is unsupported
- Where it is used: Employee dictation is shared by the payslip/employee assistant (PromptBar.swift:45, PayslipBotChatScreen.kt:405) and the calendar bot (CalendarChatBotView.swift:231, CalendarBotChatScreen.kt:302); vmm dictation exists only in GaiaChatModal
- Analytics: vmm logs speech_started when recording starts (gaiaEvents.ts:64); Employee logs 'Voice input used in message' per sent message and per bot (AnalyticsEvents.kt:248,290; iOS payslipBotVoiceInputUsedInMessage and calendarBotVoiceInputUsedInMessage)
- (platform parity) me-android shows a permission rationale with an Open settings action (VoiceInputPermissionHandlers.kt:22-23) and shows error_unexpected only for OtherError (VoiceInputHandler.kt:140-147); me-ios silently does not start when a permission is missing (TextFieldWithVoiceInputViewModel…
- (platform parity) me-ios limits the field to 3 lines and treats a typed newline as submit (TextFieldWithVoiceInputView.swift:30,63-65); me-android shows a ScreenOverlay while listening and takes the language from LanguageService (VoiceInputHandler.kt:100-102)

_Note: referee could not confirm: me-ios platform claim 'on-device transcription': SpeechRecognizerService.speechFramework.swift creates SFSpeechRecognizer() and never sets requiresOnDeviceRecognition; me-android event 'Payslip - Voice input used in message' is one of two: 'CalendarBot - Voice input used in message' also exists (AnalyticsEvents.kt:248)_

## Home and navigation

Start or Home screen overview and cards, quick shortcuts, tab bar, More sheet, cross-module search, profile menu, What's New

### CAP-008: See what needs attention across modules on Home

**Fusion:** unique · **Personas:** manager · **Confidence:** High

The manager opens Home and sees a greeting with an attention summary, one card per licensed module (Approval, Autopay, HRM) with counts, stat tiles and top items, or an all-clear card; pull-to-refresh reloads everything.

- **vmm** (Manager): screens: `StartScreen (SCREEN_NAME_START_SCREEN = 'StartScreen')`, `StartHub`, `StartGreetingHeader`, `GaiaHeroPanel`, `StartModuleCard`, `StartStatTile`, `StartAllClearCard`, `StartHubSkeleton`; endpoints: `GET approval/rest/my-tasks`, `GET autopay/transaction/list?rows=2000`, `GET dialogue/companies?Status={active}&includingMessages=true&includingSplits=t…`, `GET employee/companies/employees`, `GET {ME_BASE_URL}employee/api/v2/calendar/my-employees/feed?From={monthStart}&O…`; events: `home_card_expanded`, `home_card_collapsed`; storage: `redux loginManager.hasAccessApproval/hasAccessAutopay/hasAccessDialog/hasAccess…`, `redux autopay.combinedList/combinedListStatus`, `redux features.isDebugEmptyMode, features.isEmployeeCalendarEnabled, features.i…`, `RTK Query cache fetchMyTasks/getAllDialogues/getAllEmployeesNew/getMyEmployeesA…`; platform: `react-native`, `pull-to-refresh` · evidence `src/screens/StartScreen/components/StartHub/StartHub.tsx:136-746`

_Note: Cards gated per access flag; top 3 items per card; HRM rows ranked unread > absent > new hire (30 days) > celebration (10 days); whole Start tab gated by toggledStartPageDevFlag. Kept apart from the employee highlights carousel because the content (team work queues vs personal status) and data sources are different. referee could not confirm: StartGreetingHeader is not rendered by StartHub. It is…_

### CAP-011: See my vacation balances on the start page

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee sees a card with their remaining vacation days and taps it to open the balances overview.

- **me-ios** (Employee): screens: `PresentBalancesOverviewCoordinator`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar/balances/combined`; events: `openHighlight`; platform: `ios-native` · evidence `Employee/StartPage/Tasks/GetVacationBalancesTask.swift:16-37`
- **me-android** (Employee): screens: `HomeScreen`, `HighlightCard`; endpoints: `GET api/v1/employees/{odpUserId}/calendar/balances/combined`; events: `StartPage - Highlight opened`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/home/HomeViewModel.kt:354-415`

**How they differ:**
- (platform parity) iOS opens PresentBalancesOverviewCoordinator; the Android tap target for the balance card is not reported.
- (platform parity) Tap target: iOS opens PresentBalancesOverviewCoordinator as a modal (AbsenceCardDetailProvider.swift:88,101-104); Android calls callbacks.onOpenAbsenceSummary() (HomeEntries.kt:219-220). The claim said the Android tap target was not reported, but it is in the code.
- (platform parity) Missing total: iOS gives the card no title or subtitle text when balanceGroup.total is nil (AbsenceCardDetailProvider.swift:43,68); Android treats a missing total as 0 and shows 'no vacation days remaining' (HighlightViewModelConverter.kt:462; VacationDaysHighlightViewModel.kt:15).
- (platform parity) Number formatting: iOS cuts the days to a whole number with String(Int(vacationDays)) (AbsenceCardDetailProvider.swift:71); Android formats them with a localised decimal format set to 0 fraction digits (VacationDaysHighlightViewModel.kt:16-18), which may round rather than cut.

_Note: referee could not confirm: me-android app/src/main/java/com/visma/employee/home/HomeViewModel.kt:354-415 is the general start-page load() routine, not the vacation-balance card. The relevant code is HomeViewModel.kt:296, BalancesHighlightViewModelMapper.kt:22-23, HighlightViewModelConverter.kt:458-485 and HomeEntries.kt:219-220.; me-android string absence_vacation_days_left_part_one is not a star…_

### CAP-017: See upcoming and ongoing vacation and parental leave on the start page

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee sees cards for declined, approved, upcoming or ongoing vacation and upcoming or ongoing parental leave; tapping one opens the absence detail and a grouped card opens the calendar.

- **me-ios** (Employee): screens: `PresentAbsenceCoordinator`, `CalendarCoordinator (CalendarFeedViewModel)`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/calendar`; events: `openHighlight`; platform: `ios-native` · evidence `Employee/StartPage/Tasks/GetCalendarItemsTask.swift:16-75`
- **me-android** (Employee): screens: `HomeScreen`, `HighlightCard`; endpoints: `GET api/v1/employees/{odpUserId}/calendar`; events: `StartPage - Highlight opened`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/home/HomeViewModel.kt:354-415; app/src/main/java/com/visma/employee/navigation/ent…`

**How they differ:**
- (platform parity) Time window: iOS one week back to one month ahead (GetCalendarItemsTask.swift:16-75); Android +/-28 days (HomeViewModel.kt:354-415).
- (platform parity) Tap target: iOS grouped card opens the calendar (CalendarCoordinator); Android opens the absence tab (ABSENCE_TAB=1) and refreshes the absence feed (HomeEntries.kt:212-247).
- (platform parity) Fetch window: iOS fetches from one week back to one month ahead (GetCalendarItemsTask.swift:19-20). Android fetches +/-28 days (HomeViewModel.kt:1292-1293, CALENDAR_REQUEST_DAYS_RANGE=28 at :1559), not at the cited HomeViewModel.kt:354-415.
- (platform parity) Grouping: iOS groups only approved, declined and upcoming vacation when there is more than one (GetCalendarItemsTask.swift:35-39). Android groups any highlight class with more than one item, because no absence highlight is marked Ungroupable (HomeViewModel.kt:1247-1269). So ongoin…
- (platform parity) Grouped card tap: iOS opens CalendarCoordinator with CalendarFeedViewModel (GroupedCardDetailsProvider.swift:127-133). On Android, HighlightNavigationMapper.getNavigationDestination has no GroupedHighlight case and returns null (HighlightNavigationMapper.kt:22-44), so a grouped ta…
- (platform parity) Single card tap: iOS opens PresentAbsenceCoordinator (AbsenceCardDetailProvider.swift:80-97). Android opens event details when calendarItem is present (HomeEntries.kt:227-231). Otherwise it falls back to the Absence tab (ABSENCE_TAB=1) and refreshes the absence feed (HomeEntries.k…
- (platform parity) Declined vacation rule: iOS shows it when dateFrom is on or after today (GetCalendarItemsTask.swift:60). Android requires dateFrom to be within one month ahead (AbsenceHighlightViewModelMapper.kt:27-29).
- (platform parity) Upcoming parental leave rule: iOS accepts any future dateFrom inside the fetch window (GetCalendarItemsTask.swift:62). Android requires dateFrom to be within one month ahead (AbsenceHighlightViewModelMapper.kt:33-35).

_Note: referee could not confirm: me-android app/src/main/java/com/visma/employee/home/HomeViewModel.kt:354-415 is the generic load() flow. It holds no absence filtering and no +/-28-day window, which are at HomeViewModel.kt:1292-1293 and :1559, with the classification in AbsenceHighlightViewModelMapper.kt:23-47.; me-android: the claim that a grouped card opens the absence tab has no code behind it. Gro…_

### CAP-067: Switch between the app's main areas

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** High

A signed-in person moves between the app's main areas through a bottom tab bar that only shows the areas their roles or permissions grant.

- **vmm** (Manager): screens: `Approval (TAB_ROUTE_NAME_APPROVAL)`, `AutoPay (TAB_ROUTE_NAME_AUTOPAY)`, `HRM (TAB_ROUTE_NAME_HRM)`, `BnxtOrders (TAB_ROUTE_NAME_BNXT_ORDERS)`, `OneStop (TAB_ROUTE_NAME_OSR)`, `StartScreen (TAB_ROUTE_NAME_START_SCREEN)`, `TabBar`; events: `approval_tab_clicked`, `autopay_tab_clicked`, `hrm_tab_clicked`, `osr_tab_clicked`; storage: `redux loginManager.hasAccessApproval/hasAccessAutopay/hasAccessHRM/hasAccessDia…`, `redux features.isApprovalLazyLoadingDisabled`, `redux settings.disableHolidaysTheme`; platform: `react-native` · evidence `src/configs/navConfig/navConfig.tsx:47-98`
- **me-ios** (Employee): screens: `METabBarController`, `TabbarCoordinator`, `StartPageCoordinator`, `PayslipsListCoordinator`, `ExpensesCoordinator`, `CalendarCoordinator`, `SettingsCoordinator`; platform: `ios-native` · evidence `Employee/TabbarUI/TabbarCoordinator.swift:52-202`
- **me-android** (Employee): screens: `HomeKey`, `SalaryFeedKey`, `ExpenseInboxKey`, `AbsenceFeedKey`, `SettingsKey`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/navigation/TopLevelRoute.kt:14-56`

**How they differ:**
- Areas differ: vmm tabs are Approval, Autopay, HRM, BXN, OneStop and Start (navConfig.tsx:47-98); Employee tabs are Home, Payslips, Expenses, Calendar, Settings (TabbarCoordinator.swift:52-202, TopLevelRoute.kt:14-56).
- Gating: vmm registers a tab only when its role flag is true (HRM also for hasAccessDialog, BXN needs dev flag AND getBnxtOrdersAccess); Employee always shows Start and Settings, Payslips needs .payslips, Expenses needs .expenseClaims, Calendar needs a time/absence permission.
- Visibility: vmm hides the bar when fewer than 2 tabs, when a screen sets display none, or while an approval/autopay multiselect has checked items; Employee has no such hiding rule reported.
- Landing tab: vmm lands on Start only when toggledStartPageDevFlag is on, else Approval; Employee always lands on Home/Start.
- Overflow: vmm moves extra areas behind a More item (moreMenuMinCount default 5); Employee has no More overflow.
- Decoration: vmm shows an HRM anniversary badge and a Santa hat on the focused tab at Christmas unless disabled; nothing similar in Employee.
- Analytics: vmm logs approval_tab_clicked/autopay_tab_clicked/hrm_tab_clicked/osr_tab_clicked; no tab events reported for Employee.
- (platform parity) Calendar gating: iOS lists addTime, addAbsence, confirmTime, timeReadOnly, absenceReadOnly, absenceWrite, timeWrite (TabbarCoordinator.swift); Android uses CalendarPermissions.tab (TopLevelRoute.kt:14-56).
- Areas differ: vmm registers Approval, Autopay, HRM, BnxtOrders, OSR and StartScreen (navConfig.tsx:47-98); Employee shows Start/Home, Payslips, Expenses, Calendar, Settings (TabbarCoordinator.swift tabTypes; TopLevelRoute.kt:14-51).
- Gating: vmm adds each tab from a loginManager flag (HRM when hasAccessHRM OR hasAccessDialog; BnxtOrders via getBnxtOrdersAccess = dev flag AND BXN access) and shows nothing if no flag is set; Employee always shows Start and Settings, Payslips needs payslips, Expenses needs expenseClaims/Expense, C…
- Start tab: in vmm StartScreen is always registered, but TabBar.tsx:99-107 hides it from the bar unless toggledStartPageDevFlag is on; Employee Home/Start is always visible.
- Landing tab: vmm opens on Start only when toggledStartPageDevFlag is on, otherwise on the first registered tab (Approval) (navConfig.tsx initialRouteName); Employee opens on Start/Home.
- Visibility: vmm hides the bar when there are fewer than 2 areas, when a screen sets tabBarStyle display none, or while approval/autopay multiselect has checked items (TabBar.tsx:132-137); Employee has none of these rules.
- Overflow and personalisation: vmm moves extra areas behind a More item (computeTabLayout with features.moreMenuMinCount), and users can pin, unpin and reorder tabs in the More sheet (TabBar.tsx:206-240, events tab_pinned/tab_unpinned/tabs_reordered/more_sheet_opened); Employee has a fixed tab list…
- Decoration: vmm shows the HRM anniversary badge (EmployeeBottomTabBadgeIcon, also on More when HRM is in overflow) and a Santa hat on the focused tab at Christmas unless settings.disableHolidaysTheme is set (TabBar.tsx:275-307); Employee has neither.
- Analytics: vmm logs approval_tab_clicked, autopay_tab_clicked, hrm_tab_clicked and osr_tab_clicked on tab press (TabBar.tsx:150-169); no tab-press events in Employee code.
- Deep-link tab switching: Employee TabbarCoordinator.handle(action:) switches tabs for showCalendar, showPayslips, showReceipts/showClaims, showSettings and similar actions; vmm's only equivalent in TabBar is the openDetailsTaskId redirect to Approval (TabBar.tsx:172-195).
- (platform parity) Calendar gating: iOS uses calendarTabPermissions {addTime, addAbsence, confirmTime, timeReadOnly, absenceReadOnly, absenceWrite, timeWrite} (TabbarCoordinator.swift); Android uses CalendarPermissions.tab = Absence, Time, Absence Write, Time Write, the two ReadOnly features and Con…
- (platform parity) Bar visibility: Android shows the NavigationBar only when the current back stack has 1 entry (RootNavDisplay.kt:434-437); I found no matching hiding rule in the iOS code (grep for hidesBottomBarWhenPushed and tabBar.isHidden found nothing).
- (platform parity) Context switch: iOS rebuilds the tabs on currentContextChanged/currentUserChanged and on the StartPage didChangeUserContext callback (TabbarCoordinator.swift); on Android the list is recomputed from visibleTopLevelRoutes(userHasFeature).

_Note: vmm TabBar.tsx:172-195 redirect on approval.openDetailsTaskId > 0 looks dead code. referee could not confirm: notes: the claim that TabBar.tsx:172-195 is 'dead code' is not proven. The effect runs whenever approval.openDetailsTaskId > 0, and I did not check who sets that value.; divergence line 'Employee always lands on Home/Start': this is the default for the first tab, not an explicit rule in t…_

### CAP-068: Open any integration from the More sheet

**Fusion:** unique · **Personas:** manager · **Confidence:** High

The manager opens the More sheet, sees a grid of every integration they can use with pinned, active and new or badge marks, and opens the one tapped.

- **vmm** (Manager): screens: `MoreSheet`, `TabBar`; events: `more_sheet_opened`; platform: `react-native` · evidence `src/components/navigation/MoreSheet/MoreSheet.tsx:163-186`

**How they differ:**
- Claim overstates the badge marks: TabBar.tsx:212-215 always sets hasBadge to false, so a cell dot means only a new integration. The HRM badge shows on the More pill instead (TabBar.tsx:300).
- The More item and sheet appear only when showMoreItem is true, from computeTabLayout (TabBar.tsx:109, 293, 315). With few integrations there is no More sheet.
- The Start route appears only when the toggledStartPageDevFlag flag is on (TabBar.tsx:94-108).

_Note: A dot marks a cell with a badge or a new integration; opening an area from the sheet marks it known (TabBar.tsx:106-248)._

### CAP-069: Customize which areas are pinned to the tab bar

**Fusion:** unique · **Personas:** manager · **Confidence:** High

In the More sheet's edit mode the manager pins or unpins integrations, reorders the pinned tabs and saves; newly granted areas are marked new.

- **vmm** (Manager): screens: `MoreSheet (edit mode)`, `TabBar`; events: `NAVIGATION_EVENTS.TAB_PINNED (configs/TabBar.tsx:224)`, `more_sheet_opened`, `tab_pinned`, `tab_unpinned`, `tabs_reordered`; storage: `redux pinned tabs via setPinnedTabs (configs/TabBar.tsx:220)`, `redux settings.pinnedTabs (persisted)`, `redux settings.knownIntegrations (persisted)`, `redux features.moreMenuMinCount (persisted)`; platform: `react-native` · evidence `src/components/navigation/MoreSheet/MoreSheet.tsx:62-92; src/configs/TabBar.tsx:106-248`

_Note: 1 to MAX_PINNED_TABS=4 pins; closing discards the draft; More appears only when area count >= moreMenuMinCount (default 5, migrated from 6 in persistEngine.ts:36-53); pinned list sanitized against granted routes._

### CAP-070: Search and sort a work list

**Fusion:** unique · **Personas:** manager · **Confidence:** Medium

From a list's header bar (approvals, HRM employees, autopay) the manager opens a search field or a sort panel, a dialogue-type selector or an overflow menu.

- **vmm** (Manager): screens: `ApprovalTopBar`, `HrmEmployeeTopBar`, `AutopayTopBar`; events: `clicked_sort_icon`, `clicked_on_search_icon`; platform: `react-native` · evidence `src/components/common/HeaderBottomBar/HeaderBottomBar.tsx:99-179`

**How they differ:**
- Sort is enabled only in ApprovalTopBar (showSort={tabSelectedPresent}, onPressSort=toggleFilterButton, ApprovalTopBar.tsx:75-78). HRM and Autopay hard-code showSort={false} with an empty onPressSort (HrmEmployeeTopBar.tsx:83-86, AutopayTopBar.tsx:71-76).
- Search is hidden in Approval and Autopay unless assistStyle === 'legacy' (ApprovalTopBar.tsx:73, AutopayTopBar.tsx:68).
- The dialogue-type selector appears only in HRM, on the Dialogue tab when the user has hasAccessDialog. The overflow menu appears only on the HRM employees tab when the Dottie integration is enabled (HrmEmployeeTopBar.tsx:89-92).
- BnxtWorkspaceScreen also uses HeaderBottomBar, but with search hidden and sort off, as tabs only (BnxtWorkspaceScreen.tsx:95-102). The claim does not mention this.

_Note: Shared header component; the actual search/sort rules live in each module's domain. referee could not confirm: src/components/common/HeaderBottomBar/HeaderBottomBar.tsx only opens and closes the controls. The search filtering and sort rules are not in the cited files.; Sort is listed for all three top bars, but it is only wired up in ApprovalTopBar. HrmEmployeeTopBar and AutopayTopBar pass showSo…_

### CAP-071: Search across approvals, invoices, employees and orders

**Fusion:** unique · **Personas:** manager · **Confidence:** High

From Home the manager types a query and jumps to a matching approval task, Autopay invoice, HRM employee or Business NXT sales order, grouped by module.

- **vmm** (Manager): screens: `HomeSearchScreen (SCREEN_NAME_HOME_SEARCH = 'HomeSearch')`; endpoints: `GET approval/rest/my-tasks`, `GET employee/companies/employees`; storage: `redux features.showHomeSearch (persisted, dev-tools flag, default off)`, `redux autopay.combinedList`; platform: `react-native` · evidence `src/screens/common/HomeSearchScreen/HomeSearchScreen.tsx:112-243; src/screens/StartScreen/hooks/useHomeSearchResults.ts…`

**How they differ:**
- Missing from the claim: when a query of 2 or more characters matches nothing, the screen shows an empty state (homeSearchEmptyTitle/homeSearchEmptyBody). A homeSearchAskGaia button then sends the same text to GAiA through sendMessage(question,'home_search'), and the answer shows on this screen in t…
- Missing from the claim: before the user types, the screen shows suggested GAiA questions (homeSearchIdleTitle, startGaiaQuestionN from pickGaiaQuestions), and the event GAIA_EVENTS.ASSIST_ASK_TAPPED is logged with source 'home_search'. The claim lists no events.
- Missing from the claim: BXN orders are the one source fetched live. useBnxtOrderList calls fetchOrders from useApiNXTOrders (useBnxtOrderList.ts:32,65) when the screen opens, but no BXN endpoint appears in the claim's endpoint list.
- Missing string keys: homeSearchIdleTitle, homeSearchEmptyTitle, homeSearchEmptyBody, homeSearchAskGaia.

_Note: Min 2 chars; case- and diacritic-insensitive contains over in-store data; up to 5 rows per group with a 'more' link; BXN orders fetched only with getBnxtOrdersAccess; behind a default-off dev flag._

### CAP-073: Open a pending approval task from Home

**Fusion:** unique · **Personas:** manager · **Confidence:** High

Tapping an approval row on the Home card opens the approval task detail inside the Start stack so back returns to Home.

- **vmm** (Manager): screens: `StartHub approval card`, `ApprovalTaskScreen (SCREEN_NAME_APPROVAL_TASK in Start stack)`; endpoints: `GET approval/rest/my-tasks`; events: `home_item_opened`; platform: `react-native` · evidence `src/screens/StartScreen/components/StartHub/StartHub.tsx:298-329`

### CAP-074: Open an upcoming Autopay payment from Home

**Fusion:** unique · **Personas:** manager · **Confidence:** High

Tapping a payment row on the Home Autopay card opens that transaction's invoice details in the Autopay tab.

- **vmm** (Manager): screens: `StartHub autopay card`, `AutopayInvoiceDetailsScreen (SCREEN_NAME_AUTOPAY_INVOICE_DETAILS via TAB_ROUTE_…`; endpoints: `GET autopay/transaction/list?rows=2000`; events: `home_item_opened`; storage: `redux autopay.combinedList`; platform: `react-native` · evidence `src/screens/StartScreen/components/StartHub/StartHub.tsx:331-363`

_Note: Rows sorted by payDate ascending, top 3; addressed by {accountIban, transactionId}. referee could not confirm: src/epics/autopay/autopayListLoadEpic.ts does not contain the endpoint URL. It calls apiAutopay.getCombinedPayments(), and the URL autopay/transaction/list?rows=2000 is built at src/services/apiAutopay/apiAutopay.ts:55._

### CAP-075: Follow up on unread dialogues, absent colleagues and new hires from Home

**Fusion:** unique · **Personas:** manager · **Confidence:** High

Tapping an HRM card row opens the dialogue thread or wage-run splits list for unread messages, or the employee detail for someone absent today or recently hired.

- **vmm** (Manager): screens: `StartHub HRM card`, `DialogueTaskScreen`, `DialogueSplitsScreen`, `HrmEmployeeDetail (via TAB_ROUTE_NAME_HRM)`; endpoints: `GET dialogue/companies?Status={active}&includingMessages=true&includingSplits=t…`, `GET employee/companies/employees`, `GET {ME_BASE_URL}employee/api/v2/calendar/my-employees/feed?From={monthStart}&O…`; events: `home_item_opened`; platform: `react-native` · evidence `src/screens/StartScreen/components/StartHub/StartHub.tsx:385-406`

_Note: One split opens its thread, several open the splits list (resolveDialogueNav); new hire = employment date 0-30 days ago._

### CAP-076: Review recent activity across approval, payments and dialogues

**Fusion:** unique · **Personas:** manager · **Confidence:** High

The Home 'Recent activity' feed lists the latest 8 events from the last 30 days (own approval actions and outcomes, paid or cancelled payments, dialogue replies) and opens each in its module.

- **vmm** (Manager): screens: `StartActivityFeed`, `StartActivityRow`, `ApprovalProcessTask (SCREEN_NAME_APPROVAL_PROCESS_TASK)`, `AutopayInvoiceDetails`, `DialogueTaskScreen / DialogueSplitsScreen`; endpoints: `GET approval/rest/my-history?page=1`, `GET approval/rest/my-tasks`, `GET approval/rest/processes/{processId}/progress-details`, `GET dialogue/companies?Status={active}&includingMessages=true&includingSplits=t…`, `GET autopay/transaction/list?rows=2000`; events: `home_item_opened`; storage: `redux approvalActivity.entries (actions taken this session)`, `redux settings locale`; platform: `react-native` · evidence `src/screens/StartScreen/hooks/useStartActivityFeed.ts:311-432`

_Note: referee could not confirm: Evidence range src/screens/StartScreen/hooks/useStartActivityFeed.ts:311-432 starts mid-builder; the merge/window/cap logic is at lines 183-338 (hook at 350-432); GET autopay/transaction/list?rows=2000 is not called by the feed; it reads the cached redux autopay.combinedList (useStartActivityFeed.ts:395). The endpoint exists at vmm/src/services/apiAutopay/apiAutopay.ts:…_

### CAP-077: Jump into a licensed module from Home

**Fusion:** unique · **Personas:** manager · **Confidence:** High

The Home Integrations list gives one row per licensed module (Approval, Autopay, HRM, OneStop Reporting, BNXT orders) that opens that module's tab, plus a 'Go to <module>' link on expanded cards.

- **vmm** (Manager): screens: `StartHub Integrations section`, `IntegrationRow`, `StartModuleCard`; events: `home_go_to_module`; storage: `redux loginManager.hasOSRAccess and access flags; getBnxtOrdersAccess selector`; platform: `react-native` · evidence `src/screens/StartScreen/components/StartHub/StartHub.tsx:477-569`

_Note: Get involved section (NPS, user testing) disabled by SHOW_GET_INVOLVED_SECTION=false (StartHub.tsx:112). referee could not confirm: string 'approval' is not a translation key shown for this capability: it is an icon name / QUICK_ACTION labelKey (StartHub.tsx:125); the module title 'Approval' is hardcoded (StartHub.tsx:489)_

### CAP-078: Discover and act on What's New announcements

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** High

A person sees What's New cards about new app features on Home, can follow the call-to-action to the feature, or dismiss the card so it stays hidden.

- **vmm** (Manager): screens: `StartWhatsNew`, `StartWhatsNewCard`, `WhatsNewMedia (in StartWhatsNewCard on StartScreen)`, `ApproveFromHomeDemo`, `AskGaiaAnywhereDemo`; events: `whats_new_shown`, `whats_new_card_viewed`, `whats_new_cta_pressed`, `whats_new_dismissed`, `whats_new_tip_shown`; storage: `redux whatsNew (persisted; dismissed and seen ids)`, `Firebase Remote Config key feature_whats_new_v1`, `Remote Config What's New payload (media keys)`; platform: `react-native`, `Firebase Remote Config`, `accessibility reduce-motion/screen-reader detection` · evidence `src/screens/StartScreen/components/StartWhatsNew/StartWhatsNew.tsx:34-153; src/components/common/WhatsNewMedia/WhatsNew…`
- **me-ios** (Employee): screens: `NewFeatureCardView`, `StartPageCardBottomSheetView`, `NewFeatureCoordinator`; events: `newFeatureAction`, `newFeatureBottomSheetConfirm`, `newFeatureBottomSheetDismiss`, `openHighlight`; storage: `WelcomeService new-feature don't-show-again flag (setNewFeatureDontShowAgain, E…`, `UserDefaults newFeatureDoNotShowAgain.<feature>`, `UserDefaults newFeatureFirstDisplayedTimestamp.<feature>`; platform: `ios-native` · evidence `Employee/StartPage/Tasks/GetWhatsNewTask.swift:13-27; Employee/Welcome/WelcomeService.swift:59-219`
- **me-android** (Employee): screens: `HomeScreen`, `HighlightCardBottomSheet`, `HomeKey`; events: `StartPage - New feature action (label payslip_bot)`, `StartPage - New feature bottom sheet confirm`, `StartPage - New feature bottom sheet dismiss`; storage: `HighlightDismissalRepository keys HOME_WHATS_NEW_* per user e-mail`, `room-entity:highlight_dismissals`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/home/presentation/handlers/HighlightCardActionHandler.kt:21-56; app/src/main/java/…`

**How they differ:**
- Source: vmm reads announcements from Firebase Remote Config key feature_whats_new_v1 (or bundled tips); Employee iOS uses a bundled list NewFeatures.whatsNewFeatures that is currently empty (WelcomeService.swift:60), so it is dormant.
- Presentation: vmm shows a swipeable spotlight section with Lottie, image, icon or live-component demo media (WhatsNewMedia.tsx:30-145); Employee shows a card in the highlights carousel that opens a bottom sheet.
- Call-to-action: vmm navigates to cta.tab or CommonActions.navigate(cta.route, cta.params) from the remote payload; Employee iOS routes through NewFeatureCoordinator and Android opens the payslip bot with a holiday-pay prompt.
- Filtering: Employee filters by suppression, feature flag, user/company permissions and country code (GetWhatsNewTask.swift) and Android needs the Payslips feature; vmm filtering by user is not reported.
- Expiry: Employee auto-suppresses cards 60 days after first display or after dateTo (WelcomeService.swift, NewFeatureHighlightHidingService.kt); no expiry reported for vmm.
- Dismissal storage: vmm persists dismissed and seen ids in redux; Employee iOS uses UserDefaults newFeatureDoNotShowAgain.<feature>, Android a Room table highlight_dismissals per user e-mail.
- Analytics: vmm logs whats_new_shown/card_viewed/cta_pressed/dismissed/tip_shown; Employee logs newFeatureBottomSheetConfirm/Dismiss.
- Accessibility: vmm freezes animations for screen reader or reduce-motion; no animated media in Employee.
- (platform parity) iOS removes the card on cancel but keeps it on confirm (GetWhatsNewTask.swift); Android's dismiss removes the card from the carousel (HighlightCardActionHandler.kt), and whether confirm keeps it is not reported.
- Source: vmm fetches the payload from Firebase Remote Config key feature_whats_new_v1 (whatsNewConfig.ts:113-127, consts/firebase.ts:19) and falls back to bundled tips (useWhatsNew.ts:124). Employee iOS uses a hard-coded NewFeatures.whatsNewFeatures list, which is empty (WelcomeService.swift:60). Em…
- Gating: vmm shows nothing unless state.features.isWhatsNewEnabled is on, and that switch lives on the developer settings screen ('Show What's New on Home', SettingsDevToolsScreen.tsx:916; useWhatsNew.ts:109). Employee gates by feature flag and permissions (iOS WelcomeService.swift:119-120) or by th…
- Audience filtering: vmm filters by integration roles approval/autopay/employee/osr, by min/max app version and by environment (useWhatsNew.ts:99-124, whatsNewConfig.ts:64-72). Employee iOS filters by user and company permissions and by country code (WelcomeService.swift:129-145). The claim wrongly…
- Expiry: Employee hides a card 60 days after it is first shown (iOS WelcomeService.swift:215-218; Android WHATS_NEW_LIFESPAN_MILLIS, NewFeatureHighlightHidingService.kt:44,58), and iOS also hides it after dateTo. vmm has no time-based expiry; it only hides cards the user dismissed, plus the version…
- Call-to-action: vmm navigates to cta.tab or runs CommonActions.navigate(cta.route, cta.params) from the payload (StartHub.tsx:576-594) and drops a CTA that points back to the Home screen (useWhatsNew.ts:43-51). Employee Android always opens the payslip bot (HighlightCardActionHandler.kt:35-38).
- Presentation: vmm shows a paged section with dots and Lottie, image, icon or live-component demo media (StartWhatsNew.tsx:118-151, WhatsNewMedia.tsx). Employee shows a card in the highlights carousel that opens a bottom sheet with confirm and 'don't show again' (NewFeatureCardViewModel.swift:62,81-…
- Dismissal storage: vmm keeps dismissed and seen ids in persisted redux, for the whole device. Employee iOS uses UserDefaults newFeatureDoNotShowAgain.<feature>. Employee Android stores dismissals per user e-mail with the HOME_WHATS_NEW_ prefix (NewFeatureHighlightHidingService.kt:18-25).
- Analytics: vmm logs whats_new_shown, card_viewed, cta_pressed, dismissed and tip_shown (StartWhatsNew.tsx:59-114). Employee logs newFeatureAction(payslip_bot) (Android HighlightCardActionHandler.kt:36) and bottom-sheet confirm/dismiss events.
- (platform parity) Employee iOS ships an empty feature list, so it is dormant (WelcomeService.swift:60), while Employee Android shows a live payslip-bot new-feature card (NewFeatureHighlightHidingService.kt, HighlightCardActionHandler.kt:35-38).
- (platform parity) On iOS, cancel sets 'don't show again' (NewFeatureCardViewModel.swift:85-86), and shouldRemoveCardOnConfirm (line 77) decides what happens on confirm. On Android, dismiss goes through onDismissAction (HandleHighlightFeatureCardEvent.kt:35-40) to hideCard; I did not check whether c…

_Note: referee could not confirm: The claim says vmm filtering by user is not reported, but useWhatsNew.ts:99-124 does filter by integration roles, version, environment and dismissed ids._

### CAP-079: See personal highlights on the start page

**Fusion:** unique · **Personas:** employee · **Confidence:** High

An employee opens Home and sees a sorted carousel of highlight cards about their own pay, absences, vacation balance, expenses, check-in and messages, chosen by their permissions, with offline, placeholder and error states; tapping a card opens its detail.

- **me-ios** (Employee): screens: `StartPageViewController`, `FailedToLoadView`, `InitialViewController`; events: `startPageLoadTime`, `openHighlight`; platform: `ios-native`, `NotificationCenter AppMessage.reloadStartPage observer`, `reachability listener reloads on connectivity change`, `tab bar item (home tab)` · evidence `Employee/StartPage/StartPageViewModel.swift:111-141`
- **me-android** (Employee): screens: `HomeScreen`, `HomeCarouselSection`, `HomeHighlightsCarousel`, `HighlightCard`; endpoints: `GET api/v1/employees/{odpUserId}/allpayslips`, `GET api/v1/employees/{odpUserId}/calendar/balances/combined`, `GET api/v1/employees/{odpUserId}/expense/inbox`, `GET api/v1/employees/{odpUserId}/expense/claims`, `GET api/v1/employees/{odpUserId}/calendar`, `GET api/v1/employees/{odpUserId}/expense/currencies`, `GET api/v1/employees/{odpUserId}/expense/templates/{type}`; events: `highlightOpened(<type>)`, `StartPage - Highlight opened`; platform: `android-native`, `network connectivity observer` · evidence `app/src/main/java/com/visma/employee/home/HomeViewModel.kt:354-415; app/src/main/java/com/visma/employee/navigation/ent…`

**How they differ:**
- (platform parity) Failure handling: iOS shows a retry view only when every task fails and an alert when online and visible (StartPageViewModel.swift:111-141); Android shows a partial-failure snackbar (HomeViewModel.kt:354-415).
- (platform parity) Reload triggers: iOS reloads on AppMessage.reloadStartPage and reachability change and syncs before load; Android reloads on reconnect or EventDataChanged and waits max 6s for feature flags.
- (platform parity) Android adds a lost-expense-permission card (expense_inbox_disabled_write_permission_card_text) and suppresses expense cards when the company removed expense write; not reported for iOS.
- (platform parity) Analytics: iOS logs openHighlight and startPageLoadTime; Android logs 'StartPage - Highlight opened' / highlightOpened(<type>).
- (platform parity) Failure handling: on iOS, if every task fails it throws allResultsFailed and shows FailedToLoadView; partial failures show an alert only when online and the start page is visible (StartPageViewModel.swift:111-141, StartPageViewController.swift:311-320). Android shows a ShowProvide…
- (platform parity) Reload triggers: iOS reloads on the AppMessage.reloadStartPage observer (StartPageViewController.swift:419) and on reachability changes (line 1055). Android reloads on EventDataChanged (HomeViewModel.kt:454) and on connection-state changes, and waits for feature flags up to FLAGS_…
- (platform parity) Correction to the claim: both platforms handle a company that removed expense write. iOS swaps the claims and drafts tasks for a FeatureDisabledTask with S.Expense.closedForRegistration (StartPageViewModel.swift:226-228). Android shows expense_inbox_disabled_write_permission_card_…
- (platform parity) On iOS the card set also includes surveys, what's new and information-message tasks, which run in parallel with the feature tasks (StartPageViewModel.swift:196-208). Android prepares check-in, survey and important-info data before the highlight flows (HomeViewModel.kt:381-385).
- (platform parity) Analytics: iOS logs openHighlight(highlightType:) and startPageLoadTime (StartPageViewController.swift:1190, 491). Android logs AnalyticsEvents.highlightOpened(type) (HomeViewModel.kt:1534).

_Note: Individual card types are split into their own capabilities below (payslip, vacation and leave, vacation balance, claim status, drafts, announcements). The manager Home is a separate capability; a merged app needs a decision on whether one Home serves both personas. referee could not confirm: Claimed divergence 'Android adds a lost-expense-permission card ... not reported for iOS' is wrong: iOS h…_

### CAP-080: Open the latest or upcoming payslip from the start page

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee sees a salary card (past, future or none) or taps a 'View latest payslip' quick action to open that payslip or the payslip list.

- **me-ios** (Employee): screens: `StartPageViewController`, `PresentPayslipCoordinator`, `SendActionCoordinator(.showPayslips)`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/payslips`; events: `quickSelection(latestPayslip)`, `openHighlight`; platform: `ios-native` · evidence `Employee/StartPage/Tasks/GetLatestPayslipTask.swift:16-43`
- **me-android** (Employee): screens: `HomeScreen`, `HomeButtonsList`; endpoints: `GET api/v1/employees/{odpUserId}/allpayslips`; events: `StartPage - Quick selection: view latest payslip`, `StartPage - Highlight opened`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/home/HomeViewModel.kt:354-415; app/src/main/java/com/visma/employee/home/HomeButto…`

**How they differ:**
- (platform parity) Endpoint: iOS calls GET /employee/api/v1/employees/{odpUserId}/payslips twice (offset 1, before/after today); Android calls GET api/v1/employees/{odpUserId}/allpayslips ascending and descending offset 1 and filters by current tenant.
- (platform parity) Android also opens the latest payslip through the QC_SALARY_SUMMARY quick selection (HomeEntries.kt:194-210); iOS uses quickSelection(latestPayslip).
- (platform parity) Endpoint: iOS calls GET {employeeApiV1}/employees/{odpUserId}/payslips twice, offset 1, before and after today (PayslipService.swift:80-88; GetPayslips.swift:44). Android calls GET api/v1/employees/{odpUserId}/allpayslips with from, offset, direction and a tenantIds filter (Paysli…
- (platform parity) With no payslip, iOS sends the user to the payslip list via SendActionCoordinator(.showPayslips) (PayslipCardDetailsProvider.swift:90-91). Android's quick action passes latestPayslipItem, which can be null, to onOpenPayslipDetails (HomeEntries.kt:202-203). I did not confirm what A…
- The claim's second divergence line is not a real difference. QC_SALARY_SUMMARY is simply Android's name for the same 'view latest payslip' quick action (HomeButtonsProvider.kt:214-219, event QUICK_SELECTION_VIEW_LATEST_PAYSLIP). It matches iOS quickSelection(.latestPayslip).

_Note: referee could not confirm: me-android app/src/main/java/com/visma/employee/home/HomeButtonsProvider.kt:112-158 defines the absence and time quick-selection buttons (QC_ABSENCE_AND_TIME, QC_ABSENCE, QC_TIME), not a payslip button. The latest-payslip button is at HomeButtonsProvider.kt:210-229.; me-android HomeViewModel.kt:354-415 is mostly generic home loading. Only lines 400-408 derive the latest…_

### CAP-081: Track the status of submitted expense claims from the start page

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee sees cards for approved, rejected, sent and unsent claims and for claims whose card transaction changed, was returned automatically or failed to send for approval; tapping opens the claim or a filtered claims list.

- **me-ios** (Employee): screens: `PresentExpenseCoordinator`, `CalendarCoordinator (ClaimsCalendarViewModel)`; endpoints: `GET /employee/api/v1/employees/{odpUserId}/expense/claims`; events: `openHighlight`; platform: `ios-native` · evidence `Employee/StartPage/Tasks/GetClaimsTask.swift:16-99`
- **me-android** (Employee): screens: `HomeScreen`, `HighlightCard`; endpoints: `GET api/v1/employees/{odpUserId}/expense/claims`; events: `StartPage - Highlight opened`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/home/HomeViewModel.kt:354-415; app/src/main/java/com/visma/employee/home/highlight…`

**How they differ:**
- (platform parity) Window: iOS 3 months back to 1 month ahead with per-status recency rules (GetClaimsTask.swift:16-99); Android 84 days back (HomeViewModel.kt:354-415).
- (platform parity) Tap target: iOS grouped card opens the claims calendar filtered by status; Android opens the Expense tab (EXPENSE_TAB=2, HomeEntries.kt:212-247).
- (platform parity) Android shows a card when the company removed expense write permission and suppresses expense cards; iOS simply requires expenseClaims and expenseApiWrite.
- (platform parity) Fetch window: iOS requests 3 months back to 1 month ahead (GetClaimsTask.swift:21); Android requests 84 days back (HomeViewModel.kt:1295, 1560). The per-status recency rules are the same on both (1 week, 1 month, 3 months).
- (platform parity) One claim can show two cards on iOS: getFilteredVMs adds both a transaction-changed card and a status card (GetClaimsTask.swift:51-64). Android uses a single `when`, so a claim gets only one card and the transaction-changed card wins (ExpenseHighlightViewModelMapper.kt:27-44).
- (platform parity) Android shows transaction-changed cards only when dateFrom is within 3 months (ExpenseHighlightViewModelMapper.kt:29-34). iOS applies no recency check to them beyond the fetch window (GetClaimsTask.swift:85-100).
- (platform parity) Tap target: on Android, a single claim card opens that claim's rows (onOpenClaimRows, HomeEntries.kt:223-227), and other or grouped expense cards open the Expense tab (EXPENSE_TAB=2, HighlightNavigationMapper.kt:31-35, 47). On iOS, a single card opens the claim (PresentExpenseCoor…
- (platform parity) Android has a card for when the company removed expense permission, which opens the Expense tab (RemovedExpensePermissionFromCompanyHighlightViewModel, HighlightNavigationMapper.kt:35; the string is used at HighlightResourcesProvider.kt:92). I did not check the iOS gating on expen…

_Note: referee could not confirm: me-android HomeViewModel.kt:354-415 is the generic load() for the start page and has no claim-specific logic. The claim logic is in ExpenseHighlightViewModelMapper.kt:23-45, and the window and grouping are at HomeViewModel.kt:1236-1295 and 1560.; me-android NewFeatureHighlightHidingService.kt:13-63 hides new-feature highlight cards and is not about claim status.; The '8…_

### CAP-082: Resume unsent expense drafts from the start page

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee sees how many receipts, mileages, allowances or credit-card transactions are still unsent, with totals, and taps the card to open them and send.

- **me-ios** (Employee): screens: `ReceiptsCoordinator`; events: `openHighlight`; storage: `local receipt drafts via ReceiptsService.getReceipts()`, `currencies via CurrenciesService.getCurrencies()`; platform: `ios-native` · evidence `Employee/StartPage/Tasks/GetDraftsTask.swift:16-96`
- **me-android** (Employee): screens: `HomeScreen`, `HighlightCard`; endpoints: `GET api/v1/employees/{odpUserId}/expense/inbox`, `GET api/v1/employees/{odpUserId}/expense/currencies`; events: `StartPage - Highlight opened`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/home/HomeViewModel.kt:354-415; app/src/main/java/com/visma/employee/navigation/ent…`

**How they differ:**
- (platform parity) Data source: iOS reads local drafts via ReceiptsService.getReceipts() (GetDraftsTask.swift:16-96); Android fetches GET api/v1/employees/{odpUserId}/expense/inbox (HomeViewModel.kt:354-415).
- (platform parity) iOS merges several draft types into one grouped card; Android builds pluralised combined text per receipt/mileage/allowance/credit-card count (CombinedExpensesTextBuilder.kt).
- (platform parity) Currencies: iOS reads them from the local database (CurrenciesService.swift:30-31 getCurrenciesFromDatabase). Android fetches GET api/v1/employees/{odpUserId}/expense/currencies (ExpenseTemplatesServiceImpl.kt:223).
- (platform parity) Card layout: iOS shows a separate card per type when only one type has drafts and a grouped card when several types do (GetDraftsTask.swift:49-57). Android always maps drafts to one UnsubmittedExpensesHighlightViewModel with combined pluralised text (HomeViewModel.kt:659-667, Comb…
- (platform parity) Android hides the drafts highlight when the company has removed the permission to add claims (HomeViewModel.kt:609-620 isAnExpenseHighlight / hasCompanyRemovedPossibilityToAddClaims). The iOS GetDraftsTask has no such check.
- Correction to the claim: both platforms load drafts from the same endpoint. iOS uses GetReceipts.resourceName .../employees/{odpUserId}/expense/inbox (GetReceipts.swift:20-22). Android uses @GET api/v1/employees/{odpUserId}/expense/inbox (ExpensesInboxServiceImpl.kt:666). The data source is not a p…

_Note: referee could not confirm: me-ios storage 'local receipt drafts via ReceiptsService.getReceipts()' is wrong: getReceipts() makes a network request to .../expense/inbox (ReceiptsService.swift:30-41, GetReceipts.swift:20-22).; Divergence line 1 of the claim ('iOS reads local drafts') is wrong for the same reason.; HomeViewModel.kt:354-415 is the general load() routine. The drafts logic is at HomeVi…_

### CAP-083: Read important messages, surveys and app-update prompts on Home

**Fusion:** unique · **Personas:** employee · **Confidence:** Medium

The employee sees a remotely controlled important-info message, a survey card and an app-update card on Home, opens each in a bottom sheet to follow it (info link, survey URL, Play Store) or dismisses it so it stays hidden.

- **me-android** (Employee): screens: `Home highlights`, `HomeScreen`, `HighlightCardBottomSheet`; endpoints: `GET /api/v1/RemoteControl/employee/{odpUserId}/message`, `GET /api/v1/surveys`; events: `Survey - survey card survey opened`, `Survey - survey card opened`, `StartPage - Highlight opened`; storage: `HighlightDismissalRepository keys HOME_SURVEY_CARD_*, UPDATE_CARD_* per user e-…`, `room-entity:highlight_dismissals`; platform: `android-native`, `Play Store intent`, `external browser` · evidence `absence/src/main/java/com/visma/employee/absence/data/important_info/ImportantInfoServiceImpl.kt:20-35; app/src/main/ja…`

**How they differ:**
- (platform parity) iOS start page mentions surveys and messages among highlight cards (StartPageViewModel.swift:111-141) but no iOS fragment reports the endpoints, bottom sheet or dismissal for them; app-update card only evidenced on Android.
- (platform parity) The iOS twin does implement the information message: GetInformationMessageTask.swift:24 calls remoteControlService.getInformationMessage, and GetInformationMessage.swift:22 builds the path employeeApiV1/remoteControl/employee/{odpUserId}/message. It becomes an InformationCardViewM…
- (platform parity) The iOS twin does implement the survey card: GetSurvey.swift:16 calls employeeApiV1/surveys, and SurveyCardViewModel.swift renders it. Android sets 'dismissed' only when the user taps dismiss (HomeViewModel.kt:508-514); opening the survey does not hide the card (HighlightCardActio…
- (platform parity) App update works differently on each platform. Android shows a dismissible 'suggested update' highlight card on Home (HomeViewModel.kt:700-715, UpdateHighlightHidingService). iOS AppUpdateCoordinator.swift:32-51 swaps the window's root view for a full-screen AppUpdateView at launc…
- The important-info dismissal is not saved on Android. removeHighlightViewModel (HomeViewModel.kt:501-526) has no hiding service for ImportantInfoHighlightViewModel (the else branch does nothing), so the card is removed only from the in-memory list and comes back on the next load. The claim's 'stays…
- The claim leaves out an endpoint: the Android update card is driven by GET api/v1/RemoteControl/Config (ImportantInfoServiceImpl.kt:77). Only SuggestedUpdate produces a Home card. SuggestedOsUpdate and MandatoryUpdate are handled elsewhere.

_Note: Important info rendered as HTML when messageType=Html; only the first survey is used. referee could not confirm: The claim cites me-ios Employee/StartPage/StartPageViewModel.swift:111-141 as 'mentions surveys and messages among highlight cards'. Those lines are loadData/reloadData and mention neither.; The claim's divergence line says no iOS fragment reports the endpoints or dismissal. The iOS co…_

### CAP-084: Start a common task from Home quick selections

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee taps a Home quick-selection button to register absence or time, add a receipt or mileage, or view the latest payslip.

- **me-android** (Employee): screens: `HomeButtonsList`, `HomeScreen`; events: `StartPage - Quick selection: register time or absence`, `StartPage - Quick selection: register absence`, `StartPage - Quick selection: report time`, `StartPage - Quick selection: view latest payslip`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/home/HomeButtonsProvider.kt:112-158; app/src/main/java/com/visma/employee/navigati…`

**How they differ:**
- (platform parity) iOS has a quick-selections section (S.StartPage.quickSelections) and a latest-payslip quick action, but no iOS fragment reports register absence/time, receipt or mileage quick actions.
- (platform parity) Correction: iOS does have register-time-or-absence, register absence, report time, add receipt and add mileage quick actions (me-ios/Employee/StartPage/StartPageService.swift:91-173), grouped by the same permissions as Android. The claimed iOS gap does not exist.
- (platform parity) The claim leaves out the allowance quick action. Android shows it only with allowance-creation permission and enables it only online (HomeButtonsProvider.kt:191-206). iOS requires the expenseClaims, expenseApiWrite and createAllowances permissions and enables it only online (Start…
- (platform parity) Mileage and receipt are enabled by expense-write permission, not by connectivity, on both platforms: Android hasExpenseWritePermissionInCurrentContext (HomeButtonsProvider.kt:174-176,186-188) and iOS hasAccessForCompany(.expenseApiWrite) (StartPageService.swift:95,121). The note '…
- (platform parity) On iOS, all three time and absence buttons open the same AddAbsenceCoordinator with source startPage (StartPageService.swift:133-159). On Android they go through the generic callbacks.onButtonClick (HomeEntries.kt:208).

_Note: One combined button when both Absence and Time; enabled only online. referee could not confirm: The claim's divergence says 'no iOS fragment reports register absence/time, receipt or mileage quick actions'. That is wrong: me-ios/Employee/StartPage/StartPageService.swift:91-173 implements them._

### CAP-085: Reach HR profile, documents and benefits or the employee list from Home shortcuts

**Fusion:** unique · **Personas:** HR-only (Dottie) employee · **Confidence:** High

An employee who only has the Dottie HR permission gets start-page shortcuts to My profile, Documents and benefits and the Employee list instead of the standard quick actions.

- **me-ios** (Employee): screens: `DottieEmployeeInfoCoordinator`, `DocumentsAndBenefitsCoordinator`, `EmployeeListCoordinator`; events: `quickSelection(myProfile)`, `quickSelection(documentsAndBenefits)`, `quickSelection(employeeList)`; platform: `ios-native` · evidence `Employee/StartPage/StartPageService.swift:183-191; Employee/StartPage/StartPageViewController.swift:1107-1126`
- **me-android** (Employee): screens: `HomeButtonsList`; events: `StartPage - Quick selection: my profile`, `StartPage - Quick selection: documents and benefits`, `StartPage - Quick selection: employee list`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/home/HomeButtonsProvider.kt:47-110`

**How they differ:**
- (platform parity) Android enables these buttons only online (HomeButtonsProvider.kt:47-110); iOS offline behaviour for them not reported.
- (platform parity) iOS excludes users with expenseClaims, addTime, addAbsence, payslips, absenceWrite or timeWrite (StartPageService.swift:263-267); Android excludes Absence/Time/Payslips/Expense/absence-write/time-write. Same rule except iOS names addTime/addAbsence explicitly.
- (platform parity) Android disables all three Dottie buttons when offline (EnabledStateCondition { mConnectionManager.isNetworkAvailable() }, HomeButtonsProvider.kt:71-104). The iOS Dottie ButtonConfigurations (StartPageService.swift:182-211) set no enabled flag, while the other iOS quick actions us…
- (platform parity) Different eligibility checks. iOS checks userFeatures contains .dottie and has none of [expenseClaims, addTime, addAbsence, payslips, absenceWrite, timeWrite] (StartPageService.swift:263-264). Android checks mContextService.hasDottieHrPermission() and has none of [Features.Absence…
- (platform parity) Android returns only the Dottie buttons, early (HomeButtonsProvider.kt:26-28). iOS appends them after the expense, time/absence and payslip buttons (StartPageService.swift:269). The result is the same only because the eligibility check makes the other lists empty.
- (platform parity) The My profile destination differs: iOS opens the modal DottieEmployeeInfoCoordinator (StartPageViewController.swift:842-852), Android pushes EmployeeInfoKey (RootNavDisplay.kt:540).

_Note: referee could not confirm: me-ios Employee/StartPage/StartPageService.swift:183-191 covers only the My profile button. The three-button definition spans lines 182-215, and the eligibility rule is at 263-267.; The me-android screen 'HomeButtonsList' is a Compose component (home/presentation/components/HomeButtonsList.kt), not a screen. The real destinations are DocumentsAndBenefitsKey, EmployeesKe…_

### CAP-086: Open my user menu to reach profile, account and HR pages

**Fusion:** unique · **Personas:** employee · **Confidence:** High

The employee taps their avatar (Dottie photo or initials) to open a user menu with name and email, then switches account or opens My profile, Documents and benefits, Employee list or Emissions summary, depending on permissions.

- **me-ios** (Employee): screens: `UserProfileView`, `UserProfileFeature`, `UserProfileCoordinator`, `AccountManagerCoordinator`, `PersonalInformationCoordinator`, `DottieEmployeeInfoCoordinator`; storage: `@SharedReader dottieCurrentUserProfileImage`, `@Shared(.dottieCurrentUserProfileImage)`, `Dottie cached profile per tenant`; platform: `ios-native`, `sheet presentation (medium/large detents)` · evidence `Employee/Accounts/Feature/UserProfile/UserProfileFeature.swift:85-119; Employee/StartPage/StartPageViewController.swift…`
- **me-android** (Employee): screens: `UserMenuContent`, `UserMenuHeader`, `UserMenu`, `PersonalInformationKey`, `EmployeeInfoKey`, `DocumentsAndBenefitsKey`, `EmployeesKey`, `EmissionSummaryKey`; endpoints: `GET /api/v2/dottie/employee/me`, `GET /api/v2/dottie/employee/me/profile-image`; storage: `DottieProfileCacheStore (15-minute staleness)`; platform: `android-native` · evidence `dottie/src/main/java/com/visma/employee/dottie/presentation/user_menu/components/UserMenuContent.kt:40-198; dottie/src/…`

**How they differ:**
- (platform parity) Profile refresh: Android refetches from Dottie when the 15-minute cache is stale (DottieProfileCacheStore); iOS refreshes 'if stale' and resets on company change (StartPageViewModel.swift:91-110) with no interval reported.
- (platform parity) Initials: Android derives initials from email on the avatar (HomeViewModel.kt:314-351) and from first/last name in the menu (UserMenuViewModel.kt); iOS shows initials with no rule reported.
- (platform parity) Sheet: iOS gives Dottie users a large-only sheet (medium/large detents otherwise); Android uses a bottom modal sheet with no detent rule reported.
- (platform parity) Sheet: iOS shows a large-only sheet to Dottie users and medium/large detents to everyone else (StartPageViewController.swift:814-815). Android uses a Compose bottom modal sheet (ComposeBottomModalSheetDelegate.kt:81-109).
- (platform parity) Profile refresh: Android's refreshProfileIfStale uses a 15-minute threshold (DottieProfileCacheStore.kt:43) and runs only for Dottie HR users (UserMenuViewModel.kt resolveProfile). iOS calls refreshProfileIfStale from StartPageViewModel.swift:91-99, resets the image on context cha…
- (platform parity) Initials: iOS splits the Dottie full name into initials inside UserProfileFeature.State (UserProfileFeature.swift:20-21); if there is no full name, the user name is nil and the initials are empty. Android falls back to the last login name for both name and initials (UserMenuViewMo…
- (platform parity) Menu name before load: Android shows the login name as userName and userEmail at first (UserMenuViewModel.kt:74-77). iOS starts with userName nil and shows only the email (UserProfileFeature.swift:115).

_Note: Menu gating is the same on both: My profile with Dottie HR or EmpMan; Documents and Employee list only with Dottie; Emissions with the expense sustainability/emission permission._

### CAP-087: Sign out from the user menu

**Fusion:** shared-diverged · **Personas:** employee · **Confidence:** Medium

The employee signs out from the user menu; the app revokes tokens, clears stored auth data and unregisters the device from push.

- **me-ios** (Employee): screens: `UserProfileView`; platform: `ios-native` · evidence `Employee/Accounts/Feature/UserProfile/UserProfileFeature.swift:85-119`
- **me-android** (Employee): screens: `UserMenuContent`, `UserMenu`; storage: `AuthDataStorage (lastLoggedInUserName, connectAuthData tokens; cleared on sign-…`, `AnalyticsLogger cleared`; platform: `android-native`, `FCM device unregistration on sign-out`, `push token unregister (FirebaseMessaging token)` · evidence `dottie/src/main/java/com/visma/employee/dottie/presentation/user_menu/UserMenuViewModel.kt:72-140`

**How they differ:**
- (platform parity) Android asks for confirmation (logout_confirmation_dialog_description) and revokes access and refresh tokens plus unregisters FCM; iOS only reports the sign-out menu entry, confirmation and token handling not reported.
- Entry point: in Employee (me-ios UserProfileView/UserProfileItem .signOut; me-android UserMenuContent.kt:185) sign-out is in the user menu. In Manager (vmm) it is on SettingsScreen.tsx:421-423 (testID SETTINGS.SCREEN.LOGOUT_BUTTON, t('logout')) and on NoRolesScreen.tsx:72-73.
- Token handling: me-android revokes the access and refresh tokens itself through RevokeTokenRequest (UserMenuViewModel.kt:110-135). me-ios calls oauthService.revokeTokens()/reset() (AppStateService.swift:88-89). vmm calls apiManagerConnect.logout() once (SettingsScreen.tsx:190), with a retry on NoRo…
- Push unregistration: vmm unregisters the approval-notification device token in logoutUnregisterApprovalNotificationsEpic and resets the badge count (setBadgeCount(0), SettingsScreen.tsx:194). me-ios calls pushNotificationService.unregisterFromPushNotifications (AppStateService.swift:77). me-android…
- Failure handling: vmm stays signed in and re-enables the button if logout fails, with a 12s safety timeout (SettingsScreen.tsx:186,198-202). Both Employee twins clear local auth data no matter whether revocation succeeds (me-android UserMenuViewModel.kt:135; me-ios AppStateService.swift:86-93).
- vmm only runs logout when isLoggedInManager is true (SettingsScreen.tsx:188). Otherwise it does nothing.
- (platform parity) me-android shows a confirmation dialog (ConfirmationDialog with user_menu_sign_out / logout_confirmation_dialog_description / cancel_button, UserMenuContent.kt:62-67). me-ios signs out right away on signOutTapped with no confirmation (UserProfileCoordinator.swift:57-60).
- (platform parity) me-ios also offers logout from SettingsTableViewController.swift:483-485,623 in addition to the user menu. That was not reported for me-android in this claim.

_Note: Probably belongs with an authentication domain; kept here because it is reached from the user menu. referee could not confirm: me-ios Employee/Accounts/Feature/UserProfile/UserProfileFeature.swift:85-119 is only State.build (menu section layout) and does not sign out. The real handler is UserProfileCoordinator.swift:57-60,162-164 plus Employee/Services/AppStateService.swift:69-100.; The divergenc…_

### CAP-088: Open a specific app section from a link

**Fusion:** unique · **Personas:** employee · **Confidence:** High

A person taps a verified https app link and lands on the matching tab, payslip or year-end report, after unlocking and onboarding, falling back to Home when they lack the feature.

- **me-android** (Employee): screens: `MainActivity`, `AuthenticatedRootHost`, `HomeKey`, `SalaryFeedKey`, `PayslipDetailsKey`, `ReportDetailsKey`, `AbsenceFeedKey`, `ExpenseInboxKey` …; platform: `android-native`, `deep link https://static.mobileemployee.visma.net/app/* (autoVerify)`, `intent extras INITIAL_TAB/payslipId/companyId/reportId`, `app lock gate` · evidence `app/src/main/java/com/visma/employee/navigation/RootDeepLinks.kt:96-157; app/src/main/java/com/visma/employee/home/Main…`

**How they differ:**
- (platform parity) No iOS fragment reports universal-link handling for /app/* paths; iOS coordinator actions route to calendar, receipts, claims, payslips, payslips bot, FAQ and settings (TabbarCoordinator.swift:52-202) but the link entry point is not evidenced.
- (platform parity) me-ios claims the domain (Employee.entitlements:11-13 applinks:static.mobileemployee.visma.net) but does not route links. SceneDelegate.swift:98 scene(_:openURLContexts:) is empty. URLRouterCoordinator.swift registers only a .close route, whose handler returns false ('Not implemen…
- (platform parity) The claim's reference to TabbarCoordinator.swift:52-202 shows in-app coordinator actions, not a link entry point, so on iOS no link reaches those tabs.

### CAP-089: Acknowledge a blocking startup notice

**Fusion:** unique · **Personas:** employee · **Confidence:** Medium

At launch the employee may be shown a non-dismissable notice that must be confirmed before the app continues.

- **me-android** (Employee): screens: `StartupGateContent`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/home/dialogs/StartupGateContent.kt:13-33`

**How they differ:**
- (platform parity) No iOS equivalent reported.
- Capability misdescribed: it is a remote-config forced app update / unsupported OS gate, and confirming does not let the app continue. Android either opens the Play Store (MandatoryUpdate) or calls finish() (SuggestedOsUpdate), MainActivity.kt:354-363.
- (platform parity) iOS does have an equivalent, contrary to the claim: AppUpdateCoordinator.swift:33-53 replaces window.rootViewController with AppUpdateView at startup, and AppUpdateView.swift:55-59 hides Cancel when config.isUpdateRequired (forceUpdate).
- (platform parity) Unsupported OS: Android blocks with a non-cancelable dialog whose Close button exits the app (MainActivity.kt:359-363). iOS shows an 'open settings' text and a Cancel button (unless the update is also forced) and no App Store button, so the user can continue (AppUpdateView.swift:4…
- (platform parity) Fetch policy: Android calls RemoteControl/Config on every splash with a 5s timeout and continues normally on error or timeout (MainActivity.kt:347-351). iOS caches the config in Preferences and only refetches after 24h or an app version change (EmployeeRemoteControlService.swift:3…
- (platform parity) Suggested (optional) update: iOS shows it on the same startup screen with Cancel and App Store buttons (AppUpdateView.swift:24-27, 55-65). Android does not gate on it here and only stores it in mUpdateInfoHolder.setSuggestedUpdate for later display (MainActivity.kt:351).
- (platform parity) Precedence: Android checks suggestOSUpdate before forceUpdate (ImportantInfoServiceImpl.kt:46-49), so if both are set it shows the closable OS notice. iOS sets isUpdateRequired independently, so if both are set it hides both Cancel and the App Store button (AppUpdateView.swift:55-…

_Note: Trigger conditions are outside the fragment (MainActivity.showStartupGate, MainActivity.kt:375-397). referee could not confirm: divergence '(platform parity) No iOS equivalent reported.' is wrong: me-ios/Modules/RemoteControl/Sources/RemoteControl/UI/AppUpdateCoordinator.swift:33-53 and UI/View/AppUpdateView.swift:37-68 implement it; Description 'must be confirmed before the app continues' does n…_

### CAP-090: Go through first-run onboarding

**Fusion:** unique · **Personas:** employee · **Confidence:** Medium

On first launch or after an app update a person sees the onboarding flow once, after unlocking if a lock is set.

- **me-android** (Employee): screens: `OnboardingKey`; storage: `AppPreferencesRepository firstRun`, `AppPreferencesRepository latestVersionWelcomeScreen`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/welcome/WelcomeStateProvider.kt:24-37`

**How they differ:**
- (platform parity) iOS has a WelcomeService (Employee/Welcome/WelcomeService.swift) but no fragment reports its onboarding flow.
- (platform parity) Trigger: Android shows OnboardingKey when firstRun is set or the saved latestVersionWelcomeScreen differs from the app version, so it shows again after every app update (WelcomeStateProvider.kt:24-29). iOS shows .biometricsSetup only when securityService.getCurrentLoginType() is n…
- (platform parity) Where it appears: Android puts the flow at the root and runs it after the lock screen is dismissed (AuthenticatedRootHost.kt:52-67). iOS presents it from the start page (StartPageViewController.swift:214-233) and does not wait on the lock screen.
- (platform parity) Content: Android runs SecuritySetupFlow with biometric and device-credential branches (SecuritySetupFlow.kt:76-96). iOS shows the BiometricsSetup screen with a 'later' button (S.WelcomePage.Button.later), which cannot be swiped away (StartPageViewController.swift:222-233).
- The claim's divergence line says no iOS onboarding flow exists. That is wrong: the iOS flow is implemented in StartPageViewController.swift:214-233 and WelcomeService.swift:107-114, so the me-ios implementation should be added to this capability.

_Note: referee could not confirm: Claim's divergence text 'iOS has a WelcomeService but no fragment reports its onboarding flow' implies no iOS implementation; iOS implements it at me-ios/Employee/StartPage/StartPageViewController.swift:214-233; Name 'Go through first-run onboarding' hides what OnboardingKey actually does: it resolves to SecuritySetupFlow (me-android/app/src/main/java/com/visma/employee…_

## Notifications and inbox

Push notifications, inbox messages, HR announcements and remotely published messages

### CAP-176: Receive push notifications on this device

**Fusion:** shared-diverged · **Personas:** Manager / approver, Employee · **Confidence:** Medium

The device registers its push token with the backend so the person is notified: managers about new approval tasks, employees about new payslips, year-end reports, time-confirmation reminders, calendar messages and receipt sync. The token is re-registered when it changes.

- **vmm** (Manager): screens: `(UI-less, mounted in ApprovalNavConfig)`; endpoints: `POST Devices`; events: `approval_notifications_reregister`, `approval_notifications_register_trigger`, `approval_notifications_register_complete`; storage: `features.approvalNotificationRegistered`, `features.approvalRegisteredDeviceToken`; platform: `push (APNs token on iOS, FCM token on Android)`, `AppState foreground listener` · evidence `src/components/approval/ApprovalNotificationsReregister/ApprovalNotificationsReregister.tsx:18-95`
- **me-ios** (Employee): endpoints: `POST /employee/api/v1/notification/RegisterDevice`; storage: `UserDefaults <bundleID>.deviceToken`; platform: `push (APNs)`, `UNUserNotificationCenter delegate` · evidence `Employee/PushNotifications/PushNotificationHandlingService.swift:45-72`
- **me-android** (Employee): endpoints: `POST /api/v1/notification/RegisterDevice`; platform: `push (FCM)`, `push (FirebaseMessagingService)`, `notification channels and channel group`, `notification channels by eventId`, `POST_NOTIFICATIONS permission` · evidence `core/src/main/java/com/visma/employee/core/notification/SubscriptionServiceImpl.kt:25-37; app/src/main/java/com/visma/e…`

**How they differ:**
- Endpoint: vmm registers with POST Devices (ApprovalNotificationsReregister.tsx:18-95); Employee registers with POST /employee/api/v1/notification/RegisterDevice (iOS PushNotificationHandlingService.swift:45-72, Android SubscriptionServiceImpl.kt:25-37).
- Body: vmm sends {deviceToken, deviceTokenName, family 0=iOS/1=Android}; Employee sends {deviceToken, family} with no deviceTokenName (family=0 on iOS, family=1 on Android).
- Content: vmm notifications are approval tasks only; Employee notifications are payslip, year-end, timesheet_confirm_reminder, generic calendar and (Android) receipt_sync eventIds.
- Accounts: Employee registers every signed-in account on the device (MultiAccountPushManager); vmm registers one device token, tracked in features.approvalRegisteredDeviceToken.
- Re-register trigger: vmm re-registers on AppState foreground when the token changed; Employee Android re-registers on a new FCM token only when logged in (DefaultFirebaseMessagingService.kt:73).
- Analytics: vmm emits approval_notifications_register_trigger/complete/reregister events; Employee reports no events.
- (platform parity) Retries: iOS registers with 2 retries; Android retries up to 3 times, 1 s apart, on RecoverableError (RetryingSubscriptionService.kt).
- (platform parity) Permission denied: iOS deregisters the old token; Android only shows notifications when enabled and asks for POST_NOTIFICATIONS.
- (platform parity) Android sorts notifications into a Salary channel group (payslip, year-end, receipt sync) and an Other channel (ChannelConfigurationsProvider.kt:79-108); iOS reports no equivalent grouping.
- Endpoint: vmm POST 'Devices' (queryEndpointsApproval.ts:701-703, apiApproval.ts:322); Employee POST notification/RegisterDevice (iOS RegisterDevice.swift:30,42; Android SubscriptionServiceImpl.kt:59).
- Body: vmm sends deviceToken + deviceTokenName ('APN device token: ' / 'GCM registration ID: ') + family 0/1 (queryEndpointsApproval.ts:695-699); Employee sends deviceToken + family only (iOS family 0 at PushNotificationService.swift:49; Android default family=1 at SubscriptionServiceImpl.kt:69-74).
- Content: vmm registration serves approval notifications only (INTEGRATION_APPROVAL); Employee handles the eventIds new_payslip, new_yearend, timesheet_confirm_reminder and generic_notification (PushNotificationHandlingService.swift:19-33), plus receipt_sync on Android (ChannelConfigurationsProvider…
- Accounts: Employee iOS registers the token for each authenticated account (MultiAccountPushManager.live.swift:37-54). Because the guard uses 'return', the loop stops at the first unauthenticated user, which is a latent bug. vmm registers one token and stores it in features.approvalRegisteredDeviceT…
- Re-register trigger: vmm fetches the token on AppState 'active' and re-sends it when it changed (ApprovalNotificationsReregister.tsx:24-95); Employee Android re-registers from FCM onNewToken only when connectAuthData != null (DefaultFirebaseMessagingService.kt:67-75).
- Analytics: vmm emits approval_notifications_register_trigger/complete/reregister (ApprovalNotificationsReregister.tsx:36-92); no analytics events found in the Employee registration paths.
- Unregister: vmm deletes with DELETE Devices/{token} only on explicit logout (comment at ApprovalNotificationsReregister.tsx:14-17; apiApproval.ts:350-366); Employee uses UnregisterDevice (iOS PushNotificationService.swift:59-65, Android DELETE api/v1/notification/UnregisterDevice at SubscriptionSer…
- (platform parity) Retries: iOS uses Task.retrying(maxRetryCount: 2) (PushNotificationService.swift:51); Android retries up to 3 times, 1000 ms apart, only on RecoverableError (RetryingSubscriptionService.kt:17-18, 42-48).
- (platform parity) Multi-account: iOS loops over all users (MultiAccountPushManager.live.swift:41-53); in the code I read, Android's SubscriptionServiceImpl registers once through the single ApiFactory session, and I found no loop over accounts.
- (platform parity) Android shows a notification only if areNotificationsEnabled() (DefaultFirebaseMessagingService.kt:55) and assigns channels by eventId (ChannelConfigurationsProvider); I found no channel grouping on iOS. I could not confirm the claim that iOS deregisters the token when permission…

_Note: Merged because the user outcome (be notified on this phone) is the same and the new app will have one registration. Unsure whether approval-task push and payslip push should stay one capability; marked diverged so a person decides. referee could not confirm: me-ios Employee/PushNotifications/PushNotificationHandlingService.swift:45-72 is openNotification (routing a tapped notification by eventId)…_

### CAP-177: Stop push notifications to this device when signing out

**Fusion:** shared-diverged · **Personas:** Manager / approver, Employee · **Confidence:** Medium

When the person signs out, the device token is unregistered from the backend so notifications stop arriving on this phone.

- **vmm** (Manager): endpoints: `DELETE Devices/{token}`; storage: `features.approvalRegisteredDeviceToken` · evidence `src/components/approval/ApprovalNotificationsReregister/ApprovalNotificationsReregister.tsx:18-95 (rulesHint: unregiste…`
- **me-ios** (Employee): endpoints: `DELETE /employee/api/v1/notification/UnregisterDevice`; platform: `push (APNs)` · evidence `Employee/PushNotifications/PushNotificationHandlingService.swift:45-72`
- **me-android** (Employee): endpoints: `DELETE /api/v1/notification/UnregisterDevice?deviceToken={token}`; platform: `push (FCM)` · evidence `core/src/main/java/com/visma/employee/core/notification/SubscriptionServiceImpl.kt:40-55`

**How they differ:**
- Endpoint: vmm calls DELETE Devices/{token} from a logout epic (fragment 35 rulesHint); Employee calls DELETE /employee/api/v1/notification/UnregisterDevice?deviceToken={token} (SubscriptionServiceImpl.kt:40-55, iOS UnregisterDevice.swift).
- Auth and retries: Employee Android sends an explicit 'Authorization: Bearer <authToken>' header, skips the call unless both tokens exist and retries 3 times; vmm reports no retry.
- (platform parity) iOS also deregisters the old token when notification permission is denied (fragment 294); Android reports unregistering only on sign-out (RootHostViewModel.kt:112).
- Endpoint: vmm sends DELETE {base}Devices/{token} with the token in the path (apiApproval.ts:366, queryEndpointsApproval.ts:727). Employee sends DELETE .../notification/UnregisterDevice with deviceToken as a query parameter (iOS UnregisterDevice.swift:26-36, Android SubscriptionServiceImpl.kt:62-66).
- Which token is removed: vmm deletes the last token it successfully registered, kept in redux at features.approvalRegisteredDeviceToken (epic line 26). It does not fetch the token again, so a rotated token cannot make it delete the wrong record (apiApproval.ts:358-362). Employee iOS uses the stored…
- Logout blocking: vmm waits for the DELETE before it lets loginManagerLogout through, with an 8s timeout, and always completes the logout even on failure (epic lines 11, 30-35). Employee on both platforms runs the unregister alongside token revocation and does not block local logout (iOS AppStateSer…
- Retries: vmm has no retry. Employee iOS has no retry on unregister either (PushNotificationService.swift:59-65; only register retries, maxRetryCount 2). Employee Android retries up to 3 times, 1s apart, on RecoverableError (RetryingSubscriptionService.kt:17-18, 53-63).
- Local cleanup: after a successful call vmm clears approvalNotificationRegistered and approvalRegisteredDeviceToken (epic line 33).
- (platform parity) Android sends an explicit 'Authorization: Bearer <accessToken>' header and skips the call unless both deviceToken and authToken are non-null (SubscriptionServiceImpl.kt:44-46). iOS goes through the shared APIClient and only checks that an access token and a stored device token exi…
- (platform parity) iOS also deregisters and removes the stored token when the user denies notification permission (MainCoordinator.swift:416-420). Android unregisters on logout (RootHostViewModel.kt:112), on relog-wipe of all accounts in the Dottie user menu (UserMenuViewModel.kt:128) and on account…
- (platform parity) iOS has a second unregister path for logging out a specific account in multi-account use (AppStateManager.live.swift:19-26).

_Note: referee could not confirm: me-ios Employee/PushNotifications/PushNotificationHandlingService.swift:45-72 handles opening a tapped notification (openNotification routing by eventId), not unregistering. The real code is AppStateService.swift:70-80 and PushNotificationService.swift:59-65.; vmm src/components/approval/ApprovalNotificationsReregister/ApprovalNotificationsReregister.tsx:18-95 only regi…_

### CAP-178: Open a push notification in the right place

**Fusion:** shared-diverged · **Personas:** Employee · **Confidence:** High

Tapping a push notification switches to the right account and company and opens the matching payslip, year-end report, time-confirmation/calendar view, message inbox or home.

- **me-ios** (Employee): screens: `ShowPayslipCoordinator`, `ShowEndYearCoordinator`, `PresentInboxMessagesCoordinator`, `SendActionCoordinator(showCalendar)`; platform: `push (APNs)`, `UNUserNotificationCenter delegate` · evidence `Employee/PushNotifications/PushNotificationHandlingService.swift:45-72; Employee/MainCoordinator/MainCoordinator.swift:…`
- **me-android** (Employee): screens: `MainActivity`; platform: `push (FCM)`, `notification channels`, `deep link https://static.mobileemployee.visma.net/app?redirectTo=home/salary/ab…`, `PendingIntent to MainActivity with payslipId/odpCompanyId/odpUserId/reportId ex…` · evidence `app/src/main/java/com/visma/employee/home/NotificationHandler.kt:37-90; app/src/main/java/com/visma/employee/core/notif…`

**How they differ:**
- (platform parity) Timesheet confirm reminder: iOS opens the calendar via SendActionCoordinator(showCalendar); Android routes CALENDAR_CONFIRM_TIME to absence (NotificationHandler.kt:37-90).
- (platform parity) iOS keeps the pending payload until the start page is ready and switches user only if that user is logged in (MainCoordinator.swift:201-243); Android passes payslipId/odpCompanyId/odpUserId/reportId extras in a PendingIntent to MainActivity and falls back to home for unknown types.
- (platform parity) Android also supports deep links https://static.mobileemployee.visma.net/app?redirectTo=home/salary/absence/messageinbox; iOS reports none.
- Destinations differ. Employee (me-ios, me-android) opens a payslip, a year-end report, the time-confirmation calendar or absence view, the message inbox, or home. Manager (vmm useNotificationConsumer.ts:89-213) opens an approval task (TAB_ROUTE_NAME_APPROVAL), the dialogue chat, the HRM employee de…
- Company context differs. Employee switches both the ODP user and the company from odpUserId/odpCompanyId (MainCoordinator.swift:201-243; NotificationHandler.kt:55-64). vmm only passes attributes.companyId as a parameter to the dialogue route (useNotificationConsumer.ts:101-135), and I found no acco…
- vmm treats approve/reject action-button presses separately. They are dispatched headlessly (dispatchNotificationAction) and discarded as taps (HEADLESS_NOTIFICATION_ACTIONS). It also has iOS foreground re-display and a bridge for APNs taps (consumePendingApnsTap). Employee has no action buttons in…
- (platform parity) The timesheet confirm reminder opens the calendar on iOS (ConfirmTimeReminderNotificationPayload.swift:28, SendActionCoordinator(.showCalendar)). Android sends CALENDAR_CONFIRM_TIME_TYPE to the absence tab instead (NotificationHandler.kt:66-71).
- (platform parity) iOS keeps the payload pending until state == .startPage and accounts are not refreshing. It switches user only if that user is logged in, and it drops the navigation if the user or company still does not match (MainCoordinator.swift:201-262). Android calls accountManagerService.sw…
- (platform parity) Unknown event types fall back to the home tab on Android (NotificationHandler.kt:70). iOS ignores them (PushNotificationHandlingService.swift:69, default returns nil).
- (platform parity) Android shows the notification itself on per-event notification channels (DefaultFirebaseMessagingService.kt showNotification/getChannelByEventId) and exposes app links https://static.mobileemployee.visma.net/app?redirectTo=..., including extra segments expense and settings (RootD…

_Note: referee could not confirm: The claim leaves out vmm, which also implements opening a push into the right place: vmm/src/hooks/useNotificationEventHandlers.ts:50-120,260-330 and vmm/src/hooks/useNotificationConsumer.ts:80-215. Because of this, 'unique' is wrong.; The deep-link segment list 'home/salary/absence/messageinbox' is incomplete. RootDeepLinks.kt:30-35 also defines expense and settings._

### CAP-179: See that new HR notifications are waiting

**Fusion:** unique · **Personas:** Employee with Dottie HR permission · **Confidence:** High

The start/home page shows an inbox button with a badge dot when the server reports new Dottie HR notifications; opening the inbox clears the badge.

- **me-ios** (Employee): screens: `StartPageViewController (inbox badge)`, `PresentInboxMessagesCoordinator`; endpoints: `GET /employee/api/v2/dottie/notifications/new-count` · evidence `Modules/DottieFeature/Sources/DottieFeature/Service/DottieNotificationsService.Live.swift:30-33; Employee/StartPage/Sta…`
- **me-android** (Employee): screens: `HomeTopBar`; endpoints: `GET api/v2/dottie/notifications/new-count` · evidence `app/src/main/java/com/visma/employee/home/HomeViewModel.kt:529-541`

**How they differ:**
- (platform parity) Button visibility: iOS shows the inbox button only with addTime, addAbsence, confirmTime or dottie (StartPageViewController.swift:673-806); Android shows it when any InboxContentProvider is active (HomeViewModel.kt:529-541).
- (platform parity) iOS clamps the count to at least 0 and hides the dot when the call fails; Android reports only count>0 with Dottie HR permission.
- (platform parity) Inbox button visibility: iOS shows it only when the company has addTime, addAbsence, confirmTime or dottie (StartPageViewController.swift updateAnnouncementsNavBarButton); Android shows it when any InboxContentProvider (Native or Dottie) is active (HomeViewModel.kt:191).
- (platform parity) Clearing the badge: iOS hides the dot on tap in showInboxView; Android also cancels any badge fetch still running (HomeViewModel.kt:529-532, HomeEntries.kt:339). Both clear the badge when the inbox is opened.
- Refuted parity line: both platforms clamp the count to at least 0 and treat a failed call as 0, so the badge stays hidden (iOS DottieNotificationsService.Live.swift:30-33 with try? ?? 0; Android DottieServiceImpl.kt:173-181). This is not a real difference.

_Note: referee could not confirm: me-android HomeViewModel.kt:529-541 does not decide inbox button visibility. That is HomeViewModel.kt:191 (inboxProviders.any { it.isActive }).; The me-android endpoint citation is missing its implementing file: dottie/src/main/java/com/visma/employee/dottie/data/DottieServiceImpl.kt:173-181,503.; The second divergence line says Android does not clamp or handle failure.…_

### CAP-180: Read the combined message inbox

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

An employee opens the inbox and sees one date-sorted list, newest first, of native calendar/expense messages and Dottie HR notifications with colleague avatars; it reloads when the device comes back online.

- **me-ios** (Employee): screens: `InboxMessagesView`, `InboxMessagesFeature`, `PresentInboxMessagesCoordinator`, `InboxMessageCellView`, `DottieNotificationsInboxProvider (InboxContentProvider id dottie-notifications)`, `DottieNotificationCellView`; endpoints: `GET /employee/api/v1/notification/inbox/items`, `GET /employee/api/v2/dottie/notifications`, `GET /employee/api/v2/dottie/employee/{id}/profile-image`; platform: `push notification opens inbox (NewInboxMessageNotificationPayload)`, `network reachability monitor reloads when back online` · evidence `Modules/InboxMessages/Sources/InboxMessages/InboxMessagesFeature.swift:93-133; Modules/DottieFeature/Sources/DottieFeat…`
- **me-android** (Employee): screens: `MessageInboxScreen`, `MessageInboxKey`, `HomeTopBar`; endpoints: `GET /api/v1/notification/inbox/items`, `GET /api/v2/dottie/notifications`, `GET /api/v2/dottie/employee/{id}/profile-image`; platform: `connectivity observer` · evidence `app/src/main/java/com/visma/employee/message_inbox/presentation/message_inbox/MessageInboxScreenViewModel.kt:56-90`

**How they differ:**
- (platform parity) Native provider: iOS always includes it (InboxMessagesFeature.swift:93-133); Android activates it only if the user has a CalendarPermissions.tab feature.
- (platform parity) iOS treats 404 as an empty inbox, shows an offline overlay and a toast naming a failed provider; Android drops items without id/date, parses dates as UTC and fetches avatars max 8 concurrent at 256px.
- (platform parity) iOS opens a detail sheet when an item has a detail; Android reports no detail sheet (document opening is in a separate capability).
- (platform parity) Both twins gate the native provider by permission. iOS adds .native() only if the user has one of the time/absence permissions (me-ios/Employee/AppDependencies.swift:1474-1486). Android activates it only if the user has a CalendarPermissions.tab feature (NativeInboxContentProvider…
- (platform parity) The Dottie provider is gated on iOS by permissions.contains(.dottie) (AppDependencies.swift:1490) and on Android by contextService.hasDottieHrPermission() (DottieInboxContentProvider.kt isActive).
- (platform parity) iOS treats a 404 from the native inbox as empty (InboxMessagesService.employee.swift:27) and keeps the last items while reloading. Android drops native items that have no id or no parseable date, and parses timeUTC as UTC with the pattern yyyy-MM-dd'T'HH:mm (NativeInboxContentProv…
- (platform parity) Android fetches avatars at most 8 at a time and decodes them to 256px (DottieInboxContentProvider.kt MAX_PROFILE_IMAGE_CONCURRENCY and AVATAR_DECODE_MAX_PX). iOS fetches all avatars in an unbounded task group (DottieNotificationsInboxProvider.swift:37-48).
- (platform parity) iOS has a detail-sheet branch (InboxMessagesFeature.swift itemTapped), but both iOS providers set detail: nil, so no item opens a sheet. On Android, tapping a Dottie item opens an external link or downloads the document (MessageInboxScreenViewModel.kt onDottieCellTapped); that beh…

_Note: referee could not confirm: The claim says the native provider is always included on iOS (InboxMessagesFeature.swift:93-133). In fact AppDependencies.swift:1474-1486 gates it on time/absence permissions.; The iOS detail sheet 'when an item has a detail' never opens in practice: InboxContentProvider+Native.swift and DottieNotificationsInboxProvider.swift (makeItem) both set detail: nil._

### CAP-181: Dismiss a message from the inbox

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

The employee removes a native inbox message (deleted on the server) or hides a Dottie HR notification from the list with the close button.

- **me-ios** (Employee): screens: `InboxMessagesView`, `InboxMessageCellView`, `DottieNotificationCellView`; endpoints: `DELETE {deleteLink from inbox item response}`, `POST {href of link rel mark-as-hidden}` · evidence `Modules/InboxMessages/Sources/InboxMessages/Provider/InboxContentProvider+Native.swift:23-29; Modules/DottieFeature/Sou…`
- **me-android** (Employee): screens: `MessageInboxScreen`; endpoints: `DELETE {message.deleteLink.href}`, `POST {notification.markAsHiddenHref}` · evidence `app/src/main/java/com/visma/employee/message_inbox/presentation/message_inbox/MessageInboxScreenViewModel.kt:92-108`

**How they differ:**
- (platform parity) iOS offers hide for Dottie items only when the server supplies the mark-as-hidden link, ignores POST errors and treats 'cannot find resource' on delete as success; a missing deleteLink raises missingDeleteLink (InboxContentProvider+Native.swift:23-29). Android reports only optimis…
- (platform parity) Missing native delete link: iOS InboxMessagesRepository.employee.swift:39-40 throws missingDeleteLink, and InboxContentProvider+Native.swift:27 swallows it with try?. Android MessageInboxScreenViewModel.kt:95 skips the call with deleteLink?.let. The user sees the same result on bo…
- (platform parity) The Dottie close button needs the server's hide link on both platforms: iOS DottieNotificationsInboxProvider.swift:132 and DottieNotificationCellView.swift:91; Android DottieDefaultCell.kt:42 and DottieDocumentPreviewCell.kt:67. The claim wrongly describes this as iOS-only.
- (platform parity) Both twins remove the item before the server call and ignore any error: iOS uses try? (Native.swift:27, DottieNotificationsInboxProvider.swift:135); Android ignores the result of firstOrNull() and postHateoas (ViewModel.kt:96, 105).
- (platform parity) The native message close button always shows on both: Android MessageInboxItem.kt:146 and iOS InboxMessageCellView.swift:56.

_Note: referee could not confirm: The claim says iOS 'treats cannot find resource on delete as success'. The code does not do this: cannotFindResource is only the error text for missingDeleteLink (InboxMessagesRepository.swift:33-34).; The claim cites InboxContentProvider+Native.swift:23-29 for the missingDeleteLink throw. That lines range has no such throw; it is in InboxMessagesRepository.employee.swi…_

### CAP-182: Mark an HR notification as read

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

From a Dottie notification's context/item menu, the employee marks it as read.

- **me-ios** (Employee): screens: `DottieNotificationCellView`; endpoints: `POST {href of link rel mark-as-read}` · evidence `Modules/DottieFeature/Sources/DottieFeature/Features/Notifications/DottieNotificationsInboxProvider.swift:24-144`
- **me-android** (Employee): screens: `MessageInboxScreen`; endpoints: `POST {notification.markAsReadHref}` · evidence `app/src/main/java/com/visma/employee/message_inbox/presentation/message_inbox/MessageInboxScreenViewModel.kt:110-207`

**How they differ:**
- (platform parity) iOS offers mark-as-read only when the server supplies the link and fires it without handling errors (DottieNotificationsInboxProvider.swift:24-144); Android posts to notification.markAsReadHref (MessageInboxScreenViewModel.kt:110-207) with no reported gating.
- (platform parity) The claim says Android has no gating, which is wrong. Both twins show mark-as-read only when the item is unread and the server supplied the link: iOS checks `if !isRead, let onMarkAsRead` (DottieNotificationCellView.swift:109) with onMarkAsRead built from markAsReadLink.map (Dotti…
- (platform parity) Where the read state lives differs. iOS changes only the cell's own isRead flag (DottieNotificationCellView.swift:111). Android changes the item in the view model's list through markItemAsRead(item.id) (MessageInboxScreenViewModel.kt:112).
- (platform parity) Both twins update the screen first and then drop any error. iOS uses `try?` on markAsRead (DottieNotificationsInboxProvider.swift:139). Android ignores the Resource that postHateoas returns (MessageInboxScreenViewModel.kt:113-115). So this is not a difference between them.

_Note: referee could not confirm: The Android evidence range MessageInboxScreenViewModel.kt:110-207 is too wide. Lines 110-117 are the menu mark-as-read. Lines 119-207 belong to a different flow: confirming that an org document has been read (markOrgDocumentAsReadHref).; The claim lists screen MessageInboxScreen but cites no line for the menu. The mark-as-read menu item is at MessageInboxScreen.kt:229-2…_

### CAP-183: Open a document notification and confirm it as read

**Fusion:** unique · **Personas:** Employee · **Confidence:** Medium

The employee taps a Dottie notification to open its external link or download and preview its document; for must-read documents they are asked to confirm reading after closing the preview.

- **me-android** (Employee): screens: `MessageInboxScreen`, `DottieDocumentPreviewCell`, `PdfPreviewKey`, `ImagePreviewKey`; endpoints: `GET {notification.downloadHref}`, `POST {notification.markOrgDocumentAsReadHref}`; platform: `open external URL`, `open downloaded file with mime type` · evidence `app/src/main/java/com/visma/employee/message_inbox/presentation/message_inbox/MessageInboxScreenViewModel.kt:110-207`

**How they differ:**
- (platform parity) Only Android reports opening/downloading documents and the must-read confirmation (MessageInboxScreenViewModel.kt:110-207); no iOS fragment reports it (iOS only mentions a detail sheet when an item has a detail, InboxMessagesFeature.swift:93-133).
- (platform parity) Wrong claim corrected: iOS does implement opening or downloading the document and the must-read confirmation. Evidence: me-ios Modules/DottieFeature/Sources/DottieFeature/Features/OrgDocumentPreview/OrgDocumentPreviewFeature.swift:73-166, wired into the inbox at Features/Notificat…
- (platform parity) When the must-read confirmation appears: iOS shows it after the preview is dismissed AND after an external URL is dismissed (OrgDocumentPreviewFeature.swift:102-113). Android arms it for external links, but onExternalLinkLaunchFailed clears it, and the sheet only appears from onPr…
- (platform parity) Which documents count as must-read: iOS passes markAsReadHref only when notification.isOrgDocumentReadRequest is true (DottieNotificationsInboxProvider.swift:161). Android requires messageType.isMustReadStyle plus a non-null markOrgDocumentAsReadHref (MessageInboxScreenViewModel.k…
- (platform parity) Result of confirming: Android marks the item read locally before the POST and ignores the POST's result (MessageInboxScreenViewModel.kt:184-193). iOS sets isRead only after the call succeeds and shows a markAsReadError toast if it fails (OrgDocumentPreviewFeature.swift:115-137).

_Note: referee could not confirm: Divergence claim 'no iOS fragment reports it (iOS only mentions a detail sheet ...)': the claim implies iOS lacks the feature, but OrgDocumentPreviewFeature.swift in me-ios implements it._

### CAP-184: Read an important message from the employer or Visma

**Fusion:** unique · **Personas:** Employee · **Confidence:** High

An information, warning or error message published remotely for the employee is shown as a card on the start/home page, with an action link opened outside the app and a close action.

- **me-ios** (Employee): screens: `NewFeatureCardView`, `StartPageCardBottomSheetView`, `OpenUrlExternallyCoordinator`, `StartPage InformationCard`; endpoints: `GET /employee/api/v1/remoteControl/employee/{odpUserId}/message`; events: `newFeatureBottomSheetConfirm`, `newFeatureBottomSheetDismiss`; platform: `open URL externally (MEURLHandler)` · evidence `Employee/StartPage/Tasks/GetInformationMessageTask.swift:18-33; Modules/RemoteControl/Sources/RemoteControl/Core/Employ…`
- **me-android** (Employee): screens: `HomeScreen (ImportantInfoHighlight card)`; endpoints: `GET api/v1/RemoteControl/employee/{odpUserId}/message` · evidence `app/src/main/java/com/visma/employee/home/HomeViewModel.kt:488-495`

**How they differ:**
- (platform parity) iOS takes button texts from the server, supports HTML content, never removes the card on confirm or cancel and swallows errors (GetInformationMessageTask.swift:18-33); Android uses fixed learn_more_button/close_button strings and an icon per informationType (HighlightResourcesProv…
- (platform parity) iOS emits newFeatureBottomSheetConfirm/newFeatureBottomSheetDismiss events; Android reports none.
- (platform parity) The card stays after it is closed on iOS but not on Android. iOS sets shouldRemoveCardOnCancel and shouldRemoveCardOnConfirm to false (InformationCardViewModel.swift:81-87). On Android, dismissing calls removeHighlightViewModel, which removes the card from the home state for the s…
- (platform parity) Android falls back to local texts when the server sends no button text; iOS has no fallback. Android uses actionButtonText ?: learn_more_button and closeButtonText ?: close_button (HighlightBottomSheetMapper.kt:88-93, HighlightResourcesProvider.kt:170-181). iOS uses the server's a…
- (platform parity) iOS logs newFeatureBottomSheetConfirm and newFeatureBottomSheetDismiss for any start-page bottom-sheet card, this one included (StartPageCardBottomSheetCoordinator.swift:28,35). Android logs those events only for NewFeatureHighlightViewModel, so it logs nothing for this card (Home…
- (platform parity) Both platforms hide the card silently when the call fails. iOS catches the error and returns success([]) (GetInformationMessageTask.swift:27-29). Android maps Resource.Error to null data with logToCrashlytics=false (HomeViewModel.kt:488-495, ImportantInfoServiceImpl.kt:20-33).

_Note: referee could not confirm: Claim that 'Android uses fixed learn_more_button/close_button strings' is wrong. Android uses the server's actionButtonText and closeButtonText and falls back to those strings (HighlightBottomSheetMapper.kt:88-93).; The claim implies only iOS supports HTML content, which is wrong. Android renders HTML through HtmlCompat.fromHtml when the message type is Html (HighlightB…_

### CAP-185: Open the app's notification settings

**Fusion:** unique · **Personas:** Employee · **Confidence:** Medium

A person opens the system notification settings for the app from Settings.

- **me-android** (Employee): screens: `SettingsScreen`; platform: `system notification settings intent`, `open notification settings (PermissionHelper.launchNotificationSettings)` · evidence `app/src/main/java/com/visma/employee/navigation/RootHostActionsFactory.kt:246-248`

**How they differ:**
- (platform parity) Only Android reports a Settings entry opening system notification settings (RootHostActionsFactory.kt:246-248, PermissionHelper.launchNotificationSettings); no iOS fragment reports it.
- (platform parity) me-android's Settings row (SettingsScreen.kt:128-129, settings_notification) opens the app's system notification settings through PermissionHelper.launchNotificationSettings (PermissionHelper.kt:40-45, ACTION_APP_NOTIFICATION_SETTINGS). me-ios SettingsTableViewController.swift has…

## Sign-in and accounts

Signing in, multiple accounts, app lock with PIN or biometrics, session expiry, sign out, environment switching and choosing the active company or employer

### CAP-197: Sign in with a Visma Connect account

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** High

A person signs in through the Visma Connect web login (OAuth in a browser session), the app stores their tokens, loads who they are and what they may use, and lands them in the app.

- **vmm** (Manager): screens: `LoginSelectScreen (SCREEN_NAME_LOGIN_SELECT = 'LoginSelectScreen')`; endpoints: `GET https://connect.visma.com/connect/authorize (react-native-app-auth authoriz…`, `POST https://connect.visma.com/connect/token`; events: `clicked_on_approval_hrm_button`, `login_cancelled`, `login_authorize_recovered`; platform: `OAuth browser session (ASWebAuthenticationSession / Custom Tabs via react-nativ…`, `Universal link redirect https://visma-manager.web.app/connect-login`, `Android hardware back blocked during login`, `AppState listener recovery valve` · evidence `src/screens/common/LoginSelectScreen/LoginSelectScreen.tsx:84-179`
- **me-ios** (Employee): screens: `SelectAccountView`, `SelectAccountFeature`, `SelectAccountCoordinator`, `Visma Connect web authentication session`; endpoints: `GET https://connect.visma.com/connect/authorize`, `POST https://connect.visma.com/connect/token`, `GET /employee/api/v1/authorization/currentSession`; events: `loginMethods`; storage: `UserService users (addUser by JWT subject)`, `OAuth tokens per connectUserId`, `secure storage access token / refresh token / expiration per connect user id (K…`, `SecureStorage currentUser`, `SecureStorage loggedInUsers`, `SecureStorage <connectUserId>-scoped currentContext`; platform: `ASWebAuthenticationSession (ephemeral) with app-link callback AllowedAppLinks.h…`, `universal link callback https://static.mobileemployee.visma.net/auth/callback`, `push registration after login` · evidence `Employee/Accounts/Feature/Login/SelectAccountFeature.swift:94-128; EmployeeServices/EmployeeAPI/Sources/EmployeeAPI/OAu…`
- **me-android** (Employee): screens: `LoginRootScreen`, `LoginScreen`, `LoginScreenNormalContent`, `LoginKey`; endpoints: `GET https://connect.visma.com/connect/authorize (browser)`, `POST https://connect.visma.com/connect/token`, `GET /api/v1/authorization/currentsession`; events: `Auth - Login methods used`; storage: `AuthDataStorage pending OAuth state (code verifier + state)`, `AuthDataStorage auth data`, `UserDatabaseDao user accounts (Room)`, `AppPreferencesRepository sessionData/connectAuthData/userName/userId/accountsCo…`, `room-entity:api_keys (encrypted keys per environment)`; platform: `Chrome Custom Tabs`, `deep link https://static.mobileemployee.visma.net/auth/callback (autoVerify)`, `custom scheme vismame://auth/callback`, `browser OAuth redirect callback (code/state)`, `connectivity monitoring` · evidence `login/src/main/java/com/visma/employee/login/LoginViewModel.kt:154-285; app/src/main/java/com/visma/employee/navigation…`

**How they differ:**
- Redirect target differs: vmm uses universal link https://visma-manager.web.app/connect-login (109); Employee uses https://static.mobileemployee.visma.net/auth/callback (me-ios 331, me-android 533), and me-android also accepts the custom scheme vismame://auth/callback (533).
- Session load after sign-in: Employee calls the current-session endpoint to load user, companies (contexts) and permissions and picks a default company (me-ios 450 GET /employee/api/v1/authorization/currentSession; me-android 533/675 GET /api/v1/authorization/currentsession). The vmm fragment report…
- Fresh-login rules: Employee always sends prompt=login and max_age (me-ios 331 max_age=0, me-android 675). vmm uses forceFreshLogin to ignore cached credentials, times out authorize() after 300s and finalizeLogin after 60s, and re-enables the button 7s after a sheet dismissal that leaves authorize p…
- Multi-account: Employee saves every signed-in account on the device and sends a prefilled email/login_hint when a saved account is picked (me-ios 267/268, me-android 675). vmm keeps a single signed-in manager (109).
- Analytics differ: vmm logs clicked_on_approval_hrm_button, login_cancelled and login_authorize_recovered (109). Employee logs loginMethods (me-ios 267/331) or 'Auth - Login methods used' (me-android 533/675).
- Push registration: Employee registers the device for push after login (me-ios 331, me-android 533). The vmm sign-in fragment does not report this.
- vmm lets the user choose environment, sandbox and app language on the login screen before signing in (109). Employee shows no language choice at login.
- (platform parity) me-android disables sign-in while offline (you_have_no_network_connection) and checks that the returned OAuth state matches the stored one (675). me-ios reports neither.
- (platform parity) The current-session path is /employee/api/v1/authorization/currentSession on me-ios (450) and /api/v1/authorization/currentsession on me-android (533). This may only be a difference in base URL; needs checking.
- (platform parity) If the session fetch fails, me-android restores the previous account's auth data (675). me-ios retries the session call up to 2 times and logs out with noPermissions/unauthorizedUser on 403 (450).
- Redirect target: vmm uses the universal link https://visma-manager.web.app/connect-login (apiManagerConnect.ts:55). Employee uses https://static.mobileemployee.visma.net/auth/callback (me-ios APIInterfaceConstants.swift:70-80; me-android ConnectAuthConstants.kt:41).
- (platform parity) me-android also accepts the custom scheme vismame://auth/callback (AndroidManifest.xml:127, RootDeepLinks.kt:159). me-ios uses only the universal link.
- Session load after sign-in, correcting the claim: vmm does load a session. finalizeLogin calls GET odp/session/id, then odp/user/info, then Roles on the Visma Manager API (useLogin.ts:56-79; apiManagerConnect.ts:278-316). Employee calls authorization/currentSession to load the user, companies and p…
- Fresh-login parameters, correcting the claim: both products send prompt=login. vmm sends it by default through forceFreshLogin and also sends ui_locales (apiManagerConnect.ts:118,141,255-266). Only Employee also sends max_age=0 and login_hint (me-ios OAuthService.OAuthSwift.swift:23-28; me-android…
- vmm-only timing rules: authorize() and finalizeLogin both run under timeouts, and an AppState listener re-enables the button after a grace period when the browser sheet was dismissed but authorize() never settled (LoginSelectScreen.tsx:93,124-155,176).
- Multi-account: Employee adds each new account (me-android addNewAccount in LoginViewModel.kt:190-196; me-ios loggedInUsers) and can prefill the email of a saved account. vmm has a single signed-in session.
- Analytics: vmm logs clicked_on_approval_hrm_button, login_cancelled and login_authorize_recovered (LoginSelectScreen.tsx:85,112,151). Employee logs the login methods taken from the id_token claim (me-android LoginViewModel.kt:198-200,241-245).
- Language: vmm passes the chosen app language to Connect as ui_locales (apiManagerConnect.ts:255-259). Employee does not.
- Offline: me-android shows you_have_no_network_connection on the login screen (LoginScreenBaseContent.kt:99). I found no equivalent on me-ios, so the claim's 'me-ios reports neither' holds (platform parity).
- (platform parity) The two currentSession paths are probably the same endpoint. me-ios builds it from a base that already contains /employee/api/v1 (AppConstants.swift:95, GetCurrentSession.swift:19). me-android uses the relative path api/v1/authorization/currentsession. The only real difference is…
- (platform parity) When the session load fails: me-android restores the previously selected account's auth data and shows login_failed_no_session (LoginViewModel.kt:206-220). me-ios retries twice and logs out with noPermissions on a 403 (UserService.swift:61-81,156-183).

_Note: referee could not confirm: Claim divergence line 2 says 'The vmm fragment reports no session call'. This is misleading: vmm useLogin.ts:56-79 calls odp/session/id, odp/user/info and Roles after authorize().; Claim divergence line 3 says 'Employee always sends prompt=login' as if vmm did not. vmm also sends prompt=login (apiManagerConnect.ts:118,141,265).; Claim divergence line 7 says vmm lets the…_

### CAP-198: Stay signed in without logging in again

**Fusion:** shared-diverged · **Personas:** employee · **Confidence:** High

The app silently renews access tokens with the refresh token, on launch, on return to the foreground and when a token is about to expire, for every account saved on the device.

- **me-ios** (Employee): no detail · evidence `Employee/MainCoordinator/MainCoordinator.swift:296-349`
- **me-android** (Employee): storage: `room-entity:app_preferences (connect auth data / access_token, session_data)`; platform: `OAuth PKCE with Visma Connect (client_id com.visma.employee)` · evidence `core/src/main/java/com/visma/employee/core/network/TokenManager.kt:30-76`

**How they differ:**
- (platform parity) me-ios refreshes all saved accounts on launch and on every return to the foreground, and debounces the start page reload by 0.5s (298). me-android refreshes when the token expires within 30s, runs only one refresh at a time and holds retries back for 5s after a failure (572, 533).…
- (platform parity) me-ios shortens token expiry by 30s and deletes tokens on a 4xx refresh (331). me-android publishes EventFailedToGetToken on AuthorizationError (572).
- vmm refreshes one signed-in account (the loginManager.refreshToken in the redux store, apiManagerConnect.ts:327), while Employee refreshes every saved account: me-ios UserSessionManager.live.swift:26-40 loops over allUsers().
- vmm refreshes ahead of time 5 minutes before expiry (apolloClient.ts:13, queryApi.ts:99, apiApprovalBase.ts:18). me-ios refreshes on launch and on return to the foreground when isTokenExpired (MainCoordinator.swift:71,367-369). me-android refreshes when the token is within 30s of expiry (TokenValid…
- vmm's refresh does more than Employee's: after the token call it also fetches the GsId session (reusing a cached GsId while it is still valid) and user info (apiManagerConnect.ts:363-400). It saves the rotated refresh token right away and has a timeout guard. Employee refreshes only the OAuth token.
- vmm retries the request once after a 401 and refreshes (apiApprovalBase.ts:109,155; notificationActionDispatcher.ts:205). me-android does the same on 401/406 (AuthorizationInterceptor.kt:33-55). me-ios has no such retry in the cited code; it refreshes through OAuthHandler.swift:67.
- When refresh fails: me-ios force-logs out the current user and signs out the other failed accounts (MainCoordinator.swift:321-338), and deletes tokens on a 4xx (EmployeeAPI/OAuth/OAuthService.swift:91-92). me-android publishes EventFailedToGetToken on AuthorizationError (TokenManager.kt:44-46). vmm…
- (platform parity) me-ios refreshes every saved account on launch and foreground and skips a refresh if one is already running (MainCoordinator.swift:297-301). me-android refreshes only the current account's token (mAuthDataStorage.connectAuthData), runs one refresh at a time, and holds retries back…
- (platform parity) me-ios deletes tokens on a 4xx refresh error (OAuthService.swift:91-92). me-android publishes EventFailedToGetToken instead (TokenManager.kt:44-46).

_Note: The vmm fragments report no silent-refresh logic. They only report the session-expired dialog (56). Whether the Manager app refreshes tokens silently is unknown. referee could not confirm: The claim's note says vmm has no silent-refresh logic. That is false: see vmm/src/services/apiManagerConnect/apiManagerConnect.ts:322-360, vmm/src/services/apolloClient.ts:13-49 and vmm/src/services/queryApi/qu…_

### CAP-199: Be signed out and told why when the session ends

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** Medium

When the session expires, is revoked or the token cannot be renewed, the person is signed out and shown a message explaining why.

- **vmm** (Manager): screens: `ModalDialog (global)`; events: `user_connect_token_expired`; storage: `redux modalDialog`; platform: `app icon badge (setBadgeCount)` · evidence `src/components/common/ModalDialog/ModalDialog.tsx:12-46`
- **me-ios** (Employee): screens: `SelectAccountView` · evidence `Employee/Accounts/Feature/Login/SelectAccountFeature.swift:94-128; Employee/MainCoordinator/MainCoordinator.swift:296-3…`
- **me-android** (Employee): screens: `LoginRootHost`, `MainActivityDialogs` · evidence `app/src/main/java/com/visma/employee/home/MainActivity.kt:285-308`

**How they differ:**
- Presentation: vmm shows a global ModalDialog (session_expired_title, OK), and only on OK logs out and clears the app badge (56). Employee returns to the login screen and shows the reason there: an alert on me-ios (logoutReasonTitle, 267), and a toast plus an optional information dialog on me-androi…
- Reasons: Employee tells apart noPermissions, unauthorizedUser, incorrectPasscode, failedToGetToken and noToken, and shows no message for a manual logout or relogin (me-ios 267). vmm has a single session-expired case, limited to modal type 'logout' (56).
- Scope: Employee checks every saved account and forces the login screen only when the current account fails (me-ios 298). vmm has one account.
- Analytics: vmm logs user_connect_token_expired only when the title is session_expired_title (56). No Employee event is reported.
- (platform parity) me-android refreshes user features on launch with a 5s timeout and clears auth on AuthorizationError (498). me-ios logs out with reason failedToGetToken, isForced: true (298).
- Presentation: vmm shows a global alert (session_expired_title / session_expired_message, OK button) and only logs out and sets the badge to 0 when OK is pressed (ModalDialog.tsx:28-40). Employee first goes to the login screen and then shows the reason there: an AlertState titled logoutReasonTitle o…
- Trigger: vmm fires only when the refresh-token request returns HTTP 400 while the user is logged in and has not started a logout (apiBase.ts:97-104, apiApprovalBase.ts:71-78). me-ios fires on RefreshTokensError.refreshTokenFailed for the current user (MainCoordinator.swift:321-331).
- Reasons: me-ios maps noPermissions/unauthorizedUser to noFeaturesText, incorrectPasscode to wrongPasscodeText, and failedToGetToken/noToken to sessionExpiredUserLoggedOut. It shows nothing for manual or reloginFromPinCodeScreen (SelectAccountFeature.swift:19-28). vmm has one hard-coded session-expi…
- Accounts: me-ios checks the tokens of every saved account and forces the login screen only for the current user. Other accounts are logged out quietly with appStateManager.logoutUser (MainCoordinator.swift:322-338). vmm has a single account.
- Analytics: vmm tracks APPROVAL_EVENTS.USER_CONNECT_TOKEN_EXPIRED with trackEvent and trackEventNew (ModalDialog.tsx:23-26). The Employee code checked has no matching event.
- (platform parity) Messages per reason differ between the twins: me-android shows error_user_unauthorized for both EventUnauthorizedUser and EventFailedToGetToken, login_no_features_error for EventNoFeaturesUser, and error_unexpected for any other tag (MainActivity.kt:290-306). me-ios uses sessionEx…
- (platform parity) me-android adds a second Information dialog (logout_information_login_dialog_title/description) only when FORCE_USER_LOGOUT_HAS_STORAGE is set (MainActivity.kt:291-299). me-ios has no equivalent.
- (platform parity) On launch, me-android refreshes user features with withTimeoutOrNull(5000). On AuthorizationError it clears the auth data without showing a message (MainActivity.kt:400-421). me-ios force-logs out with reason failedToGetToken, isForced: true (MainCoordinator.swift:331).

_Note: referee could not confirm: me-android parity claim (5s user-features timeout, AuthorizationError clears auth) is not in the cited range app/src/main/java/com/visma/employee/home/MainActivity.kt:285-308. It is at MainActivity.kt:400-436.; vmm evidence ModalDialog.tsx:12-46 shows only the display. The trigger that makes it a session-expiry flow is in src/reducers/modalDialogReducer.ts:18-22 and src…_

### CAP-200: Handle an account with no access

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** Medium

A person whose account has no usable roles or permissions is told so and cannot enter the app. They can only sign out.

- **vmm** (Manager): screens: `SCREEN_NAME_NO_ROLES (NoRolesScreen)`; endpoints: `POST https://connect.visma.com/connect/revocation`, `GET https://connect.visma.com/connect/endsession`; storage: `redux loginManager (persisted)` · evidence `src/configs/navConfig/noRoles/NoRolesNavConfig.tsx:10-18; src/screens/common/NoRolesScreen/NoRolesScreen.tsx:24-90`
- **me-ios** (Employee): screens: `SelectAccountView`; endpoints: `GET /employee/api/v1/authorization/currentSession`; storage: `SecureStorage currentUser` · evidence `EmployeeServices/UserService/Sources/UserService/Service/UserService.swift:57-190`
- **me-android** (Employee): screens: `LoginRootHost`, `MainActivityDialogs` · evidence `app/src/main/java/com/visma/employee/home/MainActivity.kt:285-308`

**How they differ:**
- Flow: vmm signs the user in and shows a dedicated NoRolesScreen (no_roles_error_message) with a Log out button (104, 111). Employee refuses the session: it revokes tokens or logs out with reason noPermissions/unauthorizedUser and shows a message on the login screen (me-ios 450, 267 loginFailedNoPer…
- Rule: vmm counts integration access with getIntegrationAccessCount === 0 across HRM/Approval/OSR/Autopay/BXN (104). Employee requires at least one company context with non-empty permissions (me-ios 450).
- Logout from the no-roles screen in vmm is retried once, ignores errors, and calls both revocation and endsession (111).
- Flow: vmm lets the user in and puts a dedicated NoRolesScreen with a Log out button in front of the app (navConfig.tsx:184, NoRolesNavConfig.tsx:13, NoRolesScreen.tsx:65-77). Employee rejects the session and shows a message on the login or account screen instead (me-ios SelectAccountFeature.swift:2…
- Rule: vmm counts only four access flags, HRM, OSR, Approval and Autopay (settingsSelector.ts:38-49), and shows the no-roles screen when the count is 0. The claim's 'BXN' is not in the code. Employee iOS requires non-empty contexts with at least one non-empty permissions list (UserService.swift:135-…
- Logout in vmm: NoRolesScreen retries apiManagerConnect.logout once and ignores errors (NoRolesScreen.tsx:36-60). That logout always POSTs /connect/revocation, but opens the web endsession only when the time since first login is under CONNECT_WEB_SESSION_LIFETIME (apiManagerConnect.ts:504-534). The…
- Employee: an HTTP 403 from currentSession counts as having no permissions and ends the session (me-ios UserService.swift:82-85,172-176 revokeTokens / handleUnauthorizedUser(.unauthorizedUser); me-android AuthorizationServiceImpl.kt:105-107 publishes EventNoFeaturesUser). vmm has no equivalent handl…
- (platform parity) Android also rejects the session when features is null or features.available is empty (AuthorizationServiceImpl.kt:91-92). iOS checks only contexts and permissions (UserService.swift:135-143).
- (platform parity) Android shows the no-features message as a Toast (MainActivity.kt:302-303). iOS shows an AlertState on SelectAccountView (SelectAccountFeature.swift:21, 172-175).

_Note: referee could not confirm: vmm divergence line: 'getIntegrationAccessCount across HRM/Approval/OSR/Autopay/BXN' is wrong. The selector at settingsSelector.ts:38-49 counts only HRM, OSR, Approval and Autopay.; vmm divergence line: logout 'calls both revocation and endsession' is wrong. Endsession opens only inside the web-session lifetime (apiManagerConnect.ts:530-532).; me-android: the implementa…_

### CAP-201: Log out

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** High

A signed-in person logs out. The app revokes their tokens, unregisters push, clears local session data and returns to the login screen.

- **vmm** (Manager): screens: `SettingsScreen`; endpoints: `POST https://connect.visma.com/connect/revocation`, `GET https://connect.visma.com/connect/endsession`; events: `clicked_logout_button`, `logout_request`; platform: `app icon badge reset (setBadgeCount(0))`, `Universal link https://visma-manager.web.app/connect-logout` · evidence `src/screens/common/SettingsScreen/SettingsScreen.tsx:176-208`
- **me-ios** (Employee): screens: `SettingsTableViewController (logout row)`, `UserProfileView`; endpoints: `POST https://connect.visma.com/connect/revocation`, `DELETE /employee/api/v1/notification/UnregisterDevice`; storage: `Constants.CacheKey.currentUser (removed)`, `tokens (removed)`; platform: `push unregister` · evidence `Employee/Services/AppStateService.swift:69-101; Employee/Accounts/Feature/UserProfile/UserProfileCoordinator.swift:57-60`
- **me-android** (Employee): screens: `SettingsScreen`, `LogoutConfirmationDialog`, `UserMenuContent`; endpoints: `POST https://connect.visma.com/connect/revocation`; storage: `AuthDataStorage (cleared)`, `user and app preferences (PreferencesCleanupService)`, `Dottie profile cache`; platform: `FirebaseMessaging token for unregister` · evidence `app/src/main/java/com/visma/employee/navigation/RootHostViewModel.kt:95-145; app/src/main/java/com/visma/employee/navig…`

**How they differ:**
- Web session: vmm also calls GET https://connect.visma.com/connect/endsession when the first login is within CONNECT_WEB_SESSION_LIFETIME hours (112). Employee only calls POST /connect/revocation (me-ios 332, me-android 534).
- Push unregister: me-ios calls DELETE /employee/api/v1/notification/UnregisterDevice (272), and me-android unregisters with the FirebaseMessaging token (534). vmm unregisters the device token through the loginManagerLogoutStart epic (111), but no endpoint is reported.
- Badge: vmm resets the app icon badge with setBadgeCount(0) (112). Employee reports no badge handling.
- Safety: vmm has a 12s safety timeout that re-enables the button, and blocks back navigation while logging out (112). No Employee equivalent is reported.
- Entry points: vmm only from Settings (112). Employee from Settings and from the profile/user menu (me-ios 272/332, me-android 497/512).
- (platform parity) me-android asks for confirmation in LogoutConfirmationDialog, with text that depends on the lock type (512, 534). me-ios reports no confirmation for Settings logout (332).
- (platform parity) me-android revokes both access and refresh tokens, only when both exist, and recreates the host activity (534). me-ios revokes the refresh token and returns to SelectAccountCoordinator (332, 272).
- Web session: vmm also opens GET /connect/endsession with id_token_hint and post_logout_redirect_uri when the first login was less than 8h ago (apiManagerConnect.ts:146, 473-474, 531). Employee never ends the web session: it only calls POST /connect/revocation (me-ios OAuthService.OAuthSwift.swift:1…
- Tokens revoked: vmm and me-ios revoke only the refresh token (apiManagerConnect.ts:507; OAuthService.OAuthSwift.swift:155-158). me-android revokes the access token and the refresh token (RootHostViewModel.kt:100-117) (platform parity between me-ios and me-android).
- Push unregister: vmm unregisters in the logout epic after loginManagerLogoutStart (SettingsScreen.tsx:194-196; NoRolesScreen.tsx:53), and no endpoint was confirmed. me-ios calls UnregisterDevice only when an access token and a device token exist (AppStateService.swift:73-84; PushNotificationService…
- Badge: vmm calls setBadgeCount(0) on logout (SettingsScreen.tsx:193). Employee has no badge reset in its logout paths.
- Safety: vmm has LOGOUT_SAFETY_TIMEOUT_MS=12000, which re-enables the button, and it blocks the beforeRemove navigation while logging out (SettingsScreen.tsx:161-187). Employee has no equivalent.
- Failure handling: vmm stays signed in and re-enables the button if revocation throws (SettingsScreen.tsx:197-202). Employee always clears the local session, whatever the server result (AppStateService.swift:86-97; RootHostViewModel.kt:120-121).
- Entry points: vmm uses Settings and NoRolesScreen (NoRolesScreen.tsx:48-73). The claim said Settings only. Employee uses Settings and the profile/user menu (SettingsTableViewController.swift:483; UserProfileCoordinator.swift:57-60; SettingsEntry.kt:179; UserMenuContent.kt:61-70).
- (platform parity) me-android asks for confirmation on both its Settings and user-menu paths (SettingsEntry.kt:214-222, 245-256; UserMenuContent.kt:61-70), and the dialog text is fixed (logout_confirmation_dialog_description). me-ios calls logout directly from Settings with no confirmation (Settings…
- (platform parity) me-android makes the server calls only when both tokens exist, then recreates the host activity (RootHostViewModel.kt:98, RootHostSessionActions.kt:25-28; MainActivity.kt:808-811). me-ios revokes whenever a refresh token exists and routes to the login page via mainCoordinator.goTo…
- (platform parity) me-android clears user and app preferences and the Dottie profile cache on logout (RootHostViewModel.kt:147-157). me-ios removes only the currentUser cache key and the tokens (AppStateService.swift:92-95).

_Note: referee could not confirm: The claim says 'me-android ... LogoutConfirmationDialog, with text that depends on the lock type'. The dialog text is fixed (logout_confirmation_dialog_description, SettingsEntry.kt:245-256). The lock-type strings are the Settings row description (SettingsEntry.kt:122-126).; The claim says 'Entry points: vmm only from Settings'. vmm also logs out from NoRolesScreen (vmm…_

### CAP-202: Switch between saved accounts

**Fusion:** unique · **Personas:** employee with several accounts · **Confidence:** High

A person with several Visma accounts on the device picks one, from the login screen or from the account manager, to make it active. A still-signed-in account opens right away; a signed-out one opens the web login with the email prefilled.

- **me-ios** (Employee): screens: `SelectAccountView`, `UserAccountsView`, `UserRow`, `AccountManagerView`, `UserProfileView`; endpoints: `GET /employee/api/v1/authorization/currentSession`; events: `loginMethods`; storage: `UserService.allUsers`, `OAuth refresh token presence decides isLoggedIn`, `UserService current user`, `DottieEmployeeRepository cache cleared on switch`, `SecureStorage loggedInUsers`, `SecureStorage currentUser` · evidence `Employee/Accounts/Feature/Login/SelectAccountFeature.swift:131-138; Employee/Accounts/Feature/AccountManager/AccountMan…`
- **me-android** (Employee): screens: `LoginScreenAccountManagerContent`, `AccountManagerLayout`, `LoginKey`; endpoints: `POST https://connect.visma.com/connect/token (background refresh of tokens for…`; storage: `UserDatabaseDao user accounts (Room: email, access/refresh token, odpUserId, ga…`, `AuthDataStorage.lastLoggedInUserNameState`; platform: `background coroutine token refresh` · evidence `login/src/main/java/com/visma/employee/login/LoginViewModel.kt:143-152; app/src/main/java/com/visma/employee/home/Compo…`

**How they differ:**
- (platform parity) me-ios decides 'logged in' by whether a refresh token exists for that connectUserId, clears the Dottie cache and reloads app state on switch (268, 270). me-android keeps accounts in a Room table with an isLoggedIn flag, recreates the activity on switch, and marks an account signed…
- (platform parity) me-ios opens the account manager from the start page or the profile menu's Switch account item (270). me-android opens the account manager sheet from the Home avatar/user menu (496, 514).
- (platform parity) me-ios treats an account as signed in when a refresh token exists (UserSessionManager.live.swift:64-66). me-android reads a stored isLoggedIn flag from Room, which a failed background refresh with AuthorizationError sets to false (AccountManagerServiceImpl.kt:141-163).
- (platform parity) me-ios switches in place: UserService.switchUser sets the current user and clears the Dottie cache (UserService.swift:303-313, AppStateManager.live.swift:33). me-android picks the account and recreates the activity (ComposeBottomModalSheetDelegate.kt:122-124).
- (platform parity) The entry points differ. me-ios uses the login SelectAccount list and the account manager, which opens from the profile's Switch account item. me-android uses the login account manager content and a bottom sheet from Home.

_Note: referee could not confirm: me-ios events 'loginMethods': this is a closure on the session manager (UserSessionManager.live.swift:67), not an event; me-ios endpoint GET /employee/api/v1/authorization/currentSession exists (GetCurrentSession.swift:19), but none of the cited switch code calls it_

### CAP-203: Add another account

**Fusion:** unique · **Personas:** employee · **Confidence:** High

From the account manager a person signs in to one more Visma account. It is stored next to the existing ones and becomes the current account.

- **me-ios** (Employee): screens: `AccountManagerView`, `AccountManagerFeature`; endpoints: `GET /employee/api/v1/authorization/currentSession`; storage: `UserService users`, `SecureStorage loggedInUsers`; platform: `ASWebAuthenticationSession` · evidence `Employee/Accounts/Feature/AccountManager/AccountManagerFeature.swift:79-103`
- **me-android** (Employee): screens: `AccountManagerLayout`, `LoginScreen`; endpoints: `POST https://connect.visma.com/connect/token`, `GET /api/v1/authorization/currentsession`; storage: `UserDatabaseDao user accounts` · evidence `login/src/main/java/com/visma/employee/account_manager/presentation/AccountManagerViewModel.kt:105-111`

**How they differ:**
- (platform parity) me-ios checks that the session's connectUserId matches the account just logged in, and shows an alert with the error description on failure (451, 269). me-android saves the email, tokens, odpUserId and gaUserId from the session response to Room (677). No match check is reported.
- (platform parity) me-ios UserService.swift:65-68 throws addUserFailed when the session connectUserId does not match the id from the token. It also rejects a user who is missing required permissions (lines 73, 83). me-android LoginViewModel.kt:189-199 only checks that sessionResponse.data is not nul…
- (platform parity) On failure, me-ios shows an addUserFailed alert and stays quiet if the login was cancelled (AccountManagerFeature.swift:95-103). me-android restores the previously selected account's auth data and goes to onAuthenticationFailed with the server message or login_failed_no_session /…
- (platform parity) me-ios gets connectUserId from the JWT subject (OAuthLogin.live.swift:51). me-android saves the email, tokens, odpUserId and gaUserId from the session response, then refreshes user features (LoginViewModel.kt:192-200).

_Note: referee could not confirm: me-android evidence line range: onAddNewAccount is at AccountManagerViewModel.kt:107-113, not 105-111 (minor offset); me-ios endpoint 'GET /employee/api/v1/authorization/currentSession' was not confirmed in production Swift code; only a currentSessionPath constant appears in the EmployeeAPI tests (BaseAPIServiceTests.swift:34)_

### CAP-204: Remove a saved account from the device

**Fusion:** unique · **Personas:** employee · **Confidence:** High

In edit mode on the account list a person removes an account after confirming. The app revokes its tokens, unregisters push and deletes its local data.

- **me-ios** (Employee): screens: `UserAccountsView`, `AccountManagerView`, `SelectAccountView`; endpoints: `DELETE /employee/api/v1/notification/UnregisterDevice`; storage: `UserService.removeUser`, `OAuth tokens revoked`, `Dottie cache cleared` · evidence `Employee/Accounts/Feature/UserAccounts/UserAccountsFeature.swift:77-99`
- **me-android** (Employee): screens: `AccountManagerLayout`, `LoginScreenAccountManagerContent`, `ConfirmationDialog`, `LoginRootScreen`; endpoints: `POST https://connect.visma.com/connect/revocation`; storage: `UserDatabaseDao user accounts`, `UserPreferencesRepository`, `MileagePreferencesRepository`, `HighlightDismissalRepository`, `AppPreferencesRepository`, `Appearance cache` · evidence `login/src/main/java/com/visma/employee/account_manager/data/AccountManagerServiceImpl.kt:192-258`

**How they differ:**
- (platform parity) me-ios disables edit mode with fewer than 2 users unless allowsEditingOfSingleUser (the login screen allows it) (271). me-android turns edit mode off while offline and when there is one account or fewer (678).
- (platform parity) me-ios unregisters push via DELETE /employee/api/v1/notification/UnregisterDevice only if an access token exists, and revokes only if a refresh token exists (271). me-android revokes both tokens and clears the user, mileage, highlight, app and appearance preference stores (678).
- (platform parity) Edit mode: me-ios turns edit mode off with fewer than 2 users unless allowsEditingOfSingleUser is set (UserAccountsFeature.swift:103-106). me-android turns it off when offline or when there is 1 account or fewer (AccountManagerViewModel.kt:48-51). me-ios does not turn it off when…
- (platform parity) Unregister and revoke: me-ios unregisters push only if an access token and a device token exist, and revokes only if a refresh token exists (AppStateManager.live.swift:22-31). me-android always runs unregister (DELETE api/v1/notification/UnregisterDevice, SubscriptionServiceImpl.k…
- (platform parity) Local data: me-ios clears the Dottie cache only (AppStateManager.live.swift:33). me-android clears the user, mileage and highlight preferences for that user, and also the app preferences and appearance cache when the removed account was the selected one (AccountManagerServiceImpl.…
- (platform parity) Errors: me-ios shows a removeUserFailed alert if removal throws (UserAccountsFeature.swift:88-99). me-android shows no error; it swallows failures inside a SupervisorJob scope (AccountManagerServiceImpl.kt:238-256).
- (platform parity) Order: me-ios deletes the user record first, then logs out (UserAccountsFeature.swift:89-92). me-android logs out and clears preferences before removing the database row, then updates the stored account count (AccountManagerServiceImpl.kt:192-197).

_Note: referee could not confirm: me-android implementation lists only the revocation endpoint and omits DELETE api/v1/notification/UnregisterDevice (me-android/core/src/main/java/com/visma/employee/core/notification/SubscriptionServiceImpl.kt:62), which removeUserAccount also calls_

### CAP-205: Switch between my employers

**Fusion:** unique · **Personas:** employee with multiple employers · **Confidence:** High

An employee who works for several companies picks the active employer from the start or home page. The app then reloads with that company's data, permissions and features. When none is chosen yet, the choice is mandatory.

- **me-ios** (Employee): screens: `StartPageViewController company selector`, `CompanySelectorTableViewCell`, `UIAlertController chooseEmployer`; storage: `UserDefaults isCompanySelectorShown`, `current UserContext via UserService.setCurrentUserContext`, `SecureStorage <connectUserId>-scoped currentContext`; platform: `iOS 26 Liquid Glass UIMenu bar button` · evidence `Employee/StartPage/StartPageViewController.swift:963-989; EmployeeServices/UserService/Sources/UserService/Service/User…`
- **me-android** (Employee): screens: `Home toolbar`, `HomeScreen`, `HomeTopBar`, `CompanySelector`; endpoints: `GET /api/v1/authorization/currentsession`; storage: `ContextService currentContext` · evidence `app/src/main/java/com/visma/employee/home/HomeViewModel.kt:1426-1505; app/src/main/java/com/visma/employee/home/company…`

**How they differ:**
- (platform parity) me-ios offers a drop-down under the tappable title, a nav-bar UIMenu on iOS 26 Liquid Glass, and a forced action sheet on first launch (UserDefaults isCompanySelectorShown) (317). me-android uses a dropdown in the Home top bar (490, 514).
- (platform parity) me-ios reloads the start page for the new context and removes a stored context that is gone after a session refresh (317, 452). me-android recreates the host activity and reloads features via GET /api/v1/authorization/currentsession (551).
- (platform parity) me-ios shows the picker as a drop-down under the tappable start-page title, as a nav-bar UIMenu when Liquid Glass is supported, and as a forced chooseEmployer action sheet (StartPageViewController.swift:664) gated by the isCompanySelectorShown preference (line 854). me-android sho…
- (platform parity) The mandatory choice has a different trigger. On me-ios the action sheet is gated by a stored 'selector already shown' flag. On me-android the dropdown is forced open and cannot be dismissed while currentContext is null and there is more than one context (HomeViewModel.kt:1450-145…
- (platform parity) Reload after switching differs. me-ios updates the API config in place and reloads the start page (StartPageViewController.swift:973-983). me-android recreates the host activity (RootHostActionsFactory.kt:211) and takes feature permissions from the current context (FeaturesService…
- (platform parity) With a single company, me-android shows the company name without a selector (HomeViewModel.kt:1446-1448). me-ios checks userHasMultipleCompanies before showing its selector (StartPageViewController.swift:427).

_Note: referee could not confirm: Not an error, but misplaced: the cited endpoint GET /api/v1/authorization/currentsession is declared in core/src/main/java/com/visma/employee/core/auth/AuthorizationServiceImpl.kt:185, a file the claim does not list. FeaturesServiceImpl.kt only calls it (lines 97-98).; The Android string keys (context_selector_company_title, account_manager_title) were not found at app/…_

### CAP-206: Protect the app with Face ID, fingerprint or PIN

**Fusion:** unique · **Personas:** employee · **Confidence:** High

During first start or from Settings, an employee turns on an app lock: device biometrics, the device screen lock (Android), or a 4-digit app PIN chosen twice. They can also skip it for later.

- **me-ios** (Employee): screens: `BiometricsSetupFeature / BiometricsSetupView`, `BiometricsSetupViewControllerFactory (BiometricsSetupFeature)`, `PasscodeView (mode .set)`, `PasscodeFeature (set mode)`, `SettingsTableViewController (security toggle on)`; events: `Continue button tapped (log)`, `Later button tapped (log)`, `Skip biometrics setup selected (log)`, `changedState`, `failed`, `succeeded`; storage: `Keychain/secure storage currentLoginType (LoginType.direct=0 / pincode=1)`, `biometric token (Constants.Security.biometricTokenKey)`, `passcode (Constants.Security.passcodeKey)`, `SecureStorage passcodeKey`; platform: `biometrics (LocalAuthentication Face ID / Touch ID)`, `keychain` · evidence `Employee/Welcome/BiometricsSetup/BiometricsSetupFeature.swift:100-187; Employee/Security/Passcode/States/SetPasscodeSta…`
- **me-android** (Employee): screens: `SecuritySetupScreen`, `OnboardingKey`, `SecuritySetupKey`, `PinCodeSetScreen`; storage: `AppPreferencesRepository securityType`, `AppPreferencesRepository pinCode`, `SecurityService pinCode`, `SecurityService currentSecurityType`; platform: `biometrics`, `device credential`, `vibration` · evidence `app/src/main/java/com/visma/employee/navigation/entries/SecuritySetupFlow.kt:89-354; app/src/main/java/com/visma/employ…`

**How they differ:**
- (platform parity) me-android offers a separate device-credential (screen lock) option, and requires a backup PIN for the biometric branch when there is no device credential (507). me-ios offers biometrics or a PIN, and uses a PIN when the device cannot demand user presence (323).
- (platform parity) me-ios stores LoginType direct/pincode, a biometric token and a passcode in the keychain, and 'Later' deletes the PIN and token (323). me-android stores securityType and pinCode in AppPreferencesRepository (507, 536).
- (platform parity) If biometric setup fails, me-ios deletes the token (323), and me-android falls back to the PIN (536).
- (platform parity) me-android sets up one of three branches: biometrics, device credential (screen lock) or PIN (SecuritySetupFlow.kt:98-108). me-ios offers biometrics, or a passcode when canDemandUserPresence() is false (BiometricsSetupFeature.swift:114-117). In both apps the app picks the branch f…
- (platform parity) On me-android, the biometric branch asks for a backup PIN first when no device credential is available, then shows the biometric prompt (SecuritySetupFlow.kt:303-311, 339-343). me-ios has no backup-PIN step.
- (platform parity) If biometric setup fails, me-ios deletes the token and stays on the setup step (BiometricsSetupFeature.swift:127-131). me-android returns to the Setup intro step through onReturnToIntro or onBiometricDeclined. The callback is named onFallbackToPin but does not open the PIN keypad…
- (platform parity) On me-ios, Later sets LoginType.direct and deletes the passcode and the biometric token (BiometricsSetupFeature.swift:141-143). On me-android, Later only calls config.onCancel (SecuritySetupFlow.kt:132); whether anything is cleared depends on the caller.
- (platform parity) me-ios keeps LoginType, the biometric token and the passcode in the keychain. me-android keeps securityType and pinCode in its settings storage (PinCodeSetViewModel.kt:49).

_Note: referee could not confirm: me-android divergence claim 'falls back to the PIN (536)': the code sends the user back to the intro step instead (SecuritySetupFlow.kt:307, 318, 342)_

### CAP-207: Unlock the app with Face ID, fingerprint or PIN

**Fusion:** unique · **Personas:** employee · **Confidence:** High

When the app starts or comes back with an active session, the employee unlocks it with biometrics, the device credential or the 4-digit app PIN, after a time-of-day greeting. They can also choose to log in again, which wipes the saved accounts.

- **me-ios** (Employee): screens: `PasscodeView`, `PasscodeFeature`, `DeviceOwnerAuthView`, `DeviceOwnerAuthFeature`; events: `addedSign`, `removedSign`, `changedState`, `failed`, `succeeded`, `afterIncorrect`; storage: `SecureStorage passcodeKey`, `SecureStorage wrongAttemptsKey`, `Keychain biometricTokenKey (random 32 bytes, userPresence access control)`; platform: `separate lock UIWindow above main window`, `biometrics (LocalAuthentication)`, `Keychain access group` · evidence `Employee/Security/Passcode/PasscodeFeature.swift:80-177; Employee/Security/Biometric/DeviceOwnerAuthFeature.swift:47-75`
- **me-android** (Employee): screens: `LockEnterScreen`, `LockKey`, `BiometricsLandingScreen`, `PinCodeEnterContent`; storage: `AppPreferencesRepository pinCode (gson JSON)`, `AppPreferencesRepository securityType`, `SecurityService pinCode/currentSecurityType/timestamp`, `room-entity:app_preferences (security type, PIN code)`, `CURRENT_SECURITY_TYPE_KEY`, `CURRENT_PIN_CODE`; platform: `biometrics (BIOMETRIC_STRONG / DEVICE_CREDENTIAL BiometricPrompt)`, `device credential`, `vibration` · evidence `app/src/main/java/com/visma/employee/navigation/entries/LockEntries.kt:83-192; app/src/main/java/com/visma/employee/nav…`

**How they differ:**
- (platform parity) When the lock appears: me-ios shows it on start or resume whenever a passcode or biometric token exists and a session is active (295). me-android locks only after more than 180s in the background (SECONDS_UNTIL_LOCKED), and not over the Onboarding, SecuritySetup, CalendarBot, Logi…
- (platform parity) Wrong PIN: me-ios wipes the PIN, removes all users and logs out after 4 wrong attempts (295). me-android vibrates for 500ms and shakes, and no attempt limit is reported (506).
- (platform parity) Greeting hours differ: me-ios morning 5-12, afternoon 12-18 (296); me-android morning 5-11, afternoon 12-16 (535).
- (platform parity) me-android migrates the lock method on each lock when device security changes: it upgrades PIN users to biometrics or device credential, or downgrades to PIN or login-only (506, 569). No migration is reported on me-ios.
- (platform parity) me-ios shows the lock in a separate UIWindow, and a biometric token takes precedence over the PIN (295, 296). me-android uses BiometricPrompt BIOMETRIC_STRONG / DEVICE_CREDENTIAL and falls back to the PIN only if one is stored (535, 506).
- (platform parity) When the lock appears: me-android locks once the app has been in the background for more than 180s (SecurityService.kt SECONDS_UNTIL_LOCKED = 180; SecurityServiceImpl.kt:77). The fragment says me-ios locks on start or resume whenever a lock method is set and a session is active; I…
- (platform parity) Wrong PIN: me-ios counts wrong attempts in storage and, at maximumInccorectPasscodeAttempts = 4 (PasscodeLockConfiguration.swift:16; EnterPasscodeState.swift:28-37), deletes the passcode, removes the login type and forces a logout (PasscodeFeature.swift:168-175). me-android only v…
- (platform parity) Greeting hours: me-ios morning 5..<12, afternoon 12..<18 (DeviceOwnerAuthFeature.swift:36-40); me-android morning 5..11, afternoon 12..16 (GreetingProvider.kt).
- (platform parity) me-android runs migrateSecurityIfNeeded each time the lock screen opens, and unlocks straight away when the result is DOWNGRADED_TO_LOGIN_ONLY (LockEntries.kt DisposableEffect). No such migration exists in the me-ios lock flow.
- (platform parity) Biometric failure: on me-android a biometric error or failure falls back to the PIN keypad (RootHostBiometricActions.kt onFallbackToPin). On me-ios a failure leaves the user on the biometric screen with a retry button (DeviceOwnerAuthFeature.swift:67-69).
- (platform parity) Log in again: me-android wipes all accounts (performRelogWipeAllAccounts, RootHostActionsFactory.kt:197). me-ios cancel deletes the passcode and logs out with reason reloginFromPinCodeScreen, not forced (PasscodeFeature.swift:101-110).

### CAP-208: Turn off the app lock

**Fusion:** unique · **Personas:** employee · **Confidence:** High

In Settings the employee switches off the 'open app with Face ID/fingerprint/PIN' toggle, confirms, and verifies once more. From then on the app opens without a lock.

- **me-ios** (Employee): screens: `SettingsTableViewController (security toggle)`, `PasscodeViewFactory (enter mode)`; storage: `currentLoginType`, `biometric token`, `passcode`; platform: `biometrics` · evidence `Employee/Settings/SettingsTableViewController.swift:184-290`
- **me-android** (Employee): screens: `SettingsScreen`, `SecurityDeactivationDialog`, `LockKey(MODE_CONFIRM_DEACTIVATION)`, `LockKey(CONFIRM_DEACTIVATION)`; storage: `AppPreferencesRepository securityType`, `SecurityService currentSecurityType`; platform: `biometrics` · evidence `app/src/main/java/com/visma/employee/navigation/entries/SettingsEntry.kt:135-244`

**How they differ:**
- (platform parity) me-ios disables security without verification when the device has no passcode or biometrics and no PIN exists, and restores the toggle on cancel (324). me-android applies deactivation only after the lock returns ENTER_PIN_REQUEST_OK in CONFIRM_DEACTIVATION mode, and the dialog tex…
- (platform parity) me-ios skips verification and turns security off at once when the device can't demand user presence and no passcode exists (SettingsTableViewController.swift:240-245). me-android always sends the user to LockKey(CONFIRM_DEACTIVATION) (SettingsEntry.kt:206).
- (platform parity) me-ios deletes the biometric token and the stored passcode when turning the lock off (disableSecurity, SettingsTableViewController.swift:234-238). me-android only sets currentSecurityType to loginOnly (SettingsViewModel.kt:89-92); no PIN deletion is visible in the cited code.
- (platform parity) me-android shows a login_only_successfully snackbar after the lock is turned off (SettingsEntry.kt:145). me-ios only reloads the row.
- (platform parity) me-android's dialog has separate texts for biometrics, device credential and PIN (SettingsEntry.kt:222-227). me-ios uses one deactivate.message string with the security type name filled in, and has no device-credential type.
- (platform parity) On cancel, me-ios resets the toggle with cell.selectedValue=true. me-android calls invalidateAppLockScreenSelection() to read the state again.

_Note: referee could not confirm: me-android screens list 'LockKey(MODE_CONFIRM_DEACTIVATION)' and 'LockKey(CONFIRM_DEACTIVATION)' as two screens. They are one screen: LockModes.CONFIRM_DEACTIVATION has the value "MODE_CONFIRM_DEACTIVATION" (AppNavKeys.kt:8).; The me-android citation should start around line 132 (the deactivationRequest state), not at 135._

### CAP-209: Switch the backend environment

**Fusion:** shared-diverged · **Personas:** internal tester, developer · **Confidence:** Medium

An internal tester unlocks a hidden environment picker on the login screen and points the app at another backend (production, stage/staging, sandbox), or switches back to production.

- **vmm** (Manager): screens: `LoginSelectScreen (EnvPicker)`, `SettingsScreen`; storage: `redux settings.env (persisted settings slice)` · evidence `src/components/common/EnvPicker/EnvPicker.tsx:14-94; src/screens/common/SettingsScreen/SettingsScreen.tsx:224-237,337-3…`
- **me-ios** (Employee): screens: `SelectAccountView`; storage: `CoreUtils current environment`, `third-party keys cleared`, `UserPreferences last logged-in user reset` · evidence `Employee/Accounts/Utils/EnvironmentManager.live.swift:29-44`
- **me-android** (Employee): screens: `LoginRootScreen`, `LoginScreen`; storage: `room-entity:api_keys (encrypted keys per environment)` · evidence `app/src/main/java/com/visma/employee/navigation/entries/LoginEntries.kt:69-184`

**How they differ:**
- Unlock gesture: vmm needs 6 taps on an invisible marker, and choosing prod hides the picker again (50). me-ios needs 5 taps (278). me-android shows the picker only in builds where R.bool.env_selector_enabled / isEnvironmentSelectorVisible is set (513, 533).
- Environments: vmm has production, stage and sandbox (50). me-ios has staging and production (278).
- Side effects: me-ios wipes all accounts, third-party keys and the last logged-in user (278). vmm persists settings.env, and from Settings a switch back to prod shows an untranslated confirm alert and logs out if logged in (120).
- vmm also offers the switch back to production from Settings (120). No Settings entry is reported for Employee.
- (platform parity) The me-ios 5-tap gesture is not gated by DEBUG, so it is reachable in production builds (278). me-android limits the selector to internal builds (513, 533).
- Unlock: vmm needs 6 taps on an invisible env marker, and choosing production hides it again (EnvPicker.tsx:59-65). me-ios needs 5 taps on a clear hit area (SelectAccountView.swift:44-50). me-android has no gesture: a visible selector shows when the build flag env_selector_enabled is true (RootHostA…
- Environments: vmm offers production, staging and sandbox (consts/constants.ts:2-4, EnvPicker.tsx:23-28). me-ios offers staging and production (AppConstants.swift:43-46). me-android loads its list from R.xml.environments (LocallyStoredEnvironmentsRepository.kt), a file not found in the repo.
- Side effects: me-ios clears third-party keys, deletes all stored users and their context, resets OAuth and the API config, and resets the last logged-in user (EnvironmentManager.live.swift:29-44). vmm only dispatches envChange on the login picker (EnvPicker.tsx:39-51). Its Settings route to product…
- Entry points: vmm also offers a return to production from Settings through an 'Environment: staging/sandbox' item with a hardcoded English confirm alert (SettingsScreen.tsx:337-354). Employee offers the choice only on the login/select-account screen.
- (platform parity) me-ios wipes every account on a switch (EnvironmentManager.live.swift:29-44). me-android only saves the environment through appPreferencesRepository and recreates the host (LocallyStoredEnvironmentsRepository.kt:60-63, RootHostActionsFactory.kt:172-176).
- (platform parity) The me-ios 5-tap gesture has no DEBUG guard (the only #if DEBUG in SelectAccountView.swift, at line 131, wraps previews), so it can be reached in release builds. me-android limits the selector to debug, debugMinified and stable builds (res/values app_config.xml and strings.xml), a…

_Note: referee could not confirm: me-android storage 'room-entity:api_keys (encrypted keys per environment)' does not appear in the cited Android code; the choice is saved through appPreferencesRepository.saveEnvironment (LocallyStoredEnvironmentsRepository.kt:60-63); Neither the Android environment list file (R.xml.environments) nor a Kotlin gate named isEnvironmentSelectorVisible defining visibility e…_

### CAP-210: Choose a sandbox environment at login

**Fusion:** unique · **Personas:** internal tester, developer · **Confidence:** High

With the sandbox environment selected on the login screen, a tester picks which sandbox (by colour) the app talks to, from the sandboxes currently available.

- **vmm** (Manager): screens: `SandboxPicker (on LoginSelectScreen)`, `SettingDropdown`; endpoints: `GET https://int-vismm-sandbox-dashboard.azurewebsites.net/api/sandbox-status`; storage: `redux settings.env`, `redux settings.sandboxColor (persisted settings node)` · evidence `src/components/common/SandboxPicker/SandboxPicker.tsx:16-66`

_Note: Rendered only when env === ENV_SANDBOX. If the status call fails it falls back to SANDBOX_COLORS, and the first available colour is picked automatically._

## Settings and legal

Language, appearance, analytics consent, terms, privacy and accessibility statements, licenses, app updates, state persistence and developer tools

### CAP-108: Open app settings

**Fusion:** shared-diverged · **Personas:** manager · **Confidence:** High

Open the Settings screen from the gear button in the root header of any integration (OSR, BXN and others), or run a custom handler when the header supplies one.

- **vmm** (Manager): screens: `SCREEN_NAME_SETTINGS`; platform: `react-native` · evidence `src/components/themed/NavButtonSettings/NavButtonSettings.tsx:18-44`

**How they differ:**
- Entry point: in vmm (Manager) Settings opens from a gear icon in the root header of each integration (NavButtonSettings.tsx:18-44, used in StartScreen, Approval, Autopay, HRM list, OSR and BXN header-right components). In Employee it is a permanent last tab in the bottom tab bar (me-ios TabbarCoord…
- Per-integration routing: in vmm the header can supply a custom handler, and OSR uses one to open Settings inside its own tab stack (OsrNavConfig.tsx:41-46, ConfigurableHeaderRight.tsx:47-51). Employee has one Settings tab and no handler that changes per module.
- Programmatic entry: vmm lets the Gaia chat assistant navigate to Settings (useGaiaFrontendToolExecutor.ts:209-211). Employee opens it through a coordinator action (me-ios TabbarCoordinator.swift:155 .showSettings) or a deep link (me-android RootDeepLinks.kt:142-143 'settings' segment).
- (platform parity) me-android has a 'settings' deep-link segment in RootDeepLinks.kt:34,142. I did not trace what triggers .showSettings on me-ios; only the coordinator handler at TabbarCoordinator.swift:155 is confirmed.

_Note: The Employee fragments reach Settings too, but none of them describe how Settings is opened, so this stays unique to Manager until someone checks. referee could not confirm: The claim lists only OSR and BXN, but NavButtonSettings is also used by StartScreenHeaderRight, ApprovalHeaderRight, AutopayHomeScreenHeaderRight and HrmEmployeeListScreenHeaderRight. The evidence is correct, just incomplete.…_

### CAP-109: Choose the app language

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** High

Pick the language the app is shown in. Without a choice, the app uses the device locale or the default language.

- **vmm** (Manager): screens: `LoginSelectScreen`, `SettingsScreen`, `SCREEN_NAME_SETTINGS`; endpoints: `PUT /users/{userId}/settings`; storage: `redux settings.locale`, `redux settings locale via langChange (persisted settings slice)`, `AsyncStorage user_settings_backup (fallback)`; platform: `react-native`, `shared notification strings (syncNotificationStrings)` · evidence `src/screens/common/SettingsScreen/SettingsScreen.tsx:110-119,293-307; src/configs/langConfig.ts:8-58; src/components/ui…`
- **me-ios** (Employee): screens: `SettingsTableViewController (language row)`; events: `open app settings from language selector (log)`; platform: `ios-native`, `UIApplication.openSettingsURLString (per-app language in iOS Settings)` · evidence `Employee/Settings/SettingsTableViewController.swift:118-152`
- **me-android** (Employee): screens: `SettingsScreen`, `SettingsKey`; storage: `LanguageService currentLanguage`, `template cache (cleared)`, `room-entity:app_preferences (language, stored as JSON)`, `res/xml/languages.xml`; platform: `android-native`, `locale ContextWrapper` · evidence `app/src/main/java/com/visma/employee/navigation/RootHostViewModel.kt:89-93; core/src/main/java/com/visma/employee/core/…`

**How they differ:**
- Where the choice is made: vmm has an in-app picker on the login screen and in Settings (LangAccPicker.tsx:30-146). me-ios sends the user to iOS Settings for the per-app language (SettingsTableViewController.swift:118-152). me-android has an in-app picker in Settings (RootHostViewModel.kt:89-93).
- Backend sync: vmm saves the locale to PUT /users/{userId}/settings when the user leaves Settings (SettingsScreen.tsx:110-119). No Employee fragment reports a backend sync; the language is stored locally in AppPreferences on Android (LanguageServiceImpl.kt:22-52).
- Supported languages: vmm has da/en/nl/fi/no/sv, maps 'se'->'sv' and 'nb'->'no', and defaults to 'en' (langConfig.ts:8-58). me-android uses a bundled res/xml/languages.xml and matches '<lang>-<country>', falling back to default_language_code.
- Side effects: vmm re-syncs the notification strings on languageChanged (i18n.ts:31-37). me-android restarts the app, updates the Survicate locale and clears cached templates (RootHostViewModel.kt:89-93).
- Device locale changes: vmm predicts the language from the device only on first start and does not pick up later changes (LangInitializer.tsx:10-42).
- (platform parity) me-ios hands the language to iOS Settings and only shows CoreUtils.getCurrentAppLanguage(). me-android offers its own picker, stores the choice and restarts.
- Where the choice is made: vmm has an in-app dropdown on the login screen (LoginSelectScreen.tsx:208) and in Settings (SettingsScreen.tsx:293-307, LangAccPicker.tsx:59-78). The Employee product's language row is in Settings (me-ios SettingsTableViewController.swift:118-152; me-android SettingsEntry.…
- Backend sync: vmm saves the locale with its other settings through PUT users/{userId}/settings when the user leaves Settings (SettingsScreen.tsx:100-119, apiUserSetting.ts:96-105). The Employee product keeps it on the device only: AppPreferences JSON on Android (LanguageServiceImpl.kt:22-29), the i…
- Supported languages and fallback: vmm offers da/en/nl/fi/no/sv, maps se->sv and nb->no, and defaults to 'en' (langConfig.ts:8-33). me-android reads R.xml.languages, matches '<lang>-<country>' and falls back to default_language_code en-GB (LanguageServiceImpl.kt:48-51; translations strings.xml:2). m…
- Side effects: vmm re-syncs the notification strings on i18next languageChanged (i18n.ts:31-33). me-android sets the Survicate locale, clears cached templates (RootHostViewModel.kt:89-93) and restarts the activity (RootHostSessionActions.kt:11-23).
- Device locale: vmm predicts the language from the device locale only at first start and does not follow later device changes (LangInitializer.tsx:10-28). me-ios always follows the iOS per-app locale. me-android uses the device locale only until the user makes a choice.
- vmm's login-screen picker also includes a 'view accessibility statement' entry that opens a WebView (LangAccPicker.tsx:33-35,60-66). The Employee product has no equivalent in this flow.
- (platform parity) me-ios has no in-app picker: it shows an alert and sends the user to iOS Settings (SettingsTableViewController.swift:127-139). me-android has its own picker, saves the choice and restarts the app (RootHostSessionActions.kt:11-23).
- (platform parity) me-ios falls back to English when the language is not matched. me-android falls back to en-GB and matches on language plus country.

_Note: referee could not confirm: me-android res/xml/languages.xml is listed in storage but is not in the legacy snapshot. It is only referenced as R.xml.languages (LanguageServiceImpl.kt:32).; SCREEN_NAME_SETTINGS is a route constant, not a separate screen from SettingsScreen.; 'SettingsKey' (me-android) is a navigation key, not a screen._

### CAP-110: Choose light, dark or system appearance

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** High

Pick a light, dark or system/auto theme. The app restyles right away and remembers the choice.

- **vmm** (Manager): screens: `SettingsScreen (SCREEN_NAME_SETTINGS = 'SettingsScreen')`; endpoints: `PUT /users/{userId}/settings`, `GET /users/{userId}/settings`; events: `theme_override_selected`; storage: `redux settings.darkMode`, `AsyncStorage user_settings_backup (fallback)`; platform: `react-native` · evidence `src/screens/common/SettingsScreen/SettingsScreen.tsx:239-262,308-365`
- **me-ios** (Employee): screens: `SettingsTableViewController (appearance row)`; events: `appAppearanceChanged`; storage: `CoreUtils current appearance key (CoreUtils.setCurrentAppearance)`, `analytics user property appearance`; platform: `ios-native`, `UIWindow overrideUserInterfaceStyle` · evidence `Employee/Settings/SettingsTableViewController.swift:154-182`
- **me-android** (Employee): screens: `SettingsScreen`, `SettingsKey`; storage: `AppPreferencesRepository appearance`, `Appearance.cached`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/settings/presentation/SettingsViewModel.kt:119-127; app/src/main/java/com/visma/em…`

**How they differ:**
- Persistence: vmm saves darkMode to the backend with PUT /users/{userId}/settings when the user leaves Settings, and falls back to AsyncStorage (SettingsScreen.tsx:239-262). me-ios stores it locally in CoreUtils (SettingsTableViewController.swift:154-182). me-android stores it locally in AppPreferen…
- Interaction: vmm cycles light/dark/auto on one row. Employee offers a choice among the options (Constants.availableAppearances on iOS; System/Light/Dark labels on Android).
- Analytics: vmm logs theme_override_selected. me-ios logs appAppearanceChanged and sets an analytics user property. No event is reported for me-android.
- (platform parity) me-ios also pushes the appearance to the Survicate theme (SettingsTableViewController.swift:178). Nothing equivalent is reported for me-android, which restores the appearance at app start from a cache (Application.kt:36-38).
- Persistence: vmm keeps darkMode in redux and saves it to the backend only when the user leaves Settings (beforeRemove, SettingsScreen.tsx:101-107, then PUT users/{id}/settings at apiUserSetting.ts:103-107, with AsyncStorage if that fails), so the choice follows the user across devices. Employee sto…
- Interaction: vmm uses one row that cycles light -> dark -> auto on each tap (SettingsScreen.tsx:252-263, labels dark_mode_light/dark_mode_dark/dark_mode_auto). Employee lets the user pick directly from a selection control (iOS SelectionTableViewCell with Constants.availableAppearances, SettingsTabl…
- Restyle mechanism: vmm re-renders the whole Settings screen by bumping refreshCounter, which is used as the ScreenWrapperWhite key (SettingsScreen.tsx:258,289). iOS sets overrideUserInterfaceStyle on the window. Android calls AppCompatDelegate.setDefaultNightMode and UiModeManager (AppearanceExtens…
- Analytics: vmm logs theme_override_selected through both trackEvent and trackEventNew (SettingsScreen.tsx:259-260). me-ios logs appAppearanceChanged and sets the analytics user property 'appearance' (SettingsTableViewController.swift:176-179).
- (platform parity) me-ios logs appAppearanceChanged and sets an appearance user property. me-android's appearance path (SettingsEntry.kt:162-165, RootHostActionsFactory.kt:240) logs no analytics event.
- (platform parity) me-ios pushes the appearance to Survicate (SettingsTableViewController.swift:180). me-android has no equivalent.
- (platform parity) me-android saves the appearance twice, in the DataStore-backed AppPreferencesRepository and in an 'appearance' SharedPreferences cache (AppearanceExtension.kt:8-23), and restores it in Application.onCreate (Application.kt:36-38). me-ios reads it back from CoreUtils in the Appearan…

_Note: referee could not confirm: vmm SettingsScreen.tsx:239-262 is cited as the backend persistence code. It actually covers toggleVibrationSetting, toggleHolidaysSetting and the start of toggleDarkModeOverride (252-263). The save-on-leave code is at SettingsScreen.tsx:101-107 and useSettingsPersistence.ts:81-95, and the PUT is at apiUserSetting.ts:103-107.; me-android: Application.kt:36-38 is labelled…_

### CAP-111: Turn vibration and the holiday theme on or off

**Fusion:** unique · **Personas:** manager · **Confidence:** High

Turn vibration on select on or off and, during the Christmas season, turn the holiday theme on or off. Both are saved to the backend user settings.

- **vmm** (Manager): screens: `SettingsScreen (SCREEN_NAME_SETTINGS = 'SettingsScreen')`; endpoints: `PUT /users/{userId}/settings`; storage: `redux settings.disableHolidaysTheme`, `AsyncStorage user_settings_backup (fallback)`; platform: `react-native` · evidence `src/screens/common/SettingsScreen/SettingsScreen.tsx:308-365`

**How they differ:**
- Caveat (vmm): the save happens only when the user leaves the Settings screen and something changed (saveSettingsIfDirty, useSettingsPersistence.ts). It is not saved on each toggle, and save errors are dropped silently.
- Caveat (vmm): isChristmasTime at utils.ts:631-636 always uses the current year's Dec 10 as the start date. So the holiday toggle is hidden from Jan 1 to Jan 15, although the season end is set to Jan 15.
- Caveat (vmm): the holiday label is disable-christmas, and 'on' means the theme is turned off (disableHolidaysTheme=true). The toggle works the opposite way to how the claim describes it.
- Employee (me-ios/me-android): no vibration or holiday-theme setting. The Android vibration at LockEntries.kt:147 is a fixed haptic for a wrong PIN, not a setting.

_Note: The holiday toggle appears only when isChristmasTime(). Both toggles are visible only when logged in._

### CAP-112: Control anonymous analytics collection

**Fusion:** unique · **Personas:** manager · **Confidence:** High

Turn anonymous usage data collection on or off in Privacy settings. The consent is applied to the analytics SDK, and a Remote Config flag decides whether Snowplow is used.

- **vmm** (Manager): screens: `SettingsPrivacyScreen (SCREEN_NAME_SETTINGS_PRIVACY = 'SettingsPrivacyScreen')`; events: `analytics_consent_toggled`, `analytics_collection_value_changed`; storage: `redux settings.analyticsCollection (default true)`, `redux settings useSnowplow`; platform: `react-native`, `Firebase Remote Config (REMOTE_CONFIG_USE_SNOWPLOW)` · evidence `src/screens/common/SettingsPrivacyScreen/SettingsPrivacyScreen.tsx:30-38,107-114; src/components/uiless/AnalyticsSettin…`

**How they differ:**
- Employee (me-ios) has no user consent toggle: AppDelegate.swift:150 and SceneDelegate.swift:157 call analyticsService.enableAnalyticsCollection() unconditionally at launch. The merged app needs a decision on whether the vmm Privacy toggle also applies to Employee users.
- me-ios FirebaseService.swift:42-48: enableAnalyticsCollection() and disableAnalyticsCollection() both set isAnalyticsCollectionEnabled = false, so Firebase collection is never actually enabled in Employee iOS. This is an internal behaviour, not a user-facing capability.
- me-android: no analytics consent setting found. ConsentDialog.kt is a generic confirmation dialog used in absence and expense screens, not analytics consent. Compared with me-ios, this is only a parity note, since neither twin offers a user toggle.

_Note: No Employee fragment reports an analytics consent toggle. That is a gap to decide for the merged app. The cleanup logs the inverted previous value, and the roles custom dimension is the sorted roles joined with '+'._

### CAP-113: Read the accessibility statement

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** High

Open and read the app's accessibility statement.

- **vmm** (Manager): screens: `SettingsPrivacyScreen`, `WebviewModal (SCREEN_NAME_WEBVIEW_MODAL)`, `LoginSelectScreen`, `SettingsScreen`; events: `clicked_on_accessibility_statement`; platform: `react-native`, `react-native-webview`, `Linking.openURL for W3C WAI links` · evidence `src/screens/common/SettingsPrivacyScreen/SettingsPrivacyScreen.tsx:69-100; src/components/modals/WebviewModal/WebviewMo…`
- **me-ios** (Employee): screens: `AccessibilityView`; events: `View accessibility button tapped (log)`; storage: `bundled accessibilities.md`; platform: `ios-native` · evidence `Employee/Information/Accessibility/AccessibilityViewModel.swift:19-21; Employee/Settings/SettingsTableViewController.sw…`
- **me-android** (Employee): screens: `AccessibilityStatementScreen`, `AccessibilityStatementKey`; storage: `res/xml/accessibility_statements.xml`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/about/accessibility_statement/AccessibilityStatementViewModel.kt:1-30; app/src/mai…`

**How they differ:**
- Content source: vmm shows localized HTML (EN/NO/SV, chosen by locale) in a sanitized WebView modal (WebviewModal.tsx:17-84, htmlConst.ts). me-ios uses bundled accessibilities.md (AccessibilityViewModel.swift:19-21). me-android uses res/xml/accessibility_statements.xml.
- Follow-up action: Employee lets the user go on to send feedback (S.Settings.sendFeedback on iOS; AppLeafEntries.kt:68-76 on Android). vmm offers only OK, and only W3C WAI links open externally.
- Entry points: vmm opens it from the login language picker and from Privacy settings, and the option can be hidden with hideAccessibilityStatement. Employee opens it from Settings.
- Analytics: vmm logs clicked_on_accessibility_statement. me-ios logs 'View accessibility button tapped'. No event is reported for me-android.
- Content source: vmm builds localized HTML (NO/SV/EN chosen by locale, SettingsPrivacyScreen.tsx and LangAccPicker.tsx:73-78) and shows it sanitized in a WebView modal (WebviewModal.tsx:44-76). Employee uses bundled content: me-ios reads accessibilities.md and renders it as markdown text (Accessibil…
- Follow-up action: Employee has a Send feedback button (me-ios AccessibilityView.swift:41-48 opens presentFeedbackController; me-android AccessibilityStatementScreen.kt:68-75 calls onOpenFeedback). vmm offers only OK or tapping the backdrop to close (WebviewModal.tsx:78-81), and it opens only https:…
- Entry points: vmm opens it from Privacy settings (navStatement) and from the language picker on LoginSelectScreen. The main SettingsScreen hides that picker option with hideAccessibilityStatement (SettingsScreen.tsx:293). Employee opens it from the Settings list (me-ios SettingsTableViewController.…
- Presentation: vmm shows a modal overlay with an empty title. Employee pushes a full screen titled with S.Settings.accessibilityStatement (SettingsTableViewController.swift:722).
- Analytics: vmm tracks CLICKED_ON_ACCESSIBILITY_STATEMENT with both trackEvent and trackEventNew. me-ios logs 'View accessibility button tapped' (SettingsTableViewController.swift:617). me-android logs no analytics event on this path (platform parity).
- Content format differs between the twins: markdown on iOS versus an XML statement list on Android (platform parity).

_Note: referee could not confirm: me-ios storage 'bundled accessibilities.md': the loader CoreUtils.readFile(fileName: "accessibilities.md") exists, but the file itself is not in legacy/me-ios. The screen code is real; only the content file is missing from the snapshot._

### CAP-114: Read the terms of service and privacy information

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** Medium

Read the user terms and data-usage summary, and follow links to the Visma trust centre, data-usage and privacy pages.

- **vmm** (Manager): screens: `SettingsTosScreen (SCREEN_NAME_SETTINGS_TOS = 'SettingsTosScreen')`, `SettingsPrivacyScreen`; endpoints: `GET https://www.visma.com/trust-centre/ (in-app browser)`, `GET https://visma.com/trust-centre/smb/transparency/usage-data (in-app browser)`, `GET https://www.visma.com/privacy/customer-feedback/ (in-app browser)`; events: `clicked_on_terms_of_service`, `clicked_on_read_more_about`; platform: `react-native`, `in-app browser (react-native-inappbrowser-reborn)` · evidence `src/screens/common/SettingsTosScreen/SettingsTosScreen.tsx:25-97; src/screens/common/SettingsPrivacyScreen/SettingsPriv…`
- **me-ios** (Employee): screens: `TermsOfServiceView`, `TermsOfServiceView / TermsOfServiceFeature`; events: `View terms of service button tapped (log)`; platform: `ios-native` · evidence `Employee/Information/TermsOfService/TermsOfServiceFeature.swift:9-19; Employee/Settings/SettingsTableViewController.swi…`
- **me-android** (Employee): screens: `TermsOfServiceScreen`, `TermsOfServiceKey`; platform: `android-native`, `external browser` · evidence `app/src/main/java/com/visma/employee/about/terms_of_service/TermsOfServiceScreen.kt:39-152; app/src/main/java/com/visma…`

**How they differ:**
- Link targets: vmm links to visma.com/trust-centre and trust-centre/smb/transparency/usage-data, plus the customer-feedback privacy page from Privacy settings (SettingsTosScreen.tsx:25-97, SettingsPrivacyScreen.tsx:69-100). me-ios links to visma.com/trust-centre and visma.com/website-privacy-stateme…
- Link opening: vmm opens links in an in-app browser (react-native-inappbrowser-reborn). me-android opens them in the external browser (TermsOfServiceScreen.kt:39-152). The iOS mechanism is not reported.
- Acceptance: vmm reuses this same screen to force acceptance (see 'Accept the terms of service before continuing'). Employee shows the terms as read-only.
- Analytics: vmm logs clicked_on_terms_of_service and clicked_on_read_more_about. me-ios logs 'View terms of service button tapped'. No event is reported for me-android.
- (platform parity) The Android terms screen has an error_unexpected string for failed link opens. Nothing equivalent is reported for iOS.
- Data-usage link: vmm opens https://visma.com/trust-centre/smb/transparency/usage-data (SettingsTosScreen.tsx:22). me-ios opens https://www.visma.com/website-privacy-statements (TermsOfServiceConstants.swift:5), and me-android opens the same URL (translations/src/main/res/values/strings.xml:211). Th…
- Acceptance: vmm shows an agree_terms PrimaryButton when mustAgreeToS is set. The button dispatches addToAgreed(username) (SettingsTosScreen.tsx:50-53, 77-87), and the screen blocks the Android hardware back button while acceptance is pending (lines 32-42). The Employee screens are read-only: TermsO…
- Analytics: vmm logs clicked_on_terms_of_service when the screen opens (SettingsPrivacyScreen.tsx:78-81) and clicked_on_read_more_about with a linkKey for each link tap (SettingsTosScreen.tsx:44-47). me-ios logs only 'View terms of service button tapped' when the screen opens (SettingsTableViewContr…
- Entry point: vmm reaches the terms screen from the Privacy settings screen, which also links to the customer-feedback privacy page (SettingsPrivacyScreen.tsx:78-100). Employee reaches it directly from a Settings row (SettingsTableViewController.swift:619-621; RootNavDisplay.kt:281). Employee has no…
- (platform parity) Link opening: me-ios opens links in an in-app SFSafariViewController through .openURLInApp() (TermsOfServiceView.swift:17; SafariViewControllerViewModifier.swift:51). me-android opens them in the external browser through Intent.ACTION_VIEW (RootHostFileActions.kt:47-55). vmm uses…
- (platform parity) Android shows an error_unexpected toast when a link fails to open (AppLeafEntries.kt:80-84), and its opener rejects URLs that are not https (RootHostFileActions.kt:49-52). iOS has no equivalent error handling.
- (platform parity) Analytics: me-ios logs 'View terms of service button tapped' (SettingsTableViewController.swift:620). me-android logs no equivalent event.

_Note: The Manager customer-feedback privacy page is merged in here because it is a privacy link. Medium confidence: it could instead become its own capability. referee could not confirm: The claim says the iOS link-opening mechanism is not reported. It is: iOS opens links in an in-app SFSafariViewController through .openURLInApp() (TermsOfServiceView.swift:17).; The cited me-ios evidence (SettingsTable…_

### CAP-115: View app version and open-source licenses

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** High

See the app version and build, and browse the third-party libraries and their licenses.

- **vmm** (Manager): screens: `SettingsLicensesScreen (SCREEN_NAME_SETTINGS_LICENSES = 'SettingsLicensesScreen…`; events: `clicked_on_licences`; platform: `react-native`, `in-app browser` · evidence `src/screens/common/SettingsLicensesScreen/SettingsLicensesScreen.tsx:14-42`
- **me-ios** (Employee): screens: `LicensesView`; events: `View licenses button tapped (log)`; platform: `ios-native` · evidence `Employee/Information/Licenses/LicensesViewModel.swift:13-78; Employee/Settings/SettingsTableViewController.swift:706-714`
- **me-android** (Employee): screens: `LicensesScreen`, `LicensesKey`; storage: `res/xml/licenses.xml`, `DataStorage.getLicensesList (bundled)`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/about/licenses/LicensesScreen.kt:34-55; app/src/main/java/com/visma/employee/about…`

**How they differ:**
- License display: vmm lists the libraries and opens each license page in an in-app browser (SettingsLicensesScreen.tsx:14-42). Employee shows bundled license text: licenses.txt plus Lucide and Google Maps on iOS (LicensesViewModel.swift:13-78), res/xml/licenses.xml on Android (DataStorageImpl.kt:14-…
- Version and copyright: Employee shows the Visma copyright and the app version/build on the licenses screen (S.copyrightVisma, S.build; copyright_visma, app_version_and_build_version). The vmm licenses fragment reports no version display.
- Analytics: vmm logs clicked_on_licences. me-ios logs 'View licenses button tapped'. No event is reported for me-android.
- How licenses are shown: vmm has a list of library names only, and tapping one opens the remote license URL (for example the GitHub LICENSE page) in an in-app browser (SettingsLicensesScreen.tsx:34, licenses.ts). Employee shows the full license text bundled in the app, so it works offline (LicensesV…
- Where the version is shown: vmm shows 'v{appVersion}' without a build number on SettingsScreen (SettingsScreen.tsx:431-432) and 'v{version} ({build})' on LoginSelectScreen (LoginSelectScreen.tsx:47-49, 202-204), but not on the licenses screen. Employee shows the Visma copyright and version (build)…
- Copyright notice: Employee shows a Visma copyright (S.copyrightVisma / copyright_visma). No copyright display was found in vmm's licenses flow.
- Where the entry point sits: vmm reaches licenses from the Privacy settings sub-screen (SettingsPrivacyScreen.tsx:127, 'info_licenses'). Employee reaches it from the main Settings screen (SettingsTableViewController.swift:614; SettingsScreen.kt:167).
- Analytics: vmm tracks clicked_on_licences through both trackEvent and trackEventNew (SettingsPrivacyScreen.tsx:90-92). me-ios logs 'View licenses button tapped' (SettingsTableViewController.swift:614).
- (platform parity) me-android sends no analytics event on the licenses click (RootNavDisplay.kt:279 only navigates), while me-ios logs one.
- (platform parity) The license sets differ: me-ios adds a hardcoded Lucide license and the Google Maps SDK license (GMSServices.openSourceLicenseInfo) to licenses.txt. me-android reads only res/xml/licenses.xml. me-android also turns URLs in the license text into tappable links (LicensesScreen.kt:89…
- (platform parity) Layout: me-ios shows the copyright and version as header text above one scrolling text view. me-android shows them as the first row of the license list.

_Note: referee could not confirm: me-ios evidence 'SettingsTableViewController.swift:706-714' is only the showLicensesView navigation. The 'View licenses button tapped' log call is at SettingsTableViewController.swift:614.; The claim implies vmm shows no version, but vmm does: SettingsScreen.tsx:431-432 and LoginSelectScreen.tsx:47-49, 202-204. It is just not on the licenses screen._

### CAP-116: See the signed-in account and device info in Settings

**Fusion:** unique · **Personas:** employee · **Confidence:** High

See the login e-mail, the OS version and the app version/build in an info block at the top of Settings.

- **me-android** (Employee): screens: `SettingsScreen`; storage: `AuthDataStorage lastLoggedInUserName`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/settings/presentation/components/InfoContainer.kt:36-49; app/src/main/java/com/vis…`

**How they differ:**
- (platform parity) me-android shows the login e-mail, OS version and app version at the top of Settings (InfoContainer.kt:36-49). No me-ios fragment reports this block: iOS shows the version only under App information/Licenses (SettingsTableViewController.swift:706-714).
- (platform parity) Both twins show e-mail, OS version and app version (build) as the first block of Settings: me-android at SettingsScreen.kt:92 with InfoContainer.kt:36-53, me-ios at SettingsViewModel.swift:80-83,123-129 with SettingsTableViewController.swift:524-529. The claim's statement that iOS…
- (platform parity) The e-mail comes from different places. me-android uses the stored last logged-in user name (AuthDataStorage lastLoggedInUserNameState, SettingsViewModel.kt:75). me-ios uses the current user's emailAddress from userService (SettingsViewModel.swift:110-112).
- (platform parity) Both twins copy the block to the clipboard on tap. me-ios then shows a 'copied' message (SettingsTableViewController.swift:638-647). me-android copies silently when the whole container is tapped (InfoContainer.kt:65-74); no confirmation was seen there.
- (platform parity) The OS line is built differently. me-ios shows system name plus version, e.g. 'iOS 17.4' (SettingsViewModel.swift:114-116). me-android formats deviceAndroidVersion through the settings_info_data_os_version_body string.

_Note: referee could not confirm: me-ios SettingsTableViewController.swift:706-714 is cited as proof that iOS shows the version only under App information/Licenses. It is showLicensesView. The real iOS info block is at SettingsViewModel.swift:123-129 and SettingsTableViewController.swift:524-529._

### CAP-117: Allow or block screenshots of the app

**Fusion:** unique · **Personas:** employee · **Confidence:** High

Turn screenshots and screen capture of app content on or off. The choice is stored as a preference and applied through the window secure flag.

- **me-android** (Employee): screens: `SettingsScreen`; storage: `AppPreferencesRepository screenshotsAllowed`, `SecurityService screenshotsAllowed`, `room-entity:app_preferences (screenshotsAllowed)`, `SCREENSHOTS_ALLOWED`; platform: `android-native`, `FLAG_SECURE refresh (refreshScreenSecurityFlags)` · evidence `app/src/main/java/com/visma/employee/navigation/RootHostActionsFactory.kt:242-245; app/src/main/java/com/visma/employee…`

**How they differ:**
- (platform parity) me-android has a screenshot toggle with FLAG_SECURE (RootHostActionsFactory.kt:242-245). No me-ios fragment reports an equivalent.
- (platform parity) me-android lets the user allow or block screenshots with a preference-backed FLAG_SECURE toggle (SettingsScreen.kt:133-145, RootHostActionsFactory.kt:242-245, BaseActivity.kt:100-107). No screenshot or screen-capture protection code exists in the me-ios Swift sources.
- (platform parity) On me-android, debug and testing builds skip the block: FLAG_SECURE is always cleared when mAppConfig.isTesting or isDebugBuild is set, whatever the user chose (BaseActivity.kt:102). The claim did not mention this.

### CAP-118: Update the app when a new version is suggested or required

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** Medium

At launch or after login the app checks a backend config. It then suggests or forces a store update, or tells the user to update the OS.

- **vmm** (Manager): screens: `OverlayDialog`, `UpdateDialog`; platform: `react-native`, `deep link out: market://details?id=<playStoreId> / itms-apps://itunes.apple.com…` · evidence `src/components/uiless/UpdateCheckWatcher/UpdateCheckWatcher.tsx:15-18; src/components/common/UpdateDialog/UpdateDialog.…`
- **me-ios** (Employee): screens: `AppUpdateView`, `AppUpdateCoordinator`; endpoints: `GET /employee/api/v1/remoteControl/config`; storage: `<bundleID>.remoteControl.configJSONString (Preferences)`, `<bundleID>.remoteControl.lastUpdatedDate (Preferences)`, `<bundleID>.remoteControl.lastUpdatedVersion (Preferences)`; platform: `ios-native`, `opens App Store URL https://apps.apple.com/app/id9190****` · evidence `Modules/RemoteControl/Sources/RemoteControl/UI/AppUpdateCoordinator.swift:33-53`
- **me-android** (Employee): screens: `StartupGateContent`, `HomeScreen (UpdateHighlight card)`, `MainActivity startup gate`; endpoints: `GET api/v1/RemoteControl/Config`, `GET /api/v1/RemoteControl/Config`; storage: `HighlightDismissalRepository key HIGHLIGHT_KEY_PREFIX+message.hashCode per user`; platform: `android-native`, `Play Store intent`, `splash screen` · evidence `app/src/main/java/com/visma/employee/home/MainActivity.kt:337-398; absence/src/main/java/com/visma/employee/absence/dat…`

**How they differ:**
- Endpoint: vmm uses an RTK Query call to the backend keys endpoint (UpdateCheckWatcher.tsx:13-18; GET /keys also appears in dev tools). me-ios uses GET /employee/api/v1/remoteControl/config. me-android uses GET api/v1/RemoteControl/Config.
- Update levels: Employee has suggestUpdate, forceUpdate and suggestOSUpdate (AppUpdateCoordinator.swift:33-53; ImportantInfoServiceImpl.kt:37-70). vmm only shows an overlay 'update needed' dialog, and no forced or OS-update level is reported.
- Timing: vmm checks after login (UpdateCheckWatcher.tsx:15-18). Employee checks at launch.
- Dead code: vmm UpdateDialog, which opens the store with market:// or itms-apps://, has no caller (UpdateDialog.tsx:20-45). The dialog that actually shows is OverlayDialog.
- (platform parity) me-ios caches the config for 24h and re-fetches it when the version changes, keeping the cached copy on error. me-android times out after 5s and has no reported cache.
- (platform parity) me-android shows a suggested update as a dismissible home UpdateHighlight card, with the dismissal keyed by message hash per user. me-ios shows AppUpdateView with Cancel.
- (platform parity) Precedence: me-android applies suggestOSUpdate > forceUpdate > suggestUpdate. me-ios hides Cancel for a forced update and hides the App Store button for an OS update.
- Endpoint: vmm reads feature_app_update_values from the authenticated GET keys endpoint, /api/keys (queryEndpointsKeys.ts:86, useUpdateCheck.ts:28-29). me-ios uses GET <employeeApiV1>/remoteControl/config (GetRemoteControlConfig.swift:16). me-android uses GET api/v1/RemoteControl/Config (ImportantIn…
- Who decides: vmm compares versions on the device. It checks for a major or minor mismatch against latestAppVersion (utils.ts:594-608). Employee takes the server's booleans suggestUpdate, forceUpdate and suggestOSUpdate as they are (EmployeeRemoteControlService.swift:67-72; ImportantInfoServiceImpl.…
- Update levels: vmm has only a dismissible suggestion, with Update and Dismiss buttons (UpdateDialog.tsx:33-43). It has no forced update and no OS-update prompt. Employee has suggest, force and OS-update levels.
- OS too old: vmm stays silent when the OS is below minSupportedAndroidApiLevel or minSupportedIosVersion, because isOsSupported gates the prompt off (utils.ts:577-587, 606-608). Employee tells the user to update the OS (AppUpdateView.swift:45-46; MainActivity.kt:358-362).
- Message text: vmm shows local strings new_app_update_available_android and new_app_update_available_ios (useUpdateCheck.ts:42). Employee shows the message the server sends (data.message).
- Re-show throttle: vmm stores the next allowed date in AsyncStorage (UPDATE_APP_NOTIFICATION_DATE) and re-prompts only after the reshowAfter period (utils.ts:559-575). me-ios caches the server config for 24h and asks again on each launch while an update is available. me-android dismisses per message…
- Timing: vmm checks only for logged-in users, 750ms after the settings query resolves (useUpdateCheck.ts:26-28, 48). Employee checks at launch, before the main app: iOS after refreshAccounts (MainCoordinator.swift:70-80), Android in the splash routing, before login routing.
- Correction to the claim: vmm UpdateDialog is not dead code. App.tsx:142-149 renders it with visible={dialogVisible.type === STATE_COMPLETE}, and useUpdateCheck sets that state.
- (platform parity) me-ios caches the config in Preferences for 86400s, re-fetches it when the app version changes, and keeps the cached config on error (EmployeeRemoteControlService.swift:32-33, 56-80). me-android uses withTimeoutOrNull(5_000) and has no cache (MainActivity.kt:347-349).
- (platform parity) OS update: me-android shows a blocking gate whose only button, Close, calls finish() and exits the app (MainActivity.kt:358-362). me-ios shows Open Settings plus Cancel unless the update is also forced (AppUpdateView.swift:45-62).
- (platform parity) Forced update: me-android shows a blocking StartupGate with the Play Store button. me-ios shows AppUpdateView with Cancel hidden.
- (platform parity) Suggested update: me-android shows no startup prompt, only a dismissible home UpdateHighlight card with key UPDATE_CARD_+message.hashCode (UpdateHighlightHidingService.kt:17,30). me-ios shows the full-screen AppUpdateView with Cancel at launch.
- (platform parity) Precedence: me-android checks suggestOSUpdate, then forceUpdate, then suggestUpdate (ImportantInfoServiceImpl.kt:45-54). me-ios can combine the flags, for example forced plus OS update.

_Note: Medium confidence because the vmm keys endpoint was not resolved and the vmm UpdateDialog appears unused. referee could not confirm: vmm 'UpdateDialog has no caller / dead code (UpdateDialog.tsx:20-45)': false. App.tsx:142 renders UpdateDialog.; me-android endpoint 'GET /api/v1/RemoteControl/Config' with a leading slash: only 'api/v1/RemoteControl/Config' exists (ImportantInfoServiceImpl.kt:77).…_

### CAP-119: Keep app state after restarting or updating the app

**Fusion:** shared-diverged · **Personas:** manager · **Confidence:** Medium

Settings, login, terms, surveys, HRM, Autopay, OneStop, recent approval searches, Gaia chats and What's New state survive restarts in encrypted storage. State from the old storage format is imported once.

- **vmm** (Manager): events: `FAILED_TO_IMPORT_LEGACY_PERSISTED_SLICE (APP_EVENTS)`; storage: `mmkv:redux-state (AES-256)`, `mmkv:persist.version`, `mmkv:persist.importAttempts`, `mmkv:persist.<slice>`, `asyncstorage:persist:root (legacy, removed after import)`, `keychain encryption key (legacy, cleared after import)`; platform: `react-native`, `encrypted MMKV`, `keychain` · evidence `src/configs/reduxState.ts:107-127`

**How they differ:**
- Storage engine: vmm keeps redux slices in AES-256 encrypted MMKV 'redux-state' (persistEngine.ts:72-74). me-ios uses a KeychainAccess-backed SecureDataStorage (StorageService.swift:26-33). me-android uses an encrypted Room UserDatabase (DataStoreToRoomMigration.kt:8-12).
- Legacy import: vmm imports the AsyncStorage 'persist:root' blob and replays redux migrations 1-35 (legacyPersistImport.ts:18,150). me-android copies DataStore preferences into Room (DataStoreToRoomMigration.kt:24-36). me-ios exposes a SecureStorage.migrate(to:) (StorageService.swift:22).
- Retry policy: vmm retries a failed legacy import on at most 3 launches, tracked by persist.importAttempts (persistEngine.ts:61-62, reduxState.ts:206-225). me-android sets MIGRATION_DONE_KEY only on success, so a failed migration is retried on every launch with no cap and is only logged (DataStoreTo…
- Failure telemetry: vmm tracks FAILED_TO_IMPORT_LEGACY_PERSISTED_SLICE (legacyPersistImport.ts:27-28). me-android only calls Log.e (DataStoreToRoomMigration.kt:34).
- Reinstall behaviour: me-ios erases its keychain storage on first install (StorageService.swift:32, eraseOnFirstInstall). vmm clears the legacy keychain key only after a successful import (legacyPersistImport.ts:184).
- Data kept: vmm persists Manager-only slices (approval, autopay, OSR/OneStop, HRM, Gaia chats and runs, What's New). The Employee apps keep app and user preferences and highlight dismissals (DataStoreToRoomMigration.kt:10-12).
- (platform parity) me-ios keeps its state in the Keychain through SecureDataStorage. me-android runs a one-time DataStore-to-Room migration into an encrypted Room database. The storage models and migration paths differ between the twins.

_Note: This is infrastructure rather than a user action. Persist version 38. The legacy import retries on up to 3 launches._

### CAP-120: Use internal developer tools and feature flags

**Fusion:** shared-diverged · **Personas:** developer, internal tester · **Confidence:** Medium

In stage or test builds, internal users toggle feature flags and use debugging tools such as push device management, test notifications, forced crashes or PIN, and survey reset.

- **vmm** (Manager): screens: `SettingsDevToolsScreen (SCREEN_NAME_SETTINGS_DEV_TOOLS = 'SettingsDevToolsScree…`, `TriggerNotificationModal`, `SettingsScreen`; endpoints: `GET /keys`, `POST /Devices`, `DELETE /Devices/{deviceToken}`, `GET /Devices/all`, `DELETE /Devices/all`, `PUT /users/{userId}/reminders`, `GET approval/rest/my-tasks`; events: `get_all_devices_error`, `delete_all_devices_error`; platform: `react-native`, `local notifications via notifee (trigger + action buttons)`, `native Android debugRenderPushNotification`, `clipboard` · evidence `src/screens/common/SettingsDevToolsScreen/SettingsDevToolsScreen.tsx:205-745`
- **me-ios** (Employee): screens: `FeaturesView`, `DeveloperToolsView`, `Settings > Feature flags`; storage: `@Shared developerForcePincode`, `UserDefaults com.visma.vme.featurekit.feature_clientErrorLogging`, `UserDefaults com.visma.vme.featurekit.feature_sendForApprovalRollbackToDraft`; platform: `ios-native` · evidence `Employee/Settings/SettingsTableViewController.swift:624-637; Modules/FeatureKit/Sources/FeatureKit/UI/View/FeaturesView…`

**How they differ:**
- Access: vmm is available on stage or for usernames on a backend whitelist, and opens after tapping the version more than 6 times within 3s (SettingsDevToolsScreen.tsx:205-745). me-ios shows it only when AppDistribution.current != .appstore or developmentDistribution is set (SettingsTableViewControl…
- Tools: vmm manages push devices (POST/DELETE /Devices, GET/DELETE /Devices/all), fires test notifications, schedules a test reminder with PUT /users/{userId}/reminders, copies tokens, and forces crashes or a state purge. me-ios toggles LaunchDarkly flags, resets Survicate and forces PIN instead of…
- Flag source: me-ios overrides LaunchDarkly flags stored in UserDefaults (FeaturesView.swift:15-48). The source of vmm feature flags is not stated.
- (platform parity) No me-android fragment reports a feature-flag screen. The only Android internal tool reported is the backend environment switch.
- Access: vmm gives access on stage, or when the username matches a backend dev_tools_whitelist (case-insensitive, fails closed). Access comes from GET /api/keys through useGetAppSettingsQuery (useDevToolsAccess.ts). The screen opens after 7 taps on the build number within 3s (SettingsScreen.tsx:140-…
- Flag source: vmm flags are local Redux state (state.features.* and toggleStartPageDevFlag, SettingsDevToolsScreen.tsx:169-195, 304) with no LaunchDarkly. me-ios overrides LaunchDarkly values, persists them in UserDefaults and has a Reset back to the LaunchDarkly values (FeaturesView.swift:15-48).
- Tools: vmm has push device register and unregister (POST and DELETE /Devices, apiApproval.ts:322-366), list and delete all devices (GET and DELETE /Devices/all, apiApproval.ts:387-400), local test notifications through notifee, a test reminder through PUT users/{userId}/reminders (apiReminder.ts:19…
- Scope: vmm's flag list covers many app features (Gaia, Bnxt, Seatable, Survicate, autopay tab, employee calendar and others). me-ios lists the features defined in FeatureKit.
- (platform parity) me-android: I found no feature-flag override or developer tools screen in its Kotlin sources. The iOS FeaturesView and DeveloperToolsView have no Android counterpart.

_Note: referee could not confirm: vmm access tap count: the claim says more than 6 taps. The code in SettingsScreen.tsx:150-156 opens the screen on the 7th tap within 3s. This matches in effect, but the gesture lives in SettingsScreen.tsx, not in SettingsDevToolsScreen.tsx:205-745.; vmm GET /keys: the call comes from queryApi.ts:285 (GET /api/keys, app settings for the whitelist) through useDevToolsAcce…_

### CAP-121: Switch backend environment in test builds

**Fusion:** shared-diverged · **Personas:** internal tester · **Confidence:** High

In test builds a tester picks which backend environment (API and Connect URLs) the app talks to. Production builds always use production.

- **me-android** (Employee): storage: `AppPreferences: environment (JSON EnvironmentDescription)`, `res/xml/environments.xml`; platform: `android-native` · evidence `core/src/main/java/com/visma/employee/core/environments/LocallyStoredEnvironmentsRepository.kt:22-63`

**How they differ:**
- (platform parity) No me-ios fragment reports an environment switch.
- Product scope: vmm (Manager) has an environment switch in EnvPicker.tsx:14-90 (production/staging/sandbox, envChange action), placed on LoginSelectScreen.tsx:186. The Employee product has LocallyStoredEnvironmentsRepository.kt on Android and SelectAccountFeature.swift on iOS. So it is shared across…
- Build gating: me-android turns the switch off in production builds with R.bool.env_selector_enabled (false in app/src/main/res/values/app_config.xml:4, true in debug, debugMinified and stable) and forces Production (LocallyStoredEnvironmentsRepository.kt:32-34). vmm has no build gate: the picker is…
- Environment list: vmm offers production, staging and sandbox (constants.ts:2-4; EnvPicker.tsx:23-28). me-ios offers Staging and Production (AppConstants.swift:43-46; Localhost only under UI-Testing-Mocked, CoreUtils.swift:115). me-android reads its list from res/xml/environments.xml.
- Switch-back path: vmm also shows a Settings item on stage or sandbox that asks for confirmation, returns to production and logs the manager out (SettingsScreen.tsx:223-236, 337-353). The Employee apps only switch from the login or account-select screen.
- (platform parity) me-ios wipes state when switching: it clears third-party keys, removes all users and context, resets OAuth and updates the API config (EnvironmentManager.live.swift:29-43). me-android only saves the choice and recreates the host (LocallyStoredEnvironmentsRepository.kt:60-63; RootH…
- (platform parity) me-android shows a visible selector with the current short code (environmentSelectorText, RootHostActionsFactory.kt:178-179). me-ios hides it behind an invisible tap-5-times area in the bottom corner (SelectAccountView.swift:44-49, 110-111).
- (platform parity) The claim's line 'No me-ios fragment reports an environment switch' is false: me-ios has CoreUtils.getCurrentEnvironment/setCurrentEnvironment stored in UserDefaults (CoreUtils.swift:110-122).

_Note: referee could not confirm: storage 'res/xml/environments.xml': no environments.xml file was found under legacy/me-android (the code refers to R.xml.environments at LocallyStoredEnvironmentsRepository.kt:43, but the resource is not in the checkout); divergence line '(platform parity) No me-ios fragment reports an environment switch' is contradicted by me-ios/Employee/Accounts/Utils/EnvironmentMana…_

## Help and feedback

Info and help sheets, FAQ, sending feedback, app rating and NPS, surveys, user-testing recruitment, error logs

### CAP-095: Read how-to help for the current screen

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager taps the info icon in a screen header (approval list, document editor, Autopay, OneStop Reporting, employee list/details, settings) and reads an info sheet with a title, description and icon bullet points explaining how that screen works.

- **vmm** (Manager): screens: `InfoModal (SCREEN_NAME_INFO_MODAL)`, `OsrHeaderRight`, `NavButtonInfo`, `SCREEN_NAME_SETTINGS`; events: `approval_opened_info_modal`, `approval_document_editor_opened_info_modal`, `autopay_opened_info_modal`, `osr_opened_info_modal`, `hrm_details_opened_info_modal`, `hrm_employee_list_opened_info_modal`, `settings_opened_info_modal`; storage: `redux autopay.activeTab`; platform: `react-native` · evidence `src/components/modals/InfoModal/InfoModal.tsx:19-45; src/components/approval/ApprovalHeaderRight/ApprovalHeaderRight.ts…`

_Note: Autopay content depends on the active tab (history vs approval). Titles 'OneStop' and Autopay titles are hard-coded English, not translated. Settings info modal is pushed in the current tab stack when known, otherwise on root. referee could not confirm: screens lists OsrHeaderRight and NavButtonInfo, which are header button components, not screens (src/components/osr/OsrHeaderRight/OsrHeaderRight…_

### CAP-096: Browse help (FAQ) by topic

**Fusion:** unique · **Personas:** employee · **Confidence:** High

An employee opens Help/FAQ (from Settings, a payslip route, or a disabled/placeholder start-page card) and picks a topic (Payslips, Expense, Time & Absence, My Profile, Other) to see which of their companies have that module and read answers to frequent questions.

- **me-ios** (Employee): screens: `FAQNavigationView`, `FAQListView`, `FAQDetailView`, `FAQPushHostingController`, `SettingsTableViewController (FAQ row)`, `FAQCoordinator`, `FAQDetailCoordinator (payslip role)`, `PresentFAQCoordinator`; events: `openFAQv2`, `openFAQv2Detail`, `openFAQv2Question`, `openHighlight`; platform: `ios-native` · evidence `Employee/Information/FAQv2/ViewModels/FAQDetailViewModel.swift:69-188; Employee/Settings/SettingsTableViewController.sw…`
- **me-android** (Employee): screens: `SettingsScreen`, `FaqScreen`, `FaqContextScreen`, `FaqKey`, `FaqContextKey`; events: `FAQ - FAQ opened`, `FAQ - specific FAQ opened`, `FAQ - sub category opened per category`; platform: `android-native`, `in-app deep entry with a preselected FAQ topic (PreselectedFaqContext)` · evidence `faq/src/main/java/com/visma/employee/navigation/entries/FaqEntries.kt:43-186; app/src/main/java/com/visma/employee/navi…`

**How they differ:**
- (platform parity) iOS opens the FAQ from disabled/placeholder start-page cards (FeatureDisabledCardDetailsProvider.swift:36-39); no Android fragment reports a home-card entry, Android instead reports a preselected-topic deep entry (FaqEntries.kt PreselectedFaqContext).
- (platform parity) iOS removes two 'Other' questions for Dottie users (FAQDetailViewModel.swift); Android shows the My Profile section only with Dottie HR permission and uses faq_other_description_dottie (FaqEntries.kt, RootNavDisplay.kt:271-285).
- (platform parity) Android drops Absence when both Absence and Time are empty and removes the license question when every company has the module (FaqEntries.kt:43-186); iOS picks the question set by all/some/none contexts having the permission.
- (platform parity) iOS opens the FAQ from disabled start-page cards (FeatureDisabledCardDetailsProvider.swift:36-39, PresentFAQCoordinator). No Android home-card entry was found. Android instead has a preselected-topic deep entry (FaqKey(preselectedContext), used from SalaryFeedScreen.kt:325 for PAY…
- (platform parity) Dottie handling: iOS drops two Other questions for Dottie users (filteredOtherFAQ in FAQDetailViewModel.swift). Android shows the My Profile topic only when showMyProfileSection() is true and passes isDottieAccessible to QuestionsProvider (FaqEntries.kt:52, 173-176).
- Correction: both platforms drop Absence when neither Absence nor Time has any company (iOS correctCalendarFeatureRows at FAQDetailViewModel.swift:80-89; Android FaqContextViewModel.kt:186-190). This is not a parity gap, and the claim cited the wrong Android file.
- (platform parity) Android's FAQ list includes a Send feedback entry (FaqSendFeedbackKey, FaqEntries.kt:103-105 and 158-160). This check did not confirm an equivalent inside the iOS FAQ list, and it may belong to a separate feedback capability.

_Note: referee could not confirm: The Android rule that drops Absence when Absence and Time are both empty is cited to FaqEntries.kt:43-186. It is actually in faq/src/main/java/com/visma/employee/faq/faq_context/presentation/FaqContextViewModel.kt:186-190.; RootNavDisplay.kt:271-285 contains the Settings callbacks (onFaqClicked -> FaqKey()), not the Dottie or My Profile logic. The FAQ callbacks are at l…_

### CAP-097: Check why a module is not available for my company

**Fusion:** unique · **Personas:** employee · **Confidence:** Medium

In a help topic, the app looks up the license of each company that lacks the module and explains whether it was never activated, is activated, or was terminated/deactivated.

- **me-ios** (Employee): screens: `FAQDetailView`; endpoints: `GET /employee/api/v1/org/{orgId}/license/{featureId}`; platform: `ios-native` · evidence `Employee/Information/FAQv2/ViewModels/FAQDetailViewModel.swift:69-188`
- **me-android** (Employee): screens: `FaqContextScreen`; endpoints: `GET /api/v1/org/{orgId}/license/{featureId}`; platform: `android-native` · evidence `faq/src/main/java/com/visma/employee/faq/faq_context/presentation/FaqContextViewModel.kt:58-134`

**How they differ:**
- (platform parity) Android shows '<org> - failed to load' per company when the license call fails (FaqContextViewModel.kt:58-134); iOS fragment does not report per-company error handling.
- (platform parity) Both twins handle a failed licence call per company, in different ways. Android appends '<org> - Failed to load' (default_failed_to_load_error_message, FaqContextViewModel.kt, Status.ERROR branch). iOS sets the status to .unknown in its catch (FAQDetailViewModel.swift:308) and sho…
- (platform parity) When the response has no status, iOS falls back to terminated (FAQDetailViewModel.swift:306, `companyLicense.status ?? LicenseStatus.terminated`). Android has an `else -> ""` branch that shows nothing for an unrecognised status (FaqContextViewModel.kt, prepareLicenseQuestion).
- (platform parity) iOS re-runs getQuestionsAndAnswers, and so the licence lookup, when the network comes back (FAQDetailViewModel.swift:326-331, onReachabilityStatusChange). No matching reachability retry was seen in FaqContextViewModel.kt:58-134.
- (platform parity) iOS reassigns `companies` on each pass of the permission loop (FAQDetailViewModel.swift:230-232). When there are several permissions (calendar = absence + time), only the last permission's companies are explained. Android builds one request per licence-request context and combines…
- (platform parity) The endpoint paths differ only by base prefix. iOS uses APIConstants.URL.employeeApiV1 + /org/{orgId}/license/{featureId}. Android uses the relative path api/v1/org/{orgId}/license/{featureId}. It is probably the same backend route.

_Note: iOS evidence comes from the FAQ fragment (289), which reports license reasons fetched when access is missing; could alternatively be kept inside the FAQ capability. referee could not confirm: The claim's divergence line says the iOS fragment reports no per-company error handling. That is wrong: FAQDetailViewModel.swift:302-310 catches the failure and maps it to .unknown, which shows an error answ…_

### CAP-098: Send feedback about the app

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** High

A user writes a free-text message and sends it to Visma together with device and app version details, then sees a sent/failed confirmation.

- **vmm** (Manager): screens: `FeedbackScreen (SCREEN_NAME_FEEDBACK)`, `SettingsScreen`; endpoints: `POST {ME_BASE_URL}employee/api/v1/feedback`; events: `failed_send_feedback`, `closed_in_app_feedback`, `sent_feedback`, `clicked_on_leave_feedback`; platform: `react-native`, `react-native-device-info` · evidence `src/screens/FeedbackScreen/FeedbackScreen.tsx:57-94; src/screens/common/SettingsScreen/SettingsScreen.tsx:210-214,369-3…`
- **me-ios** (Employee): screens: `FeedbackView`, `FeedbackFeature`, `PostScreenViewController`; endpoints: `POST /employee/api/v1/feedback`; events: `feedbackSent`; platform: `ios-native` · evidence `Employee/Information/Feedback/FeedbackFeature.swift:68-111; Employee/Settings/SettingsTableViewController.swift:740-768…`
- **me-android** (Employee): screens: `FaqSendFeedbackScreen`, `FaqSendFeedbackKey`, `AccessibilityStatementScreen (onOpenFeedback)`; endpoints: `POST /api/v1/feedback`; events: `FAQ - feedback sent`; storage: `AuthDataStorage.lastLoggedInUserNameState (shown as sender)`; platform: `android-native` · evidence `faq/src/main/java/com/visma/employee/faq/FaqSendFeedbackViewModel.kt:54-77; app/src/main/java/com/visma/employee/feedba…`

**How they differ:**
- Payload: Manager sends OS, app version, phone model, integration and user roles (AutoPay/Approval/Employee/OSR) (FeedbackScreen.tsx:57-94); Employee sends only {message, osType, osVersion, appVersion} (FeedbackFeature.swift:68-111, FeedbackServiceImpl.kt:33-48).
- Entry points: Manager from Settings, Start hub and the app-rate dialog (FeedbackScreen.tsx, SettingsScreen.tsx:210-214); Employee from FAQ/Help, Settings and the accessibility statement (FeedbackFeature.swift, SettingsTableViewController.swift:740-768, FaqSendFeedbackViewModel.kt).
- Manager asks to confirm discarding a draft (cancel_question, feedback_discard_draft) and no-ops in sandbox; no discard confirmation is reported for Employee.
- Manager 'sent_feedback' analytics event fires on discard-confirm, not on send (FeedbackScreen.tsx:131-136, suspected bug); Employee logs feedbackSent / 'FAQ - feedback sent' on send.
- (platform parity) iOS shows a separate confirmation screen (PostScreenViewController.swift:150-165) and distinct no-internet vs server-error alerts; Android shows success/failure dialogs and clears the field after success (FaqSendFeedbackViewModel.kt:54-77).
- (platform parity) iOS formats appVersion as 'vX (Build N)'; Android sends BuildConfig.VERSION_NAME.
- Payload: Manager sends PascalCase {OsVersion, OsType, AppVersion, PhoneModel, Integration:'Connect', FeedbackContext:'Settings', Roles[AutoPay/Approval/Employee/OSR], Message} (FeedbackScreen.tsx:57-67). Employee sends only {message, osType, osVersion, appVersion} (FeedbackForm.swift, FeedbackServi…
- Manager hardcodes FeedbackContext 'Settings' even when the screen is opened from StartHub (StartHub.tsx:732) or the app-rate dialog (AppRateDialog.tsx:139), so the backend cannot tell entry points apart (FeedbackScreen.tsx:65).
- Entry points: Manager opens from Settings (SettingsScreen.tsx:210-214), StartHub (StartHub.tsx:732) and AppRateDialog (AppRateDialog.tsx:139). Employee iOS opens only from Settings (SettingsTableViewController.swift:720,740). Employee Android opens from FAQ (FaqEntries.kt:103,163) and the accessibi…
- Manager asks for confirmation before discarding a non-empty draft (cancel_question / feedback_discard_draft, FeedbackScreen.tsx:86-93,121-137). Employee has no discard confirmation.
- Manager treats sandbox as a no-op success because sandbox has no ME backend (apiEmployee.ts:22-25). Employee has no sandbox mode.
- Manager fires the 'sent_feedback' analytics event on discard-confirm, not on send (FeedbackScreen.tsx:131-133, likely a bug). Employee logs feedbackSent (FeedbackFeature.swift:92-94) or FAQ_FEEDBACK_SENT (FaqSendFeedbackViewModel.kt:63) on success.
- Confirmation: Manager shows a toast and goes back (FeedbackScreen.tsx:72-74). Employee iOS opens a post-screen sheet (FeedbackView.swift:66-67). Employee Android shows success or failure dialogs.
- Employee shows the sender's username (FeedbackFeature State.make(username:) at SettingsTableViewController.swift:749-751; AuthDataStorage.lastLoggedInUserNameState at FaqSendFeedbackViewModel.kt:48). Manager does not show the sender.
- (platform parity) iOS shows separate no-internet and server-error alerts (FeedbackFeature.swift:97-111). Android shows one generic failure dialog (FaqSendFeedbackViewModel.kt:67-69).
- (platform parity) iOS formats appVersion as 'vX (Build N)' (FeedbackFeature.swift:81). Android sends BuildConfig.VERSION_NAME (FeedbackServiceImpl.kt:45).
- (platform parity) Entry points differ: iOS opens feedback only from Settings; Android opens it from FAQ and the accessibility statement.

_Note: referee could not confirm: me-ios PostScreenViewController.swift:150-165: this UIKit PostScreenType.feedback path is not what the feedback flow uses; FeedbackView.swift:66-67 presents a SwiftUI PostScreenView sheet.; me-ios FAQ/Help entry point: no caller found; FeedbackFeature and FeedbackView are only presented from SettingsTableViewController.swift:720,740.; vmm sandbox no-op is in src/service…_

### CAP-099: Send feedback about Business NXT line editing

**Fusion:** unique · **Personas:** approver · **Confidence:** High

An approver writes and sends free-text feedback specifically about the Business NXT line-editing experience, with a discard confirmation when cancelling a draft.

- **vmm** (Manager): screens: `ApprovalTaskBXNLineEditFeedbackScreen`; endpoints: `POST {ME_BASE_URL}/employee/api/v1/feedback`; events: `failed_send_feedback`, `closed_in_app_feedback`, `sent_feedback`; storage: `redux loginManager.hasAccessAutopay/hasAccessApproval/hasAccessHRM/hasOSRAccess`; platform: `react-native`, `react-native-device-info (OS version, brand, model)` · evidence `src/screens/manager/ApprovalTaskBXNLineEditFeedbackScreen/ApprovalTaskBXNLineEditFeedbackScreen.tsx:23-140`

_Note: Same endpoint as general feedback, with context 'BNXT' and Integration 'Connect'. sent_feedback fires on discard-confirm (line 128)._

### CAP-100: Rate the app in the store

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** High

After enough qualifying actions the user is asked to rate the app in the App Store / Google Play.

- **vmm** (Manager): screens: `ApprovalScreen (AppRateDialog)`, `FeedbackScreen`; events: `AppRate`, `app_rate`; storage: `appRate (persisted: dismissed, completed, tasksHandled, tasksHandledAfterDismis…`; platform: `react-native`, `external store link market://details?id=com.visma.vmm`, `itms-apps://itunes.apple.com/us/app/apple-store/850373588` · evidence `src/components/approval/AppRateDialog/AppRateDialog.tsx:40-170`
- **me-ios** (Employee): screens: `SKStoreReviewController prompt`; storage: `UserPreferences payslipReviewWorthyActionCount`, `last version prompted for review`, `last time prompted for review`; platform: `ios-native`, `StoreKit review prompt` · evidence `Employee/Services/AppRatingService.swift:48-83; Employee/Payslips/Service/AppRatingService.RatingService.swift:11-18`
- **me-android** (Employee): storage: `Room UserPreferenceDbModel.app_review_threshold`, `app_review_shown_timestamp`, `app_review_shown_version`; platform: `android-native`, `Google Play In-App Review API` · evidence `app/src/main/java/com/visma/employee/core/analytics/AppReviewManagerImpl.kt:40-105; core/src/main/java/com/visma/employ…`

**How they differ:**
- Trigger: Manager counts handled approval tasks against remote thresholds (remoteShowCondition / remoteReshowCondition, remoteEnabledUntil) (AppRateDialog.tsx:40-170); Employee triggers on viewing a payslip (AppRatingService.RatingService.swift:11-18, RootHostActionsFactory.kt:78-81 view_payslip).
- Flow: Manager first asks 'enjoying the app?' and routes 'not really' to the in-app feedback screen or 'yes' to an external store link; Employee shows the native OS review prompt directly (SKStoreReviewController, Google Play In-App Review).
- Remote control: Manager is remotely enabled with an end date; Employee reports no remote switch, only local thresholds.
- (platform parity) Cool-down differs: iOS 30 days since last prompt and a different build (AppRatingService.swift:48-83); Android 90 days (7776000000 ms) and a higher version (AppReviewManagerImpl.kt:40-105).
- Trigger: Manager counts handled approval tasks against remote thresholds (default 5, remoteShowCondition / remoteReshowCondition; AppRateDialog.tsx:62-66, appRateReducer.ts:32,43-49). Employee prompts after 1 payslip view (AppRatingService.swift:39 ratingActionThreshold=1; AppReviewManagerImpl.kt:3…
- Flow: Manager shows a 3-step in-app dialog: 'enjoying?', then either feedback (FeedbackScreen) or 'mind rating?', which opens an external store URL (AppRateDialog.tsx:75-160). Employee calls the native OS review sheet straight away (SKStoreReviewController.requestReview at AppRatingService.swift:63…
- Remote control: Manager is gated by remoteEnabled and remoteEnabledUntil from remote config (appRate.ts:34, AppRateDialog.tsx:55-68). Employee has no remote switch; its gating is local only.
- Re-show and cool-down: Manager has no time cool-down. After a dismiss it waits for a separate reshow count, and once completed it never shows again (show = !completed && ...). Employee is limited by time and app version.
- Dismiss: Manager has an explicit (x) dismiss that is tracked and resets the reshow counter (AppRateDialog.tsx:114-117, appRateReducer.ts:59). Employee has no app-level dismiss; the OS controls whether the sheet appears.
- Analytics: Manager logs each step through trackEvent('AppRate') and trackEventNew(app_rate) (AppRateDialog.tsx:171-187). The cited Employee code logs no rating events.
- (platform parity) Cool-down: iOS waits 30 days (AppRatingService.swift:40,82); Android waits 90 days (AppReviewManagerImpl.kt:105, 7776000000 ms).
- (platform parity) Version gate: iOS needs a build number that differs from the last prompted one (AppRatingService.swift:80); Android needs a VERSION_NAME strictly higher than the last shown one (AppReviewManagerImpl.kt:99-102).
- (platform parity) Counter handling: Android resets the threshold to 0 after the prompt and stores its values per user email (AppReviewManagerImpl.kt:26-27,71-76). iOS caps the count at the threshold, never resets it, and does not key it by user (AppRatingService.swift:49-52).

### CAP-101: Answer an NPS satisfaction survey

**Fusion:** shared-diverged · **Personas:** manager, employee · **Confidence:** Medium

An eligible user is shown a 0-10 likelihood-to-recommend survey inside the app and can add a comment and send it.

- **vmm** (Manager): screens: `NpsDialog (embedded in ApprovalList)`, `NpsComment`; endpoints: `GET {apiBase}survey/user/Info`, `POST {apiBase}survey/user/response`; events: `triggered_initializeWootric`, `clicked_on_send_survey_button`, `send_survey_complete`, `send_survey_complete_success`, `send_survey_complete_error`, `clicked_on_comment_input`, `clicked_on_wootric_input`; storage: `redux npsSurvey (persisted: lastSurveyed, isEligible, cancelSurvey, enableNpsTe…`, `redux features.useSurvicate`, `redux settings.dontShowNpsSurvey`; platform: `react-native` · evidence `src/components/common/NpsDialog/NpsDialog.tsx:53-132`
- **me-android** (Employee): endpoints: `GET /api/v2/Configuration/third-party-keys`; events: `Survicate mobile trigger (Employee)`; storage: `cached third-party keys (RemoteKeysRepositoryImpl.persist)`; platform: `android-native`, `Survicate SDK` · evidence `core/src/main/java/com/visma/employee/core/survey/SurvicateSurveyTriggerService.kt:36-93`

**How they differ:**
- Provider: Manager uses a custom Wootric-backed dialog (survey/user/Info, survey/user/response) (NpsDialog.tsx:53-132); Employee Android uses the Survicate SDK started by a key from third-party-keys (SurvicateSurveyTriggerService.kt:36-93). Manager has a features.useSurvicate flag that hides its own…
- Trigger: Manager shows it in the approval list when the backend says isEligible (120s since lastSurveyed in test mode); Employee triggers after absence actions (AddEventViewModel.kt:288,295, EventSelectionViewModel.kt:229, AbsenceSummaryViewModel.kt:73).
- Targeting: Employee sends traits (roles, distributor, customer, company, org number, country, parent tenant) and follows the app theme; Manager sends a hardcoded ip_address and origin_url 'Manager Approval'.
- Comment: Manager allows up to 400 characters with a prompt that changes by score (<=6, 7-8, 9-10); Employee survey content is defined in Survicate, not in the app.
- (platform parity) No me-ios fragment reports a Survicate/NPS survey; only Android has it.
- Provider: Manager's default is its own dialog backed by Wootric: GET survey/user/Info, POST survey/user/response, POST survey/user/decline (apiWootric.ts). Behind the features.useSurvicate flag it uses the Survicate SDK instead (apiSurvicate.ts, ApprovalScreen.tsx:71-80). Employee on both iOS and A…
- Trigger event: Manager uses 'Survicate mobile trigger (Manager)' after an approval task is closed, and the survey appears on the approval list (apiSurvicate.ts, ApprovalScreen.tsx:66-84). The Wootric dialog appears inline in ApprovalList when the backend returns isEligible, or 120s after lastSurvey…
- Trigger points in Employee: Android fires it after absence, expense-draft and payslip actions (AddEventViewModel.kt:288,295; EventSelectionViewModel.kt:229; AbsenceSummaryViewModel.kt:73; ExpenseDraftDetailsViewModel.kt:1739; PayslipRowsViewModel.kt). iOS fires it after payslip and receipt/expense…
- After submission: iOS shows a thank-you toast (SurvicateService+ThankYouToast.swift:14-15). No Android equivalent was confirmed. (platform parity)
- Targeting: Employee sends user and context traits and follows the app theme and locale (SurvicateUserTraits.kt; SurvicateUserTraitsFactory.swift). The Manager Wootric path sends a hardcoded ip_address and origin_url 'Manager Approval' (apiWootric.ts). The Manager Survicate path sets traits, the Int…
- Opting out: the Manager dialog has dismiss, cancel (POST survey/user/decline) and a persisted "don't show again" setting (settings.dontShowNpsSurvey). In Employee, dismissing is handled by the Survicate SDK and there is no opt-out setting in the app.
- Comment and content: the Manager dialog has its own comment prompt, which changes by score, and a character limit. Employee survey content is defined in the Survicate dashboard, not in the app.

_Note: referee could not confirm: The line '(platform parity) No me-ios fragment reports a Survicate/NPS survey; only Android has it' is false. me-ios implements it in EmployeeServices/EmployeeSurvicateSurvey/Sources/EmployeeSurvicateSurvey/SurvicateService.Live.swift:135-137, sets it up in Employee/AppDependencies.swift:156-170 and triggers it from payslip and receipt flows.; The vmm entry leaves out t…_

### CAP-102: Decline the NPS survey or stop it from showing again

**Fusion:** unique · **Personas:** manager · **Confidence:** High

A manager dismisses the NPS survey and chooses Close (decline this time) or 'Don't show again' (turn it off for good).

- **vmm** (Manager): screens: `NpsDialog`; endpoints: `POST {apiBase}survey/user/decline`, `GET {apiBase}survey/user/Info`; events: `clicked_on_dismiss_survey_button`, `clicked_on_back_survey_button`, `clicked_on_cancel_survey_button`, `cancel_survey_complete_survey`; storage: `redux npsSurvey.cancelSurvey`, `redux settings.dontShowNpsSurvey (persisted settings node)`; platform: `react-native` · evidence `src/components/common/NpsDialog/NpsDialog.tsx:134-171`

**How they differ:**
- Only vmm has this, so there is nothing to diverge from. The Employee product (me-ios and me-android) shows surveys through the Survicate SDK and has no in-app decline or don't-show-again control and no survey/user/decline call.
- Note for design: 'Don't show again' is stored only on the device (npsSurvey.dontShowNpsSurvey). The server receives only the same decline POST that Close sends, so the choice is lost on reinstall or on another device.
- Note: the dialog also stays hidden when features.useSurvicate is true (NpsDialog.tsx:173). This suggests vmm may be moving toward Survicate as Employee has, and a merged design would then drop this custom decline flow.

_Note: referee could not confirm: storage 'redux settings.dontShowNpsSurvey (persisted settings node)' is wrong: the flag lives in npsSurvey.dontShowNpsSurvey (vmm/src/reducers/npsSurveyReducer.ts:21,59-60). Only the action creator is declared in actions/settingsActions.ts:58. The value is still persisted, through REDUX_NODE_NAME_NPS_SURVEY in configs/reduxState.ts:112._

### CAP-103: Take or dismiss a survey from the home card

**Fusion:** unique · **Personas:** employee · **Confidence:** High

When a survey is active, the employee sees a start-page card and either opens the survey form or dismisses it; the card is not shown again for that survey.

- **me-ios** (Employee): screens: `NewFeatureCardView`, `StartPageCardBottomSheetView`, `SafariCoordinator`; endpoints: `GET /employee/api/v1/surveys`; events: `surveyCardOpened`, `surveyCardSurveyOpened`, `surveyCardDismissed`, `newFeatureBottomSheetConfirm`, `newFeatureBottomSheetDismiss`; storage: `UserDefaults com.employee.vme.payslip.surveyDontShowAgain.{surveyId}`, `per-user UserPreferences survey dont-show-again by survey id`; platform: `ios-native`, `SFSafariViewController (SafariCoordinator)` · evidence `Employee/StartPage/Cards/ViewModels/SurveyCardViewModel.swift:76-96; Employee/Survey/Service/SurveyService.swift:36-53`
- **me-android** (Employee): screens: `HomeScreen (SurveyHighlight card)`; endpoints: `GET api/v1/surveys`; events: `Survey - survey card opened`, `Survey - survey card dismissed`; storage: `HighlightDismissalRepository key HIGHLIGHT_KEY_PREFIX+surveyId per user`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/home/HomeViewModel.kt:479-486`

**How they differ:**
- (platform parity) iOS opens a bottom sheet first and removes the card on both open and dismiss (SurveyCardViewModel.swift:76-96); Android fragment reports opening or dismissing directly from the card, with the opened event logged once per card (HomeViewModel.kt:1545-1556).
- (platform parity) iOS skips surveys with an invalid formUrl; not reported for Android.
- (platform parity) Opening the survey hides the card only on iOS. iOS calls dontShowSurveyAgain in cardViewDidConfirm with shouldRemoveCardOnConfirm=true (SurveyCardViewModel.swift:80-87). On Android the bottom-sheet positive action only opens the URL and never calls removeHighlightViewModel (HomeEn…
- (platform parity) Both twins open a bottom sheet before the survey (iOS StartPageCardBottomSheetCoordinator.swift:27-38; Android HomeEntries.kt:249-290). The claim says Android opens or dismisses directly from the card, which is wrong.
- (platform parity) The survey form opens in an in-app SFSafariViewController on iOS (SurveyCardDetailsProvider.swift:30-33) and as an external link on Android (HomeEntries.kt:93 callbacks.onOpenExternalLink).
- (platform parity) The checks on survey data differ. iOS drops the card when formUrl is not a valid URL (GetSurveyTask.swift:41-44). Android still shows the card but skips the bottom sheet when title or description is null (HighlightBottomSheetMapper.kt:47-48), and does nothing on positive when form…
- (platform parity) The analytics differ. On iOS, newFeatureBottomSheetConfirm and newFeatureBottomSheetDismiss are logged for the survey card too (StartPageCardBottomSheetCoordinator.swift:28,35). Android logs them only for NewFeatureHighlightViewModel (HomeEntries.kt:274-285). Android's 'survey car…
- (platform parity) The dismissal store differs. iOS keeps a per-survey-id flag in UserPreferences (SurveyService.swift:42,52). Android uses HighlightDismissalRepository with the key HOME_SURVEY_CARD_{surveyId} per logged-in user (SurveyHighlightHidingService.kt:14-30).

_Note: referee could not confirm: me-android divergence citation HomeViewModel.kt:1545-1556 supports the logged-once 'opened' event, but not the claim that Android opens or dismisses directly from the card. Android uses a bottom sheet (HomeEntries.kt:249-290).; me-android storage in the claim omits the actual key prefix HOME_SURVEY_CARD_ (SurveyHighlightHidingService.kt:30). HIGHLIGHT_KEY_PREFIX is the…_

### CAP-104: Volunteer for user testing

**Fusion:** unique · **Personas:** manager · **Confidence:** High

An eligible manager is invited (from an empty list or Settings) to take part in user testing, reads the test description, and submits email and optional phone, or declines/closes the invitation for good.

- **vmm** (Manager): screens: `UserTestingRecruitmentMessage (in ProcessList, AutopayHomeTabPaymentsScreen)`, `SettingsScreen`, `UserTestingSettingsItem`, `UserTestingStartingScreen (SCREEN_NAME_USER_TESTING_STARTING)`, `UserTestingTestDescriptionScreen`, `UserTestingInputsScreen`, `UserTestingFinishedScreen`; endpoints: `GET /api/keys/SeatableToken`, `POST {SEATABLE_SERVER}/api-gateway/api/v2/dtables/{baseUuid}/rows/`, `GET /api/keys/AirtableToken`, `POST https://api.airtable.com/v0/{base}/{table}`; events: `failed_fetch_seatable_token`, `failed_fetch_airtable_token`; storage: `redux features userTestingRemoteAccess (setUserTestingRemoteAccess)`, `redux features.userTestingExpiryDate`, `redux features.userTestingRecruitmentCancelled (persisted features node)`, `redux userTesting recruitmentCancelled`, `userTesting expiryDate (now + 14 days)`, `Firebase Remote Config REMOTE_CONFIG_USER_TESTING_TEST_DESCRIPTION_PROD/_STAGE`; platform: `react-native`, `Firebase Remote Config (REMOTE_CONFIG_USER_TESTING_PHASE)`, `react-native-device-info` · evidence `src/screens/UserTestingRecruitment/UserTestingInputsScreen/UserTestingInputsScreen.tsx:55-123; src/components/uiless/Us…`

**How they differ:**
- The 13-hour eligibility recheck fires once, 13 hours after mount (setTimeout with an empty dependency list, UserTestingRecruitmentAccessWatcher.tsx:37-45), not repeatedly as the claim's notes say.
- The recruitment message is also used in src/screens/manager/ApprovalScreen/components/TabPresent/TabPresent.tsx, which the claim does not list.
- Token-fetch failures call setToastMessage without dispatch (UserTestingInputsScreen.tsx:92 and :116), so the user sees no message. Only the failed_fetch_* events are tracked.

_Note: Eligibility: phase 0 off, phase 1 only stage/sandbox with a matching role, phase 2 on with a matching role (autopay, approval, employee HRM, osr); re-checked every 13 hours. Backend switch features.useSeatable (Seatable vs Airtable). Finish hides recruitment for 14 days._

### CAP-105: Review and share failed request logs

**Fusion:** unique · **Personas:** manager, support · **Confidence:** High

When requests have failed, a manager opens the error log list from Settings, views details and shares an error report via the system share sheet.

- **vmm** (Manager): screens: `RequestErrorLogsScreen (SCREEN_NAME_APPROVAL_REQ_ERROR_LOGS = 'ApprovalReqError…`, `SettingsScreen`; storage: `redux features.failedRequestsDetails`; platform: `react-native`, `system share sheet` · evidence `src/screens/common/RequestErrorLogsScreen/RequestErrorLogsScreen.tsx:12-76`

_Note: Shared report includes path, details and request payload; review for personal-data exposure._

### CAP-106: Copy account and device details for support

**Fusion:** unique · **Personas:** employee · **Confidence:** High

An employee taps their email, OS version or app version in Settings and all three are copied to the clipboard with a confirmation banner.

- **me-ios** (Employee): screens: `SettingsTableViewController (user info section)`; platform: `ios-native`, `pasteboard` · evidence `Employee/Settings/SettingsViewModel.swift:97-109`

**How they differ:**
- (platform parity) No me-android fragment reports copying account/device details to the clipboard.
- (platform parity) The claim's line saying Android has no clipboard copy is wrong. me-android InfoContainer.kt:65-74 copies email, OS version and app version (label and value on each line) when the info block is tapped, matching me-ios SettingsViewModel.swift:98-109.
- (platform parity) Confirmation: me-ios shows its own green top banner using copied.intoYour.clipboardText (SettingsTableViewController.swift:646-657). me-android shows no snackbar or toast after clipboard.setText (InfoContainer.kt:73), so it relies on the OS clipboard notice where the OS shows one.
- (platform parity) Tap target: me-ios reacts to a tap on any of three separate table rows (.userEmail, .appVersion, .osVersion). me-android makes the whole info container one clickable Column.
- (platform parity) Email source: me-ios uses userService.getCurrentUser()?.emailAddress (SettingsViewModel.swift:111-113). me-android uses mDataStorage.lastLoggedInUserNameState (SettingsViewModel.kt:76), the last logged-in user name.
- (platform parity) Text format: me-ios joins the lines as 'label: value' (colon separator). me-android writes 'label value' plus a trailing newline on each line (InfoContainer.kt:69).

_Note: referee could not confirm: The divergence line 'No me-android fragment reports copying account/device details to the clipboard' is refuted by me-android/app/src/main/java/com/visma/employee/settings/presentation/components/InfoContainer.kt:58-75._

### CAP-107: Read open-source licenses and the accessibility statement

**Fusion:** shared-diverged · **Personas:** employee · **Confidence:** Medium

From Settings an employee opens the open-source licenses or the accessibility statement (from which feedback can also be sent).

- **me-android** (Employee): screens: `SettingsScreen`, `LicensesKey`, `AccessibilityStatementKey`; platform: `android-native` · evidence `app/src/main/java/com/visma/employee/navigation/RootNavDisplay.kt:271-285`
- **me-ios** (Employee): screens: `FeedbackView / FeedbackFeature`; platform: `ios-native` · evidence `Employee/Settings/SettingsTableViewController.swift:740-768`

**How they differ:**
- (platform parity) Android fragment reports a licenses screen (LicensesKey); iOS fragment only reports the accessibility statement with its feedback link.
- Navigation: in vmm, licenses and the accessibility statement sit one level deeper, under Settings > Privacy (SettingsScreen.tsx:442 -> SettingsPrivacyScreen.tsx:117-126). Employee has them as rows directly in Settings (Android RootNavDisplay.kt:279-280; iOS SettingsTableViewController.swift:613-618…
- Feedback: Employee's accessibility statement links to the in-app feedback form (Android AppLeafEntries.kt:73 onOpenFeedback -> FaqSendFeedbackKey; iOS SettingsTableViewController.swift:719 -> presentFeedbackController/FeedbackFeature). vmm has no feedback link on the statement; a separate 'customer…
- Licenses: vmm lists each package and opens its license URL in an in-app browser (SettingsLicensesScreen.tsx:34, licenses.ts). Employee shows the license content inside the app (Android LicensesScreen from dataStorage().getLicensesList(), AppLeafEntries.kt:55-66; iOS LicensesView shows copyright, ve…
- Accessibility statement: vmm shows bundled HTML chosen by locale (NO, SV, else EN) in a WebView modal (SettingsPrivacyScreen.tsx:69-88). Employee uses a native screen: Android AccessibilityStatementScreen with AccessibilityStatementViewModel, iOS AccessibilityView with AccessibilityViewModel.
- (platform parity) Android and iOS both have licenses and the accessibility statement with a feedback link. The claim's statement that iOS lacks a licenses screen is wrong. Licenses content differs: Android uses a stored licenses list, iOS a text view that also shows copyright and app version.

_Note: Thin evidence; could be folded into a Settings/legal domain. referee could not confirm: me-ios Employee/Settings/SettingsTableViewController.swift:740-768 is presentFeedbackController only; the licenses and accessibility code is at :613-618 (row handling), :706-714 (showLicensesView) and :716-726 (showAccessibilityView); me-ios screen 'FeedbackView / FeedbackFeature' is only a side screen; the ma…_

## Journeys

### JRN-009: Clear the morning approval queue from a push notification

**Persona:** People who use Manager today (manager /…. A manager gets a push about a new invoice to approve, reviews it, fixes the accounting lines and approves it along with the rest of the queue.

1. Tap the push notification about a new approval task (CAP-176, CAP-178)
2. Review the task, its documents and workflow history (CAP-153, CAP-164, CAP-168)
3. Correct the invoice's accounting lines before approving (CAP-170, CAP-171, CAP-172)
4. Approve the invoice, or send a questionable one to a colleague (CAP-154, CAP-157, CAP-158)
5. Clear the rest of the pending queue in one go (CAP-150, CAP-151, CAP-160)

### JRN-010: Approve this week's supplier payments with BankID

**Persona:** People who use Manager today (manager /…. A payment approver spots upcoming AutoPay payments on Home, checks the warnings and signs the batch with BankID.

1. See upcoming payments on Home and open one (CAP-008, CAP-074)
2. Review the payments waiting for approval and their invoices (CAP-186, CAP-191, CAP-192)
3. Handle the warnings, move a pay date and cancel a duplicate (CAP-195, CAP-193, CAP-196)
4. Select the payments and sign them with BankID (CAP-188, CAP-189)
5. Check later that the payments reached the bank (CAP-190)

### JRN-011: Close the payroll run with the payroll bureau

**Persona:** People who use Manager today (manager /…. A manager answers the payroll bureau's questions in a dialogue, then approves the wage run.

1. Follow up on unread dialogues from Home (CAP-075, CAP-214)
2. Read the conversation and reply (CAP-216, CAP-218)
3. Check an employee's absence balance before answering (CAP-124, CAP-009)
4. Approve the wage run and close the dialogue (CAP-224, CAP-222)

### JRN-012: Ask the assistant instead of digging through screens

**Persona:** People who use Manager today (manager). A manager asks the AI assistant about pending approvals, acts on a task from the chat and picks up the conversation later from a notification.

1. Open the assistant from Home and pick a suggested question (CAP-051, CAP-053, CAP-066)
2. Ask about a pending approval and check the cited sources (CAP-049, CAP-061)
3. Approve the task directly in the chat (CAP-063, CAP-062)
4. Come back when a longer answer is ready (CAP-058, CAP-056)
5. Rate the answer (CAP-059)

### JRN-013: Check the order book and the money owed in Business NXT

**Persona:** People who use Manager today (Business…. A manager switches company, reviews open orders, sends a purchase order for approval and checks what customers owe.

1. Switch to the right company and open the orders area (CAP-030, CAP-031, CAP-032)
2. Check stock and create a purchase order (CAP-046, CAP-035, CAP-034)
3. Send the purchase order to approval and track it (CAP-036, CAP-039)
4. See what customers owe and drill into one (CAP-042, CAP-043, CAP-044)

### JRN-014: Snap a receipt and get reimbursed

**Persona:** People who use Employee today (employee). An employee photographs a receipt after a business dinner, lets the app fill it in and sends it in a claim for approval.

1. Start a receipt from Home and capture the photo (CAP-084, CAP-241, CAP-242)
2. Let the app fill in the receipt and check the fields (CAP-244, CAP-245, CAP-263)
3. Match it to the company card transaction (CAP-250, CAP-275)
4. Put the unsent expenses in a claim and send it (CAP-240, CAP-253, CAP-254)
5. Follow the claim's status (CAP-081, CAP-258)

### JRN-015: Claim mileage and per diem after a business trip

**Persona:** People who use Employee today (employee). An employee back from a two-day trip logs the drive with tolls and a travel allowance and sends both in one claim.

1. Plan the route and let the app work out distance and tolls (CAP-266, CAP-267, CAP-265)
2. Register the travel allowance with meals and hotel stays (CAP-269, CAP-270, CAP-271)
3. Add both to a claim with project accounting (CAP-255, CAP-264)
4. Send the claim and see its emissions (CAP-254, CAP-274)

### JRN-016: Register time off and keep my time sheet right

**Persona:** People who use Employee today (employee). An employee checks balances, books time off from the calendar or through the Employee Agent, and confirms the week's hours.

1. Check vacation balances (CAP-211, CAP-010)
2. Pick the days in the calendar and register the absence (CAP-001, CAP-006, CAP-012)
3. Or tell the Employee Agent what to register (CAP-021, CAP-024)
4. Check in and out during the week (CAP-018, CAP-019)
5. Confirm the worked time (CAP-020, CAP-022)

### JRN-017: Understand my payslip

**Persona:** People who use Employee today (employee). An employee opens a new payslip from a notification, asks the payslip assistant about a deduction and downloads the PDF.

1. Open the new payslip from the notification or start page (CAP-178, CAP-080)
2. Read the payslip details (CAP-225, CAP-029)
3. Ask the payslip assistant about a line (CAP-052, CAP-060)
4. Download the payslip or the year-end report (CAP-226, CAP-230)

### JRN-018: Keep my HR details and required documents up to date

**Persona:** People who use Employee today (employee). An employee updates their address and bank account, adds an emergency contact and confirms reading a new company policy.

1. Open my personal information from the user menu (CAP-086, CAP-141)
2. Update my address and salary bank account (CAP-142, CAP-143)
3. Add an emergency contact (CAP-144)
4. Open the document notification and confirm reading the policy (CAP-180, CAP-183, CAP-234)

### JRN-019: Start using the app on a new phone

**Persona:** People who use Employee today (employee). An employee installs the app, signs in, protects it with Face ID and sets up notifications.

1. Go through onboarding and sign in (CAP-090, CAP-197, CAP-200)
2. Protect the app with Face ID (CAP-206, CAP-207)
3. Allow notifications and set language and appearance (CAP-176, CAP-185, CAP-109, CAP-110)
4. Stay signed in on later visits (CAP-198)

### JRN-020: A manager who is also an employee: one app for both roles

**Persona:** People who use both Manager and Employe…. A team lead approves a direct report's request, then submits their own expenses and checks their own payslip in the same app, without switching apps.

1. Sign in once and switch employer if needed (CAP-197, CAP-205)
2. See the team's items waiting on Home and approve them (CAP-008, CAP-073, CAP-154)
3. Check who is absent in the team calendar (CAP-001, CAP-004)
4. Move to my own area and send my expense (CAP-067, CAP-257)
5. Check my own payslip and vacation balance (CAP-080, CAP-211)

## Observations

- Every Business NXT capability exists only in vmm (Manager, react-native). Neither me-ios nor me-android reported any fragment here, so all capabilities are unique and there are no platform-parity gaps.
- None of these capabilities matches an outcome in analysis/work-app/capability_index.json (29 entries across Calendar, Team overview, Balances, Absence registration, Time tracking, Employee Agent, Expenses and Pay), so no earlier names were reused.
- Everything goes through a single GraphQL endpoint (POST https://business.visma.net/api/graphql) and is scoped by redux bnxtOrders.selectedCompanyId. Company switching is therefore a cross-cutting dependency of every BXN capability.
- Access is gated in layers: the dev-tools flag isBnxtOrdersIntegrationEnabled, at least one BXN company, per-table read/update permissions (useBnxtLookupAccess, GetBnxtOrderTableAccess), and isBnxtTabbedHubEnabled for the workspace layout. The new app needs one consistent permission model.
- The hub (fragment 159) and the tabbed workspace (fragment 214) were merged into one capability, because the flag only switches layout, not outcome. A person should decide which layout survives.
- Fragment 167 mixed viewing and editing an order. It was split into 'View a Business NXT order' and 'Edit a Business NXT order's references, delivery date and lines'. Fragment 161 was split into tracking (task detail) and withdrawing a pending task.
- Fragment 1 (shared presentational list and detail rows) has no outcome of its own. Its evidence is attached to the list and detail capabilities that host those rows.
- Approving or rejecting approval tasks happens in Visma.net Approval, not in the app. This is a gap to decide on if the merged app should support approvers.
- Several failure paths show raw, untranslated server messages (cancel purchase order, withdraw approval task).
- No earlier capability in capability_index.json is the same outcome as these. CAP-021 'Register time or absence by chatting with the Employee Agent' is a different outcome, but it shares the Employee chat bubbles and voice-input field (fragments 423, 557), so the new app should build one assistant chat shell for both.
- The products have very different assistants. The Manager's Gaia is a general, streaming, tool-using agent with persistent server-side conversations, notifications, gated actions and in-app navigation. The Employee's assistant is a payslip-only beta bot with an in-memory session and no history. The main fusion decision is whether Employee gets Gaia (one assistant) or both bots are kept.
- Feedback is lost in vmm: ratings stay in redux with no backend call, while Employee sends them to /EmployeeAssistant/feedback with issue categories.
- Links: vmm opens cited sources externally, while Employee strips links and images from replies. The rule needs to be unified.
- Much of vmm's Gaia is behind dev flags or A/B switches (useGaiaHintsEnabled, useGaiaCapabilitiesEnabled, useGaiaFrontendToolsEnabled, assist style legacy/toggle), so production reach is uncertain.
- Approving a task from the chat card sends an empty comment. This may conflict with approval-domain rules that require comments on reject.
- The twins' endpoint paths differ by an /employee prefix and casing (v1 employeeassistant versus employeeAssistant), probably a base-URL difference. This should be checked.
- Two different Home concepts exist: the Manager Start hub (work queues across Approval, Autopay, HRM with counts, activity feed and search) and the Employee highlights carousel (personal pay, absence, expense status). They share no data sources. The merged app needs a product decision on whether one Home serves both personas or adapts by role.
- The Employee start-page card capabilities reuse earlier names from other domains ('See my vacation balances on the start page' CAP-011, 'See upcoming and ongoing vacation and parental leave on the start page' CAP-017) so earlier decisions stay attached.
- What's New is the one real cross-product overlap: vmm drives it from Firebase Remote Config with rich media, while iOS Employee's bundled list is empty (dormant) and Android ties it to the payslip bot. Three different dismissal stores exist (redux, UserDefaults, Room).
- The vmm Start tab and Home search sit behind dev flags (toggledStartPageDevFlag, showHomeSearch default off), so these capabilities may not be live for users.
- Several Android-only capabilities (deep links, startup gate, onboarding, important info/survey/update cards) have no reported iOS counterpart; these may be real parity gaps or shard coverage gaps.
- vmm TabBar.tsx:172-195 has an approval deep-redirect on openDetailsTaskId that nothing sets, which looks like dead code.
- Fragment 554 (paginated feed) is a reusable component rather than a user outcome and overlaps the Pay and Expenses browse capabilities.
- Financial reporting (OneStop Reporting) exists only in vmm (Manager). Neither me-ios nor me-android reported a fragment, so every capability here is unique.
- No capability in analysis/work-app/capability_index.json belongs to this domain, so no earlier names were reused.
- Endpoint paths are written two ways in the fragments: 'osr/dashboards/element' with a category and filters, and '/api/osr/dashboards/element' without a category. Both are kept exactly as reported. They are probably the same call with a base-URL prefix, but this should be confirmed.
- The reporting context has a customer, a tenant, a company, a dashboard and an interval, all persisted in redux. The new app must choose where this selection lives and whether it follows the user across devices.
- Fragment 6 mixed two outcomes: rendering a dashboard card and opening an element's details. It was split between the dashboard capability and the detail capability.
- No earlier capability in capability_index.json matches this domain; the only similar names (CAP-026, CAP-027) belong to the Employee Agent and cover different outcomes, so no earlier names were reused.
- Both products send general feedback to the same Employee feedback endpoint (/employee/api/v1/feedback) but with different payloads. A merged app can use one service with an optional context field (Manager already sends context 'BNXT' for line-edit feedback).
- vmm's 'sent_feedback' analytics event fires when a draft is discarded, not when feedback is sent (FeedbackScreen.tsx:131-136, BXN screen line 128). Fix this before comparing feedback metrics across apps.
- The two products collect satisfaction data from three providers: Wootric-style NPS in Manager, Survicate on Employee Android, and a backend /surveys card on Employee iOS and Android. Manager already has a useSurvicate flag, which suggests the products are converging on Survicate.
- Help works differently in each product: Manager explains each screen through info modals, and Employee has a topic-based FAQ with license lookups. Neither product has the other's approach.
- User-testing recruitment is only in Manager. It depends on Firebase Remote Config and gets tokens for Seatable or Airtable from /api/keys at runtime.
- Parity gaps between the Employee twins: only iOS reports clipboard copy of support details; only Android reports Survicate NPS; the store-review cool-downs differ (30 vs 90 days).
- None of these capabilities matches one in analysis/work-app/capability_index.json. It covers other domains (Calendar, Balances, Absence, Time, Agent, Expenses, Pay), so every name here is new.
- Manager saves settings (locale, dark mode, vibration, holiday theme) to the backend with PUT /users/{userId}/settings. The Employee twins store the same kind of preference only on the device. The merged app needs one policy.
- Legal and consent gaps: only Manager has an analytics consent toggle and forced terms acceptance. Only Employee Android has a screenshot-blocking toggle and an account info block.
- The update check uses three different backends: vmm uses the keys endpoint, me-ios uses /employee/api/v1/remoteControl/config, and me-android uses api/v1/RemoteControl/Config. The vmm UpdateDialog component appears to be dead code.
- Language change works differently on the two twins: iOS hands it to iOS Settings, Android has an in-app picker and restarts. This is a large parity gap.
- Internal tooling (dev tools, feature flags, environment switch) is maintainer-only. It should not anchor user journeys.
- Only one earlier capability belongs to this domain: CAP-007 'Sync team birthdays and work anniversaries to my calendar' (domain 'Team overview'). Fragment 49 reuses its exact name. No other earlier names apply.
- The two products edit the same HR data (names, phones, address, children, emergency contacts) through different backends. vmm PUTs employee/companies/{companyId}/employees/{employeeId} and polls a job (GET .../jobs/{jobId}). Employee POSTs the full EmpMan record (/api/v1/employees/{odpUserId}/EmpMan/employees/me) with an etag, and a 504 means pending. The manager-edits-employee and employee-edits…
- The Employee app has two self-service profile stacks: the classic EmpMan Personal Information and the Dottie template-driven HR profile. On iOS the choice depends on whether the company is a Dottie company (UserProfileCoordinator.swift:41-47). vmm likewise has an HRM record view and a separate Dottie profile view. In both products Dottie is a second, parallel HR source.
- Children and emergency-contact rules differ across products. vmm stores only the child's year of birth (YYYY-01-01) with sole custody. Employee stores the full date of birth, sole custody and a chronic illness period with dates. vmm always creates new contacts with relation=Other, while Employee picks the type from EmpMan selections. Both send the whole relatives array, and vmm has to re-match re…
- vmm has several deletes with no confirmation: removing a child or an emergency contact. Android Employee confirms relative deletion, while iOS Employee defers it until Save changes. The merged app needs one rule.
- The birthday/anniversary feature set (tab badge, Home card, AI greeting via POST hrm/anniversary, share/SMS, save for later, reminders, calendar sync) exists only in Manager. Saved greetings live only in the device's redux store, so they do not follow the manager to another device. The anniversary tab badge is disabled by bug VMM-7758.
- Several vmm Dottie screens use hard-coded English labels (Dottie detail sections, 'Balances', 'Post address', 'Add new contact'). The Employee equivalents are localized.
- On Android, the Personal Information settings row is hard-disabled (hasPersonalInformation=false, SettingsViewModel.kt:39). The screen is reachable only from the user menu sheet, which is an entry-point parity gap with iOS.
- No fragment reported offline behaviour for any HR capability. vmm persists the list, filter and greeting state in redux; Employee keeps only in-memory profile caches.
- The whole Approvals domain exists only in vmm (Manager). Neither me-ios nor me-android reported any approval fragment, so every capability is unique. None of them matches an earlier capability in capability_index.json (CAP-001 to CAP-029 cover Calendar, Balances, Absence, Time, Agent, Expenses and Pay), so all names are new.
- Coupling to Employee: me-ios absence and time registrations carry an approval status (CAP-014, CAP-020 confirm time for approval). vmm approval tasks include timesheet and leave tasks shown in hours or days (ApprovalTaskScreen). The merged app should connect the employee's 'submitted' view to the manager's approval inbox.
- Bulk approve is built twice inside vmm (ApprovalListMultiselectBar and HrmEmployeeApprovalTasksMultiselectBar), with different timeouts and confirm behaviour. Line editing is built three times (Financials, Business NXT, Compello), each with its own apply-to-all, discard, custom field choice and quick index. Treat these as candidates to consolidate.
- Possible defects to decide on: Forward is gated by canSendForReview, not canForward (TaskActions.tsx:167). ApprovalTaskFinancialsLinesScreen looks unregistered in navigation (dead code). The share error uses a hardcoded English alert.
- Several fragments are component-level slices of one outcome and were folded in: the shared TaskActionsDrawer (62) into approve, VoucherlinesTop switch (61) into opening accounting lines, and FieldEditSheet (55) into line editing, where its usage was only inferred by grep.
- No earlier capability in analysis/work-app/capability_index.json belongs to Notifications and inbox, so every name here is new.
- Push registration is the only part vmm and Employee share. They call different device endpoints (POST Devices vs POST /employee/api/v1/notification/RegisterDevice) with different bodies. The merged app needs one registration that covers approval-task and employee event types.
- vmm reports no inbox, no tap routing and no in-app message list. Approvers would get none of the Employee inbox unless the merged app extends it to them.
- Fragment 294 mixed registration and tap routing, and fragment 504 mixed mark-as-read and document opening. Each was split across the matching capabilities.
- The Dottie HR inbox, badge, hide and mark-as-read all rely on HATEOAS links from the server. Whether an action is offered depends on the server payload.
- Parity gaps: document preview with must-read confirmation, and a Settings link to notification settings, are reported only on Android. Receipt-sync push channels are also Android-only.
- The whole Payments domain comes from vmm (Manager, react-native) only. The fragments show no AutoPay feature in me-ios or me-android, so every capability is unique to the Manager product.
- None of these capabilities matches an entry in analysis/work-app/capability_index.json. The only pay-related entry there, CAP-029 'Browse my payslips...' (domain Pay), is a different outcome, so no earlier name was reused.
- Fragments 37-48 (components layer) and 197-203 (screens layer) describe the same features from two code layers. They were merged per outcome: browse (39+197), search (41+198), select (38+199), overview (43+200+40) and details (44+201+203).
- The approval flow is coupled to external web redirects on firebaseapp.com and web.app domains and to a strict WebView URL scheme policy. The new app has to carry these security rules over word for word.
- Search behaviour looks inconsistent. Fragment 198 says an active search keeps only companies with more than one transaction on the same IBAN (AutopayHomeTabPaymentsScreen.tsx:99-110), while fragment 41 says it simply filters by text. A person should confirm the intended rule.
- The Overview tab and search UI depend on a feature flag (showAutopayOverviewTab) and the assist style (legacy or GAiA), so the new app needs a decision on which variants survive.
- The earlier map (analysis/work-app/capability_index.json, CAP-001..CAP-029) has no Sign-in and accounts capabilities, so every name here is new and no earlier id is reused.
- Most of this domain is Employee-only: multiple saved accounts, silent refresh across accounts, employer switching and the app lock (PIN/biometrics). The Manager app (vmm) has one account and no app lock, so the merged app must decide whether managers get multi-account support and an app lock.
- The two products gate access differently. vmm checks per-integration role flags (HRM/Approval/OSR/Autopay/BXN); Employee checks per-company permissions from currentSession. A merged app needs one access model that covers both manager roles and employee company contexts.
- Both products use the same Visma Connect authorize/token/revocation endpoints, but with different redirect hosts (visma-manager.web.app vs static.mobileemployee.visma.net) and different client identities (Employee client_id com.visma.employee). A merged app needs one OAuth client and one callback domain.
- Security note: the me-ios hidden environment picker is not gated by DEBUG (EnvironmentManager / SelectAccountView.swift:48-50), so production users can reach it. me-android restricts it to internal builds.
- me-ios and me-android differ noticeably in lock behaviour: an attempt limit that wipes accounts (iOS only), a 180s background timeout (Android only), greeting hour ranges, and device-credential support. These should be settled as product rules, not left as silent platform drift.
- The current-session path differs between the twins (/employee/api/v1/... on iOS vs /api/v1/... on Android). It is probably a difference in base URL, but it should be confirmed.
- The vmm string key 'enviroment' is misspelled, and the vmm Settings confirm alert for switching to production is untranslated (120).
- The Manager product (vmm) only views someone else's time and absence data (employee calendar, balances). It cannot register, approve or confirm anything in these fragments. Every write capability is Employee-only.
- vmm's employee calendar serves mock data because the live my-employees feed returns 403 (queryEndpointsCalendar.ts:71-75,158-164). The shared-diverged calendar capabilities (CAP-001..005) depend on a backend that is not working yet for managers.
- The two products use different backends for balances: vmm uses {calendarBaseUrl}/org/{orgId}/balances and summary templates with legacyEmployeeId. Employee uses /employee/api/v1/v2 calendar balances. A merged app needs one balance model.
- Within the Employee twins, iOS and Android call the balances summary through different endpoints (v2 time-balance-summary by month vs v1 balances/combined). This is the largest parity gap. It also makes it unclear whether Android's summary matches CAP-010 or CAP-011.
- Employee paths differ by prefix only: iOS /employee/api/v1/... and Android /api/v1/... (probably different base URLs). This is treated as the same endpoint.
- Fragment 457 mixes editing an absence with fixing a failed checkout, so it was split across 'Edit a registered absence' and 'Edit or delete a check-in/check-out registration'. Fragment 459 feeds several Employee Agent capabilities.
- Entry-point fragments were folded into their outcomes: vmm 76 into the month calendar, me-ios 309 (start-page quick action) and 419 (post-save confirmation screen) into 'Register an absence or time event', and me-ios 230/242 into the agent chat capability.
- Fragment 266 (DynamicForms, Dottie employee info) and fragment 218 (vmm timeline prototype, not reachable by users) do not fit the Time and absence domain. They are kept at Low confidence so a person can re-home or drop them.
- Earlier capability CAP-017 (upcoming vacation cards on the start page) got no fragments in this batch. It is not restated here.
- The two products do not overlap in this domain. vmm (Manager) covers only payroll dialogues and wage-run approval. The Employee app (me-ios and me-android) covers only payslips and year-end reports. Every capability is therefore unique, and the only differences recorded are platform parity gaps between the Employee twins.
- Only one earlier capability matched: CAP-029 'Browse my payslips by payment date, filtered by employer'. The company filter (fragments 430 and 683) was folded into it because the earlier name already includes employer filtering. The earlier entry lists only me-ios, and me-android now joins it.
- The Employee twins call different API path prefixes: iOS uses /employee/api/v1/..., Android uses /api/v1/... Year-end report detail and PDF also use different route shapes: iOS uses employees/{odpUserId}/reports/{reportId} plus a server-provided export href, Android uses employees/report/{reportId} and report/{reportId}/export/pdf. Check with the backend team which contract the merged app should…
- Payslip export differs between the twins. iOS has a current-company endpoint (Payslip/Export) as well as exportFromAllTenants. Android uses only exportFromAllTenants.
- Every vmm dialogue write (edit, delete, complete, approve, message edit and delete) uses optimistic concurrency through a version query parameter. The merged app should keep this.
- Deleting a split: the context menu passes a splitId (fragment 85), but only a dialogue-level DELETE endpoint was reported (fragment 98). The split delete path is unverified.
- Manager dialogues and employee payslips both centre on wage runs and pay, but no fragment shows employees taking part in payroll dialogues. The two sides stay separate personas with no shared journey.
- The whole domain belongs to the Employee product (me-ios and its twin me-android); vmm (Manager) has no documents or benefits fragments, so every capability is unique. No earlier capability in capability_index.json covers this domain, so no earlier names were reused.
- All Documents and benefits features depend on the Dottie company feature and the Dottie backend (/dottie/documents/*, /dottie/benefits).
- The endpoint prefix differs between twins (/employee/api/v2 on iOS, /api/v2 on Android). This is probably a base-URL difference and should be checked before building one API client.
- iOS sends analytics events for this area and Android reports none. That is an analytics parity gap.
- The notification-driven 'open and acknowledge' flow is only evidenced on iOS, where it uses HAL link hrefs instead of fixed paths.
- The file preview and external-open capabilities are shared utilities used in other domains too (Pay, attachments). They may belong in a cross-cutting domain.
- Temp-file lifecycle differs between the twins: iOS deletes the file on preview close, while Android clears the cache dir on screen load and deletes after preview. The new app should define a single policy.
- All fragments come from the Employee product (me-ios and its Android twin me-android). No vmm (Manager) fragment exists in this domain, so every capability is 'unique' and every difference is a platform parity gap. Managers approving or declining expense claims is not reported anywhere, which is a notable gap if the new app should cover the approver side.
- Only one earlier capability belongs to this domain: CAP-028 'Browse my expense claims by year and filter by status'. Its name is reused for the claims list. CAP-013 (cost units for absence registrations) was deliberately not reused for expense cost units, because it is a different outcome.
- Claim actions are almost entirely hypermedia-driven on both platforms: update, delete, cancel, request_approval and the add-items links. The rel names differ between the twins: iOS uses addOrRemoveReceipts, addOrRemoveMileages and addOrRemoveAllowances, while Android uses update_from_drafts, update_from_mileage_drafts and update_from_allowance_drafts. A merged client must agree on one contract.
- Editability rules differ between the twins. iOS decides from the presence of an 'update' link; Android also checks the claim status (Open, Cancelled or Rejected for fields, not Sent, Paid or Approved for cost units and project). A product decision is needed.
- Contradictions inside single platforms need checking in the code: Android Smartscan confidence filtering (High/VeryHigh vs all levels, fragments 618 and 646); iOS hotel search provider (MapKit in fragment 340 vs Google Places in fragment 407); Android storage key for 'don't show again' (per user email vs last logged-in user name, fragments 621 and 597).
- Endpoint paths differ only by base prefix: iOS reports /employee/api/..., Android reports /api/... or api/.... Treat this as a base-URL difference, not a different API.
- Offline behaviour is a cross-cutting concern that touches receipts, mileages, sync, the inbox and sharing. Most send, merge and add-to-claim actions need a connection on both platforms, while draft saves are queued locally.
- No instruction-shaped text aimed at AI tools was found in the fragments. Fragment 594 has an empty 'injectionSuspects' field, which is data and not an instruction.

## Rejected by the referees

Candidates a second agent could not confirm from the cited code:

- Ask the legacy AI chat about approval tasks (unreachable): The code exists, but no user can reach it or use it. In vmm, ChatHistoryModal (src/components/modals/ChatModal/ChatHistoryModal.tsx:51) is registered as a route at src/configs/navConfig/common/CommonScreensNavConfig.tsx:320. Nothing ever opens it: no navigate() call anywhere in src uses SCREEN_NAME…
- Browse a paginated feed of past and upcoming items: The cited files exist and the code is real. ComposeFeedScreen.kt:65-150 renders the feed and FeedViewModel.kt:15-99 holds the pagination state. The claim says itself that this is a shared UI component, and the code agrees. ComposeFeedScreen is a generic composable. FeedViewModel is abstract: loadMo…
- Accept the terms of service before continuing: Refuted: the forced flow can never run. In vmm, everything that makes the terms mandatory depends on getMustAgreeToS, and that selector is hardcoded to false (legacy/vmm/src/selectors/settings/settingsSelector.ts:34-36: createSelector([getManagerLoggedIn, getManagerUsername, getToSAgreedUserList],…
- Sync team birthdays and work anniversaries to my calendar: The sync logic exists in vmm, but no user can reach it. useSyncCalendar.ts:38-258 does what the claim says: it asks for calendar permission, creates the manager birthday and anniversary calendars, saves yearly all-day events with a -1440 minute alarm, matches existing events by url == employee id,…
- Sort AutoPay payments by amount or creditor name: Refuted: the code does not let a user sort AutoPay payments. The cited component exists (vmm src/components/autopay/AutopaySortSection/AutopaySortSection.tsx:25-43) and is mounted from src/screens/autopay/AutopaySearchBar/AutopaySearchBar.tsx:51. It flips settings.autopaySortOrder between 'amount'…
