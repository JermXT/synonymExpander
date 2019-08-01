from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO

import main, json


class HTTPRequest(BaseHTTPRequestHandler):
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        expansion = main.queryExpansion(json.loads(body)['query'])
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(bytes(json.dumps({"expansion":expansion}), 'utf-8'))
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', 8000), HTTPRequest)
httpd.serve_forever()
