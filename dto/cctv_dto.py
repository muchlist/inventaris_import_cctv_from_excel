from typing import NamedTuple


class CctvDto(NamedTuple):
    cctv_name: str
    ip_address: str
    inventory_number: str
    location: str
    year: str
    merk: str
    tipe: str
    note: str
    deactive: bool
