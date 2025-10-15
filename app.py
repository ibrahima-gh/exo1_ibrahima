#!/usr/bin/env python3
"""Application Flask pour la ToDoList - API uniquement."""

from flask import Flask, jsonify, request
from controllers.task_controller import TaskController

# Initialiser Flask
app = Flask(__name__)

# Initialiser le contrôleur
controller = TaskController()


@app.route('/')
def index():
    """Page d'accueil simple."""
    return jsonify({
        'message': 'ToDoList API en cours de fonctionnement',
        'routes': [
            {'method': 'GET', 'path': '/tasks'},
            {'method': 'POST', 'path': '/tasks'},
            {'method': 'GET', 'path': '/tasks/<id>'},
            {'method': 'PUT', 'path': '/tasks/<id>'},
            {'method': 'DELETE', 'path': '/tasks/<id>'}
        ]
    })


@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Récupérer toutes les tâches."""
    tasks = controller.list_tasks()
    return jsonify([{
        'id': task.id,
        'title': task.title,
        'created_at': task.created_at.isoformat()
    } for task in tasks])


@app.route('/tasks', methods=['POST'])
def create_task():
    """Créer une nouvelle tâche."""
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({'error': 'Titre requis'}), 400
    
    title = data['title'].strip()
    
    if not title:
        return jsonify({'error': 'Titre ne peut pas être vide'}), 400
    
    try:
        task = controller.create_task(title)
        return jsonify({
            'id': task.id,
            'title': task.title,
            'created_at': task.created_at.isoformat()
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Récupérer une tâche spécifique."""
    task = controller.get_task(task_id)
    if task:
        return jsonify({
            'id': task.id,
            'title': task.title,
            'created_at': task.created_at.isoformat()
        })
    else:
        return jsonify({'error': 'Tâche introuvable'}), 404


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Modifier une tâche."""
    data = request.get_json()
    
    if not data:
        return jsonify({'error': 'Données requises'}), 400
    
    task = controller.get_task(task_id)
    if not task:
        return jsonify({'error': 'Tâche introuvable'}), 404
    
    try:
        # Mettre à jour le titre
        if 'title' in data:
            task.title = data['title'].strip()
        
        if not task.title:
            return jsonify({'error': 'Titre ne peut pas être vide'}), 400
        
        return jsonify({
            'id': task.id,
            'title': task.title,
            'created_at': task.created_at.isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Supprimer une tâche."""
    try:
        if controller.delete_task(task_id):
            return jsonify({'message': 'Tâche supprimée'}), 200
        else:
            return jsonify({'error': 'Tâche introuvable'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    print("🚀 ToDoList API en cours de fonctionnement...")
    print("📱 API disponible sur : http://localhost:8000")
    app.run(debug=True, host='0.0.0.0', port=8000)