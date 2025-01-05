# -*- coding: utf-8 -*-

import sqlite3
import os
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)


conn = sqlite3.connect(db_file)
cursor = conn.cursor()
print(cursor.execute(
    'create table user(id varchar(20) primary key, name varchar(20),score int)'))
print(cursor.execute("insert into user values('A-001','Adam',95)"))
print(cursor.execute("insert into user values('A-002','Bart',62)"))
print(cursor.execute("insert into user values('A-003','Lisa',78)"))
print(cursor.rowcount)
conn.commit()
cursor.close()
conn.close()


def get_score_in(low, high):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(
        'select name from user where ?<= score and score <=? order by score', (low, high))
    values = cursor.fetchall()
    res = []
    for val in values:
        # print(' val:', val, val[0])
        res.append(val[0])
    cursor.close()
    conn.close()
    print('res:', res)
    return res


# test
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)
print('pass')
