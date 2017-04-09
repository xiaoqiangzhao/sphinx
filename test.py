from jay_doc import para, doc, misc_item
from jinja2 import Template ,Environment, PackageLoader
import sys
sys.path.append('../..')
env = Environment(loader=PackageLoader('Sphinx.sphinx'))

temp = env.get_template('doc.rst')
doc1 = doc("my test","Jay Zhao")
p1 = para("para1")
p2 = para("para2")
p3 = para("para3")
p4 = para("para4")
doc1.add_para(p1)
doc1.add_para(p2)
doc1.add_para(p3)
p3.add_article(p4)

l3 = ['a','b','c']
ts1 = {'name':'touch me'}
i3 = misc_item('list_for_p3', l3, 'list')
tag_s1 = misc_item('ts1',ts1,'tag_s')
p1.add_article(tag_s1)
# p3 = para("para3",[p4,i3])
p3.add_article(i3)
te1 = {'name':'touch me','title':'tag'}
tag_e1 = misc_item('te1',te1,'tag_e')
p4.add_article(tag_e1)
cb_t = []
with open('./test.py','r') as f:
    cb_t = f.readlines()

cb = {'name':'example code', 'text': cb_t, 'shell': False}

code4 = misc_item('code4',cb,'code')

inc_en = {'name':'jay_doc','file_path':'../jay_doc.py'}
inc3 = misc_item('inc3',inc_en,'include_f')
p2.add_article(inc3)

url1 = misc_item('url',None,'url')
url1.entity = {'name':'Ref Code','desc':'As with more details, please see','url':'https://www.baidu.com'}
p1.add_article(url1)
dl = misc_item('download',None,'download')
dl.entity = {'name':'Click Me','desc':'Or You can download the Source File','file_path':'source/jay_doc.py'}
p1.add_article(dl)
p4.add_article(code4)



doc1.print_topo()
# p1.show_articles()
# p2.show_articles()
# p3.show_articles()
# p4.show_articles()


with open('./test/test.rst','w') as f:
    f.write(temp.render(doc = doc1))
print(temp.render(doc = doc1))
