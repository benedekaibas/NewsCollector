"""This file is for downloading news articles and then collect them in a json or txt file."""

import newspaper
from newspaper import Article
from datetime import date 

def build():
    telex = newspaper.build('http://telex.hu')
    telex_url = telex.article_urls()
    path = 'news_articles.txt'
    return telex_url, path

def open_url(telex_url, path): 
    with open(path, "w") as fh:
        convert_telex_url = str(telex_url)
        write = fh.write(convert_telex_url)
        return write
    

if __name__ == "__main__":
    telex_url, path = build()
    open_url(telex_url, path)