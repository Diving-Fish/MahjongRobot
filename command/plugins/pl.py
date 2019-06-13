from nonebot import on_command, CommandSession
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options=chrome_options)


@on_command('pl', only_to_me=False)
async def pl(session: CommandSession):
    result = session.get('result')
    await session.send(result)


@pl.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if stripped_arg:
        driver.get("https://tenhou.net/2/?q=" + stripped_arg)
        resp = driver.find_element_by_id("tehai")
        if resp.text == "INVALID QUERY":
            session.state['result'] = '查询有误'
            return
        textarea = driver.find_element_by_tag_name("textarea")
        txt = textarea.text
        arr = txt.split("\n")
        arr[0] = arr[0] + '\n' + resp.text
        txt = '\n'.join(arr)
        session.state['result'] = txt
