from pyparsing import Word, alphas,printables,Suppress,Literal,ZeroOrMore,alphanums,Optional,Combine,nums,OneOrMore
import re
class MyDSL:
    Action=""
    Fields=""
    DataTable=""
    Where=""
    WhereField={"key":None,"value":None,"type":"int"}
    Limit=""

    def convertField(self,str):
        begin = str[0]
        str = re.sub("([A-Z])", "_\g<0>", str[1:])
        return (begin + str).lower()
    def parse(self,dsl):
        action=Word(alphas)
        fields=Word(printables)
        FROM=Suppress("from")
        WHERE=Optional(Combine("where"+OneOrMore(" ")+Word(alphanums)+Literal("=")+Word(printables)),"")
        LIMIT=Optional(Combine("limit"+OneOrMore(" ")+Word(nums)+Literal(",")+Word(nums)),"")
        dataset=Word(alphas)
        query_pattern=action+fields+FROM+dataset+WHERE+LIMIT
        ret=(query_pattern.parseString(dsl))
       # print(ret)
        if len(ret) == 5:
            self.Action = ret[0]
            self.Fields = ret[1]
            self.DataTable = ret[2]
            self.Where = ret[3]
            self.Limit = ret[4]
    def parseWhere(self):
        if  self.Where.strip()!="":
            pattern = Suppress("where") + Word(alphanums) + Suppress(Literal("=")) + ZeroOrMore("'") + Word(
                alphanums) + ZeroOrMore("'")
            ret=pattern.parseString(self.Where)
            if len(ret)==2: #数字
                self.WhereField["key"]=self.convertField(ret[0])
                self.WhereField["value"]=int(ret[1])
            elif len(ret)==4:#字符串
                self.WhereField["key"] = self.convertField(ret[0])
                self.WhereField["value"] = ret[2]
                self.WhereField["type"] = 'str'



