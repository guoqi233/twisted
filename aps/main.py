from flask import Flask
import logging
import time

import pytz

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_MISSED

jobstores = {
}
executors = {
    'default': {'type': 'processpool', 'max_workers': 1},
}
job_defaults = {
    'coalesce': False,
    'misfire_grace_time': 5,
    'max_instances': 1
}
scheduler = BackgroundScheduler()
scheduler.configure(jobstores=jobstores,
                    executors=executors,
                    job_defaults=job_defaults,
                    timezone=pytz.timezone('Asia/Shanghai'))
logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.WARNING)
app = Flask(__name__)


@app.route("/", methods=["GET", ])
def index_view():
    scheduler.add_job(interval, trigger="interval", seconds=5,)
    return "hello"


def interval():
    print time.time()


def err_listener(ev):
    if ev.exception:
        print('%s error.', str(ev))
    else:
        print('%s miss', str(ev))


scheduler.add_listener(err_listener, EVENT_JOB_MISSED)

if __name__ == '__main__':
    scheduler.start()
    app.run(debug=False, host="localhost", port="5000")

