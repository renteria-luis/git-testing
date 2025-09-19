# These are the functions to make test_git.py file work

def add_task(tasks:list, task_:str, completed_:bool):
    task_dict = {}
    task_dict['task'] = task_
    task_dict['completed'] = completed_
    tasks.append(task_dict)
    print('##########################################')

def show_tasks(tasks:list):
    print('Current tasks:')    
    for i, task_ in enumerate(tasks):
        if task_['completed'] == False:
            print(f"{i}. [ ] {task_['task']}.")
        else:
            print(f"{i}. [✔] {task_['task']}.")
    print('##########################################')

def mark_as_completed(tasks:list):
    show_tasks(tasks)
    try:
        task_to_mark = input('From the list select the number of the task to mark as completed: ')
        tasks[int(task_to_mark)]['completed'] = True
        print('##########################################')
    except (IndexError, ValueError):
        print(f'Task {task_to_mark} does not exist.')
        print('##########################################')

def delete_task(tasks:list):
    show_tasks(tasks)
    try:
        task_to_delete = input('From the list select the number of the task to be deleted: ')
        tasks.pop(int(task_to_delete))
        print('##########################################')
    except (IndexError, ValueError):
        print(f'Task {task_to_delete} does not exist.')
        print('##########################################')