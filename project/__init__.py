import os

from flask import Flask
import config

#APP_SETTINGS = config.DevelopmentConfig
APP_SETTINGS = config.ProductionConfig

app = Flask(__name__)

#use this for windows
app.config.from_object(APP_SETTINGS)

#use this for linux
#app.config.from_object(os.environ['APP_SETTINGS'])

if __name__ == '__main__':
    app.run(threaded=True)

from project import views