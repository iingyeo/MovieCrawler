from moviescraper.items import MovieItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector.lxmlsel import HtmlXPathSelector


class tobestSpider(CrawlSpider):
    name = "torrent"
    allowed_domains = ["target.domain"]
    start_urls = [
        "http://target.domain/start/url"
    ]
    baseurl = "http://target.domain"
    rules = (Rule(SgmlLinkExtractor(allow=("allow/url"), restrict_xpaths=())
                  , callback="parse_list", follow=True),
             )

    def parse_list(self, response):
        hxs = HtmlXPathSelector(response)

        # print(hxs.extract())
        body = hxs.select('//div[@id="contents"]')

        # print(body.extract())

        item = MovieItem()

        item['title'] = body.select('//div[@id="bo_v_title"]/h1/text()').extract()[0]
        item['link'] = body.select('//div[@class="bo_v_file"]/a/@href').extract()[1]
        item['date'] = body.select('//div[@id="bo_v_info"]/table/tbody/tr/td/table/tbody/tr/td/text()').extract()[2]

        if not item['title']:
            print("Table Title")
        else:
            print(item)
            yield item
