import psycogreen.gevent


psycogreen.gevent.patch_psycopg()

bind = "0.0.0.0:8000"
backlog = 10
workers = 4
worker_class = "gevent"
worker_connections = 100
keepalive = 60
timeout = 30
graceful_timeout = 30
max_requests = 3000
