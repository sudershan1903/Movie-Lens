# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE

connectionString = 'nicky/rob7699'

def runSqlQuery(sqlCommand):
    sqlCommand = "set heading off;\nset serveroutput on;\n" + sqlCommand
    session = Popen(['sqlplus', '-S', connectionString], stdin = PIPE, stdout = PIPE, stderr = PIPE)
    session.stdin.write(sqlCommand.encode('utf-8'))
    result, error = session.communicate()
    return result.decode('utf-8').splitlines()


        
        
#      create table tt( id int primary key not null,name varchar(20)); 
#
#    insert into tt values(31,'Robert');
#    insert into tt values(29,'Robert');
#   dbms_output.put_line('asdverg');
#create or replace procedure pprint as begin dbms_output.put_line('Avinashi KP'); select * from tt; end;
#   
#
qq1='''create or replace procedure printt
    as
    a number;
    begin
    select count(*) into a from tt;
    dbms_output.put_line(a);
    end;
    /'''

#qq2='''set serveroutput on;
#        execute pprint;''';
sqlcommand = '@sc.sql'
queryResult = runSqlQuery(sqlcommand)
print(*queryResult, sep = '\n')