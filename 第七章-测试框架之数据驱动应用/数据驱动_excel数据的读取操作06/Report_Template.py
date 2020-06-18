# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/6/10 8:34
# @Software       : Web-Autotest-Python
# @Python_verison : 3.7

# html测试模板文件
def htmlTemplate(strData):
    htmlStr='''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>数据驱动json文件的读取测试报告</title>
    <style>
        body{
        width:80%;            /*整个body区域占浏览器的宽度百分比*/
        margin:40px auto;     /*整个body区域相对浏览器窗口摆放位置(左右，上下) */
        font-weight: bold;    /*整个body区域的字体加粗*/
        font-family: 'trebuchet MS','Lucida sans',SimSun; /*表格中文字的字体类型*/
        font-size:18px;       /*表格中文字体大小*/
        color:#000;           /*整个body区域字体的颜色*/
    }
    table{
        *border-collapse:collapse; /*合并表格边框*/
        border-spacing:0;     /*表格的边框宽度*/
        width:100%;           /*整个表格相对父元素的宽度*/
    }
    .tableStyle{
        border-style:outset;  /*整个表格外边框样式*/
        border-width:2px;     /*整个表格外边框宽度*/
        border-color:blue;    /*整个表格外边框颜色*/
    }
    .tableStyle tr:hover{
        background:rgb(173,216,230); /*鼠标滑过一行时，动态显示的颜色*/
    }
    .tableStyle td,.tableStyle th{
        border-left:solid 1px rgb(146,208,80)  /*表格竖线颜色*/
        border-top:1px solid rgb(146,208,80)   /*表格的横线颜色*/
        padding:15px;       /*表格内边框尺寸*/
        text-align:center;  /*表格内容显示位置*/
    }
    .tableStyle th{
        padding:15px;       /*表格标题栏、字体的尺寸*/
        background-color:rgb(146,208,80);      /*表格标题背景颜色*/
        background-image: -webkit-gradient(linear,left top,left bottom,from(#92D050),to(#A2D668));/*标题栏渐变色*/
    }
    
    </style>
    </head>
    <body>
    <center><h1>测试报告</h1></center><br />
    <table class=tableStyle>
        <thead>
        <tr>
        <th>Search Words</th>
        <th>Assert Words</th>
        <th>Start Time</th>
        <th>Waste Time(s)</th>
        <th>Status</th>
        </tr>
        </thead>
    '''
    endStr = ''' 
    </table>
    </body>
    </html>'''
    html = htmlStr+strData+endStr
    with open('./report.html',mode='w',encoding='utf-8') as file:
        file.write(html)
