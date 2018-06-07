from scrapy.spiders import Spider
from scrapy.http import Request
from bs4 import BeautifulSoup
from scrapyspider.items import ScrapyspiderItem

class BlogSpider(Spider):
    Item = ScrapyspiderItem()
    name = 'scrapyspider'
    allowed_domains = ['23wx.com']
    bash_url = 'http://www.5858xs.com/xiaoshuosort3/0/'
    bashurl = '.html'

    def start_requests(self):
        for i in range(1, 2):
            url = self.bash_url + str(i) + self.bashurl
            yield Request(url, self.parse)

    def parse(self, response):
        trs = BeautifulSoup(response.text).find_all('tr')
        for tr in trs:
            try:
                self.Item['name'] = tr.find_all('td')[0].string
                self.Item['chapter'] = tr.find_all('td')[1].string
                self.Item['author'] = tr.find_all('td')[2].string
                self.Item['recommend'] = tr.find_all('td')[3].string
                self.Item['length'] = tr.find_all('td')[4].string
                self.Item['time'] = tr.find_all('td')[5].string
                self.Item['status'] = tr.find_all('td')[6].string
                yield self.Item

            except:
                pass