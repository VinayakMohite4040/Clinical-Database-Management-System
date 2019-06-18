create database test_3;

use test_3

create table patient(
    P_id int(5) primary key auto_increment,
    P_name varchar(25) not null,
    DOB date,
    Gender enum('M','F'),
    P_phone_1 int check(P_phone_1 % 10000000 <> 0),
    P_phone_2 int check(P_phone_2 % 10000000 <> 0),
    Blood_group enum('B+', 'B-', 'O+', 'O-', 'A+', 'A-', 'AB+', 'AB-'),
    Add_house_no varchar(5),
    Add_street varchar(25),
    Add_city varchar(25),
    Add_state varchar(25)
    )

create table staff(
    S_id int(5) primary key auto_increment,
    S_name varchar(25) not null,
    Joining_date date,
    Gender enum('M', 'F'),
    S_phone_1 int check(P_phone_1 % 10000000 <> 0),
    S_phone_2 int check(P_phone_2 % 10000000 <> 0),
    Department varchar(25),
    Salary int,
    Post varchar(25),
    Visiting_hrs varchar(15),
    Add_house_no varchar(5),
    Add_street varchar(25),
    Add_city varchar(25),
    Add_state varchar(25)
    )

create table visit(
    Visit_id int(5) primary key auto_increment,
    S_id int(5),
    Visit_date date,
    Reason_for_visit varchar(50),
    P_id int(5),
    test_1 int(5),
    test_2 int(5),
    test_3 int(5),
    test_4 int(5),
    bill_amount int,
    Due_date date,
    Payment_status enum('completed', 'pending') default 'pending',
    Amount_pending int
    )

create table test_details(
    Test_id int(5) primary key auto_increment,
    Room_no varchar(5),
    Name varchar(25),
    test_cost int
    )

create table payment(
    Payment_id int(5) primary key auto_increment,
    Visit_id int(5),
    Paid_date date,
    Payment_method varchar(25),
    amt_paid int
    )

    delimiter $$
    CREATE FUNCTION `get_amount`(id int) RETURNS int(11)
    BEGIN
    declare cost int;
    select test_cost into cost from test_details where test_id = id;
    RETURN cost;
    END$$

    CREATE FUNCTION `inject`(pa_id int) RETURNS int(11)
    BEGIN
    declare co int default 0;
    select count(P_id) into co from patient where P_id = pa_id;
    RETURN co;
    END$$

    CREATE TRIGGER `payment_date_update`
    BEFORE INSERT
    ON `payment`
    FOR EACH ROW
    begin
    set new.Paid_date = curdate();
    end$$

    CREATE TRIGGER `visit_date_update`
    BEFORE INSERT
    ON `visit`
    FOR EACH ROW
    begin
    set new.visit_date = curdate();
    end$$
    delimiter ;