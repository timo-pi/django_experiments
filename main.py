import eel

eel.init('web')

@eel.expose
def get_data():
    return 'Hello from Python!'

eel.start('index.html')
