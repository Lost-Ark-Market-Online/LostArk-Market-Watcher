
from datetime import datetime

from modules.common.singleton import Singleton
from modules.config import Config

from PySide6.QtCore import Signal, QObject

import logging
import os

DATEFMT = '%Y-%m-%dT%H:%M:%S'
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_FILE_INFO = f'logs/{datetime.now().strftime("%m-%d-%Y")}.log'
LOG_FILE_ERROR = f'logs/{datetime.now().strftime("%m-%d-%Y")}.err'


class SignalHandler(logging.Handler):
    signal = None

    def __init__(self, signal):
        super(SignalHandler, self).__init__()
        self.signal = signal

    def emit(self, record):
        if self.signal:
            self.signal.emit(
                f'{record.asctime} - {record.levelname} - {record.message}', record.levelno)


class LoggingFilter(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        return logRecord.levelno <= self.__level


class AppLogger(metaclass=Singleton):
    logger: logging.Logger = None
    file_handler_info: logging.FileHandler = None
    file_handler_error: logging.FileHandler = None
    signal_handler_info: SignalHandler = None
    signal_handler_error: SignalHandler = None
    log_formatter: logging.Formatter = logging.Formatter(
        datefmt=DATEFMT, fmt=LOG_FORMAT)

    def __init__(self) -> None:
        self.logger = logging.getLogger('LostArkMarketWatcher')

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(self.log_formatter)
        self.logger.addHandler(stream_handler)

        if Config().debug:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)

        self.debug = self.logger.debug
        self.info = self.logger.info
        self.warning = self.logger.warning
        self.error = self.logger.error
        self.exception = self.logger.exception

        if Config().save_log:
            if os.path.exists("logs") == False:
                os.mkdir('logs')
            self.file_enable()

    def file_enable(self):
        if self.file_handler_info is None:
            self.file_handler_info = logging.FileHandler(
                LOG_FILE_INFO, mode='a')
            self.file_handler_info.setFormatter(self.log_formatter)
            self.file_handler_info.setLevel(logging.DEBUG)
            self.logger.addHandler(self.file_handler_info)

        if self.file_handler_error is None:
            self.file_handler_error = logging.FileHandler(
                LOG_FILE_ERROR, mode='a')
            self.file_handler_error.setFormatter(self.log_formatter)
            self.file_handler_error.setLevel(logging.ERROR)
            self.logger.addHandler(self.file_handler_error)

    def file_disable(self):
        if self.file_handler_info:
            self.logger.removeHandler(self.file_handler_info)
            self.file_handler_info = None
        if self.file_handler_error:
            self.logger.removeHandler(self.file_handler_error)
            self.file_handler_error = None

    def signal_enable(self, signal):
        if self.signal_handler_info is None:
            self.signal_handler_info = SignalHandler(signal)
            self.signal_handler_info.setFormatter(self.log_formatter)
            self.signal_handler_info.setLevel(logging.INFO)
            self.logger.addHandler(self.signal_handler_info)

        if self.file_handler_error is None:
            self.file_handler_error = SignalHandler(signal)
            self.file_handler_error.setFormatter(self.log_formatter)
            self.file_handler_error.setLevel(logging.ERROR)
            self.logger.addHandler(self.file_handler_error)

    def signal_disable(self):
        if self.signal_handler_info:
            self.logger.removeHandler(self.signal_handler_info)
            self.signal_handler_info = None

        if self.signal_handler_error:
            self.logger.removeHandler(self.signal_handler_error)
            self.signal_handler_error = None
