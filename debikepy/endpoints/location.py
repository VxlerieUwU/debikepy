from debikepy.utils import *


class Location:
    lat: float
    lon: float

    def __init__(self, lat: float, lon: float) -> None:
        self.lat = lat
        self.lon = lon

    @staticmethod
    def from_dict(obj: Any) -> 'Location':
        assert isinstance(obj, dict)
        lat = from_float(obj.get("lat"))
        lon = from_float(obj.get("lon"))
        return Location(lat, lon)

    def to_dict(self) -> dict:
        result: dict = {}
        result["lat"] = to_float(self.lat)
        result["lon"] = to_float(self.lon)
        return result


class Geofence:
    id: int
    bike_id: int
    user_id: int
    name: str
    center: Location
    radius: int
    active_state: int
    creation_date: str

    def __init__(self, id: int, bike_id: int, user_id: int, name: str, center: Location, radius: int, active_state: int, creation_date: str) -> None:
        self.id = id
        self.bike_id = bike_id
        self.user_id = user_id
        self.name = name
        self.center = center
        self.radius = radius
        self.active_state = active_state
        self.creation_date = creation_date

    @staticmethod
    def from_dict(obj: Any) -> 'Geofence':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        bike_id = from_int(obj.get("bike_id"))
        user_id = from_int(obj.get("user_id"))
        name = from_str(obj.get("name"))
        center = Location.from_dict(obj.get("center"))
        radius = from_int(obj.get("radius"))
        active_state = from_int(obj.get("active_state"))
        creation_date = from_str(obj.get("creation_date"))
        return Geofence(id, bike_id, user_id, name, center, radius, active_state, creation_date)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["bike_id"] = from_int(self.bike_id)
        result["user_id"] = from_int(self.user_id)
        result["name"] = from_str(self.name)
        result["center"] = to_class(Location, self.center)
        result["radius"] = from_int(self.radius)
        result["active_state"] = from_int(self.active_state)
        result["creation_date"] = from_str(self.creation_date)
        return result


def geofence_from_dict(s: Any) -> Geofence:
    return Geofence.from_dict(s)


def geofence_to_dict(x: Geofence) -> Any:
    return to_class(Geofence, x)
