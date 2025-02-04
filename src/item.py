import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self, message):
        print(message)


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        # Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        """
        Проверки, чтобы нельзя было сложить Phone или Item
        с экземплярами не Phone или Item классов.
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        raise Exception

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, file_csv='../src/items.csv'):
        """
        класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        if not os.path.exists(file_csv):
            raise FileNotFoundError('Отсутствует файл item.csv')
        with open(file_csv, encoding='CP1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for item in reader:
                if len(item) < 3:
                    raise InstantiateCSVError('Файл .csv поврежден')
                cls.all.append(cls(item['name'], item['price'], item['quantity']))


    @staticmethod
    def string_to_number(item):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(item))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
