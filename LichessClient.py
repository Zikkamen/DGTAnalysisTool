import requests


class LichessClient:
    def __init__(self):
        token = ""
        self.params = {'Authorization': f'Bearer {token}'}
        self.url = 'https://lichess.org/api/broadcast/analyse/analysis/Ppb0ymzn'
        self.broadcast_id = 'Ppb0ymzn'

    def push_pgn_to_lichess(self, game_str: str):
        r = requests.post(f"https://lichess.org/api/broadcast/round/{self.broadcast_id}/push", headers=self.params, data=game_str)

        print(r.status_code)
        print(r.text)


if __name__ == "__main__":
    lichess_client = LichessClient()
