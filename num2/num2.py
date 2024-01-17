def begin_to_end(beginword, endword): #Начало функции
    beginw = list(beginword) #начальное слово в список
    wordlist = [] #инициализируем словарь
    j = 0 #счетчик для буквы в 1 слове
    l = 0 # счетчик для итераций
    for i in list(beginword): #составление словаря
        wordlist.append(i) #добавлеине 2 раза буквы
        wordlist.append(i)
        if not i in list(endword): #если буква отсутствет в одном из слов то вернуть 0 так как отсутствует комбинация
            return 0
    while not beginword == endword: #пока не преобразует
        if j >= int(len(beginword)): #если буквы кончились то выход
            exit()
        x = list(beginword[j]) #текущая буква в сравнении
        l = 0 #обнуление для дебага
        print(beginw)
        for i in endword: #перебор в конечном слове для замены
            if list(i) == x: #если соответствует - заменяем
                beginw[l] = x
                print(beginw)
                j+=1
                l+=1
            else: #если нет, то заменяем
                l+=1

one = 'товар'
two = 'автор'
print(begin_to_end(one, two))
