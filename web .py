import requests
from bs4 import BeautifulSoup
import pandas
import ARGPARSE
import connect

parser = argparse.Argumentparser()
parser.add_argument("--page_num_max",help="enter the number of pages to parser",type=int)
parser.add_Argument("--dbname",help="enter the name ofdb",type=str)
args = parser.parse_args()

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num_MAX = args.page_num_max
scrapped_info_list = []
connect.connect(args.dbname)

for page_num in range(1,page_num_MAX):
    url = oyo_url + str(page_num)
    print("GET Request for: " + url)
    req = requests.get(url)
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
            hotel_dict["rating"]=none

        parent_amenties_element = hotel.find("div",{"class":"amenitywrapper"})
                                             
        amenities_list = []
        for amenity in parent_amenities_element.find_all("div",{"class":"amenitywrapper_amenity"}):
            amenities_list.append(amenity.find("span",{"class":"d-bady-sm"}).text.script())
                                             
        hotel_dict["amenties"] = ', '.join(amenties_list[:-1])
                                             
        scraped-info_list.append(hotel_dict)
        connect.insert_into_table(args.dbname, tuple(hotel_dict.values()))
       
        #print(hotel_name,hotel_address,hotel_price,hotel_rating,amenities_list)
dataframe = pandas.dataframe(scraped_info_list)
print("creating csv file...")
dataframe.to-csv("oyo.csv")
            
        
