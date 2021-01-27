# -*- coding: utf8 -*-
import logging
import requests
import schedule
from datetime import datetime
import time

logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)


# The URL address need to dial test. 需要拨测的URL地址
warn_retry_task_url = 'https://ucode-test.aax6.cn/api-gateway/warn/task/v1/retry/send/message'


def test_warn_retry_task():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    resp = None
    try:
        resp = requests.get(warn_retry_task_url, timeout=30)
        print(resp)
    except (
            requests.exceptions.Timeout, requests.exceptions.ConnectionError,
            requests.exceptions.ConnectTimeout) as e:
        logger.warn("请求异常:" + str(e))
    else:
        if resp.status_code >= 400:
            logger.error("相应状态码:" + str(resp.status_code))
