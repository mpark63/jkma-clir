## goal
Scrape journal articles from jkma 

#### scrapy installation 
`conda install -c conda-forge scrapy`
#### running custom spider 
`python downFiles/spiders/jkma.py`

### How it works 
JkmaSpider visits jkma.org and looks for buttons that allow you to download journal articles. It collects a list of pdf urls and downlaods them in bulk. Configures `scrapy.pipelines.files.FilesPipeline` in settings.py. 
For more information see https://www.geeksforgeeks.org/how-to-download-files-with-scrapy/
