class BasicWord():
    """
    Класс слова (слово, подслова)
    """

    def __init__(self, word='', subwords=None):
        self.word = word
        if subwords is None:
            self.subwords = []
        else:
            self.subwords = subwords

    def __repr__(self):
        return f"BasicWord(word={self.word}, subwords={self.subwords})"

    def get_word(self):
        """
        Исходное слово
        :return: str
        """
        return self.word

    def count_subwords(self):
        """
        Подсчет количества подслов в списке.
        :return: int
        """
        return len(self.subwords)

    def has_subwords(self, word):
        """
        Проверка есть ли слово введенное игроком в загаданном слове.
        :param word: слово
        :return: True/False
        """
        return word in self.subwords



