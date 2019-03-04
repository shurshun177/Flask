from flask import Flask, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)
class HelloWorld(Resource):
    def get(self):
        return {'hellow': 'world'}

todos = {'main': 'empty'}
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}
    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(HelloWorld, '/')
api.add_resource(TodoSimple, '/<string:todo_id>')

app.run(debug=True)