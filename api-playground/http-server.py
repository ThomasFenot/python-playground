from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class Server(BaseHTTPRequestHandler):
    
    def do_GET(self):
        items = [{'name': 'movies'},
                 {'name': 'actors'}]
        if self.path == '/movies':
            items = [{'id' : 1001,'name': 'Python Gladiator'},
                     {'id' : 1002,'name': 'Python Alien'},
                     {'id' : 1003,'name': 'Python Gladiator'},
                     {'id' : 1004,'name': 'Python Avatar'}]
        if self.path == '/actors':
            items = [{'id' : 2001,'name': 'Python Mel Gibson'},
                     {'id' : 2002,'name': 'Python Russel Crowe'},
                     {'id' : 2003,'name': 'Python Joaquim Phoenix'},
                     {'id' : 2004,'name': 'Python Sam Wortington'}]
        try:
            self.send_response(200)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(items).encode())
        except:
            self.send_response(404)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps(items).encode())


port = 5201
httpd = HTTPServer(('localhost', port), Server)
print(f"Server listening on port {port}")

httpd.serve_forever()