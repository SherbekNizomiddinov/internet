from mysql.connector.cursor import MySQLCursor


# 1. MySQL jadvali yaratish
def create_table(cursor):    
    cursor.execute("create database if not exists Internet")
    cursor.execute("use Internet")
    cursor.execute("""create table if not exists Domain(
                    id int auto_increment primary key,
                    domain varchar(64) not null,
                    ip varchar(64) not null 
                    );
                   """)
    
# 2. Foydalanuvchidan ma'lumot kiritish
def insert_domin(cursor, domin, ip):
    
    cursor.execute(f"""insert into Domain(domain, ip)
                        values ("{domin}", "{ip}"); 
                   """)
# 3. Barcha ma`lumotlarni ko'rsatish
def show_all(cursor):
    cursor.execute("select * from Domain")
    for i in cursor.fetchall():
        print(f"id: {i}")
    