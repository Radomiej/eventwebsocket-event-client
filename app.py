from GameLogic import GameLogic
from WebSocketClient import WebSocketClient


if __name__ == "__main__":
    game_logic = GameLogic()
    ws_client = WebSocketClient(game_logic)
