import test.performance as performance
import test.stress as stress
import test.hardware as hardware
from time import sleep
from test.lib import get_format_test_str

test_map = {
    'performance': {},
    'stress': {},
    'hardware': {}
}

test_name_zN = {
    'cpu_stress':'CPU压力测试',
    'ram_stress':'RAM压力测试',
    'cpu_frequence':'CPU性能测试',
    'emmc_speed':'EMMC性能测试',
    'ram_speed':'RAM性能测试',
    'eth_speed':'网卡模块测试',
    'jc_test':'交采模块测试'
}

for key in test_map.keys():
    global_object = globals()
    md = global_object.get(key)
    for name in dir(md):
        if name.find('__') == 0 or name.find('_') == -1:
            continue
        test_map[key][name] = getattr(md, name)


def test(test_array, test_type):
    global test_map
    result = []
    test_list = []
    print()
    print()
    print('\033[1;32m \t*********************************** \033[0m')
    print('\033[1;32m \t     {} start  \033[0m'.format(test_type))
    print('\033[1;32m \t*********************************** \033[0m')
    for test in test_array:
        try:
            test_list.append({
                'func': test_map[test_type][test['type']],
                'param': test['param']
            })
        except Exception as e:
            pass
    
    for test in test_list:
        print('\033[1;32mnow test:{} \033[0m'.format(test['func'].__name__))
        for r in test['func'](test['param']):
            r['type'] = test_name_zN[test['func'].__name__]
            result.append(r)
            print(get_format_test_str(r))
        sleep(3)
    return result