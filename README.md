# 📝 ToDoList Flask API

API REST Flask pour gérer des tâches.

## 🚀 Installation

```bash
pip install Flask
```

## 🎯 Utilisation

```bash
python3 app.py
```

API disponible sur : **http://localhost:8000**

## 📋 Routes API

| Méthode | Route | Description |
|---------|-------|-------------|
| `GET` | `/` | Statut de l'API |
| `GET` | `/tasks` | Lister toutes les tâches |
| `POST` | `/tasks` | Créer une tâche |
| `GET` | `/tasks/<id>` | Récupérer une tâche |
| `PUT` | `/tasks/<id>` | Modifier une tâche |
| `DELETE` | `/tasks/<id>` | Supprimer une tâche |

## 💻 Exemples

### Lister les tâches
```bash
curl http://localhost:8000/tasks
```

### Créer une tâche
```bash
curl -X POST http://localhost:8000/tasks \
     -H "Content-Type: application/json" \
     -d '{"title": "Ma tâche"}'
```

### Modifier une tâche
```bash
curl -X PUT http://localhost:8000/tasks/1 \
     -H "Content-Type: application/json" \
     -d '{"title": "Nouveau titre"}'
```

### Supprimer une tâche
```bash
curl -X DELETE http://localhost:8000/tasks/1
```

## ⚠️ Note

Données en mémoire (redémarrage = perte des données)