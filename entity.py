import time

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config


db = SQLAlchemy() # type:SQLAlchemy
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    return app


# ——————————————————中间表——————————————————————
# 游戏平台中间表
game_platform = db.Table("game_platform",
                         db.Column("platform_id", db.Integer, db.ForeignKey("platform.id")),
                         db.Column("game_id", db.Integer, db.ForeignKey("game.id")),
                         )
# 游戏标签中间表
game_tags = db.Table("game_tags",
                     db.Column("tags_id", db.Integer, db.ForeignKey("tags.id")),
                     db.Column("game_id", db.Integer, db.ForeignKey("game.id"))
                     )
# 游戏库中间表
game_library = db.Table("game_library",
                        db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
                        db.Column("game_id", db.Integer, db.ForeignKey("game.id")),
                        )
# 心愿单中间表
game_like = db.Table("game_like",
                        db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
                        db.Column("game_id", db.Integer, db.ForeignKey("game.id")),
                     )
# 好友中间表
class Friend(db.Model):
    __tablename__ = "friends"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 外键
    mu_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    fu_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # a_user.friends获取该用户好友
    mu = db.relationship("User", foreign_keys = mu_id, backref = "friends")
    # fu = db.relationship("User", foreign_keys = fu_id)
# ——————————————————中间表——————————————————————
# 用户
class User(db.Model):
    __tablename__ = "user"
    # 用户id
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    # 用户的openid 唯一标识
    openid = db.Column(db.String(255), nullable = False)
    # 用户性别
    gender = db.Column(db.String(50))
    # 用户昵称
    nickname = db.Column(db.String(255))
    # 用户头像url
    avatarurl = db.Column(db.String(255))
    # 用户注册时间
    registertime = db.Column(db.DateTime)
    # 用户上次登陆时间
    lastlogintime = db.Column(db.DateTime)
    #用户权限，1为管理员，0为普通用户
    type = db.Column(db.Integer)
    # a_user.games获取该用户的游戏库
    # 反向：a_game.users获取拥有该游戏的所有用户
    games = db.relationship("Game", secondary = game_library,
                            backref = db.backref("users"))
    # 用户的心愿单游戏
    likegames = db.relationship("Game", secondary = game_like,
                                backref = db.backref("likeusers"))
    # a_user.friends获取该用户好友

# 游戏
class Game(db.Model):
    __tablename__ = "game"
    # 游戏id
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    # 游戏名
    name = db.Column(db.String(255), nullable = False)
    # 游戏的发行商制作商
    company = db.Column(db.String(255))
    # 游戏类型的id
    type_id = db.Column(db.Integer,  db.ForeignKey("type.id"))
    # a_game.type可以获得该游戏的类型
    # 反向引用：a_type.games可以获得所有该类型的游戏
    it_type = db.relationship("Type", backref="games")
    # 游戏评分
    score = db.Column(db.String(10))
    # 游戏发行年份
    year = db.Column(db.String(10))
    # 游戏名的md5
    g_md5 = db.Column(db.String(255))
    # 游戏图片名
    img_name = db.Column(db.String(255))
    # 游戏游玩时长
    play_time = db.Column(db.String(50))
    # 游戏发行日期
    ss_time = db.Column(db.String(50))
    # 游戏简介
    jj = db.Column(db.String(255))
    # 游戏支持平台
    platforms = db.relationship("Platform", secondary = game_platform,
                                backref = db.backref("games"))
    #游戏的标签
    gtags = db.relationship("Tags", secondary = game_tags,
                           backref = db.backref("games"))

    # 初始化
    def __init__(self,name=None,company="NULL",score = "--",year="999",g_md5 = "",
                 img_name = "", play_time = "未知", ss_time = "9999-12-31",
                 jj = ""):
        self.name = name
        self.company = company
        self.score = score
        self.year = year
        self.g_md5 = g_md5
        self.img_name = img_name
        self.play_time = play_time
        self.ss_time = ss_time
        self.jj = jj
    def __str__(self):
        return f"name:{self.name}, company:{self.company}, score:{self.score}, year:{self.year}\n" \
               f" g_md5:{self.g_md5}, img_name:{self.img_name}, playtime:{self.play_time}, ss_time:{self.ss_time}\n jj:{self.jj}"


# 游戏类型
class Type(db.Model):
    __tablename__ = "type"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(255))
    # a_type.games可以获得所有该类型的游戏。
    # 反向引用：a_game.type可以获得该游戏的类型

# 游戏平台
class Platform(db.Model):
    __tablename__ = "platform"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))

    def __str__(self):
        return f"id:{self.id},name:{self.name}"

# 游戏标签
class Tags(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))

class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer,  db.ForeignKey("user.id"))
    game_id = db.Column(db.Integer,  db.ForeignKey("game.id"))
    content = db.Column(db.String(255))
    comment_time = db.Column(db.DateTime, default = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    isrecommend = db.Column(db.Integer)
    user_nickname = db.Column(db.String(255))
    user_avatarurl = db.Column(db.String(255))