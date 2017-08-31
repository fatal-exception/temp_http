#!/usr/bin/env python
import signal
import SimpleHTTPServer
import SocketServer
import os
import time

PORT = 3000
TIME_UP = int(os.getenv('HTTP_TIMEOUT', 30))

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

def handler(signum, frame):
    print "time up, entering useless state"
    # be useless
    while True:
        time.sleep(10)
    

def serve_http():
    print "serving http at port", PORT
    httpd.serve_forever()

signal.signal(signal.SIGALRM, handler)
signal.alarm(TIME_UP)

try:
    serve_http()
except Exception, exc:
    print exc
