from mongoengine import Document, StringField

class channels(Document):
    news_channel = StringField()
    url = StringField()
