import logging
from logging.handlers import TimedRotatingFileHandler
import config


def create_handler(path):
    formatter = logging.Formatter(
        "%(asctime)s %(filename)s:%(lineno)d %(levelname)s %(thread)d - %(message)s", '%Y-%m-%d %H:%M:%S')

    handler = TimedRotatingFileHandler(path+'/request.log', when='d', interval=1, backupCount=10,
                                       encoding="utf8", delay=False)

    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)

    return handler
