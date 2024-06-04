import http.server

class Server(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        if self.path == '/movies':
            self.path = '/movies.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

port = 80
httpd = http.server.HTTPServer(('localhost', port), Server)
print(f"Server listening on port {port}")

httpd.serve_forever()
            