import requests
from bs4 import BeautifulSoup
import pandas

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num_MAX = 3
scrapped_info_list = []

for page_num in range(1,page_num_MAX):
    req = requests.get(oyo_url + str(page_num))
    content = req.content
    
    soup = beautifulsoup(content,"html.parsel")

    all_hotels = soup.find_all("div" , {"class":"hotelcardlisting"})
    

    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find("h3",{"class":"listinghoteldecription_hotelname"}).text
        hotel_dict["address"] = hotel.find("span",{"itemprop":"streetaddress"}).text
        hotel_dict["price"] = hotel.find("span",{"class":"listingprice_finalprince"}).text
        #try....except
        try:
            hotel_dict["rating"]=hotel.find("span",{"class":"hotelrating_ratingsummary"}).text
        except AttributeError:
            pass

        parent_amenties_element = hotel.find("div",{"class":"amenitywrapper"})
                                             
        amenities_list = []
        for amenity in parent_amenities_element.find_all("div",{"class":"amenitywrapper_amenity"}):
            amenities_list.append(amenity.find("span",{"class":"d-bady-sm"}).text.script())
                                             
        hotel_dict["amenties"] = ', '.join(amenties_list[:-1])
                                             
        scraped-info_list.append(hotel_dict)
       
        #print(hotel_name,hotel_address,hotel_price,hotel_rating,amenities_list)
dataframe = pandas.dataframe(scraped_info_list)
dataframe.to-csv("oyo.csv")
            
        
