import json

from http.server import HTTPServer, BaseHTTPRequestHandler
from mongo_connector.init_mongo import init_database, init_restaurants_collection, init_neighborhoods_collection
import utils.custom_json_encoder

database = init_database()
restaurants_collection = init_restaurants_collection(database)
neighborhoods_collection = init_neighborhoods_collection(database)


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/restaurants':
            cursor = restaurants_collection.find()
        if self.path == '/neighborhoods':
           cursor = neighborhoods_collection.find()
        try:
           # Encode each document to a JSON string and then decode to a dict
            items = [json.loads(utils.custom_json_encoder.CustomJSONEncoder().encode(doc)) for doc in cursor]
            
            # Set the Content-Type header to application/json
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')  # Specify the content type as JSON
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            # Encode the final response as JSON
            response_data = utils.custom_json_encoder.CustomJSONEncoder().encode(items)
            self.wfile.write(response_data.encode())
        except Exception as e:
            self.send_error(500, str(e))

port = 5201
httpd = HTTPServer(('localhost', port), Server)
print(f"Server listening on port {port}")

httpd.serve_forever()