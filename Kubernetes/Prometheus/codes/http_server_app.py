import http.server
from prometheus_client import start_http_server

class HandleRequest(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>Hello from OpenShift!</h1></body></html>", "utf-8"))

if __name__ == "__main__":
    # Start the Prometheus client HTTP server on port 8000 (or any other port you prefer)
    start_http_server(8000)
    
    # Start your custom HTTP server on port 5001
    server = http.server.HTTPServer(('3.106.179.126', 5001), HandleRequest)
    
    # Update the print message to reflect the correct port
    print("Server running on http://3.106.179.126/:5001/")
    
    server.serve_forever()

