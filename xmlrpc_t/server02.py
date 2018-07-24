from twisted.web.xmlrpc import XMLRPC, withRequest
from twisted.web.server import Site


class Example(XMLRPC):
    @withRequest
    def xmlrpc_headerValue(self, request, headerName):
        print headerName
        return request.requestHeaders.getRawHeaders(headerName)

    @withRequest
    def xmlrpc_echo(self, request, x):
        """
        Return all passed args.
        """
        return x


if __name__ == '__main__':
    from twisted.internet import reactor, endpoints
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 7080)
    endpoint.listen(Site(Example()))
    reactor.run()
