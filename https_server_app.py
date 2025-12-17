import http.server
import ssl

class HandleRequests(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First python Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to the first Python application.</center></h2></body></html>", "utf-8"))
        self.wfile.close

if __name__ == "__main__":
    httpd = http.server.HTTPServer(('localhost', 5000), HandleRequests)

    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ssl_context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

    httpd.serve_forever()
