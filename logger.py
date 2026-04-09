import datetime
import os
import pandas as pd



#проверка 
def log():

    now = datetime.datetime.now()
    #разбивка дэйттайма
    on_date = now.date()
    on_time = now.time()


    file_check = os.path.isfile("logs.csv")
    if file_check:
        current_id = len(pd.read_csv ("logs.csv"))
    else:
        current_id = 0

    df = pd.DataFrame({"pc_username" :[], "function_name" :[], "Date in 'date.month.year" : [], "Time": [] })
    df.to_csv("logs.csv", index_label=id , mode="a", sep=",", header=not os.path.isfile("logs.csv") ) 

    #сам логгер
    def logger(func):
        def wrapper(*args, **kwargs):

         result=func(*args, **kwargs)

         with open("logs.csv", 'a', encoding='UTF-8') as filed:
              filed.write(f"{current_id()}-{os.getlogin()}-{func.__name__}-{on_date}-{on_time}")
         return wrapper
                        

    #декоратор
    @logger
    def glue(*args, **kwargs):
     res=''
     for i in args, kwargs:
         res+=i
     return res

    print(glue('qwqwq','uyht'))