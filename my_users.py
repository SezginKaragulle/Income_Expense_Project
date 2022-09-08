from my_db import Database



class Users:

    def __init__(self) -> None:
        pass

    user_id = 0
    user_name = ""
    user_password =""
    staff_name =""
    staff_surname = ""
    department = ""

    def db_users_list():
        komut = "EXEC my_users_list"
        Database.imlec.execute(komut)
        liste = Database.imlec.fetchall()
        for deger in liste:
            print("ID            : ",deger[0])
            print("KULLANICI ADI : ",deger[1])
            print("ADI           : ",deger[2])
            print("SOYADI        : ",deger[3])
            print("DEPARTMAN     : ",deger[4])
            print("")

    def Db_Users_Select_Login(user_name,user_password):
        komut = "SELECT * FROM users Where user_name = ? and user_password = ?"
        komut_parameters = [user_name,user_password]
        Database.imlec.execute(komut,komut_parameters)
        liste = Database.imlec.fetchall()
        return liste
    
    def Db_Users_Insert(user_name,user_password,staff_name,staff_surname,department):
        komut = "INSERT INTO users (user_name,user_password,staff_name,staff_surname,department) VALUES (?,?,?,?,?)"
        komut_parameters = (user_name,user_password,staff_name,staff_surname,department)
        Database.imlec.execute(komut,komut_parameters)
        Database.db.commit()
        print("KULLANICI BAŞARIYLA EKLENDİ...")

    def Db_Users_Search(user_name):
        komut = "select COUNT(*) from users Where user_name = ?"
        komut_parameters = [user_name]
        Database.imlec.execute(komut,komut_parameters)
        liste = Database.imlec.fetchall()
        return liste
    
    def Db_User_Change_Password(user_password,user_id):
        komut = "Update users SET user_password = ? WHERE user_id = ?"
        komut_parameters = (user_password,user_id)
        Database.imlec.execute(komut,komut_parameters)
        Database.db.commit()
        print("ŞİFRE GÜNCELLENDİ...")
    
    def Db_User_Delete(user_id):
        komut = "DELETE FROM users WHERE user_id = ?"
        komut_parameters = [user_id]
        Database.imlec.execute(komut,komut_parameters)
        Database.db.commit()
        print("KULLANICI BAŞARIYLA SİLİNDİ...")




    
    
    