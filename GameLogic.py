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

    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.event_bus.register_listener('YourPlayerEvent', self.your_player_listener)
        self.event_bus.register_listener('CreatePlayerEvent', self.create_player_listener)
        self.event_bus.register_listener('CreateShipEvent', self.create_ship_listener)
        self.event_bus.register_listener('ShipPositionEvent', self.ship_position_listener)

    def ship_position_listener(self, event):
        print('ship_position_listener')

    def create_ship_listener(self, event):
        print('create_player_listener')

    def create_player_listener(self, event):
        print('create_player_listener')

    def your_player_listener(self, event):
        print('your_player_listener')

    def on_message(self, message):
        print(message)

    def on_open(self, ws_client):
        def run():
            for i in range(30):
                time.sleep(1)
                ws_client.send_message(message_text)
            time.sleep(1)
            ws_client.close()
            print("thread terminating...")

        thread.start_new_thread(run, ())
