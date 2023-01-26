class Player:
    """
    Класс игрока (имя игрока и слова использованные игроком)
    """

    def __init__(self, name='', input_word=None):
        self.name = name

        if input_word is None:
            self.input_word = []
        else:
            self.input_word = input_word

    def __repr__(self):
        return f'Player(name={self.name}, input_word = {self.input_word})'

    def get_name(self):
        """
        Возврат имени игрока.
        :return: str
        """
        return self.name

    def add_word(self, word):
        """
        Добавление слова в список.
        :param word: слово
        """
        self.input_word.append(word)

    def count_input_word(self):
        """
        Возврат количества введенных слов игроком.
        :return: int
        """
        return len(self.input_word)

    def has_input_word(self, word):
        """
        Возврат использованного слова.
        :param word: Слово
        :return: True/False
        """
        return word in self.input_word

