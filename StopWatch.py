"""
Контекст
В каждом телефоне есть это замечательное приложение.
Секундомер - это программа, которая засекает сколько
времени прошло от момента запуска до момента остановки.
Также, как правило там присутствует функция “паузы”,
которая позволяет временно приостановить секундомер, с
возможностью продолжить отсчет в будущем.
● Ваша задача
Реализовать секундомер на любом языке программирования
в любой парадигме. Секундомер должен поддерживать
следующий функционал:
○ Запуск
○ Пауза
○ Выход из паузы
○ Остановка
"""
import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.end_time  = None
        self.pause_accum_time = 0
        self.status = 'idle'
        print("Press space to start >>>")

    def start(self):
        if self.status != 'idle':
            print("Reset timer before start")
        self.status = 'running'
        self.start_time = time.time()
        return 'Timer started'

    def stop(self):
        if self.status != 'running':
            print('Timer already stopped')
        self.status = 'stopped'
        self.end_time = time.time()
        return 'Estimated: {} seconds.'.format(Stopwatch.elapsed_time())

    def pause(self):
        if self.status != 'running':
            print('Timer not running')
        self.status = 'paused'
        self.end_time = time.time()
        self.pause_accum_time = self.end_time - self.start_time + self.pause_accum_time
        return f'Timer paused on {self.pause_accum_time}'

    def unpause(self):
        if self.status != 'paused':
            print('Timer not paused')
        self.status = 'running'
        self.start_time = time.time()
        return 'Timer unpaused'

    def elapsed_time(self):
        if self.start_time is None:
            raise ValueError('Timer was never started')
        if self.end_time is None:
            raise ValueError('Timer was never stopped')
        return self.end_time - self.start_time + self.pause_accum_time
