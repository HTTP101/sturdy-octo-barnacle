from flask_jwt_extended import create_access_token,JWTManager
from flask import jsonify
from application import app
from application.models.UserMaster import UserMaster
from application.config.config import Config
conf = Config()
app.config['JWT_SECRET_KEY'] =  conf.JWT_SECRET_KEY
app.config['PROPAGATE_EXCEPTIONS'] = True
jwt = JWTManager(app=app)

@jwt.expired_token_loader
def expired_token_callback(expired_token):
    print("Ex")
    token_type = expired_token['type']
    return jsonify({
        'success': 0,
        'message': 'The {} token has expired'.format(token_type)
    }), 401

@jwt.invalid_token_loader
def invalid_token_callback(reason):
    print("Inv")
    return jsonify({
        'success':0,
        'message':"The Given Token Is Invalid",
        'info':reason
    }),422

@jwt.unauthorized_loader
def unauthorized_loader_callback(reason):
    print("Unauth")
    return jsonify({
        'success':0,
        'message':"There is no Authorization Header in the request",
        'info':reason
    }),401








