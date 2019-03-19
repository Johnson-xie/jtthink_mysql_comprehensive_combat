from flask import Flask,jsonify,request,json
import pandas as pd
import datetime as dt
import numpy as np
app = Flask(__name__)

employees=pd.read_csv("./files/employees.csv",
            names=['emp_no','birth_date','first_name','last_name','gender','hire_date','ids'],
          index_col=['emp_no'], header=None,dtype={"ids":str},parse_dates=['hire_date'],
                      date_parser=lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
)
employees['hire_date_year']=employees.apply(lambda x:x['hire_date'].strftime('%Y'),axis=1)


@app.route('/<int:empno>',methods=["GET"])
def getEmp(empno):
    if empno in employees.index:
         return jsonify(employees.loc[empno].to_dict())
    else:
         return jsonify({"status":"no data"})


@app.route('/count', methods=["GET"])
def count():
    groupby = request.args.get("g", "")
    if groupby == "hire_date":

        return jsonify(employees.groupby(['hire_date_year']).count()['ids'].to_dict())

    else:
        return jsonify({"status": "error"})


if __name__ == '__main__':
    app.run() #默认端口5000
