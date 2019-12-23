from GameLogic import GameLogic
from WebSocketClient import WebSocketClient
from src.EventBus import EventBus

if __name__ == "__main__":
    event_bus = EventBus()
    game_logic = GameLogic(event_bus)

    ws_client = WebSocketClient(event_bus)

