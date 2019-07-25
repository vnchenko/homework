from dao.orm.model import *
from dao.db import OracleDb

db = OracleDb()

Base.metadata.create_all(db.sqlalchemy_engine)

session = db.sqlalchemy_session

sumsung = Company(company_title = 'logitech')

max = Worker(worker_code = '2')

music_app = Projects(project_date = '11-JAN-2003', project_name = 'music_app')

sumsung.workers.append(max)
sumsung.projects.append(music_app)


session.add_all([sumsung, max, music_app])

session.commit()