# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome1_from_dict(json.loads(json_string))

from typing import Any, List, Dict, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Characteristics:
    pass

    def __init__(self, ) -> None:
        pass

    @staticmethod
    def from_dict(obj: Any) -> 'Characteristics':
        assert isinstance(obj, dict)
        return Characteristics()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


class SecondFactorLocationVisual:
    template: str
    x: float
    y: float

    def __init__(self, template: str, x: float, y: float) -> None:
        self.template = template
        self.x = x
        self.y = y

    @staticmethod
    def from_dict(obj: Any) -> 'SecondFactorLocationVisual':
        assert isinstance(obj, dict)
        template = from_str(obj.get("template"))
        x = from_float(obj.get("x"))
        y = from_float(obj.get("y"))
        return SecondFactorLocationVisual(template, x, y)

    def to_dict(self) -> dict:
        result: dict = {}
        result["template"] = from_str(self.template)
        result["x"] = to_float(self.x)
        result["y"] = to_float(self.y)
        return result


class BikeType:
    id: int
    type: str
    name: str
    registration_flow: str
    catalog_price: int
    second_factor_location_translation_key: str
    second_factor_location_image: str
    second_factor_location_visual: SecondFactorLocationVisual
    images: List[str]
    voucher_type_id: int
    all_in_months: int
    features: Dict[str, bool]
    characteristics: Characteristics

    def __init__(self, id: int, type: str, name: str, registration_flow: str, catalog_price: int, second_factor_location_translation_key: str, second_factor_location_image: str, second_factor_location_visual: SecondFactorLocationVisual, images: List[str], voucher_type_id: int, all_in_months: int, features: Dict[str, bool], characteristics: Characteristics) -> None:
        self.id = id
        self.type = type
        self.name = name
        self.registration_flow = registration_flow
        self.catalog_price = catalog_price
        self.second_factor_location_translation_key = second_factor_location_translation_key
        self.second_factor_location_image = second_factor_location_image
        self.second_factor_location_visual = second_factor_location_visual
        self.images = images
        self.voucher_type_id = voucher_type_id
        self.all_in_months = all_in_months
        self.features = features
        self.characteristics = characteristics

    @staticmethod
    def from_dict(obj: Any) -> 'BikeType':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        type = from_str(obj.get("type"))
        name = from_str(obj.get("name"))
        registration_flow = from_str(obj.get("registration_flow"))
        catalog_price = from_int(obj.get("catalog_price"))
        second_factor_location_translation_key = from_str(obj.get("second_factor_location_translation_key"))
        second_factor_location_image = from_str(obj.get("second_factor_location_image"))
        second_factor_location_visual = SecondFactorLocationVisual.from_dict(obj.get("second_factor_location_visual"))
        images = from_list(from_str, obj.get("images"))
        voucher_type_id = from_int(obj.get("voucher_type_id"))
        all_in_months = from_int(obj.get("all_in_months"))
        features = from_dict(from_bool, obj.get("features"))
        characteristics = Characteristics.from_dict(obj.get("characteristics"))
        return BikeType(id, type, name, registration_flow, catalog_price, second_factor_location_translation_key, second_factor_location_image, second_factor_location_visual, images, voucher_type_id, all_in_months, features, characteristics)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["type"] = from_str(self.type)
        result["name"] = from_str(self.name)
        result["registration_flow"] = from_str(self.registration_flow)
        result["catalog_price"] = from_int(self.catalog_price)
        result["second_factor_location_translation_key"] = from_str(self.second_factor_location_translation_key)
        result["second_factor_location_image"] = from_str(self.second_factor_location_image)
        result["second_factor_location_visual"] = to_class(SecondFactorLocationVisual, self.second_factor_location_visual)
        result["images"] = from_list(from_str, self.images)
        result["voucher_type_id"] = from_int(self.voucher_type_id)
        result["all_in_months"] = from_int(self.all_in_months)
        result["features"] = from_dict(from_bool, self.features)
        result["characteristics"] = to_class(Characteristics, self.characteristics)
        return result


def biketype_from_dict(s: Any) -> BikeType:
    return BikeType.from_dict(s)


def biketype_to_dict(x: BikeType) -> Any:
    return to_class(BikeType, x)
