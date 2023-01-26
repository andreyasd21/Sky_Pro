import random
import requests

from Domashki_FULL.Kursovaya.basic_word import BasicWord


def load_random_word(json_url):
    """
    Функция из файла JSON возвращает случайное слово и его подслова.
    :param json_url: JSON
    :return: BasicWord
    """
    result = requests.get(json_url)
    result_data = result.json()

    word_data = random.choice(result_data)
    basic_word = BasicWord(word_data['word'], word_data['subwords'])

    return basic_word
