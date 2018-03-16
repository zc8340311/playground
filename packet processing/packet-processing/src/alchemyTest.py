import sqlalchemy

engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)
