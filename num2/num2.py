def begin_to_end(beginword, endword): #������ �������
    beginw = list(beginword) #��������� ����� � ������
    wordlist = [] #�������������� �������
    j = 0 #������� ��� ����� � 1 �����
    l = 0 # ������� ��� ��������
    for i in list(beginword): #����������� �������
        wordlist.append(i) #���������� 2 ���� �����
        wordlist.append(i)
        if not i in list(endword): #���� ����� ���������� � ����� �� ���� �� ������� 0 ��� ��� ����������� ����������
            return 0
    while not beginword == endword: #���� �� �����������
        if j >= int(len(beginword)): #���� ����� ��������� �� �����
            exit()
        x = list(beginword[j]) #������� ����� � ���������
        l = 0 #��������� ��� ������
        print(beginw)
        for i in endword: #������� � �������� ����� ��� ������
            if list(i) == x: #���� ������������� - ��������
                beginw[l] = x
                print(beginw)
                j+=1
                l+=1
            else: #���� ���, �� ��������
                l+=1

one = '�����'
two = '�����'
print(begin_to_end(one, two))
