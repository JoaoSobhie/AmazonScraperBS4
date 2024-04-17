from fastapi import FastAPI
from controllers import main
app = FastAPI()

##List of endpoints

#List all products without any filter 
@app.get('/list_all_products')
def list_products():
    return main.get_all_products()

#Filter products by name. Can be only one product or multiple, depending  on the user input. You can apply the filters on the searching products too. 
#Set best_seller as false and leave rating empty if want to use only search by name 
@app.get('/find_by_name')
def find_by_name(name:str,rating: float | None=None, best_seller:bool=False):
    return main.filter_name(best_seller, rating, name=name)

#Filter by rating 
@app.get('/filter_by_rating')
def filter_by_rating(rating:float):
    return main.list_products(rating=rating)

#Filter best seller products. It's a bool. Will bring a json with only best sellers if true
@app.get('/best_sellers')
def best_sellers(best_seller:bool):
    return main.list_products(best_seller=best_seller)

#List of products with all options. Can List all products and  add filters at once 
@app.get('/best_sellers&rating')
def filter_by_rating_best_sellers(best_seller:bool, rating:float):
    return main.list_products(best_seller=best_seller, rating=rating)

