"""This file is for downloading news articles and then collect them in a json or txt file."""

import newspaper
from newspaper import Article
from datetime import date 

class NewsArticleBuilder:
    def __init__(self, url, file_path):
        self.url = url
        self.file_path = file_path

    def build(self):
        telex = newspaper.build(self.url)
        telex_url = telex.article_urls()
        return telex_url

    def open_url(self, telex_url):
        with open(self.file_path, "w") as fh:
            convert_telex_url = str(telex_url)
            write = fh.write(convert_telex_url)
            return write
    def read_file(self):
        with open(self.file_path, "r") as fh:
            lines = fh.readlines()
            return lines

    def split_lines_in_file(self):
        lines = self.read_file()
        for line in lines:
            split = line.split(",")
            return split

if __name__ == "__main__":
    url = 'http://telex.hu'
    file_path = 'news_articles.txt'

    news_builder = NewsArticleBuilder(url, file_path)

    telex_url = news_builder.build()
    news_builder.open_url(telex_url)
    news_builder.split_lines_in_file()
