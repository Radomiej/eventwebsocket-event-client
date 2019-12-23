import websocket


class WebSocketClient:
    receivers = []

    def send_message(self, message):
        print("send message..." + message)
        self.ws.send(message)

    def on_message(self, message):
        print("received: " + message)
        for receiver in self.receivers:
            receiver.on_message(message)

    def on_error(self, error):
        print(error)

    def on_close(self):
        print("### closed ###")

    def on_open(self):
        self.running = True
        for receiver in self.receivers:
            receiver.on_open()

    def close(self):
        self.ws.close()

    def add_receiver(self, receiver):
        self.receivers.append(receiver)

    def __init__(self, receiver):
        self.running = False
        self.receivers.append(receiver)
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("ws://localhost:4649/Javity",
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever()
