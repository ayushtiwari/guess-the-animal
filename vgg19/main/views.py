from . import main
from flask import render_template, request, jsonify
from PIL import Image

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route('/')
def index():
    return render_template('home.html')


@main.route('/ajax/predict', methods=['POST'])
def predict():
    from ..ml.keras_predict import predict as predict_animal
    if request.files['image'] and request.files['image'].filename != '':
        image = request.files['image']
        image = Image.open(image)
        return jsonify(predict_animal(image))
    return jsonify({'error': 'No image uploaded'})


@main.route('/about')
def about():
    return render_template('about.html')