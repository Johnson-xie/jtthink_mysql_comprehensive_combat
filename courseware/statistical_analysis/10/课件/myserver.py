from flask import Flask,jsonify,request,json
from datacenter import Data,Data_IndexCol,Data_Names
from mydsl import MyDSL
app = Flask(__name__)

mydsl=MyDSL()
@app.before_request
def before_request():
    mydsl.parse(request.data.decode("utf8"))

@app.route('/',methods=["POST"])
def getData():
    mydsl.parseWhere()
    dataset=Data[mydsl.DataTable]
    if mydsl.WhereField["key"]!="": #代表有where条件
        if mydsl.WhereField["key"] in Data_IndexCol[mydsl.DataTable]: #代表 根据 index来取值 目前结果集是一条数据
            return jsonify(dataset.loc[mydsl.WhereField["value"]].to_dict())
        elif mydsl.WhereField["key"] in Data_Names[mydsl.DataTable]:#代表 根据 普通列来取值 目前结果集一般是多条，dataframe
            return jsonify(dataset[dataset[mydsl.WhereField["key"]]==mydsl.WhereField["value"]].head(10).to_dict(orient='records'))
    else:
         return jsonify({"status":"no data"})

@app.route('/count', methods=["GET"])
def count():
    # groupby = request.args.get("g", "")
    # if groupby == "hire_date":
    #     return jsonify(employees.groupby(['hire_date_year']).count()['ids'].to_dict())
    # else:
        return jsonify({"status": "error"})






if __name__ == '__main__':
    app.run() #默认端口5000
