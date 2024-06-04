from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        items = [{'name': 'movies'},
                 {'name': 'actors'}]
        if self.path == '/movies':
            items = [{'name':'Gladiator'},
                     {'name':'Alien'},
                     {'name':'Gladiator 2'},
                     {'name':'Alien 2'}]
        if self.path == '/actors':
            items = [{'name': 'Mel Gibson'},
                    {'name': 'Russel Crowe'},
                    {'name': 'Joaquim Phoenix'},
                    {'name': 'Sam Wortington'}]

        try:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(items).encode())
        except:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(json.dumps(items).encode())
            
port = 5201
httpd = HTTPServer(('localhost', port), Server)
print(f"Server listening on port {port}")

httpd.serve_forever()