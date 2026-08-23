from config import db

def one_to_many_fk(tablename, is_null = False):
    return db.Column(db.Integer, db.ForeignKey(f"{tablename}.id"), nullable = is_null)

def one_to_many_back_populates(
        model, 
        bp_reference, 
        delete_orphan = True,
        remote_side = None 
    ):
    return db.relationship(
        model,
        back_populates = bp_reference,
        remote_side = remote_side,
        cascade = "all, delete-orphan" if delete_orphan == True else None
    )

# remote-side
#   in normal relational tables we can tell which is the one, and which is the many 
#   in cases of self referential (other locations) this is harder to distinguish 
#   we use remote-side as when it follows (parent_location) it treates the row whose id matches the FK as the one side