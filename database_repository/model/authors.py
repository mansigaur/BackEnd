from mongoengine import Document, StringField

class authors(Document):
    author_name = StringField()
    news_channel = StringField()
    url = StringField()
