from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
import csv
class HandleCsv:
    # 定义存放csv内容的list
    csv_list = []

    def __init__(self, filename):
        self.filename = filename
        with open(self.filename)as fp:
            self.csv_list = list(csv.reader(fp))

    # 在第N行第M列空白单元格处修改内容
    def modify(self, n, m, value):
        self.csv_list[n - 1][m - 1] = value

    # 插入第N行
    def insert_row(self, n):
        self.csv_list.insert(n - 1, [])

    # 在第N行第M列单元格插入
    def insert_col(self, n, m, value):
        # 如果该单元格左边的单元格为空，那么先对左边的单元格写入空格
        if len(self.csv_list[n - 1]) < m:
            if len(self.csv_list[n - 1]) == m - 1:
                self.csv_list[n - 1].append(value)
            else:
                for i in range(len(self.csv_list[n - 1]), m - 1):
                    self.csv_list[n - 1].append('')
                self.csv_list[n - 1].append(value)
        else:
            self.modify(n, m, value)

    # 删除第N行
    def del_row(self, n):
        del self.csv_list[n - 1]

    # 获取第n行第m列单元格内容
    def get_value(self, n, m):
        return self.csv_list[n - 1][m - 1]

    def list2csv(self, file_path):
        try:
            fp = open(file_path, 'w')
            for items in self.csv_list:
                for i in range(len(items)):
                    # 若元素中含有逗号，那么需要加双引号
                    if items[i].find(',') != -1:
                        fp.write('\"')
                        fp.write(items[i])
                        fp.write('\"')
                    else:
                        fp.write(items[i])
                    # 最后一个元素不用加逗号
                    if i < len(items) - 1:
                        fp.write(',')
                fp.write('\n')
        except Exception as e:
            print(e)
def index(request):
    html = '''
        <form action='resp' method='get'>
         <p>name<input type='text' name='name'></p>
         <p>coordinate<input type='text' name='coordinate'></p>
         <p>number<input type='text' name='number'></p>
        <input type='submit' name='submit'>
        </form>
        '''
    return HttpResponse(html)

def resp(request):
    name = str(request.GET.get("name"))
    coordinate = str(request.GET.get("coordinate"))
    number = int(request.GET.get("number"))
    h_csv = HandleCsv("C:/Users/PC/Desktop/data.csv")
    co = coordinate.split(',')
    h_csv.insert_col(number, 10, co[0])
    h_csv.insert_col(number, 11, co[1])
    h_csv.list2csv("C:/Users/PC/Desktop/data.csv")
