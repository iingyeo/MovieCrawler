# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from django.db import IntegrityError
from movieapp.models import Movie


class MoviestarPipeline(object):
    def process_item(self, item, spider):
        try:
            print(item['title'])
            target = Movie.objects.all().filter(link=item['link'])
            print(len(target))

            if not target:
                item.save()

        except IntegrityError:
            print "Integrity Error when insert article to db : " + item.get('link')
        return item
