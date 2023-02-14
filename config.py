# 数据库配置
# 主机
HOST = "127.0.0.1"
# 端口
PORT = 3306
# 用户名与密码
USERNAME = "root"
PWD = "47635411"
# 数据库
DATABASE = "recommender"
#数据库URI
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USERNAME}:{PWD}@{HOST}:{PORT}/{DATABASE}?charset=utf8mb4"
#开启sql跟踪
SQLALCHEMY_ECHO = True