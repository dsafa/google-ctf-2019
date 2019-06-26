# -*- coding: utf-8 -*-
import scrapy
import scrapy.item


class CatImagesSpider(scrapy.Spider):
    name = 'cat_images'
    allowed_domains = ['emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com']
    start_urls = ['http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com']

    def parse(self, response):
        for img in response.xpath('//img[@src]/@src').getall():
            yield ImageItem(image_urls=['http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com/' + img])
            yield {'url': response.url}

        for next_page in response.xpath('//ul/li/a[@href]/@href').getall():
            yield response.follow(next_page, self.parse)

class ImageItem(scrapy.Item):
    image_urls=scrapy.Field()
    images=scrapy.Field()
    pass