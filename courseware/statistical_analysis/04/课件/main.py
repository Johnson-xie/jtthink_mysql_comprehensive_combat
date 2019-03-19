import pandas as pd

employees=pd.read_csv("./files/employees.csv",
            names=['emp_no','birth_date','first_name','last_name','gender','hire_date','ids'],
            index_col=0,header=None,dtype={"ids":str}
)

print(employees[0:5])