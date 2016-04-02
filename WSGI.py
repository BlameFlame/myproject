bottom = "\t\t<div class='bottom'>Middleware BOTTOM</div>\n"
top = "\t\t<div class='top'>Middleware TOP</div>\n"

def app(environ, start_response): #приложения
    start_response('200 OK', [('Content-Type', 'text/html')])
    path = environ['PATH_INFO']
    path = path[1:]
    if path == '':
        path = 'index.html'
    f = open(path, 'rb')
    return [f.read()]

class PutInBody(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        page = self.app(environ, start_response)[0] #html-страница, выданная приложением

        if (page.find('<body>') > 0):
            left, right = page.split('<body>')
            page = left + '<body>\n' + top + right #TOP
            left, right = page.split('</body>')
            page = left + bottom + '\t</body>' + right #BOTTOM
        return page

app = PutInBody(app) #"оборачивание" в middleware

if __name__ == '__main__':
    from paste.httpserver import serve

    serve(app, host='0.0.0.0', port=8000)
