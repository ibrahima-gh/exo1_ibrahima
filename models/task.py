"""Modèle de tâches pour la ToDoList - Version simplifiée en mémoire."""

from datetime import datetime
from typing import List, Optional


class Task:
    """Classe représentant une tâche."""
    
    _next_id: int = 1
    _tasks: List['Task'] = []
    
    def __init__(self, title: str, task_id: Optional[int] = None):
        self.id = task_id if task_id else Task._next_id
        if task_id and task_id >= Task._next_id:
            Task._next_id = task_id + 1
        else:
            Task._next_id += 1
            
        self.title = title
        self.created_at = datetime.now()
    
    @classmethod
    def create(cls, title: str) -> 'Task':
        """Crée et ajoute une nouvelle tâche."""
        task = cls(title)
        cls._tasks.append(task)
        return task
    
    @classmethod
    def get(cls, task_id: int) -> Optional['Task']:
        """Récupère une tâche par ID."""
        return next((t for t in cls._tasks if t.id == task_id), None)
    
    @classmethod
    def all(cls) -> List['Task']:
        """Retourne toutes les tâches."""
        return cls._tasks.copy()
    
    @classmethod
    def delete(cls, task_id: int) -> bool:
        """Supprime une tâche."""
        task = cls.get(task_id)
        if task:
            cls._tasks.remove(task)
            return True
        return False
    
    def __str__(self) -> str:
        return f"[{self.id}] {self.title}"