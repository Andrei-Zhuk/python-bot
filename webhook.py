import cherrypy

WEBHOOK_HOST = '192.168.0.1'

WEBHOOK_PORT = 443
WEBHOOK_LISTEN = '0.0.0.0'

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)

class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        return 'Hello World!'
        if 'content-length' in cherrypy.request.headers and \
                        'content-type' in cherrypy.request.headers and \
                        cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            return 'Hello World!'
        else:
            raise cherrypy.HTTPError(403)

cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT
})

cherrypy.quickstart(WebhookServer())