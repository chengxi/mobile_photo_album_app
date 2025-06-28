
from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Cloud Deployment Note:
# In a production environment, you would use a cloud storage service like AWS S3
# to store uploaded files. You would replace the local file saving logic with
# API calls to your cloud storage provider.

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'success': True, 'filename': filename})

@app.route('/photos', methods=['GET'])
def get_photos():
    # Cloud Deployment Note:
    # When using cloud storage, you would list files from your storage bucket here.
    photos = os.listdir(app.config['UPLOAD_FOLDER'])
    return jsonify(photos)

@app.route('/photos/<filename>')
def get_photo(filename):
    # Cloud Deployment Note:
    # For cloud storage, you would generate a signed URL for the file
    # and redirect the user to that URL.
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    # For local development, we run on 0.0.0.0 to make the server
    # accessible from the Android emulator.
    app.run(host='0.0.0.0', port=5000, debug=True)
