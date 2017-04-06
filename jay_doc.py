
SEP = ['#', '*', '=', '-', '^', "\""]
PLACEHOLD = "<ADD DESCRIPTION HERE!>"

class para(object):
    def __init__(self, title, articles = None, depth = 0):
        self.title = title
        self.depth = depth
        if articles :
            self.articles = articles
        else:
            self.articles = []
        self.des = PLACEHOLD
        self.sep = SEP
        self.type = 'para'

    def add_article(self, item):
        if isinstance(item, para):
            item.depth = self.depth + 1
        self.articles.append(item)

    def show_articles(self):
        for i in self.articles:
            if isinstance(i,misc_item):
                print(i.entity)
            else:
                print(i.title)


class misc_item:
    def __init__(self, entity= None, type_i = ''):
        self.entity = entity
        self.type = type_i


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

    def add_para(self, para):
        '''
         add paragraph
        '''
        para.depth = self.depth + 1
        self.paras.append(para)
