import time
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/healthz':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()
    print("completed")

if __name__ == '__main__':
    run()
    while True:
        with open("/app/logs/output.log", "a") as f:
            f.write(f"Generated log at {time.ctime()}\n")
        time.sleep(5)  # Log every 5 seconds
