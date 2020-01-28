import logging

# noqa
logging.basicConfig(level=logging.INFO,
    format='%(asctime)s :: %(levelname)s :: %(funcName)s ::%(filename)s :: %(lineno)d :: %(message)s')  # noqa


def get_logger(name=__name__):
    logger = logging.getLogger(name)

    return logger
