from flask import Flask, render_template
from .routes import api_routes  # Use '.' for relative import within the package

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'  # Configure upload folder

# Register Blueprints
app.register_blueprint(api_routes)

if __name__ == "__main__":
    app.run(debug=True)
