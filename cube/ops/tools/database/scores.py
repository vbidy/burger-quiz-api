from tinydb import TinyDB,Query

db = TinyDB('/var/lib/tinydb/burger/db.json')


class ScoreDatabase :

    def __init__(self):
        '''
        Constructor
        '''

    def getScore(self, team):
        ScoreQuery = Query()

        score = db.search(ScoreQuery.team == team)[0]['score']
        return score

    def getScores(self):
        teams = db.all()
        scores = {}
        for team in teams:
            scores[team['team']] = team['score']
        return scores

    def updateScore(self, json, team):
        ScoreQuery = Query()
        db.update(json, ScoreQuery.team == team)
