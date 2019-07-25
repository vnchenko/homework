from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Company(Base):
    tablename = 'company'
    company_title = Column(String(10), primary_key=True)
    workers = relationship('Worker', back_populates='company')
    projects = relationship('Projects', back_populates='company')


class Worker(Base):
    tablename = 'worker'
    worker_code = Column(Integer, primary_key=True)
    company_title_fk = Column(String(10), ForeignKey('company.company_title'))
    company = relationship('Company', back_populates='workers')


class Projects(Base):
    tablename = 'projects'
    company_title_fk = Column(String(10), ForeignKey('company.company_title'))
    project_date = Column(Date, primary_key=True)
    project_name = Column(String(10), primary_key=True)
    company = relationship('Company', back_populates='projects')
