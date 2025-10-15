# 📝 ToDoList CLI

Application CLI pour gérer des tâches en Python avec architecture MVC.

## 🚀 Installation

```bash
# Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt
```

## 🎯 Utilisation

```bash
python3 main.py
```

## 📋 Fonctionnalités

1. Ajouter une tâche
2. Lister les tâches  
3. Supprimer une tâche

## 🏗️ Architecture MVC

- **Models** : Task, TaskManager
- **Views** : CLIView
- **Controllers** : TaskController

## 💻 API

```python
from controllers.task_controller import TaskController

controller = TaskController()
task = controller.create_task("Ma tâche", "Description")
controller.delete_task(1)
```

## 📦 Dépendances

- **click** : Gestion des arguments CLI
- **rich** : Affichage coloré et formaté
- **colorama** : Couleurs cross-platform