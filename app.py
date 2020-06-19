from flask import Flask, jsonify
from flask_restful import Resource, Api
import models.create_table
from resources.db_conn import Item, ItemsList, UsersList, UserRegister, UserLogin, UserLogout
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_SECRET_KEY'] = 'abhi'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
api = Api(app)
jwt = JWTManager(app)

@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 2:
        return{'is_admin': True}
    return {'is_admin': False}

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decryted_token):
    return decryted_token['jti'] in BLACKLIST


@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'description': "The Token Has Expired",
        'error': "token_expired"
    }), 401

@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        'description': "The Token has been rovoked",
        'error': "token_revoked"
    }), 401

api.add_resource(UserRegister, '/register')
api.add_resource(UsersList, '/users')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemsList, '/items')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')

app.run(port=5000, debug=True)
