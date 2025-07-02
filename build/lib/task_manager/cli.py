from task_manager.manager import TaskManager
from task_manager.models import TaskType
class TaskManagerCli:

    def __init__(self):
        self.manager = TaskManager()


    def run(self):
        "Main Cli functionality."
        print("############ Cli ################")
        print("If you wanna to quit type 'quit' or 'exit', for help type 'help'")

        while True:
            try:
                command = input("\n> ").strip().lower()
                
                if command == "quit" or command == "exit":
                    break
                elif command == "help":
                    self.show_help()
                elif command == "add":
                    self.add_task()
                elif command == "list":
                    self.list_tasks()
                elif command.startswith("complete"):
                    self.complete_task(command)
                elif command.startswith("delete"):
                    self.delete_task(command)
                else:
                    print("Unknown command: type help for available commands")
            except KeyboardInterrupt:
                print("\n GoodBye")
                break
            except Exception as e:
                print(f"Error: {e}")

    def show_help(self):
        """Display help information"""
        help_text = """
Available commands:
- add              : Add a new task
- list             : List all tasks
- complete <id>    : Mark task as completed
- delete <id>      : Delete a task
- search <keyword> : Search tasks
- help             : Show this help
- quit/exit        : Exit the program
        """
        print(help_text)
    
    def add_task(self):
        """Add a new task"""
        print("\n=== Add New Task ===")
        title = input("Task title: ").strip()
        if not title:
            print("Title cannot be empty!")
            return
        
        description = input("Description (optional): ").strip()
        
        print("Task types:")
        print("1. Simple Task")
        print("2. Priority Task")
        print("3. Recurring Task")
        
        choice = input("Choose task type (1-3): ").strip()
        
        try:
            if choice == '1':
                task = self.manager.create_task(TaskType.SIMPLE, title, description)
            elif choice == '2':
                priority = int(input("Priority (1=Low, 2=Medium, 3=High): "))
                task = self.manager.create_task(TaskType.PRIORITY, title, description, priority=priority)
            elif choice == '3':
                frequency = input("Frequency (daily/weekly/monthly): ").strip()
                task = self.manager.create_task(TaskType.RECURRING, title, description, frequency=frequency)
            else:
                print("Invalid choice!")
                return
            
            print(f"Task created: {task}")
        
        except ValueError as e:
            print(f"Error: {e}")
    
    def list_tasks(self):
        """List all tasks"""
        tasks = self.manager.get_all_tasks()
        if not tasks:
            print("No tasks found.")
            return
        
        print(f"\n=== All Tasks ({len(tasks)}) ===")
        for task in tasks:
            print(task)
    
    def complete_task(self, command: str):
        """Complete a task"""
        parts = command.split()
        if len(parts) != 2:
            print("Usage: complete <task_id>")
            return
        
        task_id = parts[1]
        if self.manager.complete_task(task_id):
            print(f"Task {task_id} marked as completed!")
        else:
            print(f"Task {task_id} not found.")
    
    def delete_task(self, command: str):
        """Delete a task"""
        parts = command.split()
        if len(parts) != 2:
            print("Usage: delete <task_id>")
            return
        
        task_id = parts[1]
        if self.manager.delete_task(task_id):
            print(f"Task {task_id} deleted!")
        else:
            print(f"Task {task_id} not found.")

def main():
    cli = TaskManagerCli()
    cli.run()


if __name__ == "__main__":
    try:
        "cli will run this main()"
        main()
    except Exception as e:
        print(f"Error: {e}")
        raise Exception