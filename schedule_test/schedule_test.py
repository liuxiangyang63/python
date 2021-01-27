#!/usr/bin/python
# -*- coding: UTF-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
# 输出时间
def job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', seconds=1)
scheduler.start()