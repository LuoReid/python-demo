from orm import Model, StringField, IntegerField
from models import User, Blog, Comment
import asyncio
import orm

loop = asyncio.new_event_loop()
# loop = asyncio.get_running_loop()
async def test():
    await orm.create_pool(loop=loop, host='127.0.0.1', user='www-data',
                               password='www-data', db='awesome')
    u = User(name='Test2', email='test2@example.com',
             passwd='1234', image='about:blank')
    await u.save()
    rs = await User.findAll()
    print('res:', rs)
    return rs


for x in loop.run_until_complete(test()):
    print('x:', x)
    pass
loop.run_forever()
# if __name__ == '__main__':
#     user = User(id=123, name='Michael')
#     # user.insert()
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(orm.create_pool(loop=loop,
#                                             user='root', password='1q2w3e4r', db='demo'))
#     users = loop.run_until_complete(User.findAll())
#     print(user['id'])
#     print(user.id)
#     print(users)
#     # user.save()

#     loop.run_until_complete(user.save())
#     users = loop.run_until_complete(User.findAll())
#     print(users)
