
from time import sleep
from main import youtubeBot
from os.path import isfile, join
import os
from os import listdir
import os.path
from random import choice
#from threading import Thread
#from multiprocessing import Process
import asyncio



PhotoPath = "C:\\Users\\pe\\Desktop\\youtube\\videos"


os.chdir(PhotoPath)
ListFiles = sorted([f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))])
print(f'Existe: {len(ListFiles)} vídeos')

titulo_1 = ['HELLO WORD','ISSO É UM TESTE']
descricao_1 = ['HAHAHAHAHAHAHAAHAHAHAHAHAH','HELLO']

#r(self,titulo,caminho_path,descricao,keys_words:str):


print('ATRIBIU')

Bot = youtubeBot()




#Bot = youtubeBot()
#asyncio.run(Bot.startf())


sleep(3)


async def loading():

	global Bot
	print(type(Bot))
	for i in ListFiles:
		video = os.path.abspath(i)
	#print(video)
		print("=" * 10)
		print(f'Vídeo Upado: {video} \n')
		print("=" * 10)
		titulo_ = choice(titulo_1)
		descricao_ = choice(descricao_1)
		keys = "Lula ladrão, Lula13, Lula presidente"
#self,titulo,caminho_path,descricao,keys_words
		await Bot.postar(titulo = titulo_,caminho_path= video,descricao= descricao_,keys_words= keys)



async def tasks():
	global Bot
	tasks_primary = asyncio.create_task(Bot.startf())
	tasks_segundary = asyncio.create_task(loading())

	await tasks_primary
	tasks_segundary




asyncio.run(tasks())























'''async def projec():
	Bot = youtubeBot()
	Bot.start()
	Bot.login()
	Bot.navegar()
	Bot.postar()



Bot = youtubeBot()

Bot.start()
sleep(3)
Bot.login()
sleep(3)
Bot.navegar()
sleep(3)
Bot.postar()

'''

