# coding:utf8

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        pass


if __name__=="__main__":
    root_url="http://baike.baidu.com/biew/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
