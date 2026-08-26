from serialize_functions.serialize_location import serialize_location

def serialize_business(business):
    return {
        "id": business.id,
        "name": business.name,
        "country_id": business.country_id,
        "country": business.country.to_dict(
            rules=(
                "-sites",
                "-locations",
                "-continents.countries",
                "-languages",
            )
        ),

        "location_id": business.location_id,

        "location": serialize_location(
            business.location,
            include_country=False
        ),
    }