from mongoengine import connect, disconnect
from database_repository.model.channels import channels 
from furl import furl

class ChannelsRepository():
    def __init__(self):
        connect('authors_data', host='mongodb', port=27017)

    def read(self,url):

        furl_data = furl(url)
        author = channels.objects(url = furl_data.origin)

        if len(author) == 0:
            if furl_data.origin[-1] != '/':
                author = channels.objects(url = furl_data.origin + '/')

            if len(author) == 0 and len(furl_data.path.segments) > 1:
                furl_data.path.segments = [furl_data.path.segments[0]]
                author = channels.objects(url = furl_data.url)

        return author


