from uuid import UUID

from debikepy.utils import *
from debikepy.endpoints.location import Location

class Profile:
    id: int
    username: UUID
    name: str
    display_name: str
    first_name: None
    last_name: None
    initials: None
    avatar_url: str
    address: None
    city: None
    country: str
    postal_code: None
    house_number: None
    house_number_addition: None
    phone_number: None
    phone_number_formatted: None
    gender: None
    is_email_verified: bool
    creation_date: str
    timezone: str
    location: Location
    registered_on_platform: None
    privacy_statement_accepted_on: str
    email: str
    conneqtech_id: UUID
    is_demo_account: bool
    permissions: List[Any]

    def __init__(self, id: int, username: UUID, name: str, display_name: str, first_name: None, last_name: None, initials: None, avatar_url: str, address: None, city: None, country: str, postal_code: None, house_number: None, house_number_addition: None, phone_number: None, phone_number_formatted: None, gender: None, is_email_verified: bool, creation_date: str, timezone: str, location: Location, registered_on_platform: None, privacy_statement_accepted_on: str, email: str, conneqtech_id: UUID, is_demo_account: bool, permissions: List[Any]) -> None:
        self.id = id
        self.username = username
        self.name = name
        self.display_name = display_name
        self.first_name = first_name
        self.last_name = last_name
        self.initials = initials
        self.avatar_url = avatar_url
        self.address = address
        self.city = city
        self.country = country
        self.postal_code = postal_code
        self.house_number = house_number
        self.house_number_addition = house_number_addition
        self.phone_number = phone_number
        self.phone_number_formatted = phone_number_formatted
        self.gender = gender
        self.is_email_verified = is_email_verified
        self.creation_date = creation_date
        self.timezone = timezone
        self.location = location
        self.registered_on_platform = registered_on_platform
        self.privacy_statement_accepted_on = privacy_statement_accepted_on
        self.email = email
        self.conneqtech_id = conneqtech_id
        self.is_demo_account = is_demo_account
        self.permissions = permissions

    @staticmethod
    def from_dict(obj: Any) -> 'Profile':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        username = UUID(obj.get("username"))
        name = from_str(obj.get("name"))
        display_name = from_str(obj.get("display_name"))
        first_name = from_none(obj.get("first_name"))
        last_name = from_none(obj.get("last_name"))
        initials = from_none(obj.get("initials"))
        avatar_url = from_str(obj.get("avatar_url"))
        address = from_none(obj.get("address"))
        city = from_none(obj.get("city"))
        country = from_str(obj.get("country"))
        postal_code = from_none(obj.get("postal_code"))
        house_number = from_none(obj.get("house_number"))
        house_number_addition = from_none(obj.get("house_number_addition"))
        phone_number = from_none(obj.get("phone_number"))
        phone_number_formatted = from_none(obj.get("phone_number_formatted"))
        gender = from_none(obj.get("gender"))
        is_email_verified = from_bool(obj.get("is_email_verified"))
        creation_date = from_str(obj.get("creation_date"))
        timezone = from_str(obj.get("timezone"))
        location = Location.from_dict(obj.get("location.py"))
        registered_on_platform = from_none(obj.get("registered_on_platform"))
        privacy_statement_accepted_on = from_str(obj.get("privacy_statement_accepted_on"))
        email = from_str(obj.get("email"))
        conneqtech_id = UUID(obj.get("conneqtech_id"))
        is_demo_account = from_bool(obj.get("is_demo_account"))
        permissions = from_list(lambda x: x, obj.get("permissions"))
        return Profile(id, username, name, display_name, first_name, last_name, initials, avatar_url, address, city, country, postal_code, house_number, house_number_addition, phone_number, phone_number_formatted, gender, is_email_verified, creation_date, timezone, location, registered_on_platform, privacy_statement_accepted_on, email, conneqtech_id, is_demo_account, permissions)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["username"] = str(self.username)
        result["name"] = from_str(self.name)
        result["display_name"] = from_str(self.display_name)
        result["first_name"] = from_none(self.first_name)
        result["last_name"] = from_none(self.last_name)
        result["initials"] = from_none(self.initials)
        result["avatar_url"] = from_str(self.avatar_url)
        result["address"] = from_none(self.address)
        result["city"] = from_none(self.city)
        result["country"] = from_str(self.country)
        result["postal_code"] = from_none(self.postal_code)
        result["house_number"] = from_none(self.house_number)
        result["house_number_addition"] = from_none(self.house_number_addition)
        result["phone_number"] = from_none(self.phone_number)
        result["phone_number_formatted"] = from_none(self.phone_number_formatted)
        result["gender"] = from_none(self.gender)
        result["is_email_verified"] = from_bool(self.is_email_verified)
        result["creation_date"] = from_str(self.creation_date)
        result["timezone"] = from_str(self.timezone)
        result["location.py"] = to_class(Location, self.location)
        result["registered_on_platform"] = from_none(self.registered_on_platform)
        result["privacy_statement_accepted_on"] = from_str(self.privacy_statement_accepted_on)
        result["email"] = from_str(self.email)
        result["conneqtech_id"] = str(self.conneqtech_id)
        result["is_demo_account"] = from_bool(self.is_demo_account)
        result["permissions"] = from_list(lambda x: x, self.permissions)
        return result


def profile_from_dict(s: Any) -> Profile:
    return Profile.from_dict(s)


def profile_to_dict(x: Profile) -> Any:
    return to_class(Profile, x)
