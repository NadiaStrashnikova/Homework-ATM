from client_actions import  оperation_by_client
from clients_administration import get_real_client


if __name__ == '__main__':

#    Input for which one client is all about
    real_client = get_real_client()

#    What kind of action will be doing
    оperation_by_client(real_client)
