from my_users import Users
from my_accounting import Accounting


myTotalProcesses = 9

def My_Login_To_System():
    print("SİSTEME GİRİŞ")
    print("")
    Users.user_name = input("Kullanıcı Adı: ")
    Users.user_password = input("Şifre: ")
    myLoginValues = Users.Db_Users_Select_Login(Users.user_name,Users.user_password)
    if myLoginValues:
        print("GİRİŞ GERÇEKLEŞTİRİLDİ")
        print("")
        My_Project_Processes()
    else:
        print("HATALI KULLANICI ADI VEYA ŞİFRE")

def My_Project_Processes(myLocalValue=0):
    mySelectionProcess = int(myLocalValue)
    if mySelectionProcess==0:
        myChoose = input("YAPILACAK İŞLEM NUMARASINI GİRİNİZ: ")
        mySelectionProcess = int(myChoose)
        if mySelectionProcess<0 or mySelectionProcess>myTotalProcesses:
            print("BÖYLE BİR İŞLEM ADIMI YOKTUR. TEKRAR YÖNLENDİRİLİYORSUNUZ...")
            print("")
            My_Project_Processes()
    else:
        mySelectionProcess = myLocalValue
    
    if mySelectionProcess == 1:
        print("")
        print("KULLANICI LİSTELEME İŞLEMİ")
        print("")
        Users.db_users_list()

    elif mySelectionProcess == 2:
        print("")
        print("KULLANICI EKLEME İŞLEMİ")
        print("")
        Users.user_name = str(input("Kullanıcı Adı: "))
        Users.user_password = str(input("Şifre: "))
        Users.staff_name = str(input("Adı: "))
        Users.staff_surname = str(input("Soyadı: "))
        Users.department = str(input("Departman: "))

        myUserInformationValue = Users.Db_Users_Search(Users.user_name)
        
        for nextInformationValue in myUserInformationValue:
            if int(nextInformationValue[0]) == 0:
                Users.Db_Users_Insert(Users.user_name,Users.user_password,Users.staff_name,Users.staff_surname,Users.department)
                print("")
                Users.db_users_list()
            else:
                print("")
                print("Kullanıcı Adı Sistemde Mevcuttur...")
    
    elif mySelectionProcess == 3:
        print("")
        print("KULLANICI ŞİFRE DEĞİŞTİRME İŞLEMİ")
        print("")
        Users.user_id = int(input("Kullanıcı Id: "))
        Users.user_password = input("Yeni Şifre: ")
        Users.Db_User_Change_Password(Users.user_password,Users.user_id)
    
    elif mySelectionProcess == 4:
        print("")
        print("KULLANICI SİLME İŞLEMİ")
        print("")
        Users.user_id = int(input("Kullanıcı Id: "))
        Users.Db_User_Delete(Users.user_id)
        print("")
        Users.db_users_list()
    
    elif mySelectionProcess == 5:
        print("")
        print("FİŞ LİSTESİ")
        print("")
        Accounting.db_accounting_list()
    
    elif mySelectionProcess == 6:
        print("")
        print("FİŞ EKLEME İŞLEMİ")
        print("")
        Accounting.plug_explanation = input("AÇIKLAMA: ")
        Accounting.total_amount = int(input("FİŞ TUTARI: "))
        Accounting.plug_type = input("FİŞ TİPİ: ")
        Accounting.Db_Accounting_Insert(Accounting.plug_explanation,Accounting.total_amount,Accounting.plug_type)
        print("")
        Accounting.db_accounting_list()
    
    elif mySelectionProcess == 7:
        print("")
        print("FİŞ SİLME İŞLEMİ")
        print("")
        Accounting.plug_id = int(input("FİŞ NUMARASI: "))
        Accounting.Db_Accounting_Delete(Accounting.plug_id)
        print("")
        Accounting.db_accounting_list()
    
    elif mySelectionProcess == 8:
        print("")
        print("& GELİR-GİDER LİSTESİ &")
        print("")
        Accounting.plug_date_1 = input("BAŞLANGIÇ TARİHİ: ")
        Accounting.plug_date_2 = input("BİTİŞ TARİHİ    : ")

        myAccountingIncomeInformation = Accounting.Db_Accounting_Income_And_Expense("Gelir",Accounting.plug_date_1,Accounting.plug_date_2)
        myAccountingExpenseInformation = Accounting.Db_Accounting_Income_And_Expense("Gider",Accounting.plug_date_1,Accounting.plug_date_2)
        myAccountingIncomeTotalAmount = Accounting.Db_Accounting_Total_Amount("Gelir",Accounting.plug_date_1,Accounting.plug_date_2)
        myAccountingIncomeExpenseAmount = Accounting.Db_Accounting_Total_Amount("Gider",Accounting.plug_date_1,Accounting.plug_date_2)
        
        print("")
        print(" $ GELİR LİSTESİ $")
        print("")

        for nextAccountingIncomeInformation in myAccountingIncomeInformation:
                print("FİŞ ID     : ",nextAccountingIncomeInformation[0])
                print("FİŞ TARİHİ : ",nextAccountingIncomeInformation[1])
                print("AÇIKLAMA   : ",nextAccountingIncomeInformation[2])
                print("TUTAR      : ",nextAccountingIncomeInformation[3])
                print("FİŞ TİPİ   : ",nextAccountingIncomeInformation[4])
                print("FİŞ YIL    : ",nextAccountingIncomeInformation[5])
                print("")
        
        for nextAccountingIncomeTotalAmount in myAccountingIncomeTotalAmount:
            print("")
            print("TOPLAM GELİR: ",nextAccountingIncomeTotalAmount[0])
            print("")
        
        print("")
        print(" $ GİDER LİSTESİ $")
        print("")

        for nextAccountingExpenseInformation in myAccountingExpenseInformation:
                print("FİŞ ID     : ",nextAccountingExpenseInformation[0])
                print("FİŞ TARİHİ : ",nextAccountingExpenseInformation[1])
                print("AÇIKLAMA   : ",nextAccountingExpenseInformation[2])
                print("TUTAR      : ",nextAccountingExpenseInformation[3])
                print("FİŞ TİPİ   : ",nextAccountingExpenseInformation[4])
                print("FİŞ YIL    : ",nextAccountingExpenseInformation[5])
                print("")
        
        for nextAccountingIncomeExpenseAmount in myAccountingIncomeExpenseAmount:
            print("")
            print("TOPLAM GİDER: ",nextAccountingIncomeExpenseAmount[0])
            print("")
    
    elif mySelectionProcess == 9:
        print("")
        print("YIL BAZLI TOPLAM KAR - ZARAR")
        print("")
        myAccountingYear = int(input("KAR-ZARAR ALINMAK İSTENEN YIL: "))
        myAccountIncomeYearly = Accounting.Db_Accounting_Income_And_Expense_With_Year("Gelir",myAccountingYear)
        myAccountExpenseYearly = Accounting.Db_Accounting_Income_And_Expense_With_Year("Gider",myAccountingYear)
        myTotalIncome= 0
        myTotalExpense =0
        
        for nextAccountIncomeYearly in myAccountIncomeYearly:
            print(myAccountingYear , "  YILI GELİR TUTARI:  ",nextAccountIncomeYearly[0])
            myTotalIncome = int(nextAccountIncomeYearly[0])
        
        for nextAccountExpenseYearly in myAccountExpenseYearly:
            print(myAccountingYear , "  YILI GİDER TUTARI:  ",nextAccountExpenseYearly[0])
            myTotalExpense = nextAccountExpenseYearly[0]
        
        myTotalIncomeAndExpense = myTotalIncome - myTotalExpense
        print(myAccountingYear , "  YILI KAR TUTARI  :  ",myTotalIncomeAndExpense)





        
    


My_Login_To_System()

