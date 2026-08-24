def derive_country_id_on_create(
    data, 
    parent_field, 
    parent_model, 
    parent_required=True
):
    """
    Derives country_id from a parent record on creation (POST).
    - parent_field: key in `data` holding the parent's id, e.g. "parent_location_id" or "location_id"
    - parent_model: the model class to look up the parent on, e.g. OtherLocationModel
    - parent_required: if True, a missing parent_id raises rather than falling back to a client-supplied country_id
    """
    parent_id = data.get(parent_field)

    if parent_id is not None:
        parent = parent_model.query.get(parent_id)
        if not parent:
            raise ValueError(f"{parent_model.__name__} {parent_id} not found")
        data["country_id"] = parent.country_id
    elif parent_required:
        raise ValueError(f"{parent_field} is required")
    else:
        # top-level record (e.g. a state/prefecture) — country_id must be supplied directly
        if not data.get("country_id"):
            raise ValueError("A record with no parent must specify country_id")

    return data


def derive_country_id_on_update(data, parent_field, parent_model, parent_required=True):
    """
    Derives country_id from a parent record on partial update (PATCH).
    Only touches country_id if parent_field is actually present in this patch —
    leaves it untouched otherwise, and strips any client-supplied country_id
    so it can never be set independently of the parent chain.
    """
    if parent_field in data:
        parent_id = data[parent_field]

        if parent_id is not None:
            parent = parent_model.query.get(parent_id)
            if not parent:
                raise ValueError(f"{parent_model.__name__} {parent_id} not found")
            data["country_id"] = parent.country_id
        else:
            if parent_required:
                raise ValueError(f"{parent_field} cannot be unset")
            if not data.get("country_id"):
                raise ValueError(f"Removing {parent_field} requires specifying country_id")
    else:
        # not touching the parent in this patch — never let country_id change independently
        data.pop("country_id", None)

    return data