# Beautiful soup demo

This repo shows a very simple use case of how to use beautiful soup to scrape a website.

It scrapes 3 websites and extracts information about the customers of the website.


## How to run

Assuming you work on a unix based system, and that you have python3 already available.
Run the following commands to create an activate a virtual environment.
```shell
python3 -m venv venv
source venv/bin/activate
```

Install the requirements with
```shell
pip3 install -r requirements.txt
```

Run the main python file with
```shell 
python3 main.py
```
The output will be in [page_customers_info.json](page_customers_info.json)


## How to run tests
```shell
python3 -m unittest discover
```