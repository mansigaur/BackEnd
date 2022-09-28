from unittest import result
from flask_restful import Resource
from database_repository.model.channels import channels
from schemas.validate import ValidateRequestSchema
from webargs.flaskparser import use_args
from database_repository.authors_repository import AuthorRepository
from database_repository.channels_repository import ChannelsRepository
from website_parser.bbcNewsHandler import BBCHandler
from website_parser.yahooNewsHandler import YahooNewsHandler
import json 
#to process the data data received from website
class ValidateAuthorAndUrl(Resource):
    
    @use_args(ValidateRequestSchema, location="json")
    def post(self, data):

        response  = dict(result=None)
        author = AuthorRepository()
        channels = ChannelsRepository()
        bbcHandler = BBCHandler()
        yahooHandler = YahooNewsHandler()
        bbcHandler.set_next(yahooHandler) #desgin pattern-chain of responsibilty 
        channel_details = channels.read(url = data['url'])
        if len(channel_details) == 0 and 'www' in data['url']:
            url = "".join(data['url'].split("www."))
            channel_details = channels.read(url = url)

        if len(channel_details) == 0:
            response["result"] = "Not Trust Worthy."
            return response

        else:
            channel_data = channel_details[0]
            author_name = bbcHandler.handle(data['html_data'], channel_data)
            
            author_details = None
            if author_name != None: 
                author_details = author.read(author_name, channel_data.url)

            if author_details:
                response.update(json.loads(author_details[0].to_json()))
                response["result"] = 'Trust Worthy.'
            else:
                response.update(json.loads(channel_data.to_json()))
                response["result"] = 'Website is well known source but author is unknown.'

                if author_name:
                    response['author_name'] = f"{author_name} (Unknown)"

        return response
