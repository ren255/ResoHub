import json
import uuid
from django.db import models
from django.utils import timezone


class ScrapyItem(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    scrape_id = models.CharField(max_length=100, null=True)
    item_name = models.TextField(null=True)
    spider_name = models.TextField(null=True)
    data = models.TextField()  # this stands for our crawled data
    date = models.DateTimeField(default=timezone.now)

    # This is for basic and custom serialisation to return it to client as a JSON.
    @property
    def to_dict(self):
        data = {"data": json.loads(self.data), "date": self.date}
        return data

    def __str__(self):
        return str(self.unique_id)
