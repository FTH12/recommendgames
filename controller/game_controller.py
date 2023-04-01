
from flask import Blueprint,jsonify
from entity import Game,Type,Platform
from orm_util import getRes
from http import HTTPStatus
gameModule = Blueprint('game', __name__)

@gameModule.route("/initGameInfo")
def initGameInfo():
    game_paginate = Game.query.paginate(page=1,per_page=5,error_out=False).items
    res = getRes(game_paginate)
    return jsonify(res)
@gameModule.route("/newGameInfo")
def newGameInfo():
    game_paginate = Game.query.order_by(Game.ss_time.desc()).paginate(page=1, per_page=5, error_out=False).items
    res = getRes(game_paginate)
    return jsonify(res)
@gameModule.route("/goodGameInfo")
def goodGameInfo():
    game_paginate = Game.query.order_by(Game.score.desc()).paginate(page=1, per_page=5, error_out=False).items
    res = getRes(game_paginate)
    return jsonify(res)

