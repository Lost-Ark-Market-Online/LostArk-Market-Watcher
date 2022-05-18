
from concurrent.futures import ThreadPoolExecutor, wait
from datetime import datetime
import sys
from time import sleep

from modules.common.singleton import Singleton
from modules.config import Config

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Signal, QObject


import logging
import os

DATEFMT = '%Y-%m-%dT%H:%M:%S'
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_FILE_INFO = f'logs/{datetime.now().strftime("%m-%d-%Y")}.log'
LOG_FILE_ERROR = f'logs/{datetime.now().strftime("%m-%d-%Y")}.err'


class SignalHandler(logging.Handler, QObject):
    signal = Signal(str)

    def __init__(self, *args, **kwargs):
        logging.Handler.__init__(self, *args, **kwargs)
        QObject.__init__(self, *args, **kwargs)

    def emit(self, record):
        print(record.getMessage())
        self.signal.emit(record.getMessage())


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

        self.logger.setLevel(logging.INFO)

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
            self.file_handler_info.setLevel(logging.INFO)
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

    def signal_enable(self):
        if self.signal_handler_info is None:
            self.signal_handler_info = SignalHandler()
            self.signal_handler_info.setFormatter(self.log_formatter)
            self.signal_handler_info.setLevel(logging.INFO)
            self.logger.addHandler(self.signal_handler_info)

        if self.file_handler_error is None:
            self.file_handler_error = SignalHandler()
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


def test():
    sleep(1)
    AppLogger().info('This is an INFO message inside a Thread')


class TestApp(QApplication):
    def __init__(self, *args, **kwargs):
        QApplication.__init__(self, *args, **kwargs)
        AppLogger().signal_enable()
        AppLogger().signal_handler_info.signal.connect(self.test_signal)

    def test_signal(self, message):
        print(f"PRINT: {message}")


if __name__ == '__main__':
    AppLogger()
    try:
        app = TestApp()
        test_futures = []
        executor = ThreadPoolExecutor(
            max_workers=5)
        test_futures.append(executor.submit(test))
        test_futures.append(executor.submit(test))
        test_futures.append(executor.submit(test))
        test_futures.append(executor.submit(test))
        test_futures.append(executor.submit(test))
        test_futures.append(executor.submit(test))
        test_futures.append(executor.submit(test))
        test_futures.append(executor.submit(test))
        test_futures.append(executor.submit(test))
        test_futures.append(executor.submit(test))
        test_futures.append(executor.submit(test))
        test_futures.append(executor.submit(test))
        test_futures.append(executor.submit(test))
        test_futures.append(executor.submit(test))
        test_futures.append(executor.submit(test))
        test_futures.append(executor.submit(test))
        wait(test_futures)
    except Exception as e:
        AppLogger().exception(e)
