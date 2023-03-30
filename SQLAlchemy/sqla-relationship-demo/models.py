from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Department(db.Model):
    '''Department. A department has many employees'''
    __tablename__ = 'departments'

    dept_code = db.Column(db.Text, primary_key = True)
    dept_name = db.Column(db.Text, nullable = False, unique = True)
    phone = db.Column(db.Text)

    def __repr__(self):
        '''Show Department Info'''
        d = self
        return f'<Department Name: {d.dept_name}; Code: {d.dept_code}; Phone Num: {d.phone}>'

class Employee(db.Model):
    '''Employee. A employee has one department'''

    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.Text, nullable = False)
    state = db.Column(db.Text, nullable = False, default = 'NJ')
    dept_code = db.Column(db.Text, db.ForeignKey('departments.dept_code'))

    dept = db.relationship('Department', backref = 'employees')

    def __repr__(self):
        '''Show Employee Info'''
        e = self
        return f'<Employee Name: {e.name}; ID: {e.id}; State: {e.state}; Department: {e.dept_code}>'
    
def get_directory():
    all_emps = Employee.query.all()

    for emp in all_emps:
        if emp.dept is not None:
            print(emp.name, emp.dept.dept_name, emp.dept.phone)
        else:
            print(emp.name)

def get_directory_join():
    directory = db.session.query(
        Employee.name, Department.dept_name, Department.phone).join(Department).all()

    for name, dept, phone in directory:
        print(name, dept, phone)