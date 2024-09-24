from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.enemies = 100

    def run(self):
        print(f"{self.name}, на нас напали!")

        while self.enemies > 0:
            self.enemies -= self.power
            self.days += 1
            print(f'{self.name} сражается {self.days} дней(дня), осталось {self.enemies} воинов.')
            sleep(1)

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения

first_knight.start()

sleep(0.5)

second_knight.start()

first_knight.join()
second_knight.join()

print("Битвы окончены!")
