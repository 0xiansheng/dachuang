# 数据库配置信息
HOSTNAME = 'gz-cynosdbmysql-grp-o9nzvt3p.sql.tencentcdb.com'
PORT = '23303'
DATABASE = 'Test'
USERNAME = 'root'
PASSWORD = '@L12345678'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME,
                                                 PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "HELLOWORD"


#邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "1252967009@qq.com"
MAIL_PASSWORD = "aaoaihoibkhmiabf"
MAIL_DEFAULT_SENDER ="1252967009@qq.com"
MAIL_MAX_EMAILS = ""
MAIL_SUPPRESS_SEND = "1252967009@qq.com"
MAIL_ASCII_ATTACHMENTS = ""