class Application(object):
    def __call__(self, environ, start_fn):
        start_fn('200 OK', [('Content-Type', 'text/plain')])
        yield "Hello World! One more time!\n"

app = Application()
