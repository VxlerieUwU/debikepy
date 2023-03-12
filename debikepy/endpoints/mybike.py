# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome7_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Callable, Type, cast
from uuid import UUID

from debikepy.endpoints.location import Location, Geofence

T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()



class OwningUser:
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
    def from_dict(obj: Any) -> 'OwningUser':
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
        location = Location.from_dict(obj.get("location"))
        registered_on_platform = from_none(obj.get("registered_on_platform"))
        privacy_statement_accepted_on = from_str(obj.get("privacy_statement_accepted_on"))
        email = from_str(obj.get("email"))
        conneqtech_id = UUID(obj.get("conneqtech_id"))
        is_demo_account = from_bool(obj.get("is_demo_account"))
        permissions = from_list(lambda x: x, obj.get("permissions"))
        return OwningUser(id, username, name, display_name, first_name, last_name, initials, avatar_url, address, city, country, postal_code, house_number, house_number_addition, phone_number, phone_number_formatted, gender, is_email_verified, creation_date, timezone, location, registered_on_platform, privacy_statement_accepted_on, email, conneqtech_id, is_demo_account, permissions)

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


class Bike:
    id: int
    user_id: int
    user_name: str
    active_state: int
    imei: str
    name: str
    is_requesting_user_owner: bool
    last_location: None
    battery_percentage: None
    owning_user: OwningUser
    geofences: List[Geofence]
    linked_users: List[Any]
    activation_code: str
    frame_number: int
    delivery_date: str
    fabrication_date: str
    odometer: int
    key_number: None
    manufacturer: str
    type: None
    article_number: str
    color_hex: None
    bike_image_url: str
    api_version: int
    cnt_api_bike_id: int
    creation_date: str
    is_stolen: bool
    blepass: None
    blename: str
    dealer_id: None
    ride_in_progress: bool
    current_ride_user_id: None
    displacement: bool
    drop: bool
    highspeed: bool
    ischarging: bool
    lowbattery: bool
    noconnection: bool
    notcharging: bool
    powercut: bool
    service: bool
    motion: bool
    moving: bool
    freefall: bool
    sos: bool
    batterywarning: bool
    batterydegraded: bool
    vibration: bool
    invite_code: None
    invite_code_uri: None

    def __init__(self, id: int, user_id: int, user_name: str, active_state: int, imei: str, name: str, is_requesting_user_owner: bool, last_location: None, battery_percentage: None, owning_user: OwningUser, geofences: List[Any], linked_users: List[Any], activation_code: str, frame_number: int, delivery_date: str, fabrication_date: str, odometer: int, key_number: None, manufacturer: str, type: None, article_number: str, color_hex: None, bike_image_url: str, api_version: int, cnt_api_bike_id: int, creation_date: str, is_stolen: bool, blepass: None, blename: str, dealer_id: None, ride_in_progress: bool, current_ride_user_id: None, displacement: bool, drop: bool, highspeed: bool, ischarging: bool, lowbattery: bool, noconnection: bool, notcharging: bool, powercut: bool, service: bool, motion: bool, moving: bool, freefall: bool, sos: bool, batterywarning: bool, batterydegraded: bool, vibration: bool, invite_code: None, invite_code_uri: None) -> None:
        self.id = id
        self.user_id = user_id
        self.user_name = user_name
        self.active_state = active_state
        self.imei = imei
        self.name = name
        self.is_requesting_user_owner = is_requesting_user_owner
        self.last_location = last_location
        self.battery_percentage = battery_percentage
        self.owning_user = owning_user
        self.geofences: List[Geofence]
        self.activation_code = List[Any]
        self.frame_number = frame_number
        self.delivery_date = delivery_date
        self.fabrication_date = fabrication_date
        self.odometer = odometer
        self.key_number = key_number
        self.manufacturer = manufacturer
        self.type = type
        self.article_number = article_number
        self.color_hex = color_hex
        self.bike_image_url = bike_image_url
        self.api_version = api_version
        self.cnt_api_bike_id = cnt_api_bike_id
        self.creation_date = creation_date
        self.is_stolen = is_stolen
        self.blepass = blepass
        self.blename = blename
        self.dealer_id = dealer_id
        self.ride_in_progress = ride_in_progress
        self.current_ride_user_id = current_ride_user_id
        self.displacement = displacement
        self.drop = drop
        self.highspeed = highspeed
        self.ischarging = ischarging
        self.lowbattery = lowbattery
        self.noconnection = noconnection
        self.notcharging = notcharging
        self.powercut = powercut
        self.service = service
        self.motion = motion
        self.moving = moving
        self.freefall = freefall
        self.sos = sos
        self.batterywarning = batterywarning
        self.batterydegraded = batterydegraded
        self.vibration = vibration
        self.invite_code = invite_code
        self.invite_code_uri = invite_code_uri

    @staticmethod
    def from_dict(obj: Any) -> 'Bike':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        user_id = from_int(obj.get("user_id"))
        user_name = from_str(obj.get("user_name"))
        active_state = from_int(obj.get("active_state"))
        imei = from_str(obj.get("imei"))
        name = from_str(obj.get("name"))
        is_requesting_user_owner = from_bool(obj.get("is_requesting_user_owner"))
        last_location = from_none(obj.get("last_location"))
        battery_percentage = from_none(obj.get("battery_percentage"))
        owning_user = OwningUser.from_dict(obj.get("owning_user"))
        geofences = from_list(Geofence.from_dict, obj.get("geofences"))
        linked_users = from_list(lambda x: x, obj.get("linked_users"))
        activation_code = from_str(obj.get("activation_code"))
        frame_number = int(from_str(obj.get("frame_number")))
        delivery_date = from_str(obj.get("delivery_date"))
        fabrication_date = from_str(obj.get("fabrication_date"))
        odometer = from_int(obj.get("odometer"))
        key_number = from_none(obj.get("key_number"))
        manufacturer = from_str(obj.get("manufacturer"))
        type = from_none(obj.get("type"))
        article_number = from_str(obj.get("article_number"))
        color_hex = from_none(obj.get("color_hex"))
        bike_image_url = from_str(obj.get("bike_image_url"))
        api_version = from_int(obj.get("api_version"))
        cnt_api_bike_id = from_int(obj.get("cnt_api_bike_id"))
        creation_date = from_str(obj.get("creation_date"))
        is_stolen = from_bool(obj.get("is_stolen"))
        blepass = from_none(obj.get("blepass"))
        blename = from_str(obj.get("blename"))
        dealer_id = from_none(obj.get("dealer_id"))
        ride_in_progress = from_bool(obj.get("ride_in_progress"))
        current_ride_user_id = from_none(obj.get("current_ride_user_id"))
        displacement = from_bool(obj.get("displacement"))
        drop = from_bool(obj.get("drop"))
        highspeed = from_bool(obj.get("highspeed"))
        ischarging = from_bool(obj.get("ischarging"))
        lowbattery = from_bool(obj.get("lowbattery"))
        noconnection = from_bool(obj.get("noconnection"))
        notcharging = from_bool(obj.get("notcharging"))
        powercut = from_bool(obj.get("powercut"))
        service = from_bool(obj.get("service"))
        motion = from_bool(obj.get("motion"))
        moving = from_bool(obj.get("moving"))
        freefall = from_bool(obj.get("freefall"))
        sos = from_bool(obj.get("sos"))
        batterywarning = from_bool(obj.get("batterywarning"))
        batterydegraded = from_bool(obj.get("batterydegraded"))
        vibration = from_bool(obj.get("vibration"))
        invite_code = from_none(obj.get("invite_code"))
        invite_code_uri = from_none(obj.get("invite_code_uri"))
        return Bike(id, user_id, user_name, active_state, imei, name, is_requesting_user_owner, last_location, battery_percentage, owning_user, geofences, linked_users, activation_code, frame_number, delivery_date, fabrication_date, odometer, key_number, manufacturer, type, article_number, color_hex, bike_image_url, api_version, cnt_api_bike_id, creation_date, is_stolen, blepass, blename, dealer_id, ride_in_progress, current_ride_user_id, displacement, drop, highspeed, ischarging, lowbattery, noconnection, notcharging, powercut, service, motion, moving, freefall, sos, batterywarning, batterydegraded, vibration, invite_code, invite_code_uri)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["user_id"] = from_int(self.user_id)
        result["user_name"] = from_str(self.user_name)
        result["active_state"] = from_int(self.active_state)
        result["imei"] = from_str(self.imei)
        result["name"] = from_str(self.name)
        result["is_requesting_user_owner"] = from_bool(self.is_requesting_user_owner)
        result["last_location"] = from_none(self.last_location)
        result["battery_percentage"] = from_none(self.battery_percentage)
        result["owning_user"] = to_class(OwningUser, self.owning_user)
        result["geofences"] = from_list(lambda x: to_class(Geofence, x), self.geofences)
        result["linked_users"] = from_list(lambda x: x, self.linked_users)
        result["activation_code"] = from_str(self.activation_code)
        result["frame_number"] = from_str(str(self.frame_number))
        result["delivery_date"] = from_str(self.delivery_date)
        result["fabrication_date"] = from_str(self.fabrication_date)
        result["odometer"] = from_int(self.odometer)
        result["key_number"] = from_none(self.key_number)
        result["manufacturer"] = from_str(self.manufacturer)
        result["type"] = from_none(self.type)
        result["article_number"] = from_str(self.article_number)
        result["color_hex"] = from_none(self.color_hex)
        result["bike_image_url"] = from_str(self.bike_image_url)
        result["api_version"] = from_int(self.api_version)
        result["cnt_api_bike_id"] = from_int(self.cnt_api_bike_id)
        result["creation_date"] = from_str(self.creation_date)
        result["is_stolen"] = from_bool(self.is_stolen)
        result["blepass"] = from_none(self.blepass)
        result["blename"] = from_str(self.blename)
        result["dealer_id"] = from_none(self.dealer_id)
        result["ride_in_progress"] = from_bool(self.ride_in_progress)
        result["current_ride_user_id"] = from_none(self.current_ride_user_id)
        result["displacement"] = from_bool(self.displacement)
        result["drop"] = from_bool(self.drop)
        result["highspeed"] = from_bool(self.highspeed)
        result["ischarging"] = from_bool(self.ischarging)
        result["lowbattery"] = from_bool(self.lowbattery)
        result["noconnection"] = from_bool(self.noconnection)
        result["notcharging"] = from_bool(self.notcharging)
        result["powercut"] = from_bool(self.powercut)
        result["service"] = from_bool(self.service)
        result["motion"] = from_bool(self.motion)
        result["moving"] = from_bool(self.moving)
        result["freefall"] = from_bool(self.freefall)
        result["sos"] = from_bool(self.sos)
        result["batterywarning"] = from_bool(self.batterywarning)
        result["batterydegraded"] = from_bool(self.batterydegraded)
        result["vibration"] = from_bool(self.vibration)
        result["invite_code"] = from_none(self.invite_code)
        result["invite_code_uri"] = from_none(self.invite_code_uri)
        return result

def bike_from_dict(s: Any) -> List[Bike]:
    return from_list(Bike.from_dict, s)


def bike_to_dict(x: List[Bike]) -> Any:
    from_list(lambda x: to_class(Bike, x), x)

