"""Gestionnaire de tâches pour la ToDoList."""

import json
from typing import List, Optional
from pathlib import Path

from .task import Task


class TaskManager:
    """Gestionnaire pour les opérations CRUD sur les tâches."""
    
    def __init__(self, data_file: str = "data/tasks.json"):
        self.data_file = Path(data_file)
        self.tasks: List[Task] = []
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        self.load()
    
    def add(self, task: Task):
        """Ajoute une tâche."""
        self.tasks.append(task)
        self.save()
    
    def get(self, task_id: int) -> Optional[Task]:
        """Récupère une tâche par ID."""
        return next((t for t in self.tasks if t.id == task_id), None)
    
    def all(self) -> List[Task]:
        """Retourne toutes les tâches."""
        return self.tasks
    
    def delete(self, task_id: int) -> bool:
        """Supprime une tâche."""
        task = self.get(task_id)
        if task:
            self.tasks.remove(task)
            self.save()
            return True
        return False
    
    def save(self):
        """Sauvegarde les tâches."""
        data = {'tasks': [t.to_dict() for t in self.tasks]}
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def load(self):
        """Charge les tâches."""
        if not self.data_file.exists():
            return
        
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for task_data in data.get('tasks', []):
                task = Task.from_dict(task_data)
                self.tasks.append(task)
                
                if task.id >= Task._next_id:
                    Task._next_id = task.id + 1
        except Exception as e:
            print(f"Erreur chargement: {e}")
