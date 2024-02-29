"""This file is for downloading news articles and then collect them in a json or txt file."""

import newspaper
from newspaper import Article
from datetime import date 

def build():
    telex = newspaper.build('http://telex.hu')
    path = 'news_articles.txt'  
    with open(path, "w") as fh:
        convert_telex = str(telex)
        write = fh.write(convert_telex)
    return write
    

if __name__ == "__main__":
    build()
