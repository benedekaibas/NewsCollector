import newspaper

#this is to test if the program is working with websites
def main():
    telex_news = newspaper.build('http://telex.hu')
    count = 0
    for article in telex_news.articles:
        if article in telex_news.articles:
            count =+ 1 
            if count >= 1:
                firstArticle = telex_news.articles[0]
                print(firstArticle.url)
                break

if __name__ == "__main__":
    main()
