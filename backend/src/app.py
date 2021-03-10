from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_HOST'] = 'localhost'
app.config['MONGO_PORT'] = '27017'
app.config['MONGO_DBNAME'] = 'flask_react'
app.config['MONGO_USERNAME'] = 'root'
app.config['MONGO_PASSWORD'] = 'example'
app.config['MONGO_AUTH_SOURCE'] = 'admin'
app.config['MONGO_URI'] = f'mongodb://{app.config.get("MONGO_USERNAME")}:{app.config.get("MONGO_PASSWORD")}@' \
                          f'{app.config.get("MONGO_HOST")}:{app.config.get("MONGO_PORT")}/' \
                          f'{app.config.get("MONGO_DBNAME")}?authSource={app.config.get("MONGO_AUTH_SOURCE")}'
mongo = PyMongo(app)
db = mongo.db.users


@app.route('/users', methods=['POST'])
def create_user():
    print(request.json)
    id = db.insert_one({
        'name': request.json['name'],
        'email': request.json['email'],
        'password': request.json['password']
    })
    return jsonify({'id': id.inserted_id.__str__()})


@app.route('/users/int:<int:id>', methods=['PUT'])
def update_user():
    return '<h1>recivido</h1>'


@app.route('/users/int:<int:id>', methods=['GET'])
def get_user():
    return '<h1>recivido</h1>'


@app.route('/users', methods=['DELETE'])
def delete_user():
    return '<h1>recivido</h1>'


@app.route('/users', methods=['GET'])
def get_users():
    return '<h1>recivido</h1>'


if __name__ == '__main__':
    app.run(debug=True)
