from serialize_functions.serialize_location import serialize_location

def serialize_site(site):
    return {
        "id": site.id,
        "name": site.name,
        "img": site.img,
        "info": site.info,

        "country_id": site.country_id,

        "country": site.country.to_dict(
            rules=(
                "-sites",
                "-locations",
                "-continents.countries",
                "-languages",
            )
        ),

        "location_id": site.location_id,

        "location": serialize_location(
            site.location,
            include_country=False
        ),

        "interests": [
            interest.to_dict(
                rules=("-sites",)
            )
            for interest in site.interests
        ]
    }