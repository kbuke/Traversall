from config import db

def many_to_many_fk(tablename, is_null = False):
    return db.Column(db.ForeignKey(f"{tablename}.id"), nullable = is_null)

def many_to_many_reltshp(model, relationAttribute, tablename):
    relation = db.relationship(
        model,
        back_populates = relationAttribute,
        secondary = tablename
    )
    return relation