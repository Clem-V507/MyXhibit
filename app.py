from flask import Flask
from controllers.exhibition_controller import exhibition_bp

app = Flask(__name__)
app.register_blueprint(exhibition_bp)

if __name__ == '__main__':
    app.run(debug=True)
