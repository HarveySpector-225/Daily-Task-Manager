DAILY TASK MANAGER - DRY RUN
PS No. 28 - Python 3 console application (daily_task_manager.py)
B.Tech CSE (AI & ML), First Year
Name: Adamya Rajvanshi    Roll No.: RU-26-02181

======================================================================
1. AIM
======================================================================
To trace the Daily Task Manager program step by step for the four test
cases, showing how each statement changes the variables and the file
tasks.txt.

======================================================================
2. VARIABLES USED
======================================================================
FILE            string       Name of the storage file, tasks.txt
tasks           list         Holds all the task dictionaries
task / t        dictionary   One task: id, title, priority, due_date, status
title, priority, due_date    Values typed by the user while adding a task
task_id         string       ID typed by the user while completing a task
biggest         integer      Largest ID number found so far (starts at 100)
pending / count integer      Number of tasks whose status is Pending
choice          string       Menu option typed by the user

======================================================================
3. TEST CASE 1: NORMAL INPUT
======================================================================
Initial condition: tasks.txt does not exist yet (first run).
Input: option 1, title homework, priority Medium, due date 2026-11-17

Step 1  main() starts and calls load_tasks().
        open() raises FileNotFoundError, the except block catches it and
        the function returns an empty list.  tasks = []
Step 2  Menu is printed, user enters 1.
        choice = '1', so add_task(tasks) is called.
Step 3  Title is read.
        title = 'homework'. It is not empty and has no pipe symbol, so it
        is accepted.
Step 4  Priority is read.
        'Medium'.strip().capitalize() gives 'Medium', which is in the
        allowed list (High, Medium, Low), so it is accepted.
Step 5  Due date is read.
        due_date = '2026-11-17'. is_valid_date() runs: strptime succeeds
        and the length is 10, so it returns True.
Step 6  get_next_task_id(tasks) is called.
        biggest = 100. The list is empty, so the loop does not run.
        It returns 'T' + '101' = T101.
Step 7  Task dictionary is created.
        id = T101, title = homework, priority = Medium,
        due_date = 2026-11-17, status = Pending
Step 8  tasks.append(task).  tasks now holds 1 task.
Step 9  save_tasks(tasks).  tasks.txt is created and one line is written.
Step 10 Two print statements run.

Output on screen:
    Task added.
    T101 | homework | Medium | 2026-11-17 | Pending

tasks.txt after this run:
    T101|homework|Medium|2026-11-17|Pending

Result: Output matches the expected output.  PASS

======================================================================
4. TEST CASE 2: BOUNDARY / MINIMUM INPUT
======================================================================
Initial condition: no tasks in tasks.txt.
Input: option 3 (Show pending)

Step 1  load_tasks().  The file is missing or empty, so tasks = [].
Step 2  User enters 3.  choice = '3', so show_pending(tasks) is called.
Step 3  count_pending(tasks).  count starts at 0. The list is empty, so
        the loop does not run and 0 is returned.
Step 4  if pending == 0 is True, so the message is printed and the
        function returns.

Output on screen:
    No pending tasks. You are all caught up!

Result: Output matches the expected output.  PASS

======================================================================
5. TEST CASE 3: INVALID INPUT
======================================================================

(a) Invalid priority
Input: option 1, title Pay bill, priority Urgent

Step 1  add_task() reads the title.  title = 'Pay bill' (valid).
Step 2  Priority is read.  'Urgent'.capitalize() gives 'Urgent'.
Step 3  'Urgent' is not in [High, Medium, Low], so the condition is True.
Step 4  The error message is printed and the function returns.
        No date is asked and nothing is saved.

Output on screen:
    Invalid priority. Enter High, Medium or Low.

(b) Invalid date
Input: option 1, title Pay bill, priority High, due date 15-12-2026

Step 1  Title 'Pay bill' and priority 'High' are both valid.
Step 2  Due date is read.  due_date = '15-12-2026'
Step 3  is_valid_date('15-12-2026'): strptime expects a 4-digit year
        first, so it raises ValueError. The except block returns False.
Step 4  if not is_valid_date(...) is True, so the message is printed and
        the function returns. Nothing is saved.

Output on screen:
    Invalid date. Use YYYY-MM-DD.

(c) Task ID not found
Input: option 4, task ID T999

Step 1  User enters 4.  complete_task(tasks) is called.
Step 2  Task ID is read.  'T999'.strip().upper() gives 'T999'.
Step 3  The for loop checks every task. No task has the ID T999, so the
        if condition is never True.
Step 4  After the loop, the not found message is printed.

Output on screen:
    Task T999 not found.

Result: All three outputs match the expected outputs.  PASS

======================================================================
6. TEST CASE 4: DIFFERENT VALID SCENARIO
======================================================================
Initial condition: tasks.txt contains three tasks.

    T101|Submit report|High|2026-10-15|Pending
    T102|Buy milk|Low|2026-10-11|Pending
    T103|Call bank|Medium|2026-10-12|Pending

Loading the file
Step 1  The file text is cut at every newline: 3 task lines and one empty
        piece at the end.
Step 2  Each task line is cut at every pipe symbol and gives exactly 5
        parts, so a dictionary is built and appended.
Step 3  The empty last piece gives only 1 part, so it is skipped.
Step 4  tasks = [T101 Submit report High, T102 Buy milk Low,
        T103 Call bank Medium], all with status Pending.

(a) Option 2: View by priority
Step 1  view_by_priority(tasks). The list has 3 tasks, so the empty
        message is not printed.
Step 2  level = High: T101 (High) matches and is printed; T102 (Low) and
        T103 (Medium) do not.
Step 3  level = Medium: only T103 matches and is printed.
Step 4  level = Low: only T102 matches and is printed.

Output on screen:
    T101 | Submit report | High | 2026-10-15
    T103 | Call bank | Medium | 2026-10-12
    T102 | Buy milk | Low | 2026-10-11

(b) Option 4: Complete task T101
Step 1  complete_task(tasks) reads the ID.  task_id = 'T101'
Step 2  For loop, first task: its id is T101, which equals task_id, so
        the if condition is True.
Step 3  status is set to Done. Only the T101 dictionary changes; T102 and
        T103 stay Pending.
Step 4  save_tasks(tasks) rewrites tasks.txt with all three tasks.
Step 5  count_pending(tasks): T101 is Done (not counted), T102 counts 1,
        T103 counts 2. It returns 2.
Step 6  The message is printed and the function ends.

Output on screen:
    Task T101 marked as done. Pending tasks: 2

tasks.txt after completing T101:
    T101|Submit report|High|2026-10-15|Done
    T102|Buy milk|Low|2026-10-11|Pending
    T103|Call bank|Medium|2026-10-12|Pending

Result: Both outputs match the expected outputs and the other tasks are
unchanged.  PASS

======================================================================
7. EXTRA DRY RUN: NEXT TASK ID
======================================================================
With T101, T102 and T103 already in the list, get_next_task_id(tasks)
works like this:

    Start     biggest = 100
    Pass 1    T101 -> 101 is bigger than 100  -> biggest = 101
    Pass 2    T102 -> 102 is bigger than 101  -> biggest = 102
    Pass 3    T103 -> 103 is bigger than 102  -> biggest = 103

It returns 'T' + str(103 + 1) = T104. IDs never repeat because the new ID
is always one more than the largest existing ID.

======================================================================
8. SUMMARY OF RESULTS
======================================================================
1.  Normal input       Task added with ID T101, status Pending,
                       saved to tasks.txt                        PASS
2.  Boundary input     No tasks gives the all caught up message  PASS
3a. Invalid input      Priority Urgent is rejected               PASS
3b. Invalid input      Date 15-12-2026 is rejected               PASS
3c. Invalid input      ID T999 gives the not found message       PASS
4a. Valid scenario     Tasks shown in High, Medium, Low order    PASS
4b. Valid scenario     T101 marked Done, 2 tasks pending         PASS

Conclusion: The dry run shows that the program gives the expected output
for all four test cases, saves every change to tasks.txt and handles
invalid input without crashing.