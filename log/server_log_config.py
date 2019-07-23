import logging

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

handler = logging.FileHandler('main.log')
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)


def add_info(string):
    logger.info(f'{string}')
    return


def add_debug(string):
    logger.debug(f'{string}')
    return


def add_critical(string):
    logger.critical(f'{string}')
    return


def add_error(string):
    logger.error(f'{string}')
    return

