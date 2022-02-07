import datetime
import logging
from os import makedirs, path
from utils.config import project_path

nowTime = str(datetime.datetime.now().replace(microsecond=0).isoformat()).replace(':', '_')
today = str(datetime.date.today())

log_path = project_path + '\\log\\'

if not path.exists(log_path):
    makedirs(log_path)

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

input_level = 0


def logger(level, msg):
    log_file = log_path + 'activity_' + today + '_app.log'
    log = logging.getLogger('activity')

    if not log.handlers:
        handler = logging.FileHandler(log_file)
        handler.setFormatter(formatter)

        log.setLevel(level)
        log.addHandler(handler)
    if level == 0 and level >= input_level:
        log.debug(msg)
    elif level == 1 and level >= input_level:
        log.info(msg)
    elif level == 2 and level >= input_level:
        log.warning(msg)
    elif level == 3 and level >= input_level:
        log.error(msg)
    elif level == 4 and level >= input_level:
        log.critical(msg)
