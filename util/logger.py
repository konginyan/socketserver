# coding:utf-8
import logging
import logging.config
from util.conf import LOGGER_CONF


logging.config.fileConfig(LOGGER_CONF)
server_logger = logging.getLogger("server")
client_logger = logging.getLogger("client")