n_crawler = NaverCrawler()
d_crawler = DaumCrawler()
crawlers = [n_crawler, d_crawler]
news = []
for cralwer in cralwers:
    news.append(cralwer.do_crawling())
    