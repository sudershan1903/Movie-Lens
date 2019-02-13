from subprocess import Popen, PIPE
import csv

connectionString = 'nicky/rob7699'

def runSqlQuery(sqlCommand):
    sqlCommand = "set heading off;\nset serveroutput on;\n" + sqlCommand
    session = Popen(['sqlplus', '-S', connectionString], stdin = PIPE, stdout = PIPE, stderr = PIPE)
    session.stdin.write(sqlCommand.encode('utf-8'))
    result, error = session.communicate()
    return result.decode('utf-8').splitlines()

#sql file o create tables
sqlcommand = '@create_table.sql'
queryResult = runSqlQuery(sqlcommand)
print(*queryResult, sep = '\n')

#sql file(s) to create procedures to insert values in tables
#sqlcommand = '@table1.sql'
#queryResult = runSqlQuery(sqlcommand)
#print(*queryResult, sep = '\n')
#
#sqlcommand = '@table2.sql'
#queryResult = runSqlQuery(sqlcommand)
#print(*queryResult, sep = '\n')
#
#sqlcommand = '@table3.sql'
#queryResult = runSqlQuery(sqlcommand)
#print(*queryResult, sep = '\n')
#
#sqlcommand = '@table4.sql'
#queryResult = runSqlQuery(sqlcommand)
#print(*queryResult, sep = '\n')
#
#sqlcommand = '@table5.sql'
#queryResult = runSqlQuery(sqlcommand)
#print(*queryResult, sep = '\n')
#
#sqlcommand = '@table6.sql'
#queryResult = runSqlQuery(sqlcommand)
#print(*queryResult, sep = '\n')


f1=open("genome_scores.csv")
reader1=csv.reader(f1)

f2=open("genome_tags.csv")
reader2=csv.reader(f2)

f3=open("link.csv")
reader3=csv.reader(f3)

f4=open("NOrmovies.csv")
reader4=csv.reader(f4)

f5=open("rating.csv")
reader5=csv.reader(f5)

f6=open("tag.csv")
reader6=csv.reader(f6)

def data_entry1(x1,x2,x3):
    sqlcommand = 'insert into genome_scores values('+str(x1)+','+str(x2)+','+str(x3)+');'
    queryResult = runSqlQuery(sqlcommand)        
    
def data_entry2(x1,x2):
    sqlcommand = 'insert into genome_tags values('+str(x1)+','+'\''+x2+'\''+');'#    sqlcommand = 'insert into genome_tags values('+str(x1)+','+x2+');'#    sqlcommand = 'insert into genome_tags values('+chr(x1+48)+','+chr(x2+48)+');'
    queryResult = runSqlQuery(sqlcommand)        
    
def data_entry3(x1,x2,x3):
    sqlcommand = 'insert into link values('+str(x1)+','+str(x2)+','+str(x3)+');'#    sqlcommand = 'insert into genome_scores values('+chr(x1+48)+','+chr(x2+48)+','+chr(x3+48)+');'
    queryResult = runSqlQuery(sqlcommand)        
    
def data_entry4(x1,x2,x3):
    sqlcommand = 'insert into movie values('+str(x1)+','+'\''+x2+'\''+','+'\''+x3+'\''+');'#    sqlcommand = 'insert into genome_scores values('+chr(x1+48)+','+chr(x2+48)+','+chr(x3+48)+');'
    queryResult = runSqlQuery(sqlcommand)        
    
def data_entry5(x1,x2,x3,x4):
    sqlcommand = 'insert into rating values('+str(x1)+','+str(x2)+','+str(x3)+','+'\''+x4+'\''+');'#    sqlcommand = 'insert into genome_scores values('+chr(x1+48)+','+chr(x2+48)+','+chr(x3+48)+');'
    queryResult = runSqlQuery(sqlcommand)        
    
def data_entry6(x1,x2,x3):
    sqlcommand = 'insert into tag values('+str(x1)+','+'\''+x2+'\''+','+'\''+x3+'\''+');'#    sqlcommand = 'insert into genome_scores values('+chr(x1+48)+','+chr(x2+48)+','+chr(x3+48)+');'
    queryResult = runSqlQuery(sqlcommand)        


i=0
for row in reader1:
    if i!=0:
        x1=int(row[0])
        x2=int(row[1])
        x3=float(row[2])
        data_entry1(x1,x2,x3)
    i=i+1

i=0
for row in reader2:
    if i!=0:
        x1=int(row[0])
        x2=row[1]
        data_entry2(x1,x2)
    i=i+1

i=0
for row in reader3:
    if i!=0:
        x1=int(row[0])
        x2=int(row[1])
        x3=int(row[2])
        data_entry3(x1,x2,x3)
    i=i+1

i=0
for row in reader4:
    if i!=0:
        x1=int(row[0])
        x2=row[1]
        x3=row[2]
        data_entry4(x1,x2,x3)
    i=i+1

i=0
for row in reader5:
    if i!=0:
        x1=int(row[0])
        x2=int(row[1])
        x3=float(row[2])
        x4=row[3]
        data_entry5(x1,x2,x3,x4)
    i=i+1

i=0
for row in reader6:
    if i!=0:
        x1=int(row[0])
        x2=row[1]
        x3=row[2]
        data_entry6(x1,x2,x3)
    i=i+1








#i=0
#for row in reader1:
#    if i!=0 and i<300:
#        x1=int(row[0])
#        x2=int(row[1])
#        x3=float(row[2])
#        data_entry1(x1,x2,x3)
#    i=i+1
#
#i=0
#for row in reader2:
#    if i!=0:
#        x1=int(row[0])
#        x2=row[1]
#        data_entry2(x1,x2)
#    i=i+1
#
#i=0
#for row in reader3:
#    if i>141 and i<300:
#        x1=int(row[0])
#        x2=int(row[1])
#        x3=int(row[2])
#        data_entry3(x1,x2,x3)
#    i=i+1
#
#i=0
#for row in reader4:
#    if i!=0 and i<300:
#        x1=int(row[0])
#        x2=row[1]
#        x3=row[2]
#        data_entry4(x1,x2,x3)
#    i=i+1
#
#i=0
#for row in reader5:
#    if i!=0 and i<300:
#        x1=int(row[0])
#        x2=int(row[1])
#        x3=float(row[2])
#        x4=row[3]
#        data_entry5(x1,x2,x3,x4)
#    i=i+1
#
#i=0
#for row in reader6:
#    if i!=0 and i<300:
#        x1=int(row[0])
#        x2=int(row[1])
#        x3=row[2]
#        x4=row[3]
#        data_entry6(x1,x2,x3,x4)
#    i=i+1
