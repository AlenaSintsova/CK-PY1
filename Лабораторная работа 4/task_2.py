main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
""".lower() #нижний регистр

main_str = "".join(c for c in main_str if c.isalpha())

dictionary_of_symbols = {symbol: main_str.count(symbol) for symbol in main_str} #кол-во букв
print(dictionary_of_symbols)