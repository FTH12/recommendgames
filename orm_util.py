def getRes(game_paginate):
    game_list = []
    for game in game_paginate:
        type = game.it_type
        if '_sa_instance_state' in game.__dict__:
            del game.__dict__['_sa_instance_state']
        if 'it_type' in game.__dict__:
            del game.__dict__['it_type']
        game.__dict__['type'] = type.name
        game_list.append(game.__dict__)
    return {"data": game_list}