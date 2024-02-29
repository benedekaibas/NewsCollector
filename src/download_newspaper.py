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
            for url in telex_url:
                fh.write(f"{url}\n")  

    def read_file(self):
        with open(self.file_path, "r") as fh:
            lines = fh.readlines()
            return lines

    def split_lines_in_file(self):
        lines = self.read_file()
        split_urls = []
        for line in lines:
            split = line.strip()
            split_urls.append(split)
        return split_urls

    def process_urls(self):
        telex_url = self.build()
        self.open_url(telex_url)
        split_urls = self.split_lines_in_file()

        for url in split_urls:
            return url



if __name__ == "__main__":
    url = 'http://telex.hu'
    file_path = 'news_articles.txt'

    news_builder = NewsArticleBuilder(url, file_path)
    news_builder.process_urls()
