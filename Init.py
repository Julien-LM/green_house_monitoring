# coding=utf-8
"""
    File name:  Init.py
    Author:     Julien LE MELLEC
    Mail:       julien.lemellec@gmail.com
    Created:    20/09/2019

    Description: Initialization class

"""

import logging
import sys
import getopt
from SpecialFormatter import SpecialFormatter
from DefaultsValues import HTTP_default_port, HTTP_default_port_test


class Init(object):
    """
    Class Init
    """

    def __init__(self, argv):
        """Constructor for Init"""
        # Logger managing
        fmt = SpecialFormatter()
        stream_handler = logging.StreamHandler(sys.stdout)

        stream_handler.setFormatter(fmt)

        self.log = logging.getLogger('CGIHTTPServer')
        self.log.setLevel(logging.INFO)
        self.log.addHandler(stream_handler)
        self.http_port = HTTP_default_port

        try:
            opts, args = getopt.getopt(argv, "hdtp:", ["port=", "debug", "test"])
        except getopt.GetoptError:
            self.usage()
            sys.exit(1)
        for opt, arg in opts:
            if opt == '-h' or opt == '--help':
                self.usage()
                sys.exit(0)
            elif opt in ("-p", "--port"):
                self.http_port = arg
                self.log.info("HTTP port selected: {}".format(arg))
            elif opt in ("-d", "--debug"):
                self.log.setLevel(logging.DEBUG)
                self.log.info("Logging level set to DEBUG")
            elif opt in ("-t", "--test"):
                self.http_port = HTTP_default_port_test
                self.log.info("HTTP port selected: {}".format(self.http_port))

    def get_http_port(self):
        """
        http_port getter
        :return: HTTP port
        :rtype: String
        """
        return self.http_port

    def usage(self):
        """
        Script usage information
        """
        self.log.info('getUART version TODO')
        self.log.info('Usage: getUART')
        self.log.info('   or: getUART [arguments]')

        self.log.info('Arguments:')
        self.log.info('  -d or --debug:     Set logger into debug mode')
        self.log.info('  -p or --port:      Set HTTP port')
        self.log.info('  -t or --test:      Init HTTP port and disable SPI')
