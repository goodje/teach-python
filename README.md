# Teach People Python from Scratch

## Starts with a SRX Scraper
[scraper_srx_sg_condo_directory.py](scraper_srx_sg_condo_directory.py)

## Install Python
Check [docs/installation.md](docs/python_setup.md)

## Concept
* Python syntax
    * Basic operations
    * Condition
    * Loop
        * for..loop
        * while..loop
    * Function


## Scraper Concept
* **HTML**
* CSS
* Javascript
* Network
    * HTTP
        * **Request**
            * **Method**
                * GET
                * POST
            * URL
                * https://www.google.com/search?q=99.co
                * Protocol: https
                * Domain: www.google.com
                * Path: /search
                * Parameters: q=99.co
        * **Response**
        * Payload
            * Header
            * Body
    * TCP
* API
    * Endpoint
    * Format
        * **JSON**
        * XML

## Toolset
* [PyCharm Community](https://www.jetbrains.com/pycharm/download/#section=mac) (IDE)
* python 3 (Python code interpreter)

## HTML Fundamentals
```html
<html>
  <head>
    <title>Title</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <div id="header"></div>
    <div id="main">
      <div id="content">
        <ul>
          <li>Item 1</li>
          <li>Item 2</li>
        </ul>
      </div>
      <div id="sidebar"></div>
    </div>
    <div id="footer"></div>
  <script type="text/javascript" src="script.js"></script>
  </body>
</html>
```

## Exercise
* Scrap a webpage and save result in PostgreSQL
* Write an API to save a customer's infomation

## Reference
* [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Python Official Documentation](https://docs.python.org/3/)
* [Python Official Tutorial](https://docs.python.org/3/tutorial/)
* [Jupyter(interactive Python shell)](https://jupyter.org/)
* [Requests](https://requests.readthedocs.io/en/master/)