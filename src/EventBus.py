import json


class EventBus:

    subscribers = {}

    def __init__(self):
        pass

    def on_message(self, message):
        message_obj = json.loads(message)
        *others, last = message_obj['type'].split('.')
        if last in self.subscribers.keys():
            self.subscribers[last](message_obj)
        else:
            print('Subscriber for event is missing: ' + last)

    def on_open(self):
        pass

    def add_transport(self, ws_client):
        ws_client.add_receiver(self)

    def register_listener(self, event_name, handler):
        self.subscribers[event_name] = handler

