import mysql.connector as sql
connected = sql.connect(host="127.0.0.1", user="root", db="bus_ticket")
if connected.is_connected():
    print("connected successfully")
scur = connected.cursor()
scur.execute("""
create table bus_route(
    ticket_no int AUTO_INCREMENT primary key,
    ticket_type varchar(30),
    start_place int,
    end_place int,
    route varchar(100),
    
    members int,
    total float
)
""")
print("bus_route table created")
scur.execute("""
create table place(
    sno int primary key,
    city varchar(50)
)
""")
print("place table created")
scur.execute("""
create table pay_later(
    id int AUTO_INCREMENT primary key,
    name varchar(50),
    aadhar_no varchar(20),
    amount float
)
""")
print("pay_later table created")
connected.commit()
scur.close()
connected.close()
print("All tables created successfully!")