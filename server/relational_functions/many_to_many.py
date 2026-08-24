from config import db

def many_to_many_fk(tablename, is_null=False):
    return db.Column(db.ForeignKey(f"{tablename}.id"), nullable=is_null)

def get_or_create_secondary_table(tablename, left_table, right_table):
    # Both sides of a many-to-many pair call this for the same
    # secondary table name, so reuse it on the second call rather
    # than trying to redefine it.
    if tablename in db.metadata.tables:
        return db.metadata.tables[tablename]

    return db.Table(
        tablename,
        db.metadata,
        db.Column(f"{left_table}_id", db.Integer, db.ForeignKey(f"{left_table}.id"), primary_key=True),
        db.Column(f"{right_table}_id", db.Integer, db.ForeignKey(f"{right_table}.id"), primary_key=True),
    )

def many_to_many_reltshp(model, relationAttribute, tablename, left_table, right_table):
    secondary_table = get_or_create_secondary_table(tablename, left_table, right_table)
    return db.relationship(
        model,
        back_populates=relationAttribute,
        secondary=secondary_table
    )