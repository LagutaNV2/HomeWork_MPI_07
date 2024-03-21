class Stack:
    
    
    def __init__(self):
        self.stck = []
    
    def __str__(self):
        return f'{[item for item in self.stck]}'
    
    def __repr__(self):
        return self.__str__()
    
    def is_empty(self):
        return self.stck == []
        
    def push_element_to_stack(self, element):
        self.stck.append(element)
        
    def pop_from_stack(self):
        try:
            return self.stck.pop()
        except IndexError:
            return f'!pop from empty stack!'
        
    def peek_from_stack(self):
        if self.is_empty():
            return f'!peek from empty stack!'
        else:
            return self.stck[-1]
            
    def size_from_stack(self):
        return f'size of stack: {len(self.stck)}'
        
    
if __name__ == "__main__":

# вспомогательный блок тестирования класса, так как с тестовым файлом проблема
# нужен совет, как настраивается файл для тестирования класса из другого пакета
# и совет, как можно  настроить метод для печать списка, не тлько строки

    stack1 = Stack()
    print(f'первый принт, {stack1 = }')
    print(f'{stack1.size_from_stack()}, {stack1.is_empty()=}')
    print(f'{stack1.pop_from_stack()=}')
    print(f'peek1, empty: {stack1.peek_from_stack()=}')
    stack1.push_element_to_stack(1)
    print(f'{stack1.is_empty()=}')
    stack1.push_element_to_stack(2)
    print(f'{stack1 = }')
    stack1.push_element_to_stack(3)
    print(f'{stack1.size_from_stack()}, {stack1.is_empty()=}')
    print(f'peek2: {stack1.peek_from_stack()=}')
    print(f'{stack1.size_from_stack()}, {stack1.pop_from_stack()=}')
    print(f'{stack1.size_from_stack()}, {stack1.pop_from_stack()=}')
    print(f'{stack1.size_from_stack()}, {stack1.pop_from_stack()=}')
    print(f'{stack1.size_from_stack()}, {stack1.pop_from_stack()=}')
