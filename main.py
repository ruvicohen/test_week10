from flask import Flask
from app.routes.email_routes import email_blueprint

app = Flask(__name__)

app.register_blueprint(email_blueprint, url_prefix='/api/email')

if __name__ == '__main__':
    app.run()