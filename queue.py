class MyQueue:
    #Инициализация очереди размера n
    def __init__(self,n):
        self.size = n
        self.len = 0
        self.queue = [None] * n
        self.front = -1 #Передний
        self.rear = -1  #Задний
        
    #Проверка на пустоту
    def isEmpty(self):
        return self.front == -1
    
    #Проверка на переполнение
    def isFull(self):
        return self.front == 0 and self.rear == self.size - 1
    
    #Получение размера стека
    def getSize(self):
        return self.len
    
    #Проверка front элемента
    def peek(self):
        if (self.isEmpty()):
            raise ValueError('Underflow exception')
        return self.queue[self.front]
    
    #Постановка в очередь
    def enqueue(self, i):
        if(self.rear == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = i
        elif(self.rear + 1 >= self.size):
            raise ValueError('Overflow exception')
        elif(self.rear + 1 < self.size):
            self.rear += 1
            self.queue[self.rear] = i
        self.len += 1
        
    #Удаление из очереди
    def dequeue(self):
        if (self.isEmpty()):
            raise ValueError('Underflow exception')
        else:
            self.len -= 1
            ele = self.queue[self.front]
            if(self.front == self.rear):
                self.front = -1
                self.rear = -1
            else:
                self.front += 1
            return ele
    
    #Печать очереди
    def display(self):
        print('Содержимое очереди:', end=' ')
        if(self.len == 0):
            print('Очередь пуста')
        else:
            i = self.front
            while (i <= self.rear):
                #end=' ' в строку, без него - в столбец
                print(self.queue[i], end=' ') 
                i += 1
            #Возвращаем по умолчанию форматирование окончания print
            print('', end='\n')

#Тесты
#1
print('Проверка работы очереди:')
print('----------Тест 1:----------')
que = MyQueue(5)
print('Очередь пуста:', que.isEmpty())
print('Очередь заполнена:', que.isFull())
#print(que.peek())
que.display()
#2
print('----------Тест 2:----------')
que.enqueue(33)
que.enqueue(70)
que.enqueue(67)
que.enqueue(7)
print('Очередь пуста:', que.isEmpty())
print('Очередь содержит элементов:', que.getSize())
que.display()     
#3
print('----------Тест 3:----------')
que.enqueue(41)
que.display()  
print('Результат peek: ', que.peek())
que.display()  
print('Очередь заполнена:', que.isFull())  
#4
print('----------Тест 4:----------') 
print('Размер до dequeue:', que.getSize())
print('Результат dequeue: ', que.dequeue())
print('Размер после dequeue', que.getSize())
que.display()