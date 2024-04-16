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
        directory_content = response.css('div.bh-directory-content.directory-movie')
        movie_list = directory_content.css('ul.bh-tab-content.row.bh-directory-movie-list.no-bullet')
        for movie_item in movie_list.css('li.large-6.medium-6.small-12.columns'):
            link = movie_item.css('a::attr(href)').get()
            yield response.follow(link, self.parse_movie_page)
    
        next_page = response.css('div.bh-pagination.clearfix.right a.page-numbers::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_movie_page(self,response):
        active_item = response.css('li.touchcarousel-item.active')
        details_link = active_item.css('::attr(href)').get()
        if details_link:
            yield response.follow(details_link, self.parse_movie_details)
    
    def parse_movie_details(self,response):
        movie_meta = response.css('div.movie-meta')

        if movie_meta:
            title = movie_meta.css('h2.entry-title.name::text').get().strip()
            release_date = movie_meta.css('h2.release-date::text').get().strip() 

        crew_wrapper = response.css('div.crew-wrapper.row')
        crew_details = {}

        if crew_wrapper:
            for crew_group in crew_wrapper.css('ul'):
                crew_title = crew_group.css('h4.entry-title.name::text').get().strip()
                crew_members = [li.css('::text').get().strip() for li in crew_group.css('li')]
                crew_details[crew_title] = crew_members

        yield {
            'title': title,
            'release_date': release_date,
            'crew_details': crew_details,
        }   

        
