from test.lib import run_shell
import re
def deal_shell(shell_result):
    if shell_result.find("/s") == -1:
        return -1
    for line in shell_result.split("\r\n"):
        if line.find("/s") == -1:
            continue;
        ds = re.split(' *', line.strip());
        return float(ds[len(ds)-2])

def eth_speed(d):
    serverip = d["serverip"]
    standard = d["speed"]
    result = []
    command = "$HOME/test/bin/iperf -c " + serverip + " -f m"
    shell_result = run_shell(command)
    speed = deal_shell(shell_result)
    if speed == -1:
        result.append({
            "flag": False,
            "message": 'cant connect iperf server!'
        })
    elif speed < standard:
        result.append({
            "flag": False,
            "message": 'Eth speed is {} Mb/s'.format(str(speed))
        })
    elif speed >= standard:
        result.append({
            "flag": True,
            "message": 'Eth speed is {} Mb/s'.format(str(speed))
        })
    return result