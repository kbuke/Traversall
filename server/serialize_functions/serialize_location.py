def serialize_location(
    location,
    include_country=False,
    include_sites=True,
    include_parent=True,
    include_children=True
):
    if not location:
        return None

    data = {
        "id": location.id,
        "name": location.name,
        "slug": location.slug,
        "img": location.img,
        "location_type": location.location_type,
        "admin_level": location.admin_level,
        "country_id": location.country_id,
        "parent_location_id": location.parent_location_id,
    }

    if include_parent:
        data["parent_location"] = serialize_location(
            location.parent_location,
            include_country=False,
            include_sites=False,
            include_parent=True,
            include_children=False
        )

    if include_children:
        data["child_locations"] = [
            serialize_location(
                child,
                include_country=False,
                include_sites=include_sites,
                include_parent=False,
                include_children=True
            )
            for child in location.child_locations
        ]

    if include_sites:
        data["sites"] = [
            {
                "id": site.id,
                "name": site.name,
                "img": site.img,
                "info": site.info,
            }
            for site in location.sites
        ]

    if include_country:
        data["country"] = location.country.to_dict(
            rules=(
                "-sites",
                "-locations",
                "-continents",
                "-languages",
            )
        )

    return data