import time

try:
    import thread
except ImportError:
    import _thread as thread

import json

message_template = {
    'channel': 'test',
    'message': ''
}

ship_control_message = {
    'shipId': 1,
    'forceForward': 5
}

message_template['message'] = json.dumps(ship_control_message)
message_text = json.dumps(message_template)


class GameLogic:

    def __init__(self):
        pass

    def on_message(self, message):
        print(message)

    def on_open(self, ws_client):
        def run(*args):
            for i in range(30):
                time.sleep(1)
                ws_client.send_message(message_text)
            time.sleep(1)
            ws_client.close()
            print("thread terminating...")

        thread.start_new_thread(run, ())
