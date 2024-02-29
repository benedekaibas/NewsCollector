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
    
def format_txt_file(write):
    write_to_str = str(write)
    split_lines = write_to_str.splitlines(",")
    return split_lines

if __name__ == "__main__":
    telex_url, path = build()
    write = open_url(telex_url, path)
    open_url(telex_url, path)
    format_txt_file(write)
