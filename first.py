from flask import Flask, jsonify
from flask import make_response
from flask import abort
app = Flask(__name__)
app.config["DEBUG"] = True
fake_data = [
    {
        'id': 1,
        'title': 'fake_1',
        'status': False
    },
    {
        'id': 2,
        'title': 'fake_2',
        'status': True
    },
    {
        'id': 3,
        'title': 'empty',
        'status': 'fake'
    }
]

@app.route('/')
def inex():
    return 'Index page'
@app.route('/hellow')
def hellow_world():
    return 'Helow world!'
@app.route('/api/v1.0/data', methods=['GET'])
def get_data():
    print('It works')
    return jsonify({'data':fake_data})
@app.route('/api/v1.0/data/<int:data_id>', methods=['GET'])
def get_data_param(data_id):
    data = list(filter(lambda t: t['id'] == data_id, fake_data))
    if len(data) == 0:
        abort(404)
    return jsonify({'data': data[0]})
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

app.run()