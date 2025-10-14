"""Interface CLI pour la ToDoList."""

import os


class CLIView:
    """Vue en ligne de commande pour interagir avec la ToDoList."""
    
    @staticmethod
    def clear():
        """Efface l'écran."""
        os.system('clear' if os.name != 'nt' else 'cls')
    
    @staticmethod
    def show_menu():
        """Affiche le menu principal."""
        print("\n" + "="*50)
        print("  📝 ToDoList CLI")
        print("="*50)
        print("  1. Ajouter une tâche")
        print("  2. Lister les tâches")
        print("  3. Supprimer une tâche")
        print("  0. Quitter")
        print("="*50)
    
    @staticmethod
    def get_input(prompt: str) -> str:
        """Récupère une saisie utilisateur."""
        return input(f"  {prompt}: ").strip()
    
    @staticmethod
    def show_tasks(tasks):
        """Affiche la liste des tâches."""
        print("\n" + "="*50)
        print("  Liste des tâches")
        print("="*50)
        if not tasks:
            print("  Aucune tâche")
        else:
            for task in tasks:
                print(f"  {task}")
        print("="*50)
    
    @staticmethod
    def show_success(msg: str):
        """Affiche un message de succès."""
        print(f"\n  ✅ {msg}")
    
    @staticmethod
    def show_error(msg: str):
        """Affiche un message d'erreur."""
        print(f"\n  ❌ {msg}")
    
    @staticmethod
    def pause():
        """Pause."""
        input("\n  Appuyez sur Entrée...")
