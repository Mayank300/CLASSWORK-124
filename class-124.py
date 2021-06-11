from flask import Flask, jsonify, request
app = Flask(__name__)

task = [{ 
    'id': 1,
    'title': u'Learn Flask',
    'description': u'Learning Flask with WHJ',
    'done': False
},
{ 
    'id': 2,
    'title': u'Learn Ruby',
    'description': u'Learning Ruby with .....',
    'done': False
},
{ 
    'id': 3,
    'title': u'Learn React Native',
    'description': u'Learning React Native with Youtube',
    'done': False
}]

@app.route('/')

def hello():
    return 'hi :) 🔥 🔥 🔥 🔥 🔥 🔥'

@app.route('/add-data',methods=['POST'])

def addTask():
    if not request.json:
        return jsonify(
            {
                'status': 'error',
                'message': 'please provide a data'
            },
            400
        )

    tasks = {
        'id': task[-1]['id']+1,
        'title': request.json.get['title'],
        'description': request.json.get['description',''],
        'done': False
    }

@app.route('/get-data')

def getTask():
    return jsonify({
        'data': task
    })

if (__name__ == '__main__' ):
    app.run(debug=True)