from src.models.user import User
from src import myApp, db
from src.components.utils import Utils


class UserService:
    """用户逻辑层
    """
    # 新增用户
    def create_user(user):
        u = User()
        u.name = user['name']
        u.email = user['email']

        db.session.add(u)
        db.session.commit()
