from functions import create_table, insert_domin, show_all
import socket
from pprint import pprint
import json
import mysql.connector
import login
from pprint import pprint
try:
    connection = mysql.connector.connect(
        host=login.host,
        user=login.user,
        password=login.password,
        port=login.port
    )
    cursor = connection.cursor()

    dect = {}
    list2 = []
    def domin(text: list)->list:
        list2 = []
        for i in text:
            # MO ga ma`lumotlarni yuboramiz
            
            insert_domin(cursor, i, socket.gethostbyname(i))
            with open("result.txt", "a") as file:
                file.write(f"{json.dumps({'Domin': i, 'id': socket.gethostbyname(i)}, indent = 4)}\n" )
        print("Maluot MO ga muvoffaqqiyatli qo`shildi!\n")
        print("Natijani resutl.txt da ham ko`rishingiz mn")

    # Ma`lumotlar bazasini yaratib olamiz
    create_table(cursor)

    with open('domains.txt', 'r') as f:
        list1 = (f.read()).split('\n')
        domin(list1)
    while True:
        x = input("\nAgar MO dagi ma`lumotni ko`rmoqchi bo`lsangiz 1 ni bosing\nDasrurdan chiqmoqchi bo`lsangiz ixtiyoriy klavishni bosing: ")
        if x == '1':
            show_all(cursor)
        else:
            print("\nKuningiz hayirli o`tsin! \n")
            exit()
except:
    print("xato")
