import paho.mqtt.client as mqtt
import json
from time import sleep
import threading


jc_result = {
    'flag': False,
    'message':'jc module dont response'
}

mqttc = {}

def jc_test(d):
    ip = d['ip']
    port = d['port']
    interval = d['interval']
    times = d['times']
    try:
        mqtt_init(ip, port, interval, times)
    except Exception as e:
        return [{
            "flag": False,
            "message": 'create mqtt client error!'
        }]
    sleep(interval * times + 3)
    return [jc_result]


def on_message(mqttc, obj, msg):
    topic = msg.topic
    payload = bytes.decode(msg.payload)
    print(topic)
    if topic == 'test/jc/response':
        data = json.loads(payload)
        global jc_result
        if data['statusCode'] == 200:
            jc_result['flag'] = True
            jc_result['message'] = json.dumps(data['body'])
        else:
            jc_result['flag'] = False
            jc_result['message'] = data['body']['errorDesc']
        mqttc.disconnect()


def send_message(mqttc, interval, time):
    i = 0
    d = {
            "token":"123456",
            "timestamp":"",
            "body": {
                "type":"get",
            }
    }
    try:
        while i < time:
            mqttc.publish('test/jc/request', json.dumps(d))
            sleep(interval)
    except Exception as e:
        print(e)


def mqtt_init(ip, port, interval, times):
    global mqttc
    mqttc = mqtt.Client(clean_session=True, userdata=None, protocol=mqtt.MQTTv31, transport="tcp")
    mqttc.on_message = on_message
    mqttc.connect(ip, port, 30)
    threading.Thread(target=send_message, args=(mqttc, interval, times)).start()
    mqttc.subscribe('test/jc/response', 2)
    mqttc.loop_start()
    sleep(10)