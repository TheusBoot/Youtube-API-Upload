#from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
from time import sleep
from random import randint
import asyncio
#from multiprocessing import Process
#from threading import Thread


#URL = "https://accounts.google.com/ServiceLogin/identifier?continue=https%3A%2F%2Fwww.youtube.com%2F&sacu=1&passive=1209600&acui=0&flowName=GlifWebSignIn&flowEntry=ServiceLogin&cid=1&TL=AB_wV5o6Wjo1SifSNCT7_jSwyYMvBd3a10LFH2YOAErstl0lt7NhQCADlWALsc24"
'''
with sync_playwright () as p:
    browser = p.firefox.launch(headless=False)
    page = browser.new_page()
    # page.fill("nome da class ", "ser prenchido com oq") #page.fill == prencher o campo...
    page.goto(URL)
    sleep(20)
    page.goto('https://studio.youtube.com/channel/UC1QV3QXnrjolOh2oocrdONQ') # acessar o canal com o id já
    sleep(5)

    page.locator('xpath=//*[@id="upload-button"]/div').click() # clicar no botão para upar o vídeo
    sleep(5)

    page.locator('xpath=//*[@id="content"]/input').set_input_files('C:/Users/pe/Downloads/SnapTik_7145177535058349317.mp4')

    #titulo  = page.locator('/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div') 
    
    sleep(5)

    browser.close()
'''

class youtubeBot():

	def __init__(self):

		self.True_or_False = False #modo em desenvolvimento

		#URL DE LOGIN
		self.url = "https://accounts.google.com/ServiceLogin/identifier?continue=https%3A%2F%2Fwww.youtube.com%2F&sacu=1&passive=1209600&acui=0&flowName=GlifWebSignIn&flowEntry=ServiceLogin&cid=1&TL=AB_wV5o6Wjo1SifSNCT7_jSwyYMvBd3a10LFH2YOAErstl0lt7NhQCADlWALsc24"
		
		self.hyper_url = "https://studio.youtube.com/channel/UC1QV3QXnrjolOh2oocrdONQ/videos/upload?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D"




		#Process(target=self.startf())
		#Thread(target=self.startf,daemon=True).start()

		#self.start()
		#playwright = sync_playwright().start()
		#with sync_playwright () as playwright:
			#self.run_time(playwright)

			#self.browser = p.firefox.launch(headless=False)
			#self.pagina = self.browser.new_page()
		
			#self.navegar()
			#self.upload()

			#self.postar()
			
		
		#self.browser = playwright.firefox.launch(headless=False)
		#self.pagina = self.browser.new_page()

	
	#async def cube(self):
		#task = asyncio.create_task(coro=self.startf())
		#await task


	
	async def startf(self):
		""" START NO UPLOAD DO VÍDEO PARA O YOUTUBE"""

		async with async_playwright() as playwright:
			await self.run_time(playwright)
	

	async def run_time(self,playwright):

		""" Costrução do inicializador..."""

		self.browser =  await playwright.firefox.launch(headless=False)
		self.context = await self.browser.new_context()
		self.pagina = await self.context.new_page()
		#self.pagina = await self.browser.new_page()
		#self.pagina.wait_for_timeout(0)
		sleep(6)
		await asyncio.sleep(2)
		
		await self.pagina.goto(self.url)
		await asyncio.sleep(20)


	#def login(self):
		#primeira posição aposta a declaração da função
		#self.pagina.goto(self.url, timeout=0)
		#@self.pagina.goto(self.url)
		#sleep(15)
	#	#self.pagina.wait_for_timeout(30000)
#
	def navegar(self): #navegar até a rea de upload
		""" Nessa função, deve ter uma URL personalizada aonde leva ao Dowload com o ID personalizado"""
		print('NAVEGANDO...')
		hyper_url = "https://studio.youtube.com/channel/UC1QV3QXnrjolOh2oocrdONQ/videos/upload?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D"
		self.pagina.goto(hyper_url)
		#self.pagina.wait_for_timeout(30000)
		sleep(5)
		#self.pagina.locator('xpath=//*[@id="upload-button"]/div').click()
		#self.upload()
	#def upload(self,caminho_path):
		#uplaod video from youtube
		#upload self.pagina.locator('xpath=//*[@id="content"]/input').set_input_files(caminho_path)
		#sleep(3)

	def close_(self):

		# Função que fecha o naveggador!
		self.browser.close()

	def _locator(self,name,on_click=False):
		self.name = name
		self.pagina.locator(self.name)
		if on_click == True:
			self.pagina.locator(self.name).click()

	def _fil(self,Fill,msg):
		self.Fill = fill
		self.msg = msg
		self.pagina.fill(Fill,msg)

	def temp(self):
		x = randint(5000,9000)
		self.pagina.wait_for_timeout(x)


	async def postar(self,titulo,caminho_path,descricao,keys_words):
		await asyncio.sleep(6)

		"""NAVEGAR, VÁ ATÉ A AREA DE UPLOAD DO CANAL DESEJADO"""
		
		await self.pagina.goto(self.hyper_url)
		await asyncio.sleep(6)
		#sleep(10)


		#uplaod video from youtube
		await self.pagina.locator('xpath=//*[@id="content"]/input').set_input_files(caminho_path)
		await asyncio.sleep(6)
		


		self.pagina.fill('//*[@id="textbox"]',titulo)
		await asyncio.sleep(6)
		
		self.pagina.fill('xpath=/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div',descricao)
		await asyncio.sleep(6)
		

		#marcar a opção, não é para crianças
		self.pagina.locator('xpath=/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]').click()
		await asyncio.sleep(6)
		#clicar em saiba mais, liberando assim, outras opções
		self.pagina.locator('xpath=//*[@id="toggle-button"]').click()
		await asyncio.sleep(6)
		#tags keyword
		self.pagina.fill('xpath=/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[5]/ytcp-form-input-container/div[1]/div/ytcp-free-text-chip-bar/ytcp-chip-bar/div/input',keys_words)
		await asyncio.sleep(6)

		#avançar, pro proxka página
		self.pagina.locator('xpath=//*[@id="next-button"]').click()
		
		await asyncio.sleep(6)
		#proximo avançar
		self.pagina.locator('xpath=//*[@id="next-button"]').click()
		await asyncio.sleep(6)
		
		#proximo avançar
		self.pagina.locator('xpath=/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]/div').click()
		await asyncio.sleep(6)
		
		#publicar o vídeo
		self.pagina.locator('xpath=/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]').click()
		
		await asyncio.sleep(6)
		#salvar o vídeo
		self.pagina.locator('xpath=/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]/div').click()
		await asyncio.sleep(6)
		
		


#Bot = None

#async def projeto():
#	global Bot
#	Bot = youtubeBot()

#loop = get_event_loop()
#loop.run_until_complete(projeto())
#loop.close()

#async def lord():
#	task = asyncio.create_task(projeto())
#	await task

#asyncio.run(lord())

