import newspaper
from newspaper import Article
from datetime import date 

#this is to test if the program is working with websites
def main():
    todaysDate = date.today()
    freshDate = date.today()
    print(f"You are reading {todaysDate}'s news")

#TODO:
#todays date is only working with us news portals but with hungarian it is just not exceeding today's
#date but it gives all the news before today's date 
    cnn_news = newspaper.build('https://cnn.com')
    fox_news = newspaper.build('https://www.foxnews.com/')
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
if __name__ == "__main__":
    main()
