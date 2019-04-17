# jtthink_mysql_comprehensive_combat

## [统计分析优化套路篇](http://www.jtthink.com/course/75#1579)

### [第1讲:开张课、纯SQL生成统计缓存提高统计性能 试听](https://www.jtthink.com/course/play/1551)
* 为了业务简单，我们使用mysql内置数据库。先从最简单的统计分析开始

### [第2讲:使用纯SQL进行基础的手工分表（按年份）](https://www.jtthink.com/course/play/1552)
* 今天先说下手工最简单的分表方式。纯SQL实现

### [第3讲:使用PHP(swoole)进行基础手工分表（按年份）](https://www.jtthink.com/course/play/1553)
* 本节课是上节课的延续，我们使用PHP(swoole)代码来实现上节课存储过程的内容

### [第4讲:使用python进行分析统计(1):导出csv文件、引入pandas 试听](https://www.jtthink.com/course/play/1554)
* 更了进一步优化统计功能，我们要引入python了。当然，后面我们依然使用PHP来调用python功能

### [第5讲:使用python进行分析统计(2):pandas"秒"学、按日期分组统计](https://www.jtthink.com/course/play/1555)
* 上节课引入了pandas后，这节课我们来做个秒学。把我们第一节课的功能使用python来实现而不使用sql

### [第6讲:使用python进行分析统计(3): 使用Flask+pandas实现数据缓存输出](https://www.jtthink.com/course/play/1559)
* 前面我们做了数据导出，并且利用pandas读取。今天我们把读取对象常驻内存，方便后面调用，此时就要借助一些web框架了

### [第7讲:使用python进行分析统计(4): 支持按年统计、设计路由、冗余字段设置](https://www.jtthink.com/course/play/1563)
* 上节课我们借助python+pandas+数据库文件导出实现了个简单的缓存API。今天我们来说下统计功能的基本设置

### [第8讲:使用python设计自己的"查询语言"解析器(1)](https://www.jtthink.com/course/play/1571)
* 前面我们结合了mysql导出数据+python+pandas+flask实现一个简单的数据缓存和统计分析优化。
那么问题在于我们是写死的路由，这几节课我们来讲下如何利用“自定义的DSL”来让前端调用更加灵活

### [第9讲:设计自己的"查询语言"解析器:自定义解析类、支持where条件的解析(上)](https://www.jtthink.com/course/play/1574)
* 上节课我们引入自定义DSL的基本概念。这节课我们来做一些代码实现基本的条件解析。（目前先模仿SQL的语法）

### [第10讲:设计通用路由、使用自定义DSL支持where条件的pandas查询 试听](https://www.jtthink.com/course/play/1579)
* 今天功能又进了一步。当我们输入select * from tb where xx=xx时就可以从pandas中取数据,以实现缓存数据的快速查询

### [第13讲:java篇:Canal使用初步、监听数据库变化示列 试听](http://www.jtthink.com/course/play/1599)
* 前面我们把数据用python+pandas+flask做了一个简易的查询。这几节课我们来实现下当数据发生变动时如何触发实践

### [第14讲:使用java Canal拦截mysql插入数据、提交到python API(okHttp、jackson等) 试听](http://www.jtthink.com/course/play/1603)
* 今天我们写一下代码拦截新增数据，得到后请求外部API的基本套路


