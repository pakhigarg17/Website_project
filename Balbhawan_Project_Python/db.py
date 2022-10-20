import sqlite3
import os

try:
    if os.path.exists("bb_database.db"):
        connection = sqlite3.connect("bb_database.db")
        cursor = sqlite3.Cursor(connection)
    else:
        print("Database Not Exist")
        exit()

except :
    print("Unable to Connect with Database")
    exit()

def get_regno():
    sql="Select count(regno) from Student_Info"    
    cursor.execute(sql)
    count = cursor.fetchone()    
    print('Count : ',count)
    print('Type of count : ',type(count))
    return count[0]    


def get_data(sql):
    # print(sql)
    if sql=='':
        sql="Select * from student_info"
    # print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    # print("Row Count : ",cursor.rowcount)
    # print(result)
    return result

def insert_data(record):
    sql =f"""Insert Into Student_Info
                (   regno,name,dob,contact,address,qualification,course,regdate,gender,
                    fname,foccupation,fcontact,foffice,institute,examination,passing,percentage
                ) 
                values('{record[0]}',
                       '{record[1]}',
                       '{record[2]}',
                       '{record[3]}',
                       '{record[4]}',
                       '{record[5]}',
                       '{record[6]}',
                       '{record[7]}',
                       '{record[8]}',
                       '{record[9]}',
                       '{record[10]}',
                       '{record[11]}',
                       '{record[12]}',
                       '{record[13]}',
                       '{record[14]}',
                       '{record[15]}',
                       '{record[16]}'
                       )
            """
    print(sql) 
    cursor.execute(sql)
    connection.commit()        
    value = cursor.rowcount
    print("Record Insert Query : ",value)
    return cursor.rowcount

def get_batch_details():
    sql="Select * from batch_details"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    return result

'''
Batch_Details
`Batch_Code`	TEXT NOT NULL,
	`Course_Code`	TEXT,
	`Batch_Start_Date`	TEXT,
	`Batch_Time`	TEXT,
	`Faculty_Id`	TEXT,
	`Strength`	INTEGER,
	`Status`	TEXT,
	`Progress`	INTEGER,
	`Exam_Date`	TEXT,
'''

def generate_batch_code(course_code):
    sql= f"select batch_code from batch_details where course_code ='{course_code}'"
    cursor.execute(sql)
    code = cursor.fetchall()
    print('Last Batch Code ',code[-1])


def slot_time(slot_type=''):
    if len(slot_type)>0:
        sql=f"select slot_time from batch_time where slot_type='{slot_type}'"
    else:
        sql=f"select slot_time from batch_time"
    # print(sql)
    cursor.execute(sql)
    slot_time=[]
    for s in cursor.fetchall():
        slot_time.append(s[0])         
    return slot_time

def get_faculty_info(course_code=''):
    sql='Select faculty_name from faculty_details '
    cursor.execute(sql)
    faculty_names=[]
    for f in cursor.fetchall():
        faculty_names.append(f[0])
    return faculty_names

def get_course_detail():
    sql='select course_name from course_details'
    cursor.execute(sql)
    courses=[]
    for c in cursor.fetchall():
        courses.append(c[0])

    return courses

def insert_batch(args):
    sql = f'''
    insert into batch_details (batch_code,course_code,batch_start_date,batch_time,faculty_id,strength,status) values(
        '{args[0]}','{args[1]}','{args[2]}','{args[3]}','{args[4]}',{args[5]},'{args[6]}')
    '''
    print(sql)
    cursor.execute(sql)
    connection.commit()

def update_batch(args):
    sql=f'''Update Batch_Details set Course_code = '{args[1]}',
                                     Batch_Start_Date='{args[2]}',
                                     Batch_Time='{args[3]}',
                                     Faculty_Id='{args[4]}',
                                     Strength={args[5]},
                                     Status='{args[6]}'
                                     where Batch_Code='{args[0]}'   
                                    '''   
    # print(sql)
    cursor.execute(sql)
    connection.commit()

def get_batch_info(course='',batch_time='',faculty=''):
    print('Course : ',course)
    print('Batch Time : ',batch_time)
    print('Faculty : ',faculty)
    if len(course) > 0:
        if len(batch_time) > 0 :
            if len(faculty) > 0:
                sql=f"Select * from Batch_Info where course='{course}' and batch_time='{batch_time}' and faculty='{faculty}'"
            else:
                sql=f"Select * from Batch_Info where course='{course}' and batch_time='{batch_time}'"
        elif len(faculty) > 0:
            sql=f"Select * from Batch_Info where course='{course}' and faculty='{faculty}'"
        else:
            sql=f"Select * from Batch_Info where course='{course}'"
    elif len(batch_time) > 0 :
            if len(faculty) > 0:
                sql=f"Select * from Batch_Info where batch_time='{batch_time}' and faculty='{faculty}'"
            else:
                sql=f"Select * from Batch_Info where batch_time='{batch_time}'"
    elif len(faculty) > 0 :             
        sql=f"Select * from Batch_Info where faculty='{faculty}'"
    else:
        sql=f"Select * from Batch_Info"

    sql=sql + " ORDER BY Sr_No ASC"    
    print(sql)
    cursor.execute(sql)
    data=cursor.fetchall()
    
    # print(data)
    return data

def update_batch_info_data(faculty,batch_time,course='',strength='',status='',active=''):
    sql=f"""
            Update Batch_info set course='{course}',strength={strength},status='{status}',active={active} 
            where faculty='{faculty}' and batch_time='{batch_time}'
        """     

    print(sql)
    
    cursor.execute(sql)
    connection.commit()

def get_dashboard():
    sql='select * from dashboard'
    cursor.execute(sql)
    data = cursor.fetchall()
    return data
