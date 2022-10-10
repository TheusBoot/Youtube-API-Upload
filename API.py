from playwright.sync_api import sync_playwright
from time import sleep
from random import randint 


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

class youtubeBot:

	def __init__(self):

		self.test_or_production = False #modo em desenvolvimento

		#URL DE LOGIN
		self.url = "https://accounts.google.com/ServiceLogin/identifier?continue=https%3A%2F%2Fwww.youtube.com%2F&sacu=1&passive=1209600&acui=0&flowName=GlifWebSignIn&flowEntry=ServiceLogin&cid=1&TL=AB_wV5o6Wjo1SifSNCT7_jSwyYMvBd3a10LFH2YOAErstl0lt7NhQCADlWALsc24"
		
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
	
	def start(self):
		""" START NO UPLOAD DO VÍDEO PARA O YOUTUBE"""

		with sync_playwright() as playwright:
			self.run_time(playwright)
	

	def run_time(self,playwright):
		""" Costrução do inicializador..."""

		self.browser = playwright.firefox.launch(headless=False)
		self.pagina = self.browser.new_page()
		self.pagina.wait_for_timeout(5000)
		


	def login(self):
		#primeira posição aposta a declaração da função
		self.pagina.goto(self.url, timeout=0)
		self.pagina.wait_for_timeout(30000)




	def navegar(self): #navegar até a rea de upload
		""" Nessa função, deve ter uma URL personalizada aonde leva ao Dowload com o ID personalizado"""
		hyper_url = "https://studio.youtube.com/channel/UC1QV3QXnrjolOh2oocrdONQ/videos/upload?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D"
		self.pagina.goto(hyper_url, timeout=0)
		self.pagina.wait_for_timeout(30000)
		sleep(25)
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


	def postar(self,titulo,caminho_path,descricao,keys_words:str):


		#uplaod video from youtube
		self.pagina.locator('xpath=//*[@id="content"]/input').set_input_files(caminho_path)
		sleep(3)
		self.pagina.wait_for_timeout(5000)


		self.pagina.fill('//*[@id="textbox"]',titulo)
		self.pagina.wait_for_timeout(5000)
		
		self.pagina.fill('xpath=/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div',descricao)

		self.temp()

		#marcar a opção, não é para crianças
		self.pagina.locator('xpath=/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]').click()
		self.temp()

		#clicar em saiba mais, liberando assim, outras opções
		self.pagina.locator('xpath=//*[@id="toggle-button"]').click()
		self.temp()

		#tags keyword
		self.pagina.fill('xpath=/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[5]/ytcp-form-input-container/div[1]/div/ytcp-free-text-chip-bar/ytcp-chip-bar/div/input',keys_words)
		self.temp()

		#avançar, pro proxka página
		self.pagina.locator('xpath=//*[@id="next-button"]').click()
		self.temp()

		#proximo avançar
		self.pagina.locator('xpath=//*[@id="next-button"]').click()
		self.temp()
		
		#proximo avançar
		self.pagina.locator('xpath=/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]/div').click()
		self.temp()
		
		#publicar o vídeo
		self.pagina.locator('xpath=/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]').click()
		self.pagina.wait_for_timeout(15000)

		#salvar o vídeo
		self.pagina.locator('xpath=/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]/div').click()

		self.pagina.wait_for_timeout(10000)
		


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

