import http.server
import time
from prometheus_client import start_http_server, Guage

REQUEST_IN_PROGRESS = Guage('requests_inprogress', "Number of Live Request on Application")
REQUEST_LAST_EXECUTED = Guage("request_last_served", "Time the application was last served")

class HandleRequest(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        REQUEST_IN_PROGRESS.inc()
        time.sleep(5)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>Hello from OpenShift!</h1></body></html>", "utf-8"))
        self.wfile.close
        REQUEST_LAST_EXECUTED.set(time.time())
        REQUEST_IN_PROGRESS.dec()

if __name__ == "__main__":
    # Start the Prometheus client HTTP server on port 8000 (or any other port you prefer)
    start_http_server(8000)
    
    # Start your custom HTTP server on port 5001
    server = http.server.HTTPServer(('3.106.179.126', 5001), HandleRequest)
    
    # Update the print message to reflect the correct port
    print("Server running on http://3.106.179.126/:5001/")
    
    server.serve_forever()