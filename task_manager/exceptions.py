class TaskError(Exception):
    """Base exception for task-related errors."""
    pass

class TaskNotFoundError(TaskError):
    """Raised when a task is not found."""
    pass

class InvalidTaskTypeError(TaskError):
    """Raised when an invalid task type is provided."""
    pass

class TaskAlreadyCompletedError(TaskError):
    """Raised when trying to complete an already completed task."""
    pass

class TaskCreationError(TaskError):
    """Raised when there is an error creating a task."""
    pass