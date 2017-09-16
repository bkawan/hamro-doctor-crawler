# -*- coding: utf-8 -*-
import scrapy


class HamrodoctorSpider(scrapy.Spider):
    name = 'hamrodoctor'
    allowed_domains = ['hamrodoctor.com']
    start_urls = ['http://hamrodoctor.com/hospitals']

    def parse(self, response):
        districts = response.xpath("//select[@id='HospitalDistrict']/option/@value").extract()
        districts = [x for x in districts if x]

        for district in districts:
            yield scrapy.http.FormRequest.from_response(
                response,
                formid='hospitalForm',
                formdata={
                    'data[Hospital][keyword]': '',
                    'data[Hospital][district]': district,

                },

                callback=self.find_hospitals_in_disctict
            )

    def find_hospitals_in_disctict(self, response):
        pass
        # inspect_response(response, self)
