from twisted.web.resource import Resource
from twisted.web.server import NOT_DONE_YET, Site
from twisted.internet import reactor, endpoints


class DelayedResource(Resource):
    isLeaf = True
    def _delayedRender(self, request):
        request.write("<html><body>Sorry to keep you waiting.</body></html>")
        request.finish()

    def _responseFailed(self, err, call):
        print err
        call.cancel()

    def render_GET(self, request):
        call = reactor.callLater(5, self._delayedRender, request)
        request.notifyFinish().addErrback(self._responseFailed, call)
        return NOT_DONE_YET


if __name__ == '__main__':
    resource = DelayedResource()
    factory = Site(resource)
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 8888)
    endpoint.listen(factory)
    reactor.run()
