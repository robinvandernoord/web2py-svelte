# API routes that can be used from the frontend

import time


def slow_method():
    time.sleep(5)
    return {'result': 'done'}


def broken_method():
    raise HTTP(403, 'not allowed')
