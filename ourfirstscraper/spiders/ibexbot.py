import scrapy


class IbexbotSpider(scrapy.Spider):
    name = 'ibexbot'
    allowed_domains = ['www.ibex.bg/']
    start_urls = ['https://ibex.bg/']

    def parse(self, response):
        #Extracting the content using css selectors
        price = response.css('#dam-table tr td.column-price_eur::text').extract()
        time = response.css('#dam-table tr td.column-time_part::text').extract()
        date = response.css('#dam-table tr td.column-date_part::text').extract()
        for item in zip(time,price):
            scraped_info = {
                'time':item[0],
                'price':item[1],
                'date':date[2],
            }
        # votes = response.css('.score.unvoted::text').extract() times = response.css('time::attr(title)').extract() comments = 
        #response.css('.comments::text').extract() Give the extracted content row wise
        # for item in zip(titles,votes,times,comments):
        #     #create a dictionary to store the scraped info
        #     scraped_info = {
        #         'title' : item[0], 'vote' : item[1], 'created_at' : item[2], 'comments' : item[3],
        #     }
            #yield or give the scraped info to scrapy
            yield scraped_info
