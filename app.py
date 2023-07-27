from flask import Flask, make_response, request

from sqlalchemy.exc import SQLAlchemyError
from flask_migrate import Migrate

from flask_cors import cross_origin
from flask_cors import CORS

from flasgger import Swagger, swag_from
from decouple import config

from views import auth
from dict_sw import (
    sw_delete,
    sw_create,
    sw_edit,
    sw_list
)

from models import Company
from models import db


def create_app():
    app_conf = Flask(__name__)
    app_conf.config['SQLALCHEMY_DATABASE_URI'] = config('SQLALCHEMY_DATABASE_URI')
    Swagger(app_conf)
    CORS(app_conf, origins=[config('LIST_CORS')])

    db.init_app(app_conf)
    Migrate(app_conf, db)

    return app_conf


app = create_app()


@app.route('/api/create/', methods=['POST'])
@swag_from(sw_create)
@auth.login_required
def create():
    data_json_create = request.get_json()
    cnpj = data_json_create.get('cnpj')
    name_company = data_json_create.get('name_company')
    name_fantasy = data_json_create.get('name_fantasy')
    cnae = data_json_create.get('cnae')
    company = Company(
        name_company=name_company,
        name_fantasy=name_fantasy,
        cnpj=cnpj,
        cnae=cnae
    )

    try:
        company.save()
        return make_response({'success': 'Company created!'}, 201)
    except SQLAlchemyError as err:
        error = str(err.__cause__)
        return make_response({'error': f'Error creating company {error}!'}, 400)


@app.route('/api/list/', methods=['GET'])
@swag_from(sw_list)
@cross_origin()
@auth.login_required
def list_companies():
    page = request.args.get('page', 1, type=int)
    limit = min(request.args.get('limit', 10, type=int), 50)
    order = request.args.get('order', 'name_company', type=str)

    companies = Company.query.order_by(order).all()

    if not companies:
        return make_response({'error': 'Not fund companies'}, 404)

    start = (page - 1) * limit
    end = start + limit
    json_result = [company.to_dict() for company in companies[start:end]]

    return make_response(json_result, 200)


@app.route('/api/edit/', methods=['PUT'])
@swag_from(sw_edit)
@auth.login_required
def edit():
    data_json_edit = request.get_json()
    cnpj = data_json_edit.get('cnpj')
    name_fantasy = data_json_edit.get('name_fantasy')
    cnae = data_json_edit.get('cnae')

    company = Company.query.filter_by(cnpj=cnpj).first()

    if not company:
        return make_response({'error': 'Company not found!'}, 404)

    if name_fantasy and cnae:
        company.name_fantasy = name_fantasy
        company.cnae = cnae
    else:
        error_messages = []
        if not name_fantasy:
            error_messages.append('name_fantasy is required')
        if not cnae:
            error_messages.append('cnae is required')

        if error_messages:
            return make_response({'error': error_messages}, 400)

    try:
        company.save()
        return make_response({'success': 'Company updated!'}, 200)
    except SQLAlchemyError as err:
        error = str(err.__cause__)
        return make_response({'error': f'Error updating company {error}!'}, 400)


@app.route('/api/delete/', methods=['DELETE'])
@swag_from(sw_delete)
@auth.login_required
def delete():
    data_json_delete = request.get_json()
    cnpj = data_json_delete.get('cnpj')

    company = Company.query.filter_by(cnpj=cnpj).first()

    if not company:
        return make_response({'error': 'Company not found!'}, 404)

    try:
        db.session.delete(company)
        db.session.commit()
        return make_response({'success': 'Company deleted!'}, 200)
    except SQLAlchemyError as err:
        error = str(err.__cause__)
        return make_response({'error': f'Error deleting company {error}!'}, 400)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(config('PORT')))
