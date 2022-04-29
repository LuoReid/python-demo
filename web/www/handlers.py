#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'url handlers'

import re
import time
import json
import logging
import hashlib
import base64
import asyncio
from coroweb import get, post
from models import User, Comment, Blog, next_id


@get('/')
async def index(request):
    users = await User.findAll()
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary,
             created_at=time.time()-120),
        Blog(id='2', name='Something New',
             summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='Learn Swift', summary=summary,
             created_at=time.time()-7200)
    ]
    return {'__template__': 'blogs.html', 'blogs': blogs}


@get('/api/users')
def api_get_users(*, page='1'):
    # page_index = get_page_index(page)
    # num = yield from User.findNumber('count(id)')
    # p = Page(num,page_index)
    # if num == 0:
    #     return dict(page=p,users=())
    # users = yield from User.findAll(orderBy='created_at desc',limit=(p.offset,p.limit))
    us = yield from User.findAll(orderBy='created_at desc')
    for u in us:
        u.passwd = '******'
    return dict(users=us)
