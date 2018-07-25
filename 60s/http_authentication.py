from zope.interface import implements

from twisted.cred.portal import IRealm, Portal
from twisted.cred.checkers import FilePasswordDB
from twisted.web.server import Site
from twisted.web.static import File
from twisted.web.resource import IResource
from twisted.web.guard import HTTPAuthSessionWrapper, DigestCredentialFactory
from twisted.internet import reactor, endpoints


class PublicHTMLRealm(object):
    implements(IRealm)

    def requestAvatar(self, avatarId, mind, *interfaces):
        if IResource in interfaces:
            return (IResource, File("/home/%s/public_html" % (avatarId,)), lambda: None)
        raise NotImplementedError()


if __name__ == '__main__':
    portal = Portal(PublicHTMLRealm(), [FilePasswordDB('httpd.password')])
    credentialFactory = DigestCredentialFactory("md5", "localhost:8080")
    resource = HTTPAuthSessionWrapper(portal, [credentialFactory])
    factory = Site(resource)
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 8888)
    endpoint.listen(factory)
    reactor.run()
