from http.server import HTTPServer, BaseHTTPRequestHandler

class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200, 'OK')
            self.send_header('Content-Type', 'html')
            self.end_headers()
            self.wfile.write(bytes(
                "<html> <head><title> Http Server </title> </head> <body>Main Page</body>", 'UTF-8'))
        else:
            self.send_response(200, 'OK')
            self.send_header('Content-Type', 'html')
            self.end_headers()
            self.wfile.write(bytes(
                "<html> <head><title> Http Server </title> </head> <body>Unknown page</body>", 'UTF-8'))
            
port = 80
httpd = HTTPServer(('localhost', port), Server)
print(f"Server listening on port {port}")

httpd.serve_forever()