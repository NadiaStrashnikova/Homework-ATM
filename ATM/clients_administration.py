import sys

from clients import Client, ClientsList

def get_real_client(gw)-> Client:
    all_clients=ClientsList()
    all_clients.load_clients()
    #name = Inserted_user_name()
    name = gw.Inserted_user_name()
    real_client = all_clients.check_if_client_exists(name)
    if real_client == None:
        sys.exit()
    get_pin(real_client)
    real_client.print_balance()
    return real_client

def get_pin(real_client: Client):
    ok = False
    for _ in range(1, 4):
        new_pin = input('Въведете пин:')
        if new_pin == real_client.pin:
            ok = True
            break
    if not ok:
        print('Картата е блокирана')
        sys.exit()

if __name__ == '__main__':
    test_client = get_real_client()