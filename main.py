from flask import Flask
from app.db.models import SuspiciousExplosiveContent, SuspiciousHostageContent, Location, UserQuote,DeviceInfo
from app.db.psql_db import create_db, create_tables
from app.routes.user_quote_route import email_blueprint

app = Flask(__name__)

app.register_blueprint(email_blueprint, url_prefix='/api/email')

if __name__ == '__main__':
    #create_db()
    #create_tables()
    app.run()