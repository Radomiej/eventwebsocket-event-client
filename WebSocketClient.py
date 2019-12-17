import websocket


class WebSocketClient:

    def send_message(self, message):
        print("send message..." + message)
        self.ws.send(message)

    def on_message(self, message):
        print("received: " + message)
        self.messages_listener.on_message(message)

    def on_error(self, error):
        print(error)

    def on_close(self):
        print("### closed ###")

    def on_open(self):
        self.running = True
        self.messages_listener.on_open(self)

    def close(self):
        self.ws.close()

    def __init__(self, messages_listener):
        self.running = False
        self.messages_listener = messages_listener
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("ws://localhost:4649/Javity",
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever()
