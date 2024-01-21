import newspaper
from newspaper import Article

#TODO: Add date library
#TODO: Set the time to todays date
#TODO: After setting today's day write a function that gets news only that day



#this is to test if the program is working with websites
def main():
    telex_news = newspaper.build('http://telex.hu', language = 'hu')
    count = 0
    for article in telex_news.articles:
        if article in telex_news.articles:
            count += 1 
            if count >= 1:
                firstArticle = telex_news.articles[0]
                print(firstArticle.url)
                #newsSummary = article.summary
                #print(newsSummary)
                break



if __name__ == "__main__":
    main()
