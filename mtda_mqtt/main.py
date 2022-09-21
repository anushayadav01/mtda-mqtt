import os
import sys
import socket
import configparser


class MTDAMqtt(object):

    def __init__(self):
        self.name = socket.gethostname()
        self.ctrlport = 5556
        self.conport = 5557
        self.debug_level = 0
        self.is_remote = False
        self.is_server = False
        self.remote = None
        self.socket = None

    def debug(self, lvl, msg):
        if self.debug
