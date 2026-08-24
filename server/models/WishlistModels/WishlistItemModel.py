from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

from config import db

from relational_functions.one_to_many import (
    one_to_many_back_populates,
    one_to_many_fk
)

from relational_functions.many_to_many import many_to_many_reltshp


class WishlistItemModel(db.Model, SerializerMixin):
    __tablename__ = "wishlist_items"

    id = db.Column(db.Integer, primary_key=True)

    # --------------------------------------------------
    # WISHLIST
    # --------------------------------------------------

    wishlist_id = one_to_many_fk("wishlists")

    wishlist = one_to_many_back_populates(
        "WishlistModel",
        "items",
        delete_orphan=False
    )

    # --------------------------------------------------
    # POSSIBLE WISHLIST TARGETS
    # --------------------------------------------------

    continent_id = one_to_many_fk(
        "continents",
        is_null=True
    )

    country_id = one_to_many_fk(
        "countries",
        is_null=True
    )

    location_id = one_to_many_fk(
        "other_locations",
        is_null=True
    )

    site_id = one_to_many_fk(
        "sites",
        is_null=True
    )

    business_id = one_to_many_fk(
        "businesses",
        is_null=True
    )

    # --------------------------------------------------
    # RELATIONSHIPS
    # --------------------------------------------------

    continent = one_to_many_back_populates(
        "ContinentModel",
        "wishlist_items",
        delete_orphan=False
    )

    country = one_to_many_back_populates(
        "CountryModel",
        "wishlist_items",
        delete_orphan=False
    )

    location = one_to_many_back_populates(
        "OtherLocationModel",
        "wishlist_items",
        delete_orphan=False
    )

    site = one_to_many_back_populates(
        "SiteModel",
        "wishlist_items",
        delete_orphan=False
    )

    business = one_to_many_back_populates(
        "BaseBusinessModel",
        "wishlist_items",
        delete_orphan=False
    )

    # --------------------------------------------------
    # TAGS
    # --------------------------------------------------

    tags = many_to_many_reltshp(
        "TagModel",
        "wishlist_items",
        "wishlist_items_tags",
        left_table="wishlist_items",
        right_table="tags"
    )

    # --------------------------------------------------
    # SERIALIZATION
    # --------------------------------------------------

    serialize_rules = (
        "-wishlist.items",
        "-continent.wishlist_items",
        "-country.wishlist_items",
        "-location.wishlist_items",
        "-site.wishlist_items",
        "-business.wishlist_items",
        "-tags.wishlist_items",
    )

    # --------------------------------------------------
    # HELPER: WHAT WAS ADDED TO THE WISHLIST?
    # --------------------------------------------------

    @property
    def item(self):

        if self.site_id:
            return self.site

        if self.business_id:
            return self.business

        if self.location_id:
            return self.location

        if self.country_id:
            return self.country

        if self.continent_id:
            return self.continent

        return None

    # --------------------------------------------------
    # ENSURE ONLY ONE TARGET TYPE
    # --------------------------------------------------

    @validates(
        "continent_id",
        "country_id",
        "location_id",
        "site_id",
        "business_id"
    )
    def validate_exclusive_arc(self, key, value):

        others = {
            "continent_id",
            "country_id",
            "location_id",
            "site_id",
            "business_id"
        } - {key}

        if value is not None:
            for other in others:

                if getattr(self, other) is not None:
                    raise ValueError(
                        "A wishlist item can only reference one type of thing"
                    )

        return value

    # --------------------------------------------------
    # CREATE WISHLIST ITEM
    # --------------------------------------------------

    @classmethod
    def create(cls, wishlist, **kwargs):

        item = cls(
            wishlist=wishlist,
            **kwargs
        )

        db.session.add(item)

        if item.site_id:
            from models.SiteModel import SiteModel

            target = SiteModel.query.get(item.site_id)

        elif item.business_id:
            from models.UserModels.BaseBusinessModel import BaseBusinessModel
            # from models.BusinessModels.BaseBusinessModel import BaseBusinessModel

            target = BaseBusinessModel.query.get(item.business_id)

        elif item.location_id:
            from models.LocationModels.OtherLocationModel import OtherLocationModel

            target = OtherLocationModel.query.get(item.location_id)

        elif item.country_id:
            from models.LocationModels.CountryModel import CountryModel

            target = CountryModel.query.get(item.country_id)

        elif item.continent_id:
            from models.LocationModels.ContinentModel import ContinentModel

            target = ContinentModel.query.get(item.continent_id)

        else:
            target = None

        if target is None:
            raise ValueError(
                "Wishlist item must reference a valid item"
            )

        item.tags = item._build_tags(target)

        return item

    # --------------------------------------------------
    # BUILD TAGS
    # --------------------------------------------------

    def _build_tags(self, target):

        print("SITE ID:", self.site_id)
        print("SITE:", self.site)
        print("COUNTRY:", self.country)
        print("LOCATION:", self.location)
        print("CONTINENT:", self.continent)

        print("TARGET:", target)

        tags = []

        # --------------------------------------------------
        # SITE / BUSINESS
        # --------------------------------------------------

        if self.site_id or self.business_id:

            # Example:
            #
            # Ayaka Bamboo Forest
            #       ↓
            # Kyoto
            #       ↓
            # Japan
            #       ↓
            # Asia

            if target.location and target.country:

                tags += self._location_chain_tags(
                    target.location,
                    target.country
                )

            # Add interests
            if hasattr(target, "interests"):

                tags += [
                    self._get_or_create(
                        interest.name,
                        "interest"
                    )
                    for interest in target.interests
                ]

            # Add business type
            if hasattr(target, "business_type"):

                tags.append(
                    self._get_or_create(
                        target.business_type,
                        "business-type"
                    )
                )

        # --------------------------------------------------
        # OTHER LOCATION
        # --------------------------------------------------

        elif self.location_id:

            tags += self._location_chain_tags(
                target,
                target.country
            )

        # --------------------------------------------------
        # COUNTRY
        # --------------------------------------------------

        elif self.country_id:

            tags += self._location_chain_tags(
                None,
                target
            )

        # --------------------------------------------------
        # CONTINENT
        # --------------------------------------------------

        elif self.continent_id:

            tags.append(
                self._get_or_create(
                    target.name,
                    "location",
                    location_type="Continent",
                    hierarchy_level=0
                )
            )

        # --------------------------------------------------
        # REMOVE DUPLICATES
        # --------------------------------------------------

        seen = set()
        unique_tags = []

        for tag in tags:

            key = (
                tag.name,
                tag.tag_type
            )

            if key not in seen:

                seen.add(key)
                unique_tags.append(tag)

        print(
            "GENERATED TAGS:",
            [
                (tag.name, tag.tag_type)
                for tag in unique_tags
            ]
        )

        return unique_tags

    # --------------------------------------------------
    # LOCATION → COUNTRY → CONTINENT TAGS
    # --------------------------------------------------

    def _location_chain_tags(
        self,
        other_location,
        country
    ):

        tags = []

        # --------------------------------------------------
        # CONTINENT + COUNTRY
        # --------------------------------------------------

        if country:

            for continent in country.continents:

                tags.append(
                    self._get_or_create(
                        continent.name,
                        "location",
                        location_type="Continent",
                        hierarchy_level=0
                    )
                )

            tags.append(
                self._get_or_create(
                    country.name,
                    "location",
                    location_type="Country",
                    hierarchy_level=1
                )
            )

        # --------------------------------------------------
        # LOCATION HIERARCHY
        # --------------------------------------------------

        chain = []

        node = other_location

        while node is not None:

            chain.append(node)

            node = node.parent_location

        # Reverse so we get:

        # Continent
        # Country
        # Prefecture
        # City
        # Ward

        for loc in reversed(chain):

            tags.append(
                self._get_or_create(
                    loc.name,
                    "location",
                    location_type=loc.location_type,
                    hierarchy_level=2 + loc.admin_level
                )
            )

        return tags

    # --------------------------------------------------
    # GET EXISTING TAG OR CREATE ONE
    # --------------------------------------------------

    @staticmethod
    def _get_or_create(
        name,
        tag_type,
        **extra
    ):

        from models.WishlistModels.TagModel import TagModel

        tag = TagModel.query.filter_by(
            name=name,
            tag_type=tag_type
        ).first()

        if not tag:

            tag = TagModel(
                name=name,
                tag_type=tag_type,
                **extra
            )

            db.session.add(tag)

        return tag