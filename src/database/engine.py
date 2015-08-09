import sqlalchemy

engine = create_engine('mysql://scott:tiger@localhost/foo', echo=True)
