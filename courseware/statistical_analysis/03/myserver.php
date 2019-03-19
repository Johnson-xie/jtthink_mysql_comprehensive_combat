<?php
$mysql_info=[
    'host' => '192.168.222.1',
    'port' => 3306,
    'user' => 'root',
    'password' => '123123',
    'database' => 'employees',
];
define("AllYearSQL","select DISTINCT DATE_FORMAT(hire_date,'%Y') as count_year from employees  ");

function splittable(array $mysqlinfo){
    $swoole_mysql = new Swoole\Coroutine\MySQL();
    $swoole_mysql->connect($mysqlinfo);
    $years = $swoole_mysql->query(AllYearSQL);
    foreach ($years as $row)
    {
        $year=$row["count_year"];
            $mysql = new Swoole\Coroutine\MySQL();
            $mysql->connect($mysqlinfo);
            $tbName="employees_".$year;
            $sql="DROP TABLE IF EXISTS $tbName;";
            $stmt = $mysql->prepare($sql);
            $stmt->execute();
            $sql="create table $tbName like employees;";
            $stmt = $mysql->prepare($sql);
            $stmt->execute();
            $sql= "insert into $tbName select * from employees where   DATE_FORMAT(hire_date,'%Y')=$year";
            $stmt = $mysql->prepare($sql);
            $stmt->execute();
            defer(function() use($mysql,$year){
                $mysql->close();
                echo "$year done ".PHP_EOL;
            });

    }
    defer(function() use($swoole_mysql){
        $swoole_mysql->close();
    });

}
go(function() use($mysql_info){
    splittable($mysql_info);
});
