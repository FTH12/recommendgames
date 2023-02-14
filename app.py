from entity import *


app = create_app()


@app.route('/')
def hello_world():
    game = Game.query.get(1)
    platform = Platform.query.get(5)
    user = User.query.get(1)
    tags = Tags.query.get(4)
    # print(tags.games)
    # print(f"{platform.games}")
    # print(game.platforms)
    print(user.friends)
    return f"嘿嘿嘿"


if __name__ == '__main__':
    app.run()
