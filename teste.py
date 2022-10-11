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
