"""This file is for downloading news articles and then collect them in a json or txt file."""

import newspaper
from newspaper import Article
from datetime import date 

def build():
    telex_build = newspaper.build('http://telex.hu')
    
    with open(path, "w") as fh:
        path = 'news_articles.txt'
        write = fh.write(path)
        return write
    

if __name__ == "__main__":
    build()
