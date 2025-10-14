"""Modèle de tâches pour la ToDoList."""

from datetime import datetime
from typing import Optional


class Task:
    """Classe représentant une tâche."""
    
    _next_id: int = 1
    
    def __init__(self, title: str, description: str = "", task_id: Optional[int] = None):
        self.id = task_id if task_id else Task._next_id
        if task_id and task_id >= Task._next_id:
            Task._next_id = task_id + 1
        else:
            Task._next_id += 1
            
        self.title = title
        self.description = description
        self.created_at = datetime.now()
    
    def to_dict(self) -> dict:
        """Convertit la tâche en dictionnaire."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        """Crée une tâche depuis un dictionnaire."""
        task = cls(
            title=data['title'],
            description=data.get('description', ''),
            task_id=data.get('id')
        )
        if 'created_at' in data:
            task.created_at = datetime.fromisoformat(data['created_at'])
        return task
    
    def __str__(self) -> str:
        return f"[{self.id}] {self.title}"
