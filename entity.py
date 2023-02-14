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
    # 用户名
    username = db.Column(db.String(255), nullable = False)
    # 用户密码
    pwd = db.Column(db.String(255), nullable = False)
    # 用户昵称
    nickname = db.Column(db.String(255))
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
    # a_user.friends获取该用户好友

# 游戏
class Game(db.Model):
    __tablename__ = "game"
    # 游戏id
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    # 游戏名
    name = db.Column(db.String(255), nullable = False)
    # 游戏的发行商
    publisher = db.Column(db.String(255))
    # 游戏的制作商
    producer = db.Column(db.String(255))
    # 游戏类型的id
    type_id = db.Column(db.Integer,  db.ForeignKey("type.id"))
    # 游戏类型
    type = ""
    platforms = db.relationship("Platform", secondary = game_platform,
                                backref = db.backref("games"))
    tags = db.relationship("Tags", secondary = game_tags,
                           backref = db.backref("games"))

    # 初始化
    def __init__(self,name,publisher="NULL",producer="NULL",type_id = None,type = "未分类"):
        self.name = name
        self.publisher = publisher
        self.producer = producer
        self.type_id = type_id
        self.type = type
    def get_type(self):
        self.type = self.it_type.name
        return self.type


# 游戏类型
class Type(db.Model):
    __tablename__ = "type"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(255))
    # a_type.games可以获得所有该类型的游戏。
    # 反向引用：a_game.type可以获得该游戏的类型
    games = db.relationship("Game", backref="it_type")

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

