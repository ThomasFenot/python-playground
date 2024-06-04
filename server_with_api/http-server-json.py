from http.server  import HTTPServer, BaseHTTPRequestHandler
import json

class Server(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(
            [
                {'name': 'Gladiator'},
                {'name': 'Alien'},
                {'name': 'Gladiator 2'},
                {'name': 'Alien 2'},
            ]
        ).encode())
    
port = 5200
httpd = HTTPServer(('localhost', port), Server)
print(f"Server listening on port {port}")

httpd.serve_forever()