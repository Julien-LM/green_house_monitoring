#!/usr/bin/env python

import BaseHTTPServer
import cgitb
from CGIOverloadIndex import CGIHandlerOverloadIndex

cgitb.enable()  # This line enable CGI error reporting

server = BaseHTTPServer.HTTPServer
handler = CGIHandlerOverloadIndex
server_address = ("", 8000)
handler.cgi_directories = ["/"]

httpd = server(server_address, handler)
httpd.serve_forever()
