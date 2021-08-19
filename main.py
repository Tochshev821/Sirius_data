import pandas as pd
import numpy as np
import codecs
import re
import string
import nltk
nltk.download("stopwords")

from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation





# Сначала удалить ссылки, потом пунктуациЮ,
# удалить нерелевантные слова (ссылки, слова на английском, и. т .д);
# - удалить стоп слова с помощью готовых словарей ( при необходимости дополнить словарь);
# - выполнить лемматизацию ( привести все слова в их начальную словоформу).
#
# 2. Отсортировать слова по частоте их употребления и выделить топ 100 слов

#data = pd.read_csv('dannye.csv', delimiter=';')


file = codecs.open("dannye.csv", "r", "utf-8" ) # read csv file to make changes
data = file.read()
data_lower = data.lower() # all word to lower


def remove_URL(text): #delete all links
    """Remove URLs from a text string"""
    return re.sub(r"https?://[^,\s]+,?", "  ", data_lower) #re.sub(r"http://\S+|https://\S+", "", text)

def delete_tags(text):
    return re.sub(r'<.*?>', '', text)

def remove_punctuation(text):
    # remove all punctuation
    return re.sub(r'[^\w\s]', ' ', text)

def remove_non_relevant (text):
    return re.sub(r"id\S+", "", text)

def remove_tags(text):
    return re.sub(r'<.*?>','', text)


r_url = remove_URL(data_lower)
r_tags= remove_tags(r_url)
r_punctuation= remove_punctuation(r_tags)
r_non_relevant = remove_non_relevant(r_punctuation)
#print(r_non_relevant)
mystr = re.sub(r"[qwertyuiopasdfghjklzxcvbnm]", "", r_non_relevant)
print(mystr)

#Create lemmatizer and stopwords list
mystem = Mystem()
russian_stopwords = stopwords.words("russian")

#ПРИМЕР ТОГО КАК МОЖНО СТОП СЛОВА ВЫТАЩИТЬ ИЗ ТЕКсТА
# list_of_stop_words = ["в", "и", "по", "за"]
#
# # Строка со стоп-словами
# string_to_process = "Сервис по поиску работы и сотрудников HeadHunter опубликовал подборку высокооплачиваемых вакансий в России за август."
#
# # lambda-функция, фильтрующая стоп-слова
# split_str = string_to_process.split()
# filtered_str = ' '.join((filter(lambda s: s not in list_of_stop_words, split_str)))
#
# print("Отфильтрованная строка:a", filtered_str)