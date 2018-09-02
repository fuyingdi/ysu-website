# 命令相关的东西
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from runserver import app


db = None
# 创建命令管理器
manager = Manager(app)
# 绑定app到db
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server)


@manager.option('-n', '--name', dest='name')
@manager.option('-d', '--desc', dest='desc')
@manager.option('-p', '--permissions', dest='permissions')
def create_role(name, desc, permissions):
    # 创建新账号?
    pass


@manager.option('-e', '--email', dest='email')
@manager.option('-u', '--username', dest='username')
@manager.option('-p', '--password', dest='password')
@manager.option('-r', '--role_name', dest='role')
def create_administer():
    # 创建管理员账号？
    pass


if __name__ == '__main__':
    manager.run()

