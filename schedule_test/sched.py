#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import urllib2
import json
import time
import sched
import threading

reload(sys)
sys.setdefaultencoding('utf8')

# def http(cnt):
#     result = -1
#     url = "https://ucode-test.aax6.cn/warn/promotion/timer/prizeNumWarn"
#     # data = dict(prizeNumWarn="U2FsdGVkX19C/fX2+gTOFYz86dQdDXP4nDZP4asZV88=")
#     header_dict = {"Content-Type": "application/json"}
#     # body_data = json.dumps(data, ensure_ascii=False)
#     req = urllib2.Request(url=url, data='', headers=header_dict)
#     try:
#         response = urllib2.urlopen(req)
#         result = response.code
#     except Exception as e:
#         if cnt > 2:
#             raise e
#         else:
#             print(e)
#             time.sleep(5)
#             http(cnt + 1)
#     return result
#
# def main_handler(event, context):
#     print(http(0))
#
# main_handler(1,2)

ticket = 2


def sale(lock):
    global ticket
    if lock.acquire:
        if ticket > 0:
            time.sleep(1)
            ticket -= 1
            print ('【%s】买票·剩余票数：%s' % (threading.current_thread().name, ticket))
        lock.release


def main():
    lock = threading.RLock
    thread_list = [threading.Thread(target=sale, args=(lock,), name='售票员 - %s' % item) for item in range(10) ]
    for thread in thread_list:
        thread.start()

