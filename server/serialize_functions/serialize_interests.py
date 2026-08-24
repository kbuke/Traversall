def serialize_interests(
    interest,
    include_sites = True
):
    data = {
        "id": interest.id,
        "name": interest.name,
        "img": interest.img,
    }

    if include_sites:
        data["sites"] = [
            {
                "id": site.id,
                "name": site.name,
                "img": site.img,
                "info": site.info
            }
            for site in interest.sites
        ]

    return data
