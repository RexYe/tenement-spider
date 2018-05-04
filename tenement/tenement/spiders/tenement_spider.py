# -*- coding: UTF-8 -*-
import scrapy

class TenementSpider(scrapy.Spider):
    name = "tenement"
    start_urls = [
        "https://hz.lianjia.com/zufang/"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html
        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        for quote in response.xpath('//div[@class="info-panel"]'):
            yield {
                'price': quote.xpath('.//span[@class="num"]/text()').extract_first(),
                'area': quote.xpath('.//span[@class="meters"]/text()').extract_first(),
                'region': quote.xpath('.//a[@class="laisuzhou"]/span[@class="region"]/text()').extract_first(),
                'type': quote.xpath('.//span[@class="zone"]/span/text()').extract_first()
            }

        next_page_url = response.xpath('//div[@class="page-box"]/a[contains(text(), "下一页")]/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))






# scrapy crawl tenement -o items.json -s FEED_EXPORT_ENCODING=utf-8
