# coding:utf-8
import time
import heapq
from util.singleton import singleton


@singleton
class Timer(object):

    def __init__(self):
        self.tasks = []

    def add_task(self, task, delay, repeatable=False):
        heapq.heappush(self.tasks, TimeTask(task, delay, repeatable))

    def run(self):
        while self.tasks and self.tasks[0].can_run():
            task = heapq.heappop(self.tasks)
            try:
                task.run()
            except Exception as e:
                raise TaskRunError(e, task.get_task_name())
            else:
                if task.repeatable:
                    heapq.heappush(self.tasks, task)

    def run_ever(self):
        while True:
            self.run()


class TimeTask(object):

    def __init__(self, task, delay, repeatable):
        if callable(task):
            self.task = task
            self.delay = delay
            self.timeout = time.time() + delay
            self.repeatable = repeatable
        else:
            raise TaskNotFunctionError()

    def __lt__(self, other):
        return self.timeout < other.timeout

    def can_run(self):
        return self.timeout <= time.time()
    
    def run(self):
        self.task()
        if self.repeatable:
            self.timeout = time.time() + self.delay

    def get_task_name(self):
        return self.task.__name__


class TaskNotFunctionError(Exception):

    def __init__(self):
        super().__init__(self)

    def __str__(self):
        return 'non-Callable task cannot init TimeTask'


class TaskRunError(Exception):

    def __init__(self, exception, task):
        super(TaskRunError, self).__init__(self)
        self.exception = repr(exception)
        self.task = task

    def __str__(self):
        return 'task raise %s while runing %s' % (self.exception, self.task)