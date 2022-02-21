import itertools as its
import datetime

start = datetime.datetime.now()
words = '0123456789'
r = its.product(words,repeat=8)
dic = open(r"C:\\Users\\cheng.long\\study\\pass.txt",'a')
for i in r:
    dic.write(''.join(i))
    dic.write(''.join('\n'))
    print(i)
dic.close()
print('pass text finished')
end = datetime.datetime.now()
print('generate pass txt use time:{}'.format(end-start))