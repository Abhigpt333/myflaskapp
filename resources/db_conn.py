from flask import request
from flask_restful import Resource
import models.db as db
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_claims, get_raw_jwt
from werkzeug.security import safe_str_cmp
from blacklist import BLACKLIST

class UserRegister(Resource):
    def post(self):
        data = request.get_json()
        if db.find_user_by_username(data["username"]):
            return{'message': "An user with '{}' already exists".format(data["username"])}
        else:
            user = {
                "username": data["username"],
                "password": data["password"]
            }
            db.insert_user_by_username(user)
            return {'message': "User has been created with username {}".format(data["username"])}


class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        user =  db.find_user_by_username(data["username"])
        if user and safe_str_cmp(user["password"], data["password"]):
            access_token = create_access_token(identity=user['id'], fresh=True)
            refresh_token = create_refresh_token(user['id'])
            return{'message': "You are authenticated",
                   'access_token': access_token,
                   'refresh_token': refresh_token
                   }, 200
        else:
            return{'message': "Invalid Credentials"}, 403

class UserLogout(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        BLACKLIST.add(jti)
        return {'message': "Successfully Logged Out"}

class Item(Resource):
    @jwt_required
    def get(self, name):
        item = db.find_item_by_name(name)
        if item:
            return item
        return {"message": "Item Not found"}, 404

    @jwt_required
    def post(self, name):

        if db.find_item_by_name(name):
            return {'message': "An item with '{}' already exists".format(name)}, 400

        data = request.get_json()
        item = {
            "name": name,
            "price": data["price"]
        }
        db.insert_item_by_name(item)
        return item, 201

    @jwt_required
    def delete(self, name):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin Privilege is required'}, 401
        if db.find_item_by_name(name):
            db.delete(name)
            return {"message" : "Item deleted"}
        return {'message': "Item not found"}, 401

    @jwt_required
    def put(self, name):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin Privilege is required'}, 401
        data = request.get_json()
        item = db.find_item_by_name(name)
        new_item = {
            "name": name,
            "price": data["price"]
        }
        if item is None:
            db.insert_item_by_name(new_item)
            return new_item
        else:
            db.update_item(new_item)
        return new_item
class ItemsList(Resource):
    @jwt_required
    def get(self):
        item = db.get_all()
        return {"items" : item}

class UsersList(Resource):
    @jwt_required
    def get(self):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message': 'Admin Privilege is required'}, 401
        user = db.get_all_users()
        return {"users" : user}