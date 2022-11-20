from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.components.logger import Logger
import logging
import config


db = SQLAlchemy()
myApp = Flask(__name__)
# 加载config
myApp.config.from_object(config)
db.init_app(myApp)

# 设置日志格式
myApp.logger.setLevel(logging.INFO)
log_handler = Logger.create_handler(myApp.config.get('LOG_DIR'))
myApp.logger.addHandler(log_handler)

myApp.config['DEBUG'] = myApp.config.get('DEBUG')
