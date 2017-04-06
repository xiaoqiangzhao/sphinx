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
doc1.add_para(p3)
p4 = para("para4")
p3.add_article(p4)

l3 = ['a','b','c']
i3 = misc_item(l3,'list')
# p3 = para("para3",[p4,i3])
p3.add_article(i3)

doc1.add_para(p1)
doc1.add_para(p2)

p1.show_articles()
p2.show_articles()
p3.show_articles()
p4.show_articles()


with open('./test/test.rst','w') as f:
    f.write(temp.render(doc = doc1))
print(temp.render(doc = doc1))
