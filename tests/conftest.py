import pytest
from Capabilities import app_driver
from pages.AppiumScript import Autorize_methods

A_Methods = Autorize_methods()




@pytest.fixture()
def open_app():
    """Выполнение авторизации до теста и закрытия апки после теста. Авторизация с отсутствием доступа gps location"""
    A_Methods.autorization()

@pytest.fixture()
def open_close_app():
    """Выполнение авторизации до теста и закрытия апки после теста"""
    A_Methods.autorization()
    yield open_close_app  # здесь происходит тестирование
    app_driver.reset()

@pytest.fixture()
def close_app():
    """Выполнение просто принта до теста и закрытия апки после теста"""
    print('------setup close_appp-----')
    yield close_appp # здесь происходит тестирование
    print('------teardown close_appp-----')
    app_driver.reset()



import logging
import sys
from rp_logging import RPLogger, RPLogHandler


@pytest.fixture(scope="session")
def rp_logger(request):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    # Create handler for Report Portal if the service has been
    # configured and started.
    if hasattr(request.node.config, 'py_test_service'):
        # Import Report Portal logger and handler to the test module.
        logging.setLoggerClass(RPLogger)
        rp_handler = RPLogHandler(request.node.config.py_test_service)
        # Add additional handlers if it is necessary
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
    else:
        rp_handler = logging.StreamHandler(sys.stdout)
    # Set INFO level for Report Portal handler.
    rp_handler.setLevel(logging.INFO)
    return logger

