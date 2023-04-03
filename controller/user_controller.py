import json
import time
from entity import db
from flask import Blueprint, request, jsonify
from entity import User
import requests
userModule = Blueprint('user', __name__)



@userModule.route('/login',methods=['POST'])
def login():
    appid = 'wxbc0bb3d567068528'
    secret = '74545a3971bc4abcb3635544bcb6efe0'
    code = request.json.get("code")
    userInfo = request.json.get("userInfo")
    print(userInfo)
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
        db.session.add(user)
    else:
        user.lastlogintime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        user.nickname = userInfo['nickName']
        user.gender = userInfo['gender']
    if '_sa_instance_state' in user.__dict__:
        del user.__dict__['_sa_instance_state']
    response = jsonify(user.__dict__)
    db.session.commit()
    return response

# @userModule.route('/credit')
# def credit():
#     token = request.values.get('token')
#     session = db['session'][token]
#     if token in db['session']:
#         session = db['session'][token]
#         if session['openid'] in db['user']:
#             db['user'][session['openid']]['credit'] += 10
#             return db['user'][session['openid']]
#         else:
#             return {'err': '用户不存在或未登录'}