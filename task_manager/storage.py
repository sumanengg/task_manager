from abc import ABC, abstractmethod
from models import Task
from typing import Optional, Any, Dict, List
class Storage(ABC):
    """A class to handle storage operations."""
    @abstractmethod
    def save_task(self, task: Task) -> None:
        pass

    @abstractmethod
    def get_task(self, task_id: str) -> Optional[Task]:
        """Retrieve a task by its ID."""
        pass

    @abstractmethod
    def get_all_tasks(self) -> List[Task]:
        """Retrieve all tasks."""
        pass

    def delete_task(self, task_id: str) -> bool:
        "Remove a task by its ID."
        pass

    def update_task(self, task: Task) -> None:
        """Update a task by its ID."""
        pass


class InMemoryStorage(Storage):
    " A simple in-memory storage implementation for tasks."

    def __init__(self):
        self.tasks: Dict[str, Task] = {}

    def save_task(self, task) -> None:
        self.tasks[task.task_id] = task

    def get_task(self, task_id: str) -> Optional[Task]:
        return self.tasks.get(task_id)
    
    def get_all_tasks(self) -> List[Task]:
        return list(self.tasks.values())
    
    def delete_task(self, task_id) -> bool:
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False
    
    def update_task(self, task: Task) -> None:
        self.tasks[task.task_id] = task

