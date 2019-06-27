from nonebot import on_command, CommandSession
import requests
import json
import math


def up(num):
    return math.ceil(num / 100) * 100


def get_yaku_info(id, mq):
    if id > 100:
        return '宝牌', id - 100
    elif id > 200:
        return '赤宝牌', id - 200
    elif id > 300:
        return '里宝牌', id - 300
    ids = [1, 2, 3, 4, 5, 6, 71, 72, 73, 74, 75, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
           26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
    names = ["立直", "一发", "门前清自摸和", "平和", "断幺九", "一杯口", "役牌：场风牌", "役牌：自风牌", "役牌：白", "役牌：发",
             "役牌：中", "海底捞月", "河底捞鱼", "枪杠", "岭上开花", "两立直", "七对子", "一气通贯", "三色同顺", "混全带幺九",
             "三色同刻", "三暗刻", "对对和", "小三元", "混老头", "三杠子", "混一色", "纯全带幺九", "二杯口", "清一色", "国士无双",
             "大三元", "四暗刻", "小四喜", "字一色", "绿一色", "清老头", "九莲宝灯", "四杠子", "天和", "地和", "国士无双十三面",
             "大四喜", "四暗刻单骑", "纯正九莲宝灯"]
    fan_mq = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 6, 13, 13, 13, 13,
              13, 13, 13, 13, 13, 13, 13, 26, 26, 26, 26]
    fan_fl = [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 0, 5, 13, 13, 13, 13,
              13, 13, 13, 13, 13, 13, 13, 26, 26, 26, 26]
    index = ids.index(id)
    return names[index], fan_mq[index] if mq else fan_fl[index]


@on_command('point', only_to_me=False)
async def point(session: CommandSession):
    result = session.get("result")
    await session.send(result)


@point.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if not stripped_arg:
        session.state['result'] = '查询有误'
        return

    data = stripped_arg.split('\r\n')

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
    rtext = ''
    rjson = json.loads(r.text)
    yakus = rjson['data']['yakus']
    mq = rjson['data']['inner']
    for yaku in yakus:
        space = ' ' * 4
        yakuname, fan = get_yaku_info(yaku, mq)
        yakuname += space * (8 - len(yakuname))
        yakuname += str(fan) + "番\r\n"
        rtext += yakuname
    rtext += "%d符%d番\r\n" % (rjson['data']['fu'], rjson['data']['fan'])
    if rjson['data']['isQin']:
        if rjson['data']['isTsumo']:
            rtext += "%dAll" % up(2 * rjson['data']['perPoint'])
        else:
            rtext += str(up(6 * rjson['data']['perPoint']))
    else:
        if rjson['data']['isTsumo']:
            rtext += "%d-%d" % (up(rjson['data']['perPoint']), up(2 * rjson['data']['perPoint']))
        else:
            rtext += str(up(4 * rjson['data']['perPoint']))
    session.state['result'] = rtext