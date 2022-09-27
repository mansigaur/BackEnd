from website_parser.abstractHandler import AbstractHandler
from database_repository.model.channels import channels
from bs4 import BeautifulSoup as bs

class YahooNewsHandler(AbstractHandler):
    def handle(self, data, channel: channels) -> str:
        if "Yahoo News".lower() == channel.news_channel.lower() or "Yahoo News UK".lower() == channel.news_channel.lower():
            author_name = None
            soup = bs(data, 'html5lib')

            # Using CSS selector extracting the author name 
            author_tags = soup.find('div', {"class": "caas-attr-item-author"})

            if author_tags != None:
                # author_tag.text return the "By Author Name"
                # Splitting the data based on "By " and -1 return the last value from list

                author_name = author_tags.text
            return author_name
        else:
            return super().handle(data, channel)