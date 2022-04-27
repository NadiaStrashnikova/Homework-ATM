import sys

from clients import Client, ListClients

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

def оperation_by_client(real_client: Client):
    izbor = int(input('Какво избирате Теглене/Внасяне/Баланс (1/2/3) : '))
    if izbor == 1:
        withdrawing_money(real_client)
    elif izbor == 2:
        money_laundering(real_client)
    elif izbor == 3:
        real_client.print_balance()
        sys.exit()
