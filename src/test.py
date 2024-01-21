import newspaper
from newspaper import Article
from datetime import date 


def main():
    #setting today's date so we only get the newest news
    todaysDate = date.today()
    freshDate = date.today()
    print(f"You are reading {todaysDate}'s news")

    #getting data from websites
    cnn_news = newspaper.build('https://cnn.com')
    fox_news = newspaper.build('https://www.foxnews.com/')
    #with adding memoize_articles it gives back all the articles that are found and not just the ones
    #which are published after we run the program again 
    index_news = newspaper.build('https://index.hu/', memoize_articles = False)
    telex_news = newspaper.build('https://telex.hu', memoize_articles = False)
    magyarJelen_news = newspaper.build('https://magyarjelen.hu/')
    
    #chechk how many articles there are on the website 
    numberOfArticles = cnn_news.size()
    print(numberOfArticles)

    # I am not sure if it is the most efficient and fastest way of scraping the websites so I might change it 
    if freshDate == todaysDate:
        for article in cnn_news.articles:
            firstArticle = cnn_news.articles[0]
            print(firstArticle.url)
            break
        for article in fox_news.articles:
            print(article.url)
            break
        for article in index_news.articles:
            print(article.url)
            break
        for article in magyarJelen_news.articles:
            print(article)
            break
        for article in telex_news.articles:
            print(article)
            break
if __name__ == "__main__":
    main()
