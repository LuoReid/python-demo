from wsgiref.simple_server import make_server
from my_wsgi import application

httpd = make_server('', 8000, application)
print('Server HTTP on port 8000...')
httpd.serve_forever()
