# Part 20- Database Testing using Robot Framework | Selenium with Python

*** Settings ***
Library  DatabaseLibrary
Library  OperatingSystem

Suite Setup    Connect To Database  pymysql     ${DBName}   ${DBUser}   ${DBPass}   ${DBHost}   ${DBPort}
Suite Teardown      Disconnect From Database

*** Variables ***
${DBName}   mydbd
${DBUser}   root
${DBPass}   root
${DBHost}   127.0.0.1
${DBPort}   3306

*** Test Cases ***
Create person table
    ${output}=  execute sql string  Create table person(id integer,first_name varchar(20),last_name varchar(20));
    log to console  ${output}
    should be equal as strings  ${output} None

Inserting Data in person Table
    # single record
    ${output}=  execute sql string  Insert into person values(101,"John","canady");
    log to console  ${output}
    should be equal as strings  ${output} None


Inserting Data in person Table through sql
    # multiple record
    ${output}=  execute sql script  ./TestData/mydb_person_insertData.sql
    log to console  ${output}
    should be equal as strings  ${output} None

check David record present in Person Table
    check if exists in database  select id mydb.person where first_name="David";

check Jio record not present in Person Table
    check if not exists in database  select id mydb.person where first_name="Jio";

check Person Table exists in mydb database
    table must exist  person

verify Row Count is Zero
    row count is 0  Select * From mydb.person WHERE first_name='xyz';

verify Row count is equal to some value
    row count is equal to x   Select * From mydb.person WHERE first_name='David';   1

verify Row count is Greater than some value
    row count is greater than x   Select * From mydb.person WHERE first_name='David';   0


verify Row count is less than some value
    row count is less than x   Select * From mydb.person WHERE first_name='David';   5

update record in person table
    ${output}=  execute sql string   Update mydb.person set frist_name="Jio" where id=104;
    log to console  ${output}
    should be equal as strings  ${output}   None


Retrive records in person table
    @{QueryResults}=  query     select * from mydb.person;
    # many keyword is used to retirve many results at a time
    log to console  many    @{QueryResults}

Delete records from person table
    ${output}=  EXECUTE SQL STRING  Delete from mydb.person;
    should be equal as strings  ${output}   None


























