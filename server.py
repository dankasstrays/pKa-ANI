from flask import Flask, request, jsonify
import os
from pkaani.pkaani import calculate_pka

app = Flask(__name__)

# Ensure the upload folder exists
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Root route


@app.route('/')
def home():
	return "Your app is successfully deployed and running!"


@app.route('/upload', methods=['POST'])
def upload_file():
	if 'file' not in request.files:
		return jsonify({"error": "No file part"}), 400

	file = request.files['file']

	if file.filename == '':
		return jsonify({"error": "No selected file"}), 400

	file_path = os.path.join(UPLOAD_FOLDER, file.filename)
	file.save(file_path)

	pka = calculate_pka([file_path])

	if pka is not None:
		os.remove(file_path)

	for key in pka:
		return str(pka[key])

if __name__ == '__main__':
	app.run(debug=True)

