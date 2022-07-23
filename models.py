from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

GENERIC_IMAGE = "https://image.shutterstock.com/z/stock-vector-character-cartoon-basic-animals-dog-cat-rat-pig-porcupine-rabbit-chicken-duck-pigeon-384302530.jpg"

class Pet(db.Model):
    
    __tablename__ = "pets"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        return self.photo_url or GENERIC_IMAGE


def connect_db(app):
    db.app = app
    db.init_app(app)