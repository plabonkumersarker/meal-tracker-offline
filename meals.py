#plabon - 2021-07-25 04:06:55.146181 - https://linktr.ee/noncsdude
import datetime
import codecs
import re

def list_maker():
    print("Seperate by commas(,) Such as- milk,banana...etc")
    x = input("Breakfast: ")
    y = input("Lunch: ")
    z = input("Dinner: ")
    html_parts = "<ul><li>"+ x +"</li>"+"<li>"+ y +"</li>"+"<li>"+ z +"</li></ul>\n"
    print("Submitted!!!")
    return html_parts

html = ''
a = datetime.date.today()
today = "<h2>"+ str(a.day) + "-" + str(a.month) + "-" + str(a.year)+"</h2>"
with codecs.open("meal-list.html","r","utf-8") as fp:
    html+=fp.read()


sep = "<h1>========</h1>\n"
if today in html:
    print("WARNING! You already submitted todays meal. Your current change will update it automatically.")
    index = html.find(today)
    first_portion = html[:index]
    index_list = re.finditer(r'<h1>========</h1>',html)
    idx_li = []
    for each in index_list:
        s = each.start()
        idx_li.append(s)
    last_index = idx_li[1]
    middle_portion = list_maker()
    last_portion = html[last_index:]
    final_html = first_portion + today + middle_portion + last_portion

else:
    index = html.find("<h1>========</h1>")
    first_portion = html[:index]
    middle_portion = list_maker()
    last_portion = html[index:]
    final_html = first_portion + sep + today + middle_portion + last_portion

with codecs.open("meal-list.html","w","utf-8") as fp:
    fp.writelines(final_html)

