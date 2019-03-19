from flask import Flask,jsonify
import pandas as pd
app = Flask(__name__)
employees=pd.read_csv("./files/employees.csv",
            names=['emp_no','birth_date','first_name','last_name','gender','hire_date','ids'],
          index_col=0, header=None,dtype={"ids":str}
)

@app.route('/')
def index():
    return 'index'
#localhost:5000/
@app.route('/<int:empno>',methods=["GET"])
def getEmp(empno):
    return jsonify(employees.loc[empno].to_dict())


if __name__ == '__main__':
    app.run() #默认端口5000
