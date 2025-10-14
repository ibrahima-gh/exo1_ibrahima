#!/usr/bin/env python3
"""Exemples d'utilisation de l'API ToDoList."""

from controllers.task_controller import TaskController

# Initialiser le contrôleur
controller = TaskController()

# Créer des tâches
task1 = controller.create_task("Apprendre Python", "Maîtriser la POO")
task2 = controller.create_task("Faire les courses")
task3 = controller.create_task("Projet urgent", "Deadline demain")

# Lister toutes les tâches
print("📋 Toutes les tâches:")
for task in controller.list_tasks():
    print(f"  {task}")

# Supprimer une tâche
controller.delete_task(task2.id)
print(f"\n🗑️  Tâche {task2.id} supprimée")

# Afficher les tâches restantes
print("\n📋 Tâches restantes:")
for task in controller.list_tasks():
    print(f"  {task}")
