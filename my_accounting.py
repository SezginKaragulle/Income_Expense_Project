from my_db import Database

class Accounting:

    def __init__(self) -> None:
        pass
    
    plug_id = 0
    plug_date_1 = ""
    plug_date_2 = ""
    plug_explanation = ""
    total_amount = 0
    plug_type =""

    def db_accounting_list():
        komut = "EXEC my_accounting_list"
        Database.imlec.execute(komut)
        liste = Database.imlec.fetchall()
        for deger in liste:
            print("FİŞ ID     : ",deger[0])
            print("FİŞ TARİHİ : ",deger[1])
            print("AÇIKLAMA   : ",deger[2])
            print("TUTAR      : ",deger[3])
            print("FİŞ TİPİ   : ",deger[4])
            print("FİŞ YIL    : ",deger[5])
            print("")
    
    def Db_Accounting_Insert(plug_explanation,total_amount,plug_type):
        komut = "INSERT INTO IncomeAndExpense (plug_explanation,total_amount,plug_type) VALUES (?,?,?)"
        komut_parameters = (plug_explanation,total_amount,plug_type)
        Database.imlec.execute(komut,komut_parameters)
        Database.db.commit()
        print("FİŞ BAŞARIYLA EKLENDİ...")
    
    def Db_Accounting_Delete(plug_id):
        komut = "DELETE FROM IncomeAndExpense WHERE plug_id = ?"
        komut_parameters = [plug_id]
        Database.imlec.execute(komut,komut_parameters)
        Database.db.commit()
        print("FİŞ BAŞARIYLA SİLİNDİ...")
    
    def Db_Accounting_Total_Amount(plug_type,plug_date_1,plug_date_2):
        komut = "Select SUM(total_amount) From IncomeAndExpense Where plug_type = ? And plug_date Between ? and ?"
        komut_parameters = [plug_type,plug_date_1,plug_date_2]
        Database.imlec.execute(komut,komut_parameters)
        liste = Database.imlec.fetchall()
        return liste
    
    def Db_Accounting_Income_And_Expense(plug_type,plug_date_1,plug_date_2):
        komut = "Select * From IncomeAndExpense Where plug_type = ? And plug_date Between ? and ?"
        komut_parameters = [plug_type,plug_date_1,plug_date_2]
        Database.imlec.execute(komut,komut_parameters)
        liste = Database.imlec.fetchall()
        return liste
    
    def Db_Accounting_Income_And_Expense_With_Year(plug_type,plug_year):
        komut = "Select SUM(total_amount) From IncomeAndExpense Where plug_type = ? And plug_year = ?"
        komut_parameters = [plug_type,plug_year]
        Database.imlec.execute(komut,komut_parameters)
        liste = Database.imlec.fetchall()
        return liste
    
    
