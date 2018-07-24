from twisted.web import xmlrpc, server
from twisted.internet import endpoints, reactor


class EchoHandler(object):
    def echo(self, x):
        return x


class AddHandler(object):
    def add(self, a, b):
        return a + b


class Example(xmlrpc.XMLRPC):
    def __init__(self):
        xmlrpc.XMLRPC.__init__(self)
        self._addHandler = AddHandler()
        self._echoHandler = EchoHandler()

        self._procedureToCallable = {
            'add': self._addHandler.add,
            'echo': self._echoHandler.echo
        }

    def lookupProcedure(self, procedurePath):
        try:
            return self._procedureToCallable[procedurePath]
        except KeyError as e:
            raise xmlrpc.NoSuchFunction(self.NOT_FOUND, "procedure {} not found".format(procedurePath))

    def listProcedures(self):
        return ["add", "echo"]


if __name__ == '__main__':
    r = Example()
    endpoint = endpoints.TCP4ServerEndpoint(reactor, 7080)
    endpoint.listen(server.Site(r))
    reactor.run()

