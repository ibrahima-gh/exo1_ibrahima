"""Contrôleur pour gérer la logique de l'application ToDoList."""

from models.task import Task


class TaskController:
    """Contrôleur pour gérer les opérations sur les tâches."""
    
    def create_task(self, title: str) -> Task:
        """Crée une tâche."""
        return Task.create(title)
    
    def list_tasks(self):
        """Liste toutes les tâches."""
        return Task.all()
    
    def get_task(self, task_id: int):
        """Récupère une tâche."""
        return Task.get(task_id)
    
    def delete_task(self, task_id: int) -> bool:
        """Supprime une tâche."""
        return Task.delete(task_id)