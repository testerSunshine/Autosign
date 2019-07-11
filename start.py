# -*- coding: UTF-8 -*-
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from red import redGrab
from sign_in import signIn

if __name__ == '__main__':

    cookie = "isg=BOLiWhcNyxiqXdZyVZYAuhHmOWxEM-ZN8YS37Sx7DdUr_4F5FMCpWvTsKf2odF7l; UTUSER=13427833; ut_ubt_ssid=esdsjykvbd6j51tpnazd6pgcxf9err7f_2019-07-10; tzyy=0e652fd568ee60d48e3d6a94b4971d3b; _utrace=57b668bd1b7ebe88b473406d60dd537d_2018-12-14; cna=ffeZFOshGXQCAbfvpoparfGj; track_id=1544751458|54c1a55c86c1a9ace6ea3e04d283945bd0c259ad9676626eac|6fce7a0c2f3ea42754a659127f065306; ubt_ssid=aucakq7qtf2n8v98iy5cs62nslkrn77b_2018-12-14; perf_ssid=91ocoxg4sesq2m126eqhernl65dsm1lc_2018-12-14; USERID=13427833; SID=bZm0fK8PjJCoKoaqmUI4lQigt63YMIEiXBSA"
    scheduler = BlockingScheduler()
    redGrab = redGrab()
    sign = signIn()
    # 抢红包
    scheduler.add_job(func=redGrab.sendRed, args=(cookie,), trigger='cron', hour=8, minute=59, second=59)
    scheduler.add_job(func=redGrab.sendRed, args=(cookie,), trigger='cron', hour=13, minute=59, second=59)
    scheduler.add_job(func=redGrab.sendRed, args=(cookie,), trigger='cron', hour=16, minute=59, second=59)
    scheduler.add_job(func=redGrab.sendRed, args=(cookie,), trigger='cron', hour=19, minute=59, second=59)
    scheduler.add_job(func=redGrab.sendRed, args=(cookie,), trigger='cron', hour=20, minute=30, second=40)

    # 签到
    scheduler.add_job(func=sign.sendSign, args=(cookie,), trigger='cron', hour=1, minute=30, second=40)

    print("调度任务执行" + " " + datetime.datetime.now().strftime('%H:%M:%S.%f'))
    scheduler.start()
