import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random


TOKEN = 'YOUR_TOKEN'

def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, id_сообщества)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('New message:')
            print('For me from:', event.obj.message['from_id'])
            print('Text:', event.obj.message['text'])
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj.message['from_id'],
                             message="Thank you for writing to us. We will definitely respond",
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()