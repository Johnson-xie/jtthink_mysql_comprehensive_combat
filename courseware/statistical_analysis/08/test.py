from pyparsing import Word, alphas,printables,Suppress


myDSL="select * from employees"

action=Word(alphas)
fields=Word(printables)
FROM=Suppress("from")
dataset=Word(alphas)
query_pattern=action+fields+FROM+dataset
print(query_pattern.parseString(myDSL))