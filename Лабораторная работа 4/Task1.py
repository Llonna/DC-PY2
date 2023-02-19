class Social_media:
    def __init__(self, corporate_color: str, user_id: int):
        """
        Создание и подготовка к работе объекта "Социальная сеть"
        :param corporate_color: Цвет аватарки пользователя сети
        :param user_id: Идентификатор пользователя
        """

        if not isinstance(corporate_color, str):
            raise TypeError("Цвет пользователя сети должен быть типа string")
        self.corporate_color = corporate_color

        if not isinstance(user_id, int):
            raise TypeError("Номер пользователя социальной сети должен быть типа int")
        if user_id < 0:
            raise TypeError("Номер пользователя социальной сети должен быть неотрицательным")
        self.user_id = user_id

    def __str__(self) -> str:
        return f'Пользователь использует цвет {self.corporate_color!r}, его номер в сети - {self.user_id}'

    def __repr__(self) -> str:
        return f'self.__class__.__name__({self.corporate_color!r}, {self.user_id})'

    def get_rgb_corporate_color_code(self):
        """
        Метод, возвращающий цвет аватарки из социальной сети в формате RGB кода.
        :return: Корпоративный цвет в формате RGB кода
        """
        ...

    def get_user_index(self) -> bool:
        """
        Метод, возращающий информацию о том, существует ли пользователь в какой-то сети.
        :return: существует ли пользователь в какой-то сети.
        """
        ...


class Facebook(Social_media):
    def __init__(self, corporate_color: str, user_id: int, own_income: float, users=None):
        """
        Создание и подготовка к работе объекта "Facebook"
        :param users: Пользователь
        :param own_income: Доход пользователя
        """
        super().__init__(corporate_color, user_id)

        if not isinstance(own_income, (int, float)):
            raise TypeError("Доход пользователя сети должен быть типа int или float")
        self.__own_income = own_income
        # Атрибут private для сохранения приватности доходов при создании дополнительных дочерних классов

        if users is None:
            self.users = []
        else:
            self.users = users

    def __str__(self):
        str_super = super().__str__()
        return f'{str_super}, доход пользователя составлет {self.__own_income}'

    def __repr__(self):
        repr_super = super().__repr__()
        return f'{self.__class__.__name__}({repr_super}, {self.__own_income})'

    # Метод get_rgb_corporate_color_code(self) унаследован

    def get_user_index(self) -> bool:
        """
        Метод, возращающий информацию о том, существует ли пользователь в сети Facebook.
        Метод перегружатеся, потому что в этом классе требуется конкретика по сети Facebook.
        :return: существует ли пользователь в сети Facebook.
        """
        ...

if __name__ == '__main__':
    meta = Facebook("blue", 12345, 10, )
    print(meta)
