from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from application import create_app
from model.DwModel import Dw
from model.DwModel import db

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)


manager.add_command('db', MigrateCommand)

# enable python shell with application context
@manager.shell
def shell_ctx():
    return dict(app=app,
                db=db,
                Dw=Dw)

if __name__ == '__main__':
    manager.run()