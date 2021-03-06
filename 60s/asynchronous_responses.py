from twisted.web.resource import Resource
from twisted.web.server import Site, NOT_DONE_YET
from twisted.internet import reactor


class DelayedResource(Resource):
    isLeaf = True
    def _delayedRender(self, request):
        request.write("<html><body>Sorry to keep you waiting.</body></html>")
        request.finish()

    def render_GET(self, request):
        reactor.callLater(5, self._delayedRender, request)
        return NOT_DONE_YET


if __name__ == '__main__':
    resource = DelayedResource()
    factory = Site(resource)
    reactor.listenTCP(8888, factory)
    reactor.run()
