from class_stack import Stack


def brackets_balance_check(subsequence):
    if len(subsequence) == 0 or len(subsequence) % 2 != 0:
        return f'последовательность {subsequence} несбалансированная'
    
    brackets = ['{}', '()', '[]']
    brackets_open = ['{', '(', '[']
    
    stack_1 = Stack()
    
    for smbl in subsequence:
        
        if smbl in brackets_open:
            stack_1.push_element_to_stack(smbl)
        
        elif stack_1.is_empty():
            return (f'для {smbl=} скобки нет никаких открывающих-> несбалансиров; '
                    f'последовательность {subsequence} несбалансированная')
        
        else:
            pre_simbol = stack_1.peek_from_stack()
            pair = '' + pre_simbol+smbl
            
            if pair in brackets:
                stack_1.pop_from_stack()
            else:
                return (f'для закрывающей скобки {smbl=} нет открывающей ->'
                        f'последовательность {subsequence} несбалансированная')

    return f'последовательность {subsequence} сбалансированная'


if __name__ == "__main__":
    print('test1', brackets_balance_check('(((([{}]))))'))
    print('-----------------------------------------------')
    print('test2', brackets_balance_check('[([])((([[[]]])))]'))
    print('-----------------------------------------------')
    print('test3', brackets_balance_check('{()}'))
    print('-----------------------------------------------')
    print('test4', brackets_balance_check('{{[()]}}'))
    print('-----------------------------------------------')
    print('test5', brackets_balance_check('}{}'))
    print('-----------------------------------------------')
    print('test6', brackets_balance_check('{{[(])]}}'))
    print('-----------------------------------------------')
    print('test7', brackets_balance_check('[[{())}]'))
    print('-----------------------------------------------')
    print('test8', brackets_balance_check('(((([{]}]))))'))
    print('-----------------------------------------------')
                
            
            
            
            
            
    


    
        
    
    