import os

from flask import Flask, render_template, request

# Import table definitions.
from models import *

app = Flask(__name__)

# Tell Flask what SQLAlchemy databas to use.
#mysql+mysqlconnector://sql7714366:RHN8d4F6p6@sql7.freesqldatabase.com:3306/sql7714366
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:@localhost:3307/qrconnect"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Link the Flask app with the database (no Flask app is actually being run yet).
db.init_app(app)

def main():
  # Create tables based on each table definition in `models`
  db.create_all()
  db.session.commit()
  print("tables were created")
if __name__ == "__main__":
  # Allows for command line interaction with Flask application
  with app.app_context():
      main()
