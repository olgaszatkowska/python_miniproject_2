import sqlalchemy as sa

from src.settings import BASE, TABLE_NAME


class University(BASE):
    __tablename__ = TABLE_NAME
    ranking = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String)
    location = sa.Column(sa.String)
    number_of_students = sa.Column(sa.String)
    students_staff_ratio = sa.Column(sa.String)
    percentage_int_stud = sa.Column(sa.String)
    gender_ratio = sa.Column(sa.String)