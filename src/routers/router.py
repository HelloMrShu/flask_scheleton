from flask import Blueprint
from src.controllers.default import index, test
from flask_cors import CORS
from src.controllers.user import user_index

# 创建蓝图
routerbp = Blueprint('routemap', __name__)
# 解决跨域问题
CORS(routerbp)

# 路由配置
routerbp.route('/', methods=['GET'])(index)
routerbp.route('/test', methods=['GET'])(test)

# user
routerbp.route('/user/index', methods=['GET'])(user_index)
