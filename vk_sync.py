import os
import getpass
import vk


APP_ID = os.environ.get('VK_APP_ID')


def get_user_login():
    return input('Enter login: ')


def get_user_password():
    return getpass.getpass('Enter password: ')


def create_session(login='#', password='#'):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=os.environ.get('VK_APP_LOGIN'),
        user_password=os.environ.get('VK_APP_PASS'),
        scope=['account', 'friends', 'docs'],
        )
    api_session = vk.API(session)
    return api_session


def get_online_friends(api):
    friends_id_online = api.friends.getOnline()
    friends_online = api.users.get(user_ids=friends_id_online)
    return friends_online


def get_acc_info(api):
    info = api.account.getCounters()
    return info


def get_docs(api):
    docs = api.docs.get()
    return docs

def output_friends_to_console(friends_online):
    print('Friends are currently online:')
    for friend in friends_online:
        print(friend['last_name'], friend['first_name'])


if __name__ == '__main__':
    # login = get_user_login()
    # password = get_user_password()
    api = create_session()
#    friends_online = get_online_friends(api)
    acc_info = get_acc_info(api)
    print(acc_info)
    docs = get_docs(api)
    print(docs)
#    output_friends_to_console(friends_online)
