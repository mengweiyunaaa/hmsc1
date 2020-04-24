
import os

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
class Applciation(Flask):
    def __init__(self,import_name,template_folder="templates",root_path=None,static_folder=None):
        super(Applciation, self).__init__(import_name,template_folder=template_folder,root_path=root_path,static_folder=static_folder)
        # 从配置文件加载
        self.config.from_pyfile('config/base_setting.py')
        db.init_app(self)
db = SQLAlchemy()

app = Applciation(__name__,template_folder=os.getcwd()+'/web/templates/',root_path=os.getcwd(),static_folder=os.path.join(os.getcwd(), 'web/static/'))  #入口函数

manage = Manager(app)

# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY','dev')
from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
