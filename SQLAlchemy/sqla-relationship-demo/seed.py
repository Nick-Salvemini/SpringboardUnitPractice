from models import Department, Employee, db
from app import app

db.drop_all()
db.create_all()

d1 = Department(dept_code = 'mktg', dept_name = 'Marketing', phone = '(201) 555-1234');
d2 = Department(dept_code = 'lgl', dept_name = 'Legal');
d3 = Department(dept_code = 'hr', dept_name = 'Human Resources', phone = '(201) 555-9111');
d4 = Department(dept_code = 'sales', dept_name = 'Sales', phone = '(201) 555-1213');

e1 = Employee(name = 'Bob Bilby', state = 'AK', dept_code = 'lgl')
e2 = Employee(name = 'Bandit Heeler', dept_code = 'mktg')
e3 = Employee(name = 'Muffin Top', state = 'WA', dept_code = 'lgl')
e4 = Employee(name = 'Toby Flenderson', state = 'PA', dept_code = 'hr')
e5 = Employee(name = 'Chili Heeler', dept_code = 'mktg')
e6 = Employee(name = 'Pat Lab', state = 'NY', dept_code = 'sales')
e7 = Employee(name = 'Michele Bichele', state = 'IL', dept_code = 'sales')
e8 = Employee(name = 'Jean Paul Jean Paul', dept_code = 'mktg')
e9 = Employee(name = 'Chico Resch', state = 'VA', dept_code = 'sales')
e10 = Employee(name = 'Steve Dangle', state = 'CT', dept_code = 'sales')
e11 = Employee(name = 'Link Zelda', dept_code = 'mktg')
e12 = Employee(name = 'Joe Schmo', state = 'CA', dept_code = 'sales')

db.session.add_all([d1,d2,d3,d4])

db.session.commit()

db.session.add_all([e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12])

db.session.commit()