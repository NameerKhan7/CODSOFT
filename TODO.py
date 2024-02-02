from queue import Queue

class TodoList:
    def __init__(self):
        self.tasks = Queue()

    def add_task(self, task):
        self.tasks.put(task)
        print(f'Task "{task}" added to the to-do list.')

    def complete_task(self):
        if not self.tasks.empty():
            completed_task = self.tasks.get()
            print(f'Task "{completed_task}" marked as completed.')
        else:
            print('No tasks in the to-do list.')

    def view_tasks(self):
        if not self.tasks.empty():
            print('To-Do List:')
            for task in list(self.tasks.queue):
                print(f"- {task}")
        else:
            print('No tasks in the to-do list.')

def main():
    todo_list = TodoList()

    while True:
        print('\nMenu:')
        print('1. Add Task')
        print('2. Complete Task')
        print('3. View Tasks')
        print('4. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.complete_task()
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print('Exiting the To-Do List application.')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
