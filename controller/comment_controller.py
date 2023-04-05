from flask import Blueprint, request

from entity import Comment, db

commentModule = Blueprint('comment', __name__)

# 获取游戏的评论
@commentModule.route('/getCommentByGameId/<gameId>')
def getCommentByGameId(gameId):
    comments = Comment.query.filter(Comment.game_id == gameId).all()
    comment_list = []
    for comment in comments:
        if '_sa_instance_state' in comment.__dict__:
            del comment.__dict__['_sa_instance_state']
        comment_list.append(comment.__dict__)
    return {"data": comment_list}

@commentModule.route('/addComment', methods=['POST'])
def addComment():
    userInfo = request.json.get("userInfo")
    print(userInfo)
    content = request.json.get("content")
    gameId = request.json.get("gameId")
    isrecommend = request.json.get("isrecommend")
    comment = Comment()
    comment.user_id = userInfo['id']
    comment.user_avatarurl = userInfo['avatarurl']
    comment.user_nickname = userInfo['nickname']
    comment.content = content
    comment.game_id = gameId
    comment.isrecommend = isrecommend
    db.session.add(comment)
    db.session.commit()

    return {'success': 1}