from sqlalchemy import event
from config import db 
from models.UserModels.BaseUserModel import BaseUserModel
from models.WishlistModels.WishlistModel import WishlistModel

@event.listens_for(BaseUserModel, "after_insert")
def create_wishlist_for_user(
    mapper,
    connection,
    target
):
    connection.execute(
        WishlistModel.__table__.insert(),
        {"user_id": target.id}
    )