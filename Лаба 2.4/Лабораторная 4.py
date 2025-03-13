from typing import List


class СоциальнаяСеть:
    """
    Базовый класс для представления социальной сети.

    Атрибуты:
        название (str): Название социальной сети.
        пользователи (List[str]): Список пользователей социальной сети.
    """

    def __init__(self, название: str, пользователи: List[str]) -> None:
        """
        Конструктор базового класса.

        Аргументы:
            название (str): Название социальной сети.
            пользователи (List[str]): Список пользователей социальной сети.
        """
        self.название = название
        self.пользователи = пользователи

    def __str__(self) -> str:
        """
        Возвращает строковое представление социальной сети.

        Возвращает:
            str: Строковое представление социальной сети.
        """
        return f"Социальная сеть: {self.название}, Пользователи: {len(self.пользователи)}"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление социальной сети.

        Возвращает:
            str: Официальное строковое представление социальной сети.
        """
        return f"СоциальнаяСеть(название={self.название}, пользователи={self.пользователи})"

    def добавить_пользователя(self, пользователь: str) -> None:
        """
        Добавляет пользователя в социальную сеть.

        Аргументы:
            пользователь (str): Имя пользователя для добавления.
        """
        self.пользователи.append(пользователь)

    def количество_пользователей(self) -> int:
        """
        Возвращает количество пользователей в социальной сети.

        Возвращает:
            int: Количество пользователей.
        """
        return len(self.пользователи)


class VK(СоциальнаяСеть):
    """
    Дочерний класс для представления социальной сети VK.

    Атрибуты:
        название (str): Название социальной сети.
        пользователи (List[str]): Список пользователей социальной сети.
        группы (List[str]): Список групп в социальной сети VK.
    """

    def __init__(self, название: str, пользователи: List[str], группы: List[str]) -> None:
        """
        Конструктор дочернего класса VK.

        Аргументы:
            название (str): Название социальной сети.
            пользователи (List[str]): Список пользователей социальной сети.
            группы (List[str]): Список групп в социальной сети VK.
        """
        super().__init__(название, пользователи)
        self.группы = группы

    def __str__(self) -> str:
        """
        Возвращает строковое представление социальной сети VK.

        Возвращает:
            str: Строковое представление социальной сети VK.
        """
        return f"VK: {self.название}, Пользователи: {len(self.пользователи)}, Группы: {len(self.группы)}"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление социальной сети VK.

        Возвращает:
            str: Официальное строковое представление социальной сети VK.
        """
        return f"VK(название={self.название}, пользователи={self.пользователи}, группы={self.группы})"

    def добавить_группу(self, группа: str) -> None:
        """
        Добавляет группу в социальную сеть VK.

        Аргументы:
            группа (str): Название группы для добавления.
        """
        self.группы.append(группа)

    def количество_групп(self) -> int:
        """
        Возвращает количество групп в социальной сети VK.

        Возвращает:
            int: Количество групп.
        """
        return len(self.группы)


class Facebook(СоциальнаяСеть):
    """
    Дочерний класс для представления социальной сети Facebook.

    Атрибуты:
        название (str): Название социальной сети.
        пользователи (List[str]): Список пользователей социальной сети.
        страницы (List[str]): Список страниц в социальной сети Facebook.
    """

    def __init__(self, название: str, пользователи: List[str], страницы: List[str]) -> None:
        """
        Конструктор дочернего класса Facebook.

        Аргументы:
            название (str): Название социальной сети.
            пользователи (List[str]): Список пользователей социальной сети.
            страницы (List[str]): Список страниц в социальной сети Facebook.
        """
        super().__init__(название, пользователи)
        self.страницы = страницы

    def __str__(self) -> str:
        """
        Возвращает строковое представление социальной сети Facebook.

        Возвращает:
            str: Строковое представление социальной сети Facebook.
        """
        return f"Facebook: {self.название}, Пользователи: {len(self.пользователи)}, Страницы: {len(self.страницы)}"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление социальной сети Facebook.

        Возвращает:
            str: Официальное строковое представление социальной сети Facebook.
        """
        return f"Facebook(название={self.название}, пользователи={self.пользователи}, страницы={self.страницы})"

    def добавить_страницу(self, страница: str) -> None:
        """
        Добавляет страницу в социальную сеть Facebook.

        Аргументы:
            страница (str): Название страницы для добавления.
        """
        self.страницы.append(страница)

    def количество_страниц(self) -> int:
        """
        Возвращает количество страниц в социальной сети Facebook.

        Возвращает:
            int: Количество страниц.
        """
        return len(self.страницы)


# Пример использования
if __name__ == "__main__":
    vk = VK("VK", ["user1", "user2"], ["group1", "group2"])
    facebook = Facebook("Facebook", ["user3", "user4"], ["page1", "page2"])

    print(vk)
    print(repr(vk))
    vk.добавить_пользователя("user5")
    vk.добавить_группу("group3")
    print(f"Количество пользователей VK: {vk.количество_пользователей()}")
    print(f"Количество групп VK: {vk.количество_групп()}")

    print(facebook)
    print(repr(facebook))
    facebook.добавить_пользователя("user6")
    facebook.добавить_страницу("page3")
    print(f"Количество пользователей Facebook: {facebook.количество_пользователей()}")
    print(f"Количество страниц Facebook: {facebook.количество_страниц()}")