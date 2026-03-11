from flask import Flask
app  = Flask(__name__)

@app.about('/')
def home():
  return "Merhaba,Turkiyeden Selam!"
