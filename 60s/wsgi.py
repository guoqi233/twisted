from twisted.web.wsgi import WSGIResource
from twisted.web.server import Site
from twisted.internet import reactor, endpoints


def application(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    return ['Hello, world!']


if __name__ == '__main__':
    resource = WSGIResource(reactor, reactor.getThreadPool(), application)
    factory = Site(resource)
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 8888)
    endpoint.listen(factory)
    reactor.run()
