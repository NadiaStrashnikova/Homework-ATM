import sys

from clients import Client, ListClients


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


def withdrawing_money(real_client: Client):
    tegli_suma = float(input('Колко теглите:'))
    while real_client.balance < tegli_suma:
        tegli_suma = float(input('Сумата е повече от наличното. Колко теглите:'))
    real_client.subtract_from_balance(tegli_suma)
    real_client.print_balance()
    sys.exit()


def money_laundering(real_client: Client):
    add_s = float(input('Колко внасяте:'))
    real_client.add_to_balance(add_s)
    real_client.print_balance()
    sys.exit()


if __name__ == '__main__':
    all_clients = ListClients()
    all_clients.load_clients()

#    Input for which one client is all about
    name = input('Въведете име:')
    real_client = all_clients.check_if_client_exists(name)
    if real_client == None:
        sys.exit()
    get_pin(real_client)
    real_client.print_balance()

#    What kind of action will be doing
    izbor = int(input('Какво избирате Теглене/Внасяне/Баланс (1/2/3) : '))
    if izbor == 1:
        withdrawing_money(real_client)
    elif izbor == 2:
        money_laundering(real_client)
    elif izbor == 3:
        real_client.print_balance()
        sys.exit()
