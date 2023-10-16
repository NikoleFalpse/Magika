#Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
import collections
words = input("Введите текст: ").split()
counter = collections.Counter(words)
most_common, frequency = counter.most_common()[0]
longest = max(words, key=len)
print("Часто встречающееся: "+str(most_common),"Самое длинное:"+ str(longest), sep="\n")