"""
Считайте файл согласно вашему варианту и подсчитайте частоту каждого слова в тексте. В результирующем файле выведите
полученные данные в порядке убывания:
word1:freq1
word2:freq2
word3:freq3
-----------
wordN:freqN
"""
import string

with open('text_1_var_67.txt', 'r') as file:
    data = file.read()

to_translate = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
data = data.translate(to_translate)

words = data.split()

print(words[:5])
print(len(words))

unique_items = set(words)
print(len(unique_items))

empty = words.count(' ')
print(empty)

words_frequency = {}
for word in words:
    if word not in words_frequency:
        words_frequency[word] = words.count(word)

words_frequency = dict(sorted(words_frequency.items(), key=lambda item: item[1], reverse=True))
print(words_frequency)
print(type(words_frequency))

with open('text_1_var_67_result.txt', 'w') as result:
    for key, value in words_frequency.items():
        result.write(key + ':' + str(value) + '\n')
