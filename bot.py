import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import main_token

vk_session = vk_api.VkApi(token = main_token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def sender(id, text):
	vk_session.method("messages.send", {'user_id' : id, "message" : text, "random_id" : 0})

for event in longpoll.listen():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me: 
			msg = event.text.lower()
			id = event.user_id

			if msg == 'привет':
				sender(id, 'Привет, лох.')
			if msg == 'сам такой':
				sender(id, 'Нет ты!')
input()
