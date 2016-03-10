import logging
import sys

LEVELS = { 'debug':logging.DEBUG,
			'info':logging.INFO,
			'warning':logging.WARNING,
			'error':logging.ERROR,
			'critical':logging.CRITICAL,
			}
LOG_FILENAME = 'loglog.txt'

level = LEVELS.get('logging.DEBUG', logging.NOTSET)

logging.basicConfig(filename=LOG_FILENAME,
                    level=level,
                    )

logging.debug('lol')

def poop():
	print('lol')