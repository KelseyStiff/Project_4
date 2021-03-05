from model import Park
import peewee


def save_park(name, city, state, description, latitude, longitude, image1, image2, image3):  
    park = Park(
        park_name = name, park_city = city, park_state = state, 
        park_description = description, latitude = latitude, 
        longitude = longitude, image_1 = image1, image_2 = image2, 
        image_3 = image3
        )
    park.save()


def get_park_by_name(name):
    return Park.get(park_name = name)


def get_all_parks():
    parks = Park.select()
    return parks


    


