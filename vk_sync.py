import os
import json
import vk


ACCESS_TOKEN = os.environ.get('VK_A_T')


def create_session():
    session = vk.Session(access_token=ACCESS_TOKEN)
    api_session = vk.API(session)
    return api_session


def get_online_friends(api):
    friends_id_online = api.friends.getOnline()
    friends_online = api.users.get(user_ids=friends_id_online)
    return friends_online


def output_friends_to_console(friends_online):
    print('Friends are currently online:')
    for friend in friends_online:
        print(friend['last_name'], friend['first_name'])


def get_acc_info(api):
    info = {
    'getInfo': api.account.getInfo(),
    'getProfileInfo': api.account.getProfileInfo(),
    'gifts': api.account.getCounters(),
    }
    return info


def get_docs(api):
    docs = api.docs.get()
    return docs


def get_chats(api):
    chats = api.messages.get()
    return chats


def get_photos(api):
    photos = api.photos.getAll()
    return photos


def get_videos(api):
    videos = api.video.get()
    return videos


def save_to_file(data, file_name, as_json=False):
    with open(file_name, 'w') as data_file:
        if as_json:
            data_file.write(json.dumps(data))
        else:
            data_file.write(data)


if __name__ == '__main__':
    api = create_session()
