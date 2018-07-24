import time
from twisted.web import xmlrpc, server


class Example(xmlrpc.XMLRPC):
    def xmlrpc_echo(self, x):
        """
        Return all passed args.
        """
        return x

    def xmlrpc_add(self, a, b):
        """
        Return sum of arguments.
        """
        return a + b


class Date(xmlrpc.XMLRPC):
    def xmlrpc_time(self):
        return time.time()


if __name__ == '__main__':
    from twisted.internet import reactor, endpoints
    r = Example()
    date = Date()
    r.putSubHandler('date', date)
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 7080)
    endpoint.listen(server.Site(r))
    reactor.run()
