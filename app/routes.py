from flask import Blueprint, render_template, request, redirect, url_for
from app.api_integration import handle_translation, handle_tts
import os

api_routes = Blueprint('api_routes', __name__)

# Ensure 'uploads' folder exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

@api_routes.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@api_routes.route('/create-course', methods=['POST'])
def create_course():
    course_title = request.form['courseTitle']
    course_content = request.form['courseContent']
    language = request.form['language']
    add_voiceover = 'addVoiceover' in request.form

    # Handle image upload
    image_path = None
    image_file = request.files['uploadImage']
    if image_file and image_file.filename != '':
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
        image_file.save(image_path)

    # Call Translation API
    translated_text = handle_translation(course_content, language)

    # Optionally, call TTS API for voiceover
    voiceover_file = None
    if add_voiceover:
        voiceover_file = handle_tts(translated_text, language)

    return render_template('result.html', 
                           title=course_title, 
                           content=translated_text, 
                           voiceover=voiceover_file_path,
                           image_path=image_path)  # Pass image path to template
