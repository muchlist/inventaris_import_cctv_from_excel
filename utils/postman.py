import requests

from dto.cctv_dto import CctvDto


class Postman(object):
    base_url = ""
    token = ""

    def __init__(self):
        self.base_url = "http://localhost:5001"

    def set_base_url(self, base_url: str):
        self.base_url = base_url

    def set_token(self, token: str):
        self.token = f"Bearer {token}"

    def get_token(self, user_name: str, password: str) -> str:
        url = f"{self.base_url}/login"
        body_post = {
            "username": user_name,
            "password": password
        }
        x = requests.post(url, json=body_post)
        if x.status_code == 200:
            json_response = x.json()
            return json_response["access_token"]
        else:
            return "Error"

    def post_cctv(self, data: CctvDto) -> str:
        url = f"{self.base_url}/api/cctvs"

        headers = {'Content-Type': 'application/json',
                   'Authorization': self.token, }
        body_post = {
            "cctv_name": data.cctv_name,
            "inventory_number": data.inventory_number,
            "ip_address": data.ip_address,
            "location": data.location,
            "merk": data.merk,
            "year": data.year,
            "note": data.note,
            "tipe": data.tipe,
            "deactive": False
        }
        x = requests.post(url, json=body_post, headers=headers)
        if x.status_code == 200 or x.status_code == 201:
            response_json = x.json()
            return f'Berhasil - {response_json["cctv_name"]}'
        else:
            return f"Gagal - {data.cctv_name}"
