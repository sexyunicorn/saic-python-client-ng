import logging
from dataclasses import dataclass
from pydantic import BaseModel
from pydantic.dataclasses import dataclass as pydanticdataclass

from enum import Enum

logger = logging.getLogger(__name__)


@pydanticdataclass
@dataclass
class LoginResp:
    @dataclass
    class LoginRespDetail:
        languageType: str = None

    access_token: str = None
    account: str = None
    avatar: str = None
    client_id: str = None
    dept_id: str = None
    detail: LoginRespDetail = None
    expires_in: int = None
    jti: str = None
    languageType: str = None
    license: str = None
    oauth_id: str = None
    post_id: str = None
    refresh_token: str = None
    role_id: str = None
    role_name: str = None
    scope: str = None
    tenant_id: str = None
    token_type: str = None
    user_id: str = None
    user_name: str = None


class GpsStatus(Enum):
    NO_SIGNAL = 0
    TIME_FIX = 1
    FIX_2D = 2
    FIX_3d = 3


@pydanticdataclass
@dataclass
class GpsPosition:
    @dataclass
    class WayPoint:
        @dataclass
        class Position:
            altitude: int = None
            latitude: int = None
            longitude: int = None

        hdop: int = None
        heading: int = None
        position: Position = None
        satellites: int = None
        speed: int = None

    gpsStatus: int = None
    timeStamp: int = None
    wayPoint: WayPoint = None

    @property
    def gps_status_decoded(self) -> GpsStatus | None:
        value = self.gpsStatus
        if value is None:
            return None
        try:
            return GpsStatus(value)
        except ValueError:
            logger.error(f"Could not decode {value} as GpsStatus")
            return None


from pydantic import BaseModel
from dataclasses import dataclass
from typing import Type


def dataclass_to_pydantic_model(kls: Type[dataclass]) -> Type[BaseModel]:
    """
    Converts a standard dataclass to a Pydantic BaseModel.
    Args:
        kls (Type[dataclass]): The dataclass to convert.
    Returns:
        Type[BaseModel]: A Pydantic model class based on the dataclass.
    """

    class BaseModelDataclass(BaseModel, kls):  # Dynamically create the Pydantic model
        pass

    return BaseModelDataclass


# print(dataclass_to_pydantic_model(GpsPosition).schema_json())
