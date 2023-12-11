#!/home/users/1/main.jp-se-nichijo/web/fastapi-sample/fast-api-venv/bin/python3
from wsgiref.handlers import CGIHandler
from fastapi_sample.main import wsgi_app
CGIHandler().run(wsgi_app)
