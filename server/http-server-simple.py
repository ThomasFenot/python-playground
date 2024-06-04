import http.server

class Server(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'First page')

httpd = http.server.HTTPServer(('localhost', 80), Server)
print('Server listening on port 80')
httpd.serve_forever()

