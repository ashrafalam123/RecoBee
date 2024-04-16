import scrapy

class MovieSpider(scrapy.Spider):
    name = "movies"
    def start_requests(self):
        start_urls = [
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/A/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/B/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/C/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/D/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/E/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/F/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/G/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/H/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/I/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/J/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/K/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/L/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/M/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/N/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/O/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/P/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/Q/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/R/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/S/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/T/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/U/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/V/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/W/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/X/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/Y/",
        "https://www.bollywoodhungama.com/directory/movies-list/alphabet/Z/"
            ]

        for url in start_urls:
            yield scrapy.Request(url = url, callback= self.parse)
        
    def parse(self,response):
        
        

        
