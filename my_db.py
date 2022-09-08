import pypyodbc

class Database:

    def __init__(self) -> None:
        pass
        
    db = pypyodbc.connect(
        'Driver={SQL Server};'
        'Server=SEZGIKARAGULLEN;'
        'Database=DbIncomeAndExpense;'
        'Trusted_Connection=True;'
    )
    imlec = db.cursor()
