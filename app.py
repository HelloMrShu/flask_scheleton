from src import myApp
from src.routers.router import routerbp
from src.command.foo import foobp

# 注册router
myApp.register_blueprint(routerbp)
# 注册command
myApp.register_blueprint(foobp)

if __name__ == '__main__':
    myApp.run()
