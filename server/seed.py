from datetime import date

from models.LocationModels.ContinentModel import ContinentModel
from models.LocationModels.CountryModel import CountryModel
from models.LocationModels.OtherLocationModel import OtherLocationModel

from models.CountryMedia.FilmTvModel import FilmTvModel
from models.CountryMedia.SongModel import SongModel

from models.UserModels.BaseUserModel import BaseUserModel
from models.UserModels.BaseBusinessModel import BaseBusinessModel

from models.SiteModel import SiteModel

from models.WishlistModels.WishlistItemModel import WishlistItemModel

from models.InterestModel import InterestModel

from models.LanguagesModel import LanguagesModel

from models.CountryEvents.NotableEventsModel import NotableEventModel

from models.CountryPeople import PeopleModel

from app import app
from config import db

def get_instances_by_name(model):
    return {
        instance.name: instance
        for instance in model.query.all()
    }

def seed_many_to_many_rltshp(
    relation_model,
    seeded_examples,
    relation_attribute,
    instance_model,
    relation_type,
    new_instance_type
):
    relation_instances = get_instances_by_name(relation_model)

    instances_list = []

    for data in seeded_examples:

        relation_names = data.pop(relation_attribute)

        instance = instance_model(**data)

        for relation_name in relation_names:

            relation = relation_instances.get(relation_name)

            if not relation:
                raise ValueError(
                    f"{relation_type} '{relation_name}' not found"
                )

            getattr(instance, relation_attribute).append(relation)

        instances_list.append(instance)

    db.session.add_all(instances_list)
    db.session.commit()

    print(f"Seeded {len(instances_list)} {new_instance_type}")


#------------------------- CONTINENTS -------------------------
CONTINENTS = [
    {
        "name": "Asia",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT14ZXSewVdUnhHlDbrtdfzRWJJQrVx8ax8MUSPSxsvYGqNzapyY2k4VNo&s=10",
        "location_type": "Continent",
        "info": "Asia is the largest continent in the world"
    },

    {
        "name": "Africa",
        "img": "https://m.media-amazon.com/images/I/71hi1R1G3EL._AC_UF1000,1000_QL80_.jpg",
        "location_type": "Continent",
        "info": "Africa is the second largest continent in the world."
    },

    {
        "name": "North America",
        "img": "https://images.trvl-media.com/place/31/2311a76e-17ea-43c6-a997-7d8702bef072.jpg",
        "location_type": "Continent",
        "info": "North America is very big"
    }
]

def seed_continents():
    continents = [ContinentModel(**data) for data in CONTINENTS]
    db.session.add_all(continents)
    db.session.commit()
    print(f"Seeded {len(continents)} continents")

#------------------------- COUNTRIES -------------------------
COUNTRIES = [
    {
        "name": "Japan",
        "img": "https://www.lot.com/content/dam/lot/lot-com/destination-photos/japonia/Tokyo-5%20.coreimg.jpg/1723628368208/Tokyo-5%20.jpg",
        "location_type":"Country",
        "info": "My fave country",
        "native_name": "にほん",
        "native_pronounciation": "Nihon",
        "population": 122_300_000,
        "passport_img": "https://kaan-buke.imgbb.com/?page=3&seek=gTrhmTn",
        "safety_level": "Very Safe",

        "continents": ["Asia"]
    },

    {
        "name": "South Africa",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdUyT3bShbkD50NgLvNCMlSSB9URQhCZ8ZCWJrHAByvnehRNhk4OapbWkf&s=10",
        "location_type":"Country",
        "info": "The country i live in",
        "population": 63_520_000,
        "passport_img": "https://i.ibb.co/s6zQGhQ/South-Africa.png",
        "safety_level": "Caution",

        "continents": ["Africa"]
    },

    {
        "name": "United States of America",
        "img": "https://www.flamingotravels.co.in/blog/wp-content/uploads/2023/01/Feture-image.jpg",
        "location_type":"Country",
        "info": "Yawn",
        "population": 349_000_000,
        "passport_img": "https://i.ibb.co/9471js6/USA.png",
        "safety_level": "Caution",

        "continents": ["North America"]
    },

    {
        "name": "Democratic People's Republic of Korea",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTT_WRrVHflMQq5msl4d0Kyrbr6obO9pQUu8oyvXbozBeCzoNtfIWpY6r4&s=10",
        "location_type":"Country",
        "info": "Craze Place",
        "population": 26_650_000,
        "passport_img": "https://i.ibb.co/6twT2HC/Poland.png",
        "safety_level": "Dangerous",

        "continents": ["Asia"]
    },
]

def seed_countries():
    seed_many_to_many_rltshp(
        ContinentModel,
        COUNTRIES,
        "continents",
        CountryModel,
        "Continent",
        "countries"
    )

#------------------------- OTHER LOCATIONS -------------------------
OTHER_LOCATIONS = [
    {
        "name": "Hiroshima",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGgeZNyiND9NKrS6_H7pxh9YdirRNg9WhCpu_mAEgRA5sJLvlwJQ5Ko9c&s=10",
        "location_type": "Prefecture",
        "info": "A beautiful city that is recovering from the Atomic Bomb",
        "admin_level": 1,
        "country_id": 1
    },

    {
        "name": "Hiroshima",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSGgeZNyiND9NKrS6_H7pxh9YdirRNg9WhCpu_mAEgRA5sJLvlwJQ5Ko9c&s=10",
        "location_type": "City",
        "info": "A beautiful city that is recovering from the Atomic Bomb",
        "admin_level": 2,
        "country_id": 1,
        "parent_location_id": 1
    },

    {
        "name": "Western Cape",
        "img": "https://velvetescape.com/wp-content/uploads/2022/02/IMG_5340-1-1-1280x920.jpeg",
        "location_type": "Province",
        "info": "A beautiful province in South Africa",
        "admin_level": 1,
        "country_id": 2
    },

    {
        "name": "Cape Town",
        "img": "https://www.outlooktravelmag.com/media/Western-Cape-Landscape-Share-Image-png-webp.webp",
        "location_type": "City",
        "info": "Great vineyards",
        "admin_level": 2,
        "country_id": 2,
        "parent_location_id": 3
    },
]

def seed_locations():
    locations = [OtherLocationModel(**data) for data in OTHER_LOCATIONS]
    db.session.add_all(locations)
    db.session.commit()
    print(f"Seeded {len(locations)} locations")

#------------------------- MEDIA -------------------------
FILMS = [
    {
        "name": "Grave of the Fireflies",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCIe1eRWYIxv03Fihgf-9Jd9iNzpeGXew2lMc7OhKtZQ&s=10",
        "year": 1988,
        "info": "A brother and sister trying to survive the end of World War 2",
        "run_time": 88,
        "film_category": "Movie",

        "countries": ["Japan"]
    }
]

def seed_films():
    seed_many_to_many_rltshp(
        CountryModel,
        FILMS,
        "countries",
        FilmTvModel,
        "Country",
        "films"
    )

SONGS = [
    {
        "name": "House of the Rising Son",
        "img": "https://upload.wikimedia.org/wikipedia/en/thumb/a/a8/Rising_sun_animals_US.jpg/250px-Rising_sun_animals_US.jpg?utm_source=en.wikipedia.org&utm_campaign=parser&utm_content=thumbnail",
        "year": 1964,
        "info": "An American classic",
        "length": 4.29,
        "artist": "The Animals",

        "countries": ["United States of America"]
    }
]

def seed_songs():
    seed_many_to_many_rltshp(
        CountryModel,
        SONGS,
        "countries",
        SongModel,
        "Country",
        "songs"
    )

        

#------------------------- Users -------------------------
USERS = [
    {
        "name": "Kaan Buke"
    },

    {
        "name": "Zahra Hirji"
    },

    {
        "name": "Louis"
    }
]

def seed_users():
    users = [BaseUserModel(**data) for data in USERS]
    db.session.add_all(users)
    db.session.commit()
    print(f"Seeded {len(users)} users")

#------------------------- BUSINESSES -------------------------
BUSINESSES = [
    {
        "name": "Hiroshima Pancake House",
        "location_id": 2,
        "country_id": 1
    }
]

def seed_businesses():
    businesses = [BaseBusinessModel(**data) for data in BUSINESSES]
    db.session.add_all(businesses)
    db.session.commit()
    print(f"Seeded {len(businesses)} businesses")


#------------------------- WISHLIST ITEMS -------------------------
WISHLIST_ITEMS = [
    {
        "wishlist_id": 1,
        "business_id": 1
    },

    {
        "wishlist_id": 2,
        "site_id": 1
    },

    {
        "wishlist_id": 3,
        "country_id": 3
    }
]

def seed_wishlist_items():
    wishlist_items = [WishlistItemModel(**data) for data in WISHLIST_ITEMS]
    db.session.add_all(wishlist_items)
    db.session.commit()
    print(f"Seeded {len(wishlist_items)} wishlisted items")

#------------------------- INTERESTS -------------------------
INTERESTS = [
    {
        "name": "History",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMt3r8ryRN6j-LKIcKLfhqZfvd3vlasv72WqZJ-iHvGw&s=10"
    },

    {
        "name": "Culture",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTucRenx8q4Z2wOFahgmCWVqTsX9t0xRzDMMp2_-_i3KWU7rcvYDLuNB_2o&s=10"
    },

    {
        "name": "Food",
        "img": "https://media.cnn.com/api/v1/images/stellar/prod/gettyimages-1273516682.jpg?c=original"
    }
]

def seed_interests():
    interests = [InterestModel(**data) for data in INTERESTS]
    db.session.add_all(interests)
    db.session.commit()
    print(f"Seeded {len(interests)} interests")

#------------------------- LANGUAGES -------------------------
LANGUAGES = [
    {
        "name": "English",

        "countries": ["United States of America", "South Africa"]
    },

    {
        "name": "Japanese",

        "countries": ["Japan"]
    },

    {
        "name": "Zulu",

        "countries": ["South Africa"]
    }
]
def seed_languages():
    seed_many_to_many_rltshp(
        CountryModel,
        LANGUAGES,
        "countries",
        LanguagesModel,
        "Country",
        "languages"
    )

#------------------------- SITES -------------------------
SITES = [
    {
        "name": "Hiroshima Atomic Dome",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRhhL1BRbQWdX7aaB5iKipdGTOqa7LBs3hQjB3jW3c3vA&s=10",
        "info": "Where the bomb was dropped",
        "location_id": 1,
        "country_id": 1,

        "interests": ["History"]
    }
]

def seed_sites():
    seed_many_to_many_rltshp(
        InterestModel,
        SITES,
        "interests",
        SiteModel,
        "Interest",
        "sites"
    )

#------------------------- NOTABLE EVENTS -------------------------
NOTABLE_EVENTS = [
    {
        "name": "World War 2",
        "img": "https://res.cloudinary.com/aenetworks/image/upload/c_fill,w_1200,h_630,g_auto/dpr_auto/f_auto/q_auto:eco/v1/wwii-battles-gettyimages-538297253",
        "start_date": date(1939, 9, 1),
        "end_date": date(1945, 9, 2),
        "info": "The bloodiest conflict in human history",

        "countries_involved": ["United States of America", "Japan"]
    },

    {
        "name": "Hiroshima: Atomic Bomb",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXQaOIPsJJMc-g1P_iHPOEtOyazP0DnpP_etPm4VNQwrcnMJ96ss9jDlA&s=10",
        "start_date": date(1945, 8, 6),
        "end_date": date(1945, 8, 6),
        "info": "The bloodiest conflict in human history",
        "location_id": 1,
        "parent_event_id": 1,

        "countries_involved": ["United States of America", "Japan"]
    }
]

def seed_notable_events():
    seed_many_to_many_rltshp(
        CountryModel,
        NOTABLE_EVENTS,
        "countries_involved",
        NotableEventModel,
        "Country",
        "notable-event"
    )

#-------------------------  -------------------------

#-------------------------  -------------------------

#-------------------------  -------------------------

#-------------------------  -------------------------

#-------------------------  -------------------------

#-------------------------  -------------------------

#-------------------------  -------------------------

#-------------------------  -------------------------

#-------------------------  -------------------------

#-------------------------  -------------------------

#-------------------------  -------------------------

#-------------------------  -------------------------

#-------------------------  -------------------------


if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        seed_continents()
        seed_countries()
        seed_locations()
        seed_films()
        seed_songs()
        seed_users()
        seed_businesses()
        seed_wishlist_items()
        seed_interests()
        seed_languages()
        seed_sites()
        seed_notable_events()