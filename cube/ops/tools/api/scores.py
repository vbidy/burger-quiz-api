import logging
from flask import jsonify
from flask.globals import request
from cube import app
from cube.ops.tools.utils import progutils
from cube.ops.tools.database.scores import ScoreDatabase
from flask_cors import CORS, cross_origin

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/scores/<team>', methods=['GET', 'PATCH'])
@cross_origin()
def score(team):
    scoreDb = ScoreDatabase()
    if request.method == 'GET':
        # logging.getLogger("burger").info("called hello")
        return str(scoreDb.getScore(team)), 200
    if request.method == 'PATCH':
        scoreToUpdate = request.get_json()
        modified = False
        currentScore = scoreDb.getScore(team)
        if isinstance(scoreToUpdate['score'], int) and scoreToUpdate['score'] <= 25:
            if currentScore != scoreToUpdate['score']:
                modified = True
                scoreDb.updateScore(scoreToUpdate, team)
        else:
            return '', 400

        if modified:
            return '', 204
        else:
            return '', 304


@app.route('/scores/', methods=['GET'])
@cross_origin()
def scores():
    # logging.getLogger("burger").info("called hello")
    scoreDb = ScoreDatabase()
    return jsonify(scoreDb.getScores()), 200

