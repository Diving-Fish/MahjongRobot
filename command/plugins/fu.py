from nonebot import on_command, CommandSession
import requests
import json

@on_command('fu', only_to_me=False)
async def fu(session: CommandSession):
    result = session.get('result')
    await session.send(result)


@fu.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if stripped_arg:
        data = stripped_arg.split(" ", 1)
        url = 'http://47.100.50.175:8000/cal'
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        s = json.dumps({
            "inner": data[0], \
            "outer": data[1], \
            "dora": "", \
            "innerdora": "", \
            "reach": False, \
            "tsumo": True, \
            
            "selfwind": 0, \
            "placewind": 0, \
            
            "yifa": False, \
            "haidi": False, \
            "hedi": False, \
            "lingshang": False, \
            "qianggang": False, \
            "wreach": False, \
            "tianhe": False, \
            "dihe": False \
        })
        r = requests.post(url, headers=headers, data=s)
        j = json.loads(r.text)
        session.state['result'] = ((stripped_arg + ' ' + j['data']['fu']) if j['status'] == 200 else "查询有误")
