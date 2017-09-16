# -*- coding: utf-8 -*-
import scrapy
from HamroDoctor.items import HamrodoctorItem


class HamrodoctorSpider(scrapy.Spider):
    name = 'hamrodoctor'
    allowed_domains = ['hamrodoctor.com']
    start_urls = ['http://hamrodoctor.com/hospitals']
    base_url = 'http://hamrodoctor.com'

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

                callback=self.find_hospitals_in_disctict,
                meta={'district': district}
            )

    def find_hospitals_in_disctict(self, response):
        hospitals = response.xpath("//h3/a/@href").extract()
        for hospital in hospitals:
            yield scrapy.Request('{}{}'.format(self.base_url, hospital),
                                 callback=self.get_hospital_detail,
                                 meta={'district': response.meta['district']}
                                 )

    def get_hospital_detail(self, response):
        item = HamrodoctorItem()
        about_hospital = response.xpath("//div[@class='big_team_widget']/p/text()").extract_first()
        name = response.xpath("//div[@class='col-lg-12']/h2/text()").extract_first()
        if about_hospital:
            short_description = about_hospital
        else:
            short_description = ""
        li_selectors = response.xpath("//div[@class='doctor-details']/ul/li")
        data = {
            'district': response.meta['district'],
            'short_description': short_description,
            'name': name
        }
        for li in li_selectors:
            k = li.xpath(".//span/text()").extract_first().strip().lower()
            v = li.xpath("text()").extract_first()
            data.update({
                k: v
            })

        item.update(data)
        yield item
