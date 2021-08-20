import codecs
import re
from collections import Counter
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pymorphy2


file = codecs.open("dannye.csv", "r", "utf-8" ) # read csv file to make changes
data = file.read()
data_lower = data.lower() # all word to lower


def remove_URL(text): #delete all links
    """Remove URLs from a text string"""
    return re.sub(r"https?://[^,\s]+,?", "  ", data_lower) #re.sub(r"http://\S+|https://\S+", "", text)

def delete_tags(text):
    return re.sub(r'<.*?>', ' ', text)

def remove_punctuation(text):
    # remove all punctuation
    return re.sub(r'[^\w\s]', ' ', text) #re.sub(r'[_,:;#"\'\.!?№><»«]', ' ', text)

def remove_non_relevant (text):
    return  re.sub(r'[a-z]\S+|[a-z]', ' ', text) #re.sub(r"id\S+|club\S+", "", text)

def remove_tags(text):
    return re.sub(r'<.*?>',' ', text)


r_url = remove_URL(data_lower)
r_tags= remove_tags(r_url)
r_punctuation= remove_punctuation(r_tags)
r_non_relevant = remove_non_relevant(r_punctuation)


a= word_tokenize(r_non_relevant, language='Russian') # Убераю стоп слова из текста
#print(a)
s = []
en_stops = set(stopwords.words('russian'))
for word in a:
    if word not in en_stops:
        s.append(word)
#print(s)



#lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in s])
#print(lemmatized_output)

# КОД НИЖЕ ВЫПОЛНЯЕТ УДАЛЕНИЕ ОКОНЧАНИЯ НЕ ЛЕМАНТИЗАЦИЮ
# from nltk.stem.snowball import SnowballStemmer
# stemmer = SnowballStemmer("russian")
# l=[stemmer.stem(word) for word in s]
# print(l)

#КОД НИЖЕ ВЫПОЛНЯЕТ НЕ КОНТЕКСТНУЮ ЛЕМАНТЕЗАЦИЮ
res = []
morph = pymorphy2.MorphAnalyzer()
for word in s:
    p = morph.parse(word)[0]
    res.append(p.normal_form)
#print(res)
counter = Counter(res)
print(sorted(res, key=counter.get, reverse=True)) # Отсортированные слова по частоте употребления

print(counter.most_common(100))# ВЫВОДИТ ТОП 100 самых популярных слов


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