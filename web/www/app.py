#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from datetime import datetime
from aiohttp import web
import asyncio
import os
import json
import time
import orm
from models import User, Blog, Comment
__author__ = 'Long Cheng'

logging.basicConfig(level=logging.INFO)


def index(request):

    return web.Response(body='<h1>Awesome</h1>', headers={'content-type': 'text/html'})


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))



loop.run_forever()
