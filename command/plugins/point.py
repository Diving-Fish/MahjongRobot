from nonebot import on_command, CommandSession
import requests
import json


@on_command('point', only_to_me=False)
async def point(session: CommandSession):
    result = session.get("result")
    await session.send(result)


@point.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if not stripped_arg:
        return '查询有误'

    data = stripped_arg.split('\n')

    tiles = data[0].split(' ', 1)
    if len(tiles) == 1:
        tiles = [tiles[0], ""]

    args = {
        "inner": tiles[0],
        "outer": tiles[1],
        "dora": "",
        "innerdora": "",
        "reach": False,
        "tsumo": False,

        "selfwind": 0,
        "placewind": 0,

        "yifa": False,
        "haidi": False,
        "hedi": False,
        "lingshang": False,
        "qianggang": False,
        "wreach": False,
        "tianhe": False,
        "dihe": False
    }

    extras = data[1].split(' ')
    for extra in extras:
        if extra == '':
            continue
        elif extra == '立直':
            args["reach"] = True
        elif extra == '自摸':
            args["tsumo"] = True
        elif extra == '场风东':
            args["placewind"] = 0
        elif extra == '场风南':
            args["placewind"] = 1
        elif extra == '场风西':
            args["placewind"] = 2
        elif extra == '场风北':
            args["placewind"] = 3
        elif extra == '自风东':
            args["selfwind"] = 0
        elif extra == '自风南':
            args["selfwind"] = 1
        elif extra == '自风西':
            args["selfwind"] = 2
        elif extra == '自风北':
            args["selfwind"] = 3
        elif extra == '一发':
            args["yifa"] = True
        elif extra == '海底':
            args["haidi"] = True
        elif extra == '河底':
            args["hedi"] = True
        elif extra == '岭上':
            args["lingshang"] = True
        elif extra == '枪杠':
            args["qianggang"] = True
        elif extra == '抢杠':
            args["qianggang"] = True
        elif extra == '双立直':
            args["wreach"] = True
            args["reach"] = True
        elif extra == '两立直':
            args["wreach"] = True
            args["reach"] = True
        elif extra == '天和':
            args["tianhe"] = True
        elif extra == '地和':
            args["dihe"] = True

    request_body = json.dumps(args)
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    url = 'http://47.100.50.175:8000/cal'
    r = requests.post(url, headers=headers, data=request_body)
    return r.text
