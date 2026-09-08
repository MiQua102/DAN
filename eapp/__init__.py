from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'chuyen_nganh_cntt_2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Abc123@127.0.0.1:3307/hoteldb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app=app)