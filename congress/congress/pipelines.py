# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CongressPipeline(object):
    def process_item(self, item, spider):
        # full_text = ""
        # item['text_blob'] = full_text
        return item
