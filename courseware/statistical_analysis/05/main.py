import pandas as pd
import datetime as dt
employees=pd.read_csv("./files/employees.csv",
            names=['emp_no','birth_date','first_name','last_name','gender','hire_date','ids'],
          index_col=0, header=None,dtype={"ids":str}
)

#dataframe
#series

#统计功能，需要hire_date作为index
countByHireDate=employees.reset_index()#重置索引
countByHireDate.set_index("hire_date",inplace=True)

 #1981-5-6
print(countByHireDate['emp_no'].groupby(lambda x:dt.datetime.strptime(x,'%Y-%m-%d').strftime('%Y')).count())



