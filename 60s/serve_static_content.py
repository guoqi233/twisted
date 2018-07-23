from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor

if __name__ == '__main__':
    resource = File("/root/PythonProj/proj/twt/work/finger")
    factory = Site(resource)
    reactor.listenTCP(8888, factory)
    reactor.run()
