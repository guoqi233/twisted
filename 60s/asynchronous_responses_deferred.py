from twisted.internet.task import deferLater
from twisted.web.resource import Resource
from twisted.web.server import NOT_DONE_YET, Site
from twisted.internet import reactor, endpoints


class DelayedResource(Resource):
    isLeaf = True
    def _delayedRender(self, request):
        request.write(b"<html><body>Sorry to keep you waiting.</body></html>")
        request.finish()

    def render_GET(self, request):
        d = deferLater(reactor, 5, lambda: request)
        d.addCallback(self._delayedRender)
        return NOT_DONE_YET


if __name__ == '__main__':
    resource = DelayedResource()
    factory = Site(resource)
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 8888)
    endpoint.listen(factory)
    reactor.run()
