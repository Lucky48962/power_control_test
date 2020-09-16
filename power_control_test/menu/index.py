from time import sleep
def menu(config):
    level = 1
    d = ''
    print('\033[1;31m')
    while level:
        if level == 2:
            d = second_level(int(d), config)
        if level == 1:
            d = first_level()
            if d == '1':
                return config
        if d == 'exit':
            return False
        if d == 'back':
            level = level -1
            if level == 0:
                level = 1
            continue
        if level == 1:
            level = level + 1
            continue
        if level == 2:
            print('\033[0m')
            return d
        
def second_level(t, config):
    print('test:')
    items = []
    index = 0
    result = {
        'Stress_Test':[],
        'Performance_Test':[],
        'Hardware_Test':[]
    }
    for k in config:
        print(k+":")
        for item in config[k]:
            items.append({
                'index': index,
                'item': item,
                'type': k
            })
            print('\t{}. {}'.format(index, item['type']))
            index = index + 1
    while 1:
        d = ''
        if t == 2:
            d = input('please input test num:').strip()
        if t == 3:
            d = input('please input tests num(like:0 2 3):\n').strip()
        if d == 'exit' or d == 'back':
            return d
        if t == 2:
            if d.isdigit() == False:
                print('input error(back: to parent menu, exit: exit)\n')
                continue
            d = int(d)
            if d >= index:
                print('too large num')
                continue
            result[items[d]['type']].append(items[d]['item'])
            return result
        if t == 3:
            ds = d.split(' ')
            for num in ds:
                if num.isdigit() == False:
                    print('input error(back: to parent menu, exit: exit)\n')
                    continue
                num = int(num)
                if num >= index:
                    print('input error(back: to parent menu, exit: exit)\n')
                    continue
                result[items[num]['type']].append(items[num]['item'])
            return result

def first_level():
    print(
        'please select test type:\n'
        '1.entire test\n'
        '2.one test\n'
        '3.userdefine test\n'
        'input exit to exit'
    )
    result = input('input No.:')
    if result.isdigit():
        if int(result) > 4:
            return 'back'
        return result
    if result.strip() == "exit":
        return "exit"
    return 'back'