from nonebot import on_command, CommandSession


@on_command('help', only_to_me=False)
async def help(session: CommandSession):
    text = '欢迎使用日麻机器人。\r\n' \
           '牌理：/pl <牌型>，例子：\r\n' \
           '/pl 12345678m23p4567s\r\n' \
           '符：/fu <牌型> <是否自摸(0/1)>，例子：\r\n' \
           '/fu 234m234p2345677s4s 1\r\n' \
           '点数：/point <牌型> [可选参数]\r\n' \
           '可选参数需要换行，可以是：立直 自摸 自风x 场风x 宝牌xx 里宝牌xx 一发等。\r\n' \
           '例子：\r\n' \
           '/point 123456789m2377s4s\r\n' \
           '立直 一发 自摸 宝牌4m 里宝牌7s 自风西 场风南\r\n' \
           '完整帮助列表：https://github.com/Diving-Fish/MahjongRobot/blob/master/help.md'
    await session.send(text)
