from wxpy import *

from wechat_sender import *
bot = Bot()


import logging

from wechat_sender import LoggingSenderHandler
logger = logging.getLogger(__name__)

def test_spider():
  logger.exception('exception:xxx')

def init_logger():
  sender_logger = LoggingSenderHandler('spider',level=logging.EXCEPTION)
  logger.addHandler(sender_logger)

if __name__ == '__main__':
  init_logger()
  test_logger()