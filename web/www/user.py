from orm import Model, StringField, IntegerField
import asyncio


class User(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()


if __name__ == '__main__':
    user = User(id=123, name='Michael')
    # user.insert()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(User.create_pool(user='root',password='1q2w3e4r',db='demo'))
    users = loop.run_until_complete(User.findAll())
    print(user['id'])
    print(user.id)
    print(users)
    # user.save()

    loop.run_until_complete(user.save())
    users = loop.run_until_complete(User.findAll())
    print(users)
