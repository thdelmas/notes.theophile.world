#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import re

def get_amazon_search_results(search_query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    
    # Format the search URL
    search_url = f"https://www.amazon.com/s?k={search_query.replace(' ', '+')}"
    
    # Make a request to get the search results page
    response = requests.get(search_url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve the search results")
        return None
    
    return response.text

def parse_search_results(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all product containers in the search results
    products = soup.find_all('div', {'data-component-type': 's-search-result'})
    
    product_list = []
    for product in products:
        # Extract product title
        title = product.h2.text.strip()
        
        # Extract product URL
        link = product.h2.a['href']
        full_link = f"https://www.amazon.com{link}"
        
        # Extract number of reviews (used as a proxy for "most sold")
        reviews = product.find('span', {'class': 'a-size-base'}).text
        reviews = int(re.sub(r'[^\d]', '', reviews)) if reviews else 0
        
        product_list.append((title, full_link, reviews))
    
    return product_list

def get_most_sold_product(product_list):
    if not product_list:
        return None
    
    # Find the product with the highest number of reviews
    most_sold_product = max(product_list, key=lambda x: x[2])
    return most_sold_product

def main():
    search_query = input("Enter the search query: ")
    
    html_content = get_amazon_search_results(search_query)
    if not html_content:
        return
    
    product_list = parse_search_results(html_content)
    most_sold_product = get_most_sold_product(product_list)
    
    if most_sold_product:
        print(f"Most sold product: {most_sold_product[0]}")
        print(f"Link: {most_sold_product[1]}")
    else:
        print("No products found")

if __name__ == "__main__":
    main()

