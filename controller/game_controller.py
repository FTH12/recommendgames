
from flask import Blueprint,jsonify
from entity import Game,Type,Platform,Tags
from orm_util import getRes
from http import HTTPStatus
gameModule = Blueprint('game', __name__)
@gameModule.route("/initGameInfo")
#获取最热游戏列表
def initGameInfo():
    game_paginate = Game.query.paginate(page=1,per_page=5,error_out=False).items
    res = getRes(game_paginate)
    return jsonify(res)
@gameModule.route("/newGameInfo")
#获取最新游戏列表
def newGameInfo():
    game_paginate = Game.query.order_by(Game.ss_time.desc()).paginate(page=1, per_page=5, error_out=False).items
    res = getRes(game_paginate)
    return jsonify(res)
@gameModule.route("/goodGameInfo")
#获取好评游戏列表
def goodGameInfo():
    game_paginate = Game.query.order_by(Game.score.desc()).paginate(page=1, per_page=5, error_out=False).items
    res = getRes(game_paginate)
    return jsonify(res)

#通过游戏id获取游戏信息
@gameModule.route('/getGameById/<gameId>')
def getGameById(gameId):
    game = Game.query.get(gameId)
    type = game.it_type
    platforms = game.platforms
    tags = game.gtags
    if '_sa_instance_state' in game.__dict__:
        del game.__dict__['_sa_instance_state']
    platform_list = []
    for platform in platforms:
        platform_list.append(platform.name)
    tag_list = []
    for tag in tags:
        tag_list.append(tag.name)
    game.__dict__['gtags'] = tag_list
    game.__dict__['it_type'] = type.name
    game.__dict__['platforms'] = platform_list
    print(game.__dict__)
    return game.__dict__

#通过名字搜索游戏
@gameModule.route('/getGamesByName/<gameName>')
def getGamesByName(gameName):
    game_list = []
    games = Game.query.filter(Game.name.like(f"%{gameName}%")).order_by(Game.year.desc()).all()
    for game in games:
        if '_sa_instance_state' in game.__dict__:
            del game.__dict__['_sa_instance_state']
        type = Type.query.get(game.type_id)
        game.__dict__['it_type'] = type.name
        game_list.append(game.__dict__)
    res = {"games": game_list}
    return res

#通过类型搜索游戏
@gameModule.route('/getGameByType/<typeId>')
def getGameByType(typeId):
    game_list = []
    type = Type.query.get(typeId)
    games = Game.query.filter(Game.type_id==typeId).order_by(Game.year.desc()).paginate(page=1, per_page=5, error_out=False).items
    for game in games:
        if '_sa_instance_state' in game.__dict__:
            del game.__dict__['_sa_instance_state']
        game.__dict__['it_type'] = type.name
        game_list.append(game.__dict__)
    res = {"games": game_list}
    return res