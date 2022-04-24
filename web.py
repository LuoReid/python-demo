import asyncio
from datetime import datetime 
import random


async def hello(request):
    name = request.match_info.get("name", "foo")
    # print('req:', str(request.rel_url.query), name)
    n = datetime.now().isoformat()
    delay = random.randint(0, 1)
    await asyncio.sleep(delay)
    headers = {"content_type": "text/txt", "delay": str(delay), "date": n}
    # with open("frank.html", "rb") as html_body:
    #     print("{}:{} delay: {}".format(n, request.path, delay))
    #     res = web.Response(body=html_body.read(), headers=headers)
    #     return res
    web.Response(text="{}:{} delay:{}".format(n, request.path, delay))

app = web.Application()
app.router.add_route("GET", "/{name}", hello)
web.run_app(app)
