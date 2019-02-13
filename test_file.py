import csv 
import sqlite3

f1=open("genome_scores.csv")
reader1=csv.reader(f1)

f2=open("genome_tags.csv")
reader2=csv.reader(f2)

f3=open("link.csv")
reader3=csv.reader(f3)

f4=open("movie.csv")
reader4=csv.reader(f4)

f5=open("rating.csv")
reader5=csv.reader(f5)

f6=open("tag.csv")
reader6=csv.reader(f6)

conn=sqlite3.connect('firsttrydb.db')
c=conn.cursor()

#def create_table1():
#    c.execute('CREATE TABLE IF NOT EXISTS genome_scores(movieid REAL,tagid REAL,relevance REAL)')
#
#def create_table2():
#    c.execute('CREATE TABLE IF NOT EXISTS genome_tags(tagid REAL,tag TEXT)')
#
#def create_table3():
#    c.execute('CREATE TABLE IF NOT EXISTS link(movieid REAL,imdbid REAL,tmdbid REAL)')
#
#def create_table4():
#    c.execute('CREATE TABLE IF NOT EXISTS movie(movieid REAL,title TEXT,genre TEXT)')
#
#def create_table5():
#    c.execute('CREATE TABLE IF NOT EXISTS rating(userid REAL,movieid REAL,rating REAL,timestamp TEXT)')
#
#def create_table6():
#    c.execute('CREATE TABLE IF NOT EXISTS tag(userid REAL,movieid REAL,tag TEXT,timestamp TEXT)')
#
#def data_entry1(x1,x2,x3):
#    c.execute("INSERT INTO genome_scores VALUES(?,?,?)",(x1,x2,x3))
#    conn.commit()
#    
#def data_entry2(x1,x2):
#    c.execute("INSERT INTO genome_tags VALUES(?,?)",(x1,x2))
#    conn.commit()
#    
#def data_entry3(x1,x2,x3):
#    c.execute("INSERT INTO link VALUES(?,?,?)",(x1,x2,x3))
#    conn.commit()
#    
#def data_entry4(x1,x2,x3):
#    c.execute("INSERT INTO movie VALUES(?,?,?)",(x1,x2,x3))
#    conn.commit()
#    
#def data_entry5(x1,x2,x3,x4):
#    c.execute("INSERT INTO rating VALUES(?,?,?,?)",(x1,x2,x3,x4))
#    conn.commit()
#    
#def data_entry6(x1,x2,x3,x4):
#    c.execute("INSERT INTO tag VALUES(?,?,?,?)",(x1,x2,x3,x4))
#    conn.commit()
#
#create_table1()
#create_table2()
#create_table3()
#create_table4()
#create_table5()
#create_table6()
#
#
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

script='''SELECT * FROM genome_scores where relevance > 0.5;'''
script1='''CREATE PROCEDURE inslist AS
           BEGIN
           SELECT * FROM genome_scores WHERE relevance > 0.5;
           END;'''
script2='''execute printing()'''
#c.executescript(script)
c.execute(script1)
#c.execute(script2)

for row in c:
    print(row)

c.close()
conn.close()