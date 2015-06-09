# coding: utf-8

import time
import sched
import requests
from lxml import html

from leancloud import Engine

from app import app


engine = Engine(app)


@engine.define
def hello(**params):
    if 'name' in params:
        return 'Hello, {}!'.format(params['name'])
    else:
        return 'Hello, LeanCloud!'


def load_tasks():
    s = sched.scheduler(time.time, time.sleep)
    _check(5, s)
    s.run()


def _check(interval, sc):
    print time.time(), "Start checking ..."
    r = requests.get("http://www.zufangzi.com/area/1b90B-22200/1/")
    if r.status_code == 200:
        tree = html.fromstring(r.text)
        houses = tree.xpath('//div[@id="houseList"]/div[@class="listCon wid1000"]')
        num = 0
        for house in houses:
            num += 1
            print 'House #', num
            for block in house.iterchildren():
                if block.get('class') == 'listCon_Img':
                    for link in block.iterlinks():
                        if link[1] == 'src':
                            print link[2]
                elif block.get('class') == 'listCon_con':
                    for ele in block.xpath('//p[@class="listcon_1"]/em/a'):
                        print ele.text_content()
    sc.enter(interval, 1, _check, (interval, sc,))
