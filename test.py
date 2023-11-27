print("Hello, It's Ritesh\nWelcome to you in test.py!")

print("*"*35)
print("\t\tlet's check the pod")
print("*"*35)
# test.py

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
    print("*"*31)
    print("Checking Done")
    print("*"*31)

if __name__ == '__main__':
    run()
