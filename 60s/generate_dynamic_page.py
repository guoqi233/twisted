from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
import time


class ClockPage(Resource):
    isLeaf = True
    def render_GET(self, request):
        print request
        return "<html><body>{}</body></html>".format(time.ctime(),)


if __name__ == '__main__':
    resource = ClockPage()
    factory = Site(resource)
    reactor.listenTCP(8888, factory)
    reactor.run()
