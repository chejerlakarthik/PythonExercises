import sqlite3

def db_tuples():
    db = sqlite3.connect('emp_db')
    db.execute('drop table if exists emp')
    db.execute('create table emp(empId int, empName text)')
    db.execute('insert into emp(empId, empName) values(?,?)', (1, 'Karthik'))
    db.execute('insert into emp(empId, empName) values(?,?)', (2, 'Aarthi'))
    db.execute('insert into emp(empId, empName) values(?,?)', (3, 'Uday'))
    db.execute('insert into emp(empId, empName) values(?,?)', (4, 'Divya'))
    db.execute('insert into emp(empId, empName) values(?,?)', (5, 'Sanjeev'))
    db.execute('insert into emp(empId, empName) values(?,?)', (6, 'Archana'))
    db.commit()

    cursor = db.execute('select * from emp')

    for row in cursor:
        print(row)

def db_dicts():
    db = sqlite3.connect('student_db')
    db.row_factory = sqlite3.Row
    db.execute('drop table if exists student')
    db.execute('create table student(studentId int, studentName text)')
    db.execute('insert into student(studentId, studentName) values(?,?)', (1, 'Karthik'))
    db.execute('insert into student(studentId, studentName) values(?,?)', (2, 'Aarthi'))
    db.execute('insert into student(studentId, studentName) values(?,?)', (3, 'Uday'))
    db.execute('insert into student(studentId, studentName) values(?,?)', (4, 'Divya'))
    db.execute('insert into student(studentId, studentName) values(?,?)', (5, 'Sanjeev'))
    db.execute('insert into student(studentId, studentName) values(?,?)', (6, 'Archana'))
    db.commit()

    cursor = db.execute('select * from student')

    for row in cursor:
        print(dict(row))

if __name__ == '__main__':
    db_tuples()

    db_dicts()