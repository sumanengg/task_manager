from task_manager.manager import TaskManager
from task_manager.models import TaskType

def test_singleton():
    m1 = TaskManager()
    m2 = TaskManager()
    assert m1 is m2, "TaskManager is not a singleton."

def test_create_task():
    manager = TaskManager()
    task = manager.create_task(TaskType.SIMPLE, "Test", "Testing singleton task creation")
    assert task.title == "Test"
    assert task.description == "Testing singleton task creation."

def test_get_task():
    manager = TaskManager()
    task = manager.create_task(TaskType.SIMPLE, "Test-Get-Task", "Testing singleton task creation")
    fetched_task = manager.get_task(task.task_id)
    assert fetched_task is not None
    assert fetched_task.title == "Test-Get-Task"
    assert fetched_task.description == "Testing singleton task creation"

def get_all_task():
    manager = TaskManager()
    Task1 = manager.create_task(TaskType.SIMPLE, "Test-Get-Task1", "Testing singleton task creation")
    Task2 = manager.create_task(TaskType.SIMPLE, "Test-Get-Task2", "Testing singleton task creation")
    all_tasks = manager.get_all_tasks()
    task_title = [t.title for t in all_tasks]
    assert "Test-Get-Task1" in task_title
    assert "Test-Get-Task2" in task_title

def complete_task():
    manager = TaskManager()
    Task1 = manager.create_task(TaskType.SIMPLE, "Test-Get-Task1", "Testing singleton task creation")
    result = manager.complete_task(Task1.task_id)
    assert result is True
    completed_task = manager.get_task(Task1.task_id)
    assert completed_task.status.value == "completed"

def delete_task():
    manager = TaskManager()
    Task1 = manager.create_task(TaskType.SIMPLE, "Test-Get-Task1", "Testing singleton task creation")
    deleted = manager.delete_task(Task1.task_id)
    assert deleted is True



if __name__ == "__main__":
    test_singleton()
    test_create_task()
    test_get_task()
    get_all_task()
    complete_task()
    delete_task()
    print("All tests passed")
