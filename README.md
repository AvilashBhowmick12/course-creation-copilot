# Course Creation Copilot

This Flask application helps you create course content by providing translation and text-to-speech (TTS) functionality.

## Features

- **Translate course content:** Translate your course materials into different languages using Google Translate API.
- **Generate voiceovers:** Add voiceovers to your course content using either Google Cloud Text-to-Speech or Sarvam TTS API.
- **Image upload:** Include images with your course content.

## Project Setup

These instructions assume you are using a Unix-like terminal (macOS, Linux, or Cloud Shell).

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AvilashBhowmick12/course-creation-copilot.git
   cd course-creation-copilot
2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv env
    source env/bin/activate

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Set up API keys and credentials:**

 - Google Cloud Platform:

 - - Create a project on Google Cloud Platform.
 - - Enable the Translation and Text-to-Speech APIs.
 - - Download the JSON credentials file for your project.
 - - Set the GOOGLE_APPLICATION_CREDENTIALS environment variable:
    ```bash
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
(Replace /path/to/your/credentials.json with the actual path to your downloaded JSON file)
 - - Sarvam TTS (optional):

- - Obtain an API key from Sarvam.
- - Set the SARVAM_API_KEY environment variable:
    ```bash
    export SARVAM_API_KEY="your_sarvam_api_key"

5. **Run the application:**

    ```bash
    export FLASK_APP=app.py
    flask run
6. **Access the application: Open a web browser and go to `http://127.0.0.1:5000/.`**

Usage
Enter your course title and content in the provided fields.
Select the desired target language.
Choose whether to add a voiceover.
Optionally, upload an image.
Click "Create Course".
The application will translate the content, generate a voiceover (if selected), and display the results.

## File Structure

course-creation-copilot/
│
├── app/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── script.js
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   ├── routes.py
│   ├── api_integration.py
│   └── utils.py
│
├── config/
│   └── settings.py
│
├── venv/
│   └── (virtual environment files)
│
├── requirements.txt
├── app.py
├── README.md
└── .gitignore


Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
MIT

**Remember to replace the placeholder values (e.g., API keys, paths) with your actual information.**
