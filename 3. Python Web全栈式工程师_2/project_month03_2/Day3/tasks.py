from celery import Celery

app = Celery('steven', broker='redis://:@127.0.0.1:6379/1')


# 创建任务函数
@app.task
def task_test():
    print("task is running....")
