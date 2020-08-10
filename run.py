#imports
import markdown
import os
import shelve
from flask import Flask, g
from flask_restful import Resource, Api, reqparse

# create app instance of flask
app = Flask(__name__)
api = Api(app)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("employees.db")
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    #display documentation

    with open(os.path.dirname(app.root_path) + '\\REST API\\README.md', 'r') as markdown_file:
        content = markdown_file.read()

        return markdown.markdown(content)

class EmployeeList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        employees = []

        for key in keys:
            employees.append(shelf[key])

        return {'message': 'Success', 'data': employees}

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('ssid', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('role', required=True)

        args = parser.parse_args()

        shelf = get_db()
        shelf[args['ssid']] = args

        return {'message': 'Employee Added', 'data': args}, 201

class Employee(Resource):
    def get(self, ssid):
        shelf = get_db()

        if not (ssid in shelf):
            return {'message': 'Employee not found', 'data': {}}, 404

        return {'message': 'Employee Found', 'data': shelf[ssid]}, 200

    def delete(self, ssid):
        shelf = get_db()

        if not (ssid in shelf):
            return {'message': 'Employee not found', 'data': {}}, 404

        del shelf[ssid]
        return '', 204

api.add_resource(EmployeeList, '/employees')
api.add_resource(Employee, '/employee/<string:ssid>')