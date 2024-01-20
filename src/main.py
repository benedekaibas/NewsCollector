import newspaper

#this is to test if the program is working with websites
def main():
    telex_news = newspaper.build('http://telex.hu')
    for article in telex_news.articles:
        print(article.url)


if __name__ == "__main__":
    main()