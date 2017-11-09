from icrawler.builtin import GoogleImageCrawler


if __name__ == '__main__':

    classes = [     ('salad', 'salad'),
                    ('pasta', 'pasta'),
                    ('hotdog', 'hotdog'),
                    ('frenchfry', 'frenchfry'),
                    ('burger', 'burger'),
                    ('apple', 'fruit apple'),
                    ('banana', 'banana'),
                    ('broccoli', 'broccoli'),
                    ('pizza', 'pizza'),
                    ('egg', 'egg'),
                    ('tomato', 'tomato'),
                    ('rice', 'rice'),
                    ('strawberry', 'strawberry'),
                    ('cookie', 'cookie')
                ]

    for class_name, keyword in classes:

        google_crawler = GoogleImageCrawler(parser_threads=4, downloader_threads=8,
                                            storage={'root_dir': './dataset/downloaded_images/' + class_name})
        google_crawler.crawl(keyword=keyword, max_num=1000,
                             date_min=None, date_max=None,
                             min_size=(200,200), max_size=(600,600))