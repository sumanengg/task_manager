from enum import Enum
import uuid
from datetime import datetime
from abc import ABC, abstractmethod
from typing import Dict, Optional, Any

class TaskStatus(Enum):
    COMPLETED = "completed"
    CANCENLED = "canceled"
    IN_PROGRESS = "in_progress"
    PENDING = "pending"

class TaskType(Enum):
    SIMPLE = "simple"
    PRIORITY = "priority"
    RECURRING = "recurring"

class Task(ABC):
    "Abstruct class for Task creation"

    def __init__(self, title: str, description: str):
        self.task_id = str(uuid.uuid4())[:8]
        self.title = title
        self.description = description
        self.status = TaskStatus.PENDING
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @abstractmethod
    def get_task_type(self) -> TaskType:
        pass

    def mark_completed(self):
        self.status = TaskStatus.COMPLETED
        self.updated_at = datetime.now()
    
    def mark_in_progress(self):
        self.status = TaskStatus.IN_PROGRESS
        self.updated_at = datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        return {
            'task_id': self.task_id,
            'title': self.title,
            'description': self.description,
            'status': self.status.value,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'type': self.get_task_type().value
        }
    
    def __str__(self):
        return f"Task({self.task_id}): {self.title} [{self.status.value}]"
    
class SimpleTask(Task):
    "Basic Simple Task"

    def get_task_type(self) -> TaskType:
        return TaskType.value
    
class PriorityTask(Task):
    "Task with Prority"

    def __init__(self, title: str, description: str="", priority: int=1):
        super.__init__(title, description)
        self.priority = priority

    def get_task_type(self) -> TaskType:
        return TaskType.PRIORITY
    
    def to_dict(self) -> Dict[str, Any]:
        data = super.to_dict()
        data["priority"] = self.priority
    
    def __str__(self):
        return f"PriorityTask({self.id}): {self.title} [Priority: {self.priority}, Status: {self.status.value}]"

class RecurringTask(Task):
    "Task that repeats at a set interval"
    def __init__(self, title: str, description: str="", frequency: str="daily"):
        super().__init__(title, description)
        self.frequency = frequency

    def get_task_type(self) -> TaskType:
        return TaskType.RECURRING
    
    def to_dict(self) -> Dict[str, Any]:
        data = super().to_dict()
        data["frequency"] = self.frequency
        return data
    
    def __str__(self):
        return f"RecurringTask({self.id}): {self.title} [Frequency: {self.frequency}, Status: {self.status.value}]"
        
class TaskFactory:
    "Factory class for creating tasks"

    @staticmethod
    def create_task(task_type: TaskType, title: str, description: str = "", **kwargs) -> Task:
        if task_type == TaskType.SIMPLE:
            return SimpleTask(title, description)
        elif task_type == TaskType.PRIORITY:
            return PriorityTask(title, description, kwargs.get('priority', 1))
        elif task_type == TaskType.RECURRING:
            return RecurringTask(title, description, kwargs.get('frequency', 'daily'))
        else:
            raise ValueError(f"Unknown task type: {task_type}")


