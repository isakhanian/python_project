from flask import Flask # достает класс
app = Flask(__name__) # создается экземпляр класса Flask

@app.route('/') # синтаксис определения ручки
def hello_world():
    return 'Hello, World!'

app.run(port='3939')