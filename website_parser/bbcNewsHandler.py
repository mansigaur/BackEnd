from website_parser.abstractHandler import AbstractHandler
from database_repository.model.channels import channels
from bs4 import BeautifulSoup as bs

class BBCHandler(AbstractHandler):
    def handle(self, data, channel: channels) -> str:
        if "BBC News".lower() == channel.news_channel.lower() or "BBC".lower() == channel.news_channel.lower():
            author_name = None
            soup = bs(data, 'html5lib')

            author_tag = soup.find('p', {"class": "ssrcss-ugte5s-Contributor"})

            if author_tag != None and author_tag.find('strong'):
                # author_tag.text return the "By Author Name"
                # Splitting the data based on "By " and -1 return the last value from list

                author_name = author_tag.find('strong').text.split('By ')[-1] 
            return author_name
        else:
            return super().handle(data, channel)