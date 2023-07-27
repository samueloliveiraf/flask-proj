from flask_sqlalchemy import SQLAlchemy
from flask import abort

from views import validate_cnpj

db = SQLAlchemy()


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_company = db.Column(db.String(255), nullable=False)
    name_fantasy = db.Column(db.String(255), nullable=True)
    cnpj = db.Column(db.String(50), nullable=False, unique=True)
    cnae = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'name_company': self.name_company,
            'name_fantasy': self.name_fantasy,
            'cnpj': self.cnpj,
            'cnae': self.cnae,
        }

    def save(self):
        if not validate_cnpj(self.cnpj):
            abort(400, "The CNPJ provided is invalid.")
        db.session.add(self)
        db.session.commit()
