import time
import BaseHTTPServer
from os import environ


HOST_NAME = '0.0.0.0' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 8080 # Maybe set this to 9000.
e1=environ.get('ENV1')
e2=environ.get('ENV2')

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Build-trigger-test</title></head>")
        s.wfile.write("<h2> When I say Hey </h1><br>")
        s.wfile.write("<h2> You say </h2>")
        s.wfile.write("<h3> "+e1+" </h3>")
        s.wfile.write("<h3> "+e2+" </h3>")

        s.wfile.write("</body></html>")

if __name__ == '__main__':
	

    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)