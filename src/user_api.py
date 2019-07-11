from flask import Blueprint, Response, request
import json

user_api = Blueprint('user_api', __name__, url_prefix = '/user')

users = [{
        'name':'Cebestian',
        'age':32,
        'city':'Texas'
    },{
        'name':'Scarlet',
        'age':29,
        'city':'California'
    },{
        'name':'Chris',
        'age':23,
        'city':'San Fransisco'
    }]

@user_api.route('/', methods=['GET'])
def getUsers():
    """
    Endpoint returning a list of users
    ---
    tags:
      - User
    responses:
      200:
        description: A list of user 
    """
    return Response(json.dumps(users), content_type='application/json')

@user_api.route('/<name>', methods=['GET'])
def getUserByName(name):
    """
    Endpoint returning an object of user filtered by given name
    ---
    tags:
      - User
    parameters:
      - name: name
        in: path
        type: string
        required: true
    responses:
      200:
        description: An object of user 
    """
    resp = {
        'status': 'failure',
        'message': 'could not found user by name : ' + name
    }
    for u in users:
        if u['name'] == name:
            resp = u
    return Response(json.dumps(resp), content_type='application/json')

@user_api.route('/', methods=['POST'])
def newUser():
    """
    Endpoint to create new user
    ---
    tags:
      - User
    parameters:
      - name: body
        in: body
        type: string
        required: true
        schema:
          id: user
          required:
            - name
              age
              city
          properties:
            name:
              type: string
              description: The user's name.
              default: "User name"
            age:
              type: number
              description: The user's name.
              default: "User name"
            city:
              type: string
              description: The city of the user.
              default: "Los Diago"
    responses:
      200:
        description: An object of user  which is created
    """
    users.append(request.json)
    return Response(json.dumps(request.json), content_type='application/json')

@user_api.route('/', methods=['PUT'])
def updateUser():
    """
    Endpoint to create new user
    ---
    tags:
      - User
    parameters:
      - name: body
        in: body
        type: string
        required: true
        schema:
          id: user
          required:
            - name
              age
              city
          properties:
            name:
              type: string
              description: The user's name.
              default: "User name"
            age:
              type: number
              description: The user's name.
              default: "User name"
            city:
              type: string
              description: The city of the user.
              default: "Los Diago"
    responses:
      200:
        description: An object of user  which is created
    """
    resp = {
        'status': 'failure',
        'message': 'unable to update user detail, could not found user by name : ' + request.json['name']
    }
    existingUser = None
    for u in users:
        if u['name'] == request.json['name']:
            existingUser = u
    if existingUser is not None:
        users.remove(existingUser)
        users.append(request.json)
        resp = request.json
    return Response(json.dumps(resp), content_type='application/json')