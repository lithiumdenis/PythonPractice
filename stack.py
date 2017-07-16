class MyStack:
    #Инициализация стека размера n
    def __init__(self, n=0):
        self.size = n
        self.len = 0
        self.arr = [None] * n
        self.top = -1
        
    #Проверка стека на пустоту
    def isEmpty(self):
        return self.top == -1
    
    #Проверка стека на переполнение
    def isFull(self):
        return self.top == self.size - 1
    
    #Получение размера стека
    def getSize(self):
        return self.len
    
    #Проверка top элемента
    def peek(self):
        if (self.isEmpty()):
            raise ValueError('Underflow exception')
        return self.arr[self.top]
    
    #Добавление элемента в стек
    def push(self, i):
        if(self.top + 1 >= self.size):
            raise ValueError('Overflow exception')
        if(self.top + 1 < self.size):
            self.top += 1
            self.arr[self.top] = i
        self.len = self.len + 1
        
    #Взятие элемента из стека
    def pop(self):
        if (self.isEmpty()):
            raise ValueError('Underflow exception')
        self.len = self.len - 1
        self.top -= 1
        return self.arr[self.top + 1]
    
    #Печать стека
    def display(self):
        print('Содержимое стека: ', end=' ')
        if(self.len == 0):
            print('Стек пуст')
        else:
            i = self.top
            while (i >= 0):
                #end=' ' в строку, без него - в столбец
                print(self.arr[i], end=' ') 
                i -= 1
            #Возвращаем по умолчанию форматирование окончания print
            print('', end='\n')
    

#Test's
#1
print('Проверка работы стека:')
print('----------Тест 1:----------')
myst = MyStack(5)
print('Стек пуст:', myst.isEmpty())
print('Стек заполнен:', myst.isFull())
#print(myst.peek())
myst.display()
#2
print('----------Тест 2:----------')
myst.push(33)
myst.push(70)
myst.push(67)
myst.push(7)
print('Стек пуст:', myst.isEmpty())
print('Стек содержит элементов:', myst.getSize())
myst.display()     
#3
print('----------Тест 3:----------')
myst.push(41)
myst.display()  
print('Результат peek: ', myst.peek())
myst.display()  
print('Стек заполнен:', myst.isFull())
#4
print('----------Тест 4:----------') 
print('Размер до pop:', myst.getSize())
print('Результат pop: ', myst.pop())
print('Размер после pop', myst.getSize())
myst.display()