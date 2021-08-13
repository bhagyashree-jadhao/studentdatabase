import pymysql
con=pymysql.connect(host="localhost",database='student',user="root",password="root")
sqlquery="create table student(STUDENT_NO int (3),STUDENT_NAME varchar (30),STUDENT_DOB DATE,STUDENT_DOJ DATE)"
crsr=con.cursor()
#crsr.execute(sqlquery)
insertdataquery="insert into student(STUDENT_NO,STUDENT_NAME,STUDENT_DOB,STUDENT_DOJ) values(%s,%s,%s,%s)"

data=[(1,"Rohan","2008-05-21","2019-08-21"),(2,"Raju","2007-06-12","2019-08-21"),(4,"Rohith","2006-08-17","2020-04-11")]
#crsr.executemany(insertdataquery,data)
#con.commit()
#to update the place of the student _no(1) to 5
updateSTUDENT_NO="update student set STUDENT_NO=5 where STUDENT_NO=1"
updateSTUDENT_NAME="update student set STUDENT_NAME='Shekhar' where STUDENT_NAME='Raju'"
crsr.execute(updateSTUDENT_NO)
crsr.execute(updateSTUDENT_NAME)
con.commit()
#to delete the details of Rohan student
deletedata="delete from student where STUDENT_NO=5"
crsr.execute(deletedata)
con.commit()
#WAP to read the details of the student present in student database:
readalldata="select * from student"
crsr.execute(readalldata)
data=crsr.fetchall()
for i in data:
    print(i)