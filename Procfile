web: gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 "app:create_app()" 
release: flask db upgrade