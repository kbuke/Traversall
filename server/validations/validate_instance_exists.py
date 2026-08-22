def validate_instance_exists(
        model,
        id,
        model_type
):
    exists = model.query.filter(model.id == id).first()
    if not exists:
        raise ValueError(f"{model_type}-{id} does not exist")
    return exists