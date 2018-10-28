from flask.app import Flask
from flask_restful import Api
from flask_socketio import SocketIO

app = Flask(__name__)
api = Api(app)
socketio = SocketIO(app)

import cube.ops.tools.api.scores