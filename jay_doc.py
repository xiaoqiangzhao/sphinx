
SEP = ['#', '*', '=', '-', '^', "\""]
PLACEHOLD = "<ADD DESCRIPTION HERE!>"
TYPE = ['doc','para','list','tag_s','tag_e','code','url','download','include_f']

class para(object):
    def __init__(self, name, articles = None, depth = 0):
        self.name = name
        self.depth = depth
        if articles :
            self.articles = articles
        else:
            self.articles = []
        self.des = PLACEHOLD
        self.sep = SEP
        self.type = 'para'

    def add_article(self, item):
        item.depth = self.depth + 1
        self.articles.append(item)

    def print_topo(self):
        print("  "*self.depth, self.type, ":",  self.name)
        for a in self.articles:
            a.print_topo()

    def show_articles(self):
        for i in self.articles:
            if isinstance(i,misc_item):
                print(i.entity)
            else:
                print(i.name)


class misc_item:
    def __init__(self, name , entity= None, type_i = '', depth = 0):
        self.entity = entity
        self.type = type_i
        self.depth = depth
        self.name = name

    def print_topo(self):
        print("  "*self.depth, self.type, ":", self.name)



class doc:
    def __init__(self, topic, author):
        '''
        version : 1.0
        args: topic , author'''
        self.topic = topic
        self.author = author
        self.paras = []
        self.depth = 0
        self.sep = SEP
        self.des = PLACEHOLD
        self.type = 'doc'

    def add_para(self, para):
        '''
         add paragraph
        '''
        para.depth = self.depth + 1
        self.paras.append(para)

    def print_topo(self):
        print(self.topic)
        for p in self.paras:
            p.print_topo()
