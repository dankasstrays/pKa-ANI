from flask import Flask, request, jsonify
import os
from pkaani.pkaani import calculate_pka
from pkaani import prep_pdb

application = Flask(__name__)

# Ensure the upload folder exists
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Root route

# device to run the training
device = torch.device('cpu')

print("Loading pKa-ANI Models and ANI-2x...")
#FEATURES
tyr_features=joblib.load(os.path.join(os.path.dirname(__file__),'pkaani/models/FTYR.joblib'))
asp_features=joblib.load(os.path.join(os.path.dirname(__file__),'pkaani/models/FASP.joblib'))
glu_features=joblib.load(os.path.join(os.path.dirname(__file__),'pkaani/models/FGLU.joblib'))
lys_features=joblib.load(os.path.join(os.path.dirname(__file__),'pkaani/models/FLYS.joblib'))
his_features=joblib.load(os.path.join(os.path.dirname(__file__),'pkaani/models/FHIS.joblib'))

#MODELS
asp_model=joblib.load(os.path.join(os.path.dirname(__file__),'pkaani/models/ASP_ani2x_FINAL_MODEL_F100.joblib'))
glu_model=joblib.load(os.path.join(os.path.dirname(__file__),'pkaani/models/GLU_ani2x_FINAL_MODEL_F75.joblib'))
his_model=joblib.load(os.path.join(os.path.dirname(__file__),'pkaani/models/HIS_ani2x_FINAL_MODEL_F100.joblib'))
lys_model=joblib.load(os.path.join(os.path.dirname(__file__),'pkaani/models/LYS_ani2x_FINAL_MODEL_F25.joblib'))
tyr_model=joblib.load(os.path.join(os.path.dirname(__file__),'pkaani/models/TYR_ani2x_FINAL_MODEL_F25.joblib'))

#######################################################################        
#call ani

ani = torchani.models.ANI2x(periodic_table_index=True)
print('Finished Loading.')



@application.route('/')
def home():
    return "Your application is successfully deployed and running!"


@application.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    prep_pdb(file_path)
    pka = calculate_pka([file_path], ani)

    if pka is not None:
        os.remove(file_path)
        base_name = file.filename.rsplit(".", 1)[0]
        pdb_cp = base_name+"_0.pdb"
        base_path = os.path.join(UPLOAD_FOLDER, pdb_cp) 
        os.remove(base_path)

        
        

    for key in pka:
        return str(pka[key])

if __name__ == '__main__':
    application.run(debug=True)

