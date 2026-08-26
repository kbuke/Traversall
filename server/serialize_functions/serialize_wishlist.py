def serialize_site_for_wishlist(site):
    return {
        "id": site.id,
        "name": site.name,
        "img": site.img,
        "info": site.info
    }


def serialize_country_for_wishlist(country):
    return {
        "id": country.id,
        "name": country.name
    }


def serialize_location_for_wishlist(location):
    return {
        "id": location.id,
        "name": location.name,
        "location_type": location.location_type
    }


def serialize_continent_for_wishlist(continent):
    return {
        "id": continent.id,
        "name": continent.name
    }


def serialize_business_for_wishlist(business):
    return {
        "id": business.id,
        "name": business.name
    }


def serialize_wishlist_item(item):

    data = {
        "id": item.id,

        "tags": [
            {
                "id": tag.id,
                "name": tag.name,
                "slug": tag.slug,
                "tag_type": tag.tag_type,
                "location_type": tag.location_type,
                "hierarchy_level": tag.hierarchy_level
            }
            for tag in item.tags
        ]
    }

    if item.site_id:
        data["site"] = serialize_site_for_wishlist(item.site)

    elif item.country_id:
        data["country"] = serialize_country_for_wishlist(item.country)

    elif item.location_id:
        data["location"] = serialize_location_for_wishlist(item.location)

    elif item.continent_id:
        data["continent"] = serialize_continent_for_wishlist(item.continent)

    elif item.business_id:
        data["business"] = serialize_business_for_wishlist(item.business)

    return data


def serialize_wishlist(wishlist):

    return {
        "id": wishlist.id,
        "user_id": wishlist.user_id,
        "items": [
            serialize_wishlist_item(item)
            for item in wishlist.items
        ]
    }


def serialize_user(user):

    return {
        "id": user.id,
        "name": user.name,
        "wishlist": [
            serialize_wishlist(wishlist)
            for wishlist in user.wishlist
        ]
    }