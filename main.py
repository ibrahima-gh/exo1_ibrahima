#!/usr/bin/env python3
"""Point d'entrée principal de l'application ToDoList CLI."""

from controllers.task_controller import TaskController
from views.cli_view import CLIView


def main():
    """Fonction principale."""
    controller = TaskController()
    view = CLIView()
    
    while True:
        view.clear()
        view.show_menu()
        
        choice = view.get_input("Votre choix")
        
        if choice == "0":
            print("\n  Au revoir! 👋\n")
            break
        
        elif choice == "1":
            title = view.get_input("Titre")
            desc = view.get_input("Description (optionnel)")
            task = controller.create_task(title, desc or "")
            view.show_success(f"Tâche créée (ID: {task.id})")
            view.pause()
        
        elif choice == "2":
            tasks = controller.list_tasks()
            view.show_tasks(tasks)
            view.pause()
        
        elif choice == "3":
            try:
                task_id = int(view.get_input("ID de la tâche"))
                if controller.delete_task(task_id):
                    view.show_success("Tâche supprimée")
                else:
                    view.show_error("Tâche introuvable")
            except ValueError:
                view.show_error("ID invalide")
            view.pause()
        
        else:
            view.show_error("Choix invalide")
            view.pause()


if __name__ == "__main__":
    main()
