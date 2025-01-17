import csv


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
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        """Отображает информацию об объекте класса в режиме отладки."""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Отображает информацию об объекте класса для пользователя."""
        return f'{self.__name}'

    def __add__(self, other):
        """Сложение экземпляров класса `Phone` и `Item` (сложение по количеству товара в магазине)"""
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """
        Возвращает наименования товара.
        """
        return self.__name

    @name.setter
    def name(self, name_quantity):
        """
        Проверяет длину наименования товара.
        """
        if len(name_quantity) < 10:
            self.__name = name_quantity
        else:
            raise Exception("Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls):
        """
        Возвращает число из числа-строки.
        """
        Item.all.clear()
        with open('../src/items.csv') as file:
            item = csv.DictReader(file)
            for word in item:
                cls(word['name'], word['price'], word['quantity'])

    @staticmethod
    def string_to_number(number):
        """
        Возвращает число из числа-строки.
        """
        return int(float(number))
