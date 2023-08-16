""" Задача 1

Создайте класс TodoList, который хранит ваши задачи.
Реализуйте магические методы, которые позволят добиться следующего поведения:

>>> tasks = ['task1', 'task2']

>>> list1 = TodoList(tasks)

>>> print(repr(list1))
TodoList(list[str])

>>> print(list1)
task1
task2

Задача 2

Реализуйте магический метод, который позволит складывать два списка задач
(экземпляра класса TodoList) и получать новый список,
содержащий задачи обоих сладываемых списков:

>>> list2 = TodoList(['task3', 'task4'])

>>> list3 = list1 + list2

>>> print(list3)
task1
task2
task3
task4

Задача 3

Дополните класс TodoList, чтобы выполнялось следующее поведение:

>>> print(len(list3))
4
"""


class TodoList():

    """ Класс для предоставления списка задач """

    # -> None - возвращаем ничего
    def __init__(self, tasks: list[str]) -> None:

        """ Инициализируем атрибуты класса """

        self.tasks = tasks


    # -> str - возвращаем строку
    def __repr__(self) -> str:

        """ Магический метод для отображения информации
        об объекте класса для разработчиков """

        # self.__class__.__name__ - выводит название класса
        return f"{self.__class__.__name__}{(self.tasks)}"


    def __str__(self) -> str:

        """ Магический метод для отображения информации
        об объекте класса дял пользователей
        (тут мы делаем строку, куда записываем задачи из списка
        и плюс \n для переноса строк на новый абзац)"""

        text = ""

        for task in self.tasks:
            text += task + "\n"

        return text


    def __add__(self, other: "TodoList") -> "TodoList":

        """ Магический метод, который позволяет складывать 2 списка задач
        *self.tasks - распаковываем """

        str_tasks = [*self.tasks, *other.tasks]
        # str_tasks = self.tasks
        # str_tasks.extend(other.tasks)

        return TodoList(str_tasks)


    def __len__(self) -> int:

        """ Магический метод, который позволяет применить
        функцию len к экземплярам класса """

        return len(self.tasks)


if __name__ == '__main__':

    tasks = ["task1", "task2"]

    list1 = TodoList(tasks)

    # вызов метода repr
    print(repr(list1)) # TodoList['task1', 'task2']

    # вызов метода str
    print(list1) # task1
                 # task2

    list2 = TodoList(["task3", "task4"])

    list3 = list1 + list2

    print(list3) # task1
                 # task2
                 # task3
                 # task4

    print(len(list3)) # 4