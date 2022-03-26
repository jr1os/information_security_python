from threading import Thread
import time


def car(velocity, pilot):
    path = 0
    while path <= 100:
        print('car', pilot, path)
        path += velocity
        time.sleep(0.5)


t_car = Thread(target=car, args=[1, 'python'])
t_car2 = Thread(target=car, args=[2, 'golang'])

t_car.start()
t_car2.start()
