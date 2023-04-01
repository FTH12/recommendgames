from entity import *
from input_json import *
from controller.game_controller import *
app = create_app()
app.register_blueprint(gameModule, url_prefix = '/game')

@app.route('/asd')
def hello_world():
    games = Game.query.limit(10).all()
    # platform = Platform.query.get(5)
    # user = User.query.get(1)
    # tags = Tags.query.get(4)
    # print(tags.games)
    # print(f"{platform.games}")
    for game in games:
        print("游戏平台：",end="")
        print(game.it_type,end="123456")
    # print(user.friends)
    return f"嘿嘿嘿"
# @app.route("/")
# def save_json():
#     main_run()
#     return "导入成功"


if __name__ == '__main__':
    app.run()
