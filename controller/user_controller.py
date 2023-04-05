import json
import time
from entity import db, Game, User
from flask import Blueprint, request, jsonify
import requests

from orm_util import getRes

userModule = Blueprint('user', __name__)



@userModule.route('/login',methods=['POST'])
def login():
    appid = ''
    secret = ''
    code = request.json.get("code")
    userInfo = request.json.get("userInfo")
    url = f"https://api.weixin.qq.com/sns/jscode2session?appid={appid}&secret={secret}&js_code={code}&grant_type=authorization_code"
    r = requests.get(url)
    res = json.loads(r.text)
    user = User.query.filter(User.openid == res['openid']).first()
    # 新用户
    if not user:
        user = User()
        user.openid = res['openid']
        user.nickname = userInfo['nickName']
        user.gender = userInfo['gender']
        user.registertime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        user.lastlogintime = user.registertime
        user.type = 0
        user.avatarurl = userInfo['avatarUrl']
        db.session.add(user)
    else:
        user.lastlogintime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        user.nickname = userInfo['nickName']
        user.gender = userInfo['gender']
        user.avatarurl = userInfo['avatarUrl']
    if '_sa_instance_state' in user.__dict__:
        del user.__dict__['_sa_instance_state']
    response = jsonify(user.__dict__)
    db.session.commit()
    return response
# 判断用户是否拥有和想要该游戏
@userModule.route('/ishasgame/<userId>/<int:gameId>')
def ishasgame(userId,gameId):
    user = User.query.get(userId)
    games = user.games
    likegames = user.likegames
    ishas = 0
    islike = 0
    for game in games:
        if gameId == game.id:
            ishas = 1
            break
    for game in likegames:
        if gameId == game.id:
            islike = 1
            break
    return {'ishas': ishas, 'islike': islike}

# 添加到用户游戏库
@userModule.route('/havegame/<userId>/<int:gameId>')
def havegame(userId,gameId):
    user = User.query.get(userId)
    game = Game.query.get(gameId)
    user.games.append(game)
    db.session.commit()
    return {'success': 1}

# 将游戏从用户游戏库中删除
@userModule.route('/delgamefromlibrary/<userId>/<int:gameId>')
def delgamefromlibrary(userId,gameId):
    user = User.query.get(userId)
    game = Game.query.get(gameId)
    user.games.remove(game)
    db.session.commit()
    return {'success': 1}

# 添加到用户心愿单
@userModule.route('/likegame/<userId>/<int:gameId>')
def likegame(userId,gameId):
    user = User.query.get(userId)
    game = Game.query.get(gameId)
    user.likegames.append(game)
    db.session.commit()
    return {'success': 1}

# 将游戏从用户心愿单中删除
@userModule.route('/delgamefromlike/<userId>/<int:gameId>')
def delgamefromlike(userId,gameId):
    user = User.query.get(userId)
    game = Game.query.get(gameId)
    user.likegames.remove(game)
    db.session.commit()
    return {'success': 1}

# 获取用户游戏库
@userModule.route('/getGameByUserId/<userId>')
def getGameByUserId(userId):
    user = User.query.get(userId)
    games = user.games
    res = getRes(games)
    return res

# 获取用户心愿单
@userModule.route('/getLikeGameByUserId/<userId>')
def getLikeGameByUserId(userId):
    user = User.query.get(userId)
    games = user.likegames
    res = getRes(games)
    return res
