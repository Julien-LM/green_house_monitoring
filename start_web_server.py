#!/usr/bin/env python
# coding=utf-8
"""
    File name:  start_web_server.py
    Author:     Julien LE MELLEC
    Mail:       julien.lemellec@gmail.com
    Created:    20/09/2019

    Start basic CGI HTTP server

"""

import BaseHTTPServer
import cgitb
import sys
import logging

from CGIOverloadIndex import CGIHandlerOverloadIndex
from Init import Init
from DefaultsValues import HTTP_default_port_test


class Main(object):
    """
    Class Main
    """

    def __init__(self, argv):
        # Init logger and opt
        self.init = Init(argv)

        # Get HTTP port from Init method
        self.http_port = self.init.get_http_port()

        # Get logger from Init class
        self.log = logging.getLogger('CGIHTTPServer')

    def main(self):
        # cgitb.enable()  # This line enable CGI error reporting

        self.log.info("main running, HTTP port {}".format(self.http_port))
        self.log.debug("main running as debug")

        server = BaseHTTPServer.HTTPServer
        handler = CGIHandlerOverloadIndex
        server_address = ("", self.http_port)
        handler.cgi_directories = ["/"]

        httpd = server(server_address, handler)
        httpd.serve_forever()


if __name__ == "__main__":
    Main(sys.argv[1:]).main()
