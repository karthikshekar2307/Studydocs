import http.server
import time
from prometheus_client import start_http_server, Histogram

REQUEST_LATENCY_TIME=Histogram('request_latency_time', 'Response latency in seconds')

class HandleRequest(http.server.BaseHTTPRequestHandler):
    
    @REQUEST_LATENCY_TIME.time()
    def do_GET(self):
        startTime = time.time()
        self.send_response(200)
        time.sleep(1)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body><h1>Hello from OpenShift!</h1></body></html>", "utf-8"))
        self.wfile.close
        end_time = time.time() - startTime
        REQUEST_LATENCY_TIME.observe(end_time)

if __name__ == "__main__":
    # Start the Prometheus client HTTP server on port 8000 (or any other port you prefer)
    start_http_server(8000)
    
    # Start your custom HTTP server on port 5001
    server = http.server.HTTPServer(('3.106.179.126', 5001), HandleRequest)
    
    # Update the print message to reflect the correct port
    print("Server running on http://3.106.179.126/:5001/")
    
    server.serve_forever()