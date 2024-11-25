from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import io
from db.dbConnect import get_db_connection
from ftplib import FTP, all_errors, error_perm  # Importar ftplib y all_errors

app = Flask(__name__)
CORS(app)

ftp = FTP()

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the FTP server API"}), 200

@app.route('/connect', methods=['POST'])
def connect():
    data = request.get_json()
    print("Datos recibidos:", data)

    server = data['server']
    username = data['username']
    password = data['password']
    
    if not username or not password:
        return jsonify({"status": "Username and password are required"}), 400
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    
    if result and result[0] == password:
        try:
            ftp.connect(server, 2121)
            ftp.login(username, password)
            return jsonify({"status": "Login successful"}), 200
        except all_errors as e:
            return jsonify({"status": str(e)}), 500
    else:
        return jsonify({"status": "Invalid credentials"}), 401

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'status': 'No file selected'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'status': 'No file selected'}), 400
    
    file_path = os.path.join('files', file.filename)
    file.save(file_path)
    return jsonify({'status': 'File uploaded successfully'}), 200

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    filename = data.get('filename')
    if not filename:
        return jsonify({'status': 'No filename specified'}), 400
    
    file_path = os.path.join('files', filename)
    if not os.path.exists(file_path):
        return jsonify({'status': 'File not found'}), 404
    
    return send_file(file_path, as_attachment=True, download_name=filename)

@app.route('/list_files', methods=['GET'])
def list_files():
    try:
        ftp.cwd('/files')
        files = ftp.nlst()
        return jsonify({"files": files}), 200
    except error_perm as e:
        print("Error al listar los archivos:", e)
        return jsonify({"status": f"Error: {str(e)}"}), 500

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({"message": "User added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)