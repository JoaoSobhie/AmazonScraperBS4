from bs4 import BeautifulSoup 
import re
import json

#Function to read and list all products in a page
def get_all_products():
    # Read html
    with open("pages/content.html", "r", encoding="utf8") as e_commerce_html:
        html_content = e_commerce_html.read()
    html_content=html_content.replace("\n", '').replace("\xa0",'')
    # Parse html
    soup = BeautifulSoup(html_content, "html.parser")
    #Search for the products in page
    product_elements = soup.find_all("div", {'data-component-type':"s-search-result"})
    products_list= []
    #Get  each product data and append it to the list of products
    for product in product_elements:
        body = {"name": re.sub(" +", " ", product.find("span", class_="a-size-base-plus a-color-base a-text-normal").text),
                "price":float(product.find("span", class_="a-price-whole").text.replace(',','')),#replace("\xa0","").replace("R$","").replace(",", ".")
                "best-seller": True if product.find("span", class_="a-badge-text") else False,
                "rating":float(product.find("span", class_="a-icon-alt").text.split(" de")[0].replace(',','.'))
            }
        products_list.append(body)
    #return list of products
    return products_list

#Function to apply best seller or rating filters 
def list_products(best_seller=False, rating=None):
    #Get all products
    products_list = get_all_products()
    bSeller=[]
    rating_list= []
    #Apply the filter depending on user  input
    if rating !=None:
        rating = float(rating)
        for product in products_list:
            print(product.get("rating"))
            if product.get("rating")>= rating:
                rating_list.append(product)
        if best_seller == False:
            return rating_list
        
    if  best_seller==True and rating != None:
        for product in rating_list:
            if product.get("best-seller"):
                bSeller.append(product)

        return bSeller
        
    if  best_seller == True  and rating == None :
        for product in products_list:
            if product.get("best-seller"):
                bSeller.append(product)

        return bSeller
    
    return products_list

#Function to filter by name on product List
def filter_name(best_seller=False, rating=None, name=None):
    products = list_products(best_seller=best_seller, rating=rating)
    filtered_products = []
    for product in products:
        if name in  product["name"]:
            filtered_products.append(product)
    return filtered_products