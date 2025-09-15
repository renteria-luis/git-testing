from tasks import add_task, show_tasks, mark_as_completed, delete_task

tasks = []
option = ''
while option != '5':
    print('1. Add a task.')
    print('2. Show tasks.')
    print('3. Mark task as completed.')
    print('4. Delete task.')
    print('5. Exit.')
    option = input('Choose an option from the menu: ')
    print('##########################################')
    
    if option in '12345':

        if option == '1':
            task_to_add = input('What is the new task to add?: ')
            task_completed = input('Is it completed? (Y/N): ').lower()
            if task_completed == 'y':
                task_completed_bool = True
            else:
                task_completed_bool = False
            add_task(tasks, task_to_add, task_completed_bool)
        
        elif option == '2':
            if len(tasks) >= 1:
                show_tasks(tasks)
            else:
                print('!!! MESSAGE: There are no current tasks to show.')
                print('##########################################')


        elif option == '3':
            if len(tasks) >= 1:
                mark_as_completed(tasks)
            else:
                print('!!! MESSAGE: There are no current tasks to show.')
                print('##########################################')

        elif option == '4':
            if len(tasks) >= 1:
                delete_task(tasks)
            else:
                print('!!! MESSAGE: There are no current tasks to show.')
                print('##########################################')


        elif option == '5':
            print('Thank you')
            print('Exiting...')
            print('##########################################')

    else:
        print('!!! MESSAGE: That is not an option.')
        print('##########################################')
