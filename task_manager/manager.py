from abc import ABC, abstractmethod
from models import TaskFactory, Task, TaskType
from storage import InMemoryStorage, Storage
from typing import List

class TaskManager:
    """
    It do all the operation.
    For data consistency using singlenton.
    """
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaskManager, cls).__new__(cls)
            cls._instance._initialize = False
        return cls._instance

    def __init__(self):
        if self._initialize:
            return
        self.factory = TaskFactory()
        self.storage: Storage = InMemoryStorage()
        self._initialize = True

    def create_task(self, task_type: TaskType, title: str, description: str = "", **kwargs) -> Task:
        "Create the task"
        task = self.factory.create_task(task_type, title=title, description=description, **kwargs)
        self.storage.save_task(task)
        return task
    
    def get_task(self, task_id: int) -> Task:
        "Get the task using task_id"
        return self.storage.get_task(task_id=task_id)

    def get_all_tasks(self) -> List[Task]:
        "Get all task from storage"
        return self.storage.get_all_tasks()
    
    def complete_task(self, task_id: int) -> bool:
        "Complete a task and update it status"
        task = self.storage.get_task(task_id)
        if task:
            task.mark_completed()
            self.storage.update_task(task=task)
            return True
        return False
    
    def search_task(self, keyword: str) -> Task:
        "Search task depend on keyword. Assuming keyword should be the title or description"
        keyword = keyword.lower()
        return [task for task in self.get_all_tasks() 
                if keyword in task.title.lower() or keyword in task.description.lower()]
    
    def delete_task(self, task_id) -> bool:
        "Delete task."
        return self.storage.delete_task(task_id)