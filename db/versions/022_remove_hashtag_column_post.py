from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    posts = Table('posts', meta, autoload=True)

    # users.c.password.drop()
    posts.c.hashtags.drop()
    pass


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)

    # users = Table('users', meta, autoload=True)
    posts = Table('posts', meta, autoload=True)

    # password = Column("password", String(128), nullable=False)
    hashtags = Column("hashtags", Text)

    # password.create(users)
    posts.create(hashtags)
    pass
