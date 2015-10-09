from django.contrib.auth.middleware import RemoteUserMiddleware


class RemoteUserCustomHeaderMiddleware(RemoteUserMiddleware):
    header = 'HTTP_REMOTE_USER'
