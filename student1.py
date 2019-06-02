import sqlite3
connection = sqlite3.connect('student.db')
print("Database opened successfully.")

TABLE_NAME = "student_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

def create_table():
    connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " + STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);")
    print("table created successfully")
# for i in range(2):
#     name= input('enter your name')
#     college= input('enter your college')
#     address= input('enter your address')
#     phone= input('enter your phone number')
def insert_record(name,college,address,phone):
    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " + STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " + STUDENT_PHONE + ") VALUES ( '"+name+"', '"+college+"', " + "'"+address+"' , "+str(phone)+");")
    connection.commit()
def display_record():
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    for row in cursor:
        print("Student is: ", row[0])
        print("Student name is: ", row[1])
        print("Student college is: ", row[2])
        print("Student address is: ", row[3])
        print("Student phone is : ", row[4])



def close_database():
    connection.close()
