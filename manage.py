import os
from flask_migrate import Migrate, MigrateCommand
from vgg19 import create_app, db
from flask_script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)
manager = Manager(app)


def make_shell_context():
    return dict(db=db)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

