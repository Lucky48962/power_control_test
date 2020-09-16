
def record(result):
    #test = [{'message': 'average CPU freq 1800.001MHZ!', 'type': 'CPU性能测试', 'flag': True}, {'message': 'num: 0 CPU freq: 1800.001MHZ!', 'type': 'CPU性能测试', 'flag': True}, {'message': 'num: 1 CPU freq: 1800.001MHZ!', 'type': 'CPU性能测试', 'flag': True}, {'message': 'num: 2 CPU freq: 1800.001MHZ!', 'type': 'CPU性能测试', 'flag': True}, {'message': 'num: 3 CPU freq: 1800.001MHZ!', 'type': 'CPU性能测试', 'flag': True}]
    for joins in result:
        read_file(str(joins.get('type'))+ ','+ str(joins.get('message'))+ ','+ str(joins.get('flag'))+ '\r\n')

def read_file(read):
    f = open("result_log.txt", "a")
    f.write(read)
