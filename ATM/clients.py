import json
from os import path


class Client:

    def __init__(self, first_name: str, pin: str, balance: float):
        self._first_name = first_name
        self._pin = pin
        self.balance = balance

    @property
    def first_name(self):
        return self._first_name

    @property
    def pin(self):
        return self._pin

    def print_balance(self):
        print(f"Наличност по карта: {self.balance}")

    def subtract_from_balance(self, value_to_subtract: float):
        self.balance -= value_to_subtract

    def add_to_balance(self, value_to_add: float):
        self.balance += value_to_add


class ClientsList:

    def __init__(self):
        self._all_clients = []
        self.load_clients()

    def load_clients(self):
        file_name = path.abspath('ATM.list_clients.json')
        with open(file_name, "r") as f:
            self._all_clients = json.load(f)

    def check_if_client_exists(self, s: str) -> Client:
        for one_client in self._all_clients:
            if one_client["_name"] == s:
                founded_client = Client(s, one_client["_pin"], one_client["balance"])
                return founded_client
        print('Няма такова име')
        return None
