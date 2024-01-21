import newspaper
from newspaper import Article
from datetime import date 

#this is to test if the program is working with websites
def main():
    todaysDate = date.today()
    freshDate = date.today()
    print(f"You are reading {todaysDate}'s news")


    cnn_news = newspaper.build('https://cnn.com')
    fox_news = newspaper.build('https://www.foxnews.com/')
    #with adding memoize_articles it gives back all the articles that are found and not just the ones
    #which are published after we run the program again 
    index_news = newspaper.build('https://index.hu/', memoize_articles = False)
    magyarJelen_news = newspaper.build('https://magyarjelen.hu/')
    #chechk how many articles there are on the website 
    numberOfArticles = cnn_news.size()
    print(numberOfArticles)
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
         
if __name__ == "__main__":
    main()
