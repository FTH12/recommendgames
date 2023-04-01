import json
from exts import db
from entity import *


def read_file(src):
    f = open(src, "r", encoding="utf-8")
    game_dics = json.load(f)
    # print(type(game_dic))
    return game_dics["result"]

def sovle_dic(game_dic:dict):
    game = Game()
    game.__dict__.update(game_dic)
    g_type = Type.query.filter(Type.name==game_dic["g_type"]).first()
    game.it_type = g_type
    for pt in game_dic["plts"]:
        plt = Platform.query.filter(Platform.name==pt).first()
        game.platforms.append(plt)
    for tg in game_dic["tags"]:
        gtg = Tags.query.filter(Tags.name==tg).first()
        game.gtags.append(gtg)
    return game
def main_run():
    # types = Type.query.all()
    game_dics=[]
    games = []
    for year in range(2023,2022,-1):
        src = f"gamejsons/games_{year}.json"
        game_dics.extend(read_file(src))
    for game_dic in game_dics:
        game = sovle_dic(game_dic)
        db.session.add(game)
        games.append(game)
    print(len(games))
    # db.session.bulk_save_objects(games)
    db.session.commit()

