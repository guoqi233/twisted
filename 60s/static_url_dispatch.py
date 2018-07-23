from twisted.web.server import Site
from twisted.web.resource import Resource
from twisted.internet import reactor
from twisted.web.static import File

root = Resource()
root.putChild("foo", File("/root/PythonProj/proj/twt"))
root.putChild("bar", File("/lost+found"))
root.putChild("baz", File("/opt"))

if __name__ == '__main__':
    factory = Site(root)
    reactor.listenTCP(8880, factory)
    reactor.run()
