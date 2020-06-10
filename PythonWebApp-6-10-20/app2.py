class app(object):

    def __init__(self, environ, start_fn):
        self.environ = environ
        self.start_fn = start_fn

    def __iter__(self):
        self.start_fn('200 OK', [('Content-Type', 'text/plain')])
        yield "Hello Again World!\n"
