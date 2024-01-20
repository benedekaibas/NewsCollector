from newspaper import Article
def main():
    urlTelex = "https://telex.hu/"
    article = Article(urlTelex)
    downloadedArticle = article.download()
    print(downloadedArticle)


    
if __name__ == "__main__":
    main()