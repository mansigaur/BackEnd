#code file for performing functions on authors file in database
from mongoengine import connect, disconnect
from database_repository.model.authors import authors 

class AuthorRepository():
    def __init__(self):
        connect('authors_data', host='mongodb', port=27017)

    def read(self,author_name, url):

        author_list = authors.objects(author_name = author_name, url = url)
    
        if len(author_list) == 0:
            author_list = authors.objects(author_name = '-'.join(author_name.split(" ")), url = url)
            if len(author_list) > 0:
                author_list[0].author_name = author_name

        if len(author_list) == 0 and "www" in url:
            new_url = "".join(url.split("www"))
            author_list = authors.objects(author_name = author_name, url = new_url)
            if len(author_list) > 0:
                author_list[0].author_name = author_name


        return author_list


