"""Contrôleur pour gérer la logique de l'application ToDoList."""

from models.task import Task
from models.task_manager import TaskManager


class TaskController:
    """Contrôleur pour gérer les opérations sur les tâches."""
    
    def __init__(self):
        self.manager = TaskManager()
    
    def create_task(self, title: str, description: str = "") -> Task:
        """Crée une tâche."""
        task = Task(title, description)
        self.manager.add(task)
        return task
    
    def list_tasks(self):
        """Liste toutes les tâches."""
        return self.manager.all()
    
    def get_task(self, task_id: int):
        """Récupère une tâche."""
        return self.manager.get(task_id)
    
    def delete_task(self, task_id: int) -> bool:
        """Supprime une tâche."""
        return self.manager.delete(task_id)
