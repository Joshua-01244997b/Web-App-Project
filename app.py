from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)

# In a real application, you would use a database
# For this example, we'll use a simple list
notes = [
    "my name is daniel",
    "atu is my 17th choice",
    "This is a sample note from the web app"
]

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/save_note', methods=['POST'])
def save_note():
    note_text = request.json.get('note')
    if note_text and note_text.strip():
        notes.append(note_text.strip())
        return jsonify({'success': True, 'message': 'Note saved successfully!'})
    return jsonify({'success': False, 'message': 'Note cannot be empty!'})

@app.route('/delete_note/<int:index>', methods=['DELETE'])
def delete_note(index):
    if 0 <= index < len(notes):
        deleted_note = notes.pop(index)
        return jsonify({'success': True, 'message': f'Note deleted: {deleted_note}'})
    return jsonify({'success': False, 'message': 'Invalid note index!'})

@app.route('/update_note/<int:index>', methods=['PUT'])
def update_note(index):
    new_text = request.json.get('note')
    if 0 <= index < len(notes) and new_text and new_text.strip():
        notes[index] = new_text.strip()
        return jsonify({'success': True, 'message': 'Note updated successfully!'})
    return jsonify({'success': False, 'message': 'Invalid request!'})

if __name__ == '__main__':
    app.run(debug=True)