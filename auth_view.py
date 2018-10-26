from flask import Flask, jsonify, request

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    jwt_refresh_token_required, create_refresh_token,
    get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies
)
import datetime

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'THANOS-was-here'
#app.config['JWT_TOKEN_LOCATION'] = ['query_string']
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['RESTPLUS_VALIDATE'] = True

token_expire = datetime.timedelta(days=0.1)

# HOW TO: ../protected?jwt=<ACCESS_TOKEN>

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username != 'admin' or password != 'admin':
        return jsonify({'login': False}), 401

    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)

    resp = jsonify({'login': True})
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)
    return resp, 200

@app.route('/token/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
 
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    
    resp = jsonify({'refresh': True})
    set_access_cookies(resp, access_token)
    return resp, 200

@app.route('/logout', methods=['POST'])
def logout():
    resp = jsonify({'logout': True})
    unset_jwt_cookies(resp)
    return resp, 200


