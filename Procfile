web: daphne channelstut.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker --settings=channelstut.settings -v2