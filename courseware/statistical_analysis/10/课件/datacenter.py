import pandas as pd

Data={}
Data_IndexCol={"employees":['emp_no']}
Data_Names={"employees":['emp_no','birth_date','first_name','last_name','gender','hire_date','ids']}
employees=pd.read_csv("./files/employees.csv",
            names=Data_Names['employees'],
          index_col=Data_IndexCol['employees'], header=None,dtype={"ids":str},parse_dates=['hire_date'],
                      date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
)
employees['hire_date_year']=employees.apply(lambda x:x['hire_date'].strftime('%Y'),axis=1)

Data["employees"]=employees