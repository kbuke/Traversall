from config import db

def one_to_many_fk(tablename, is_null = False):
    return db.Column(db.Integer, db.ForeignKey(f"{tablename}.id"), nullable = is_null)

def one_to_many_back_populates(model, bp_reference, delete_orphan = True):
    return db.relationship(
        model,
        back_populates = bp_reference,
        cascade = "all, delete-orphan" if delete_orphan == True else None
    )