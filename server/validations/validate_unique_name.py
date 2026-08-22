def validate_unique_name(value, model, model_type):
    exists = model.query.filter(model.name == value).first()
    if exists:
        raise ValueError(f"{value} is an already registered {model_type}")
    return value