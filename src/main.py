import newspaper
from newspaper import Article
from datetime import date 
#TODO: Add date library
#TODO: Set the time to todays date
#TODO: After setting today's day write a function that gets news only that day



#this is to test if the program is working with websites
import newspaper
from newspaper import Article
from datetime import date 

#this is to test if the program is working with websites
def main():
    todaysDate = date.today()
    freshDate = date.today()
    print(todaysDate)

    telex_news = newspaper.build('https://cnn.com')
    if freshDate == todaysDate:
        for article in telex_news.articles:
            firstArticle = telex_news.articles[0]
            print(firstArticle.url)

if __name__ == "__main__":
    main()

