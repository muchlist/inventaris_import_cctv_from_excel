import pandas as pd

from dto.cctv_dto import CctvDto


class ExcelExtractor(object):
    path_file = ""

    def __init__(self, path: str):
        self.path_file = path

    def get_cctv_dto(self) -> list:
        data = pd.read_excel(self.path_file)
        df = pd.DataFrame(data, columns=["Nama",
                                         "Lokasi",
                                         "IP",
                                         "Merk",
                                         "Tipe",
                                         "Tahun",
                                         "Note",
                                         "Inventaris"]).fillna('')
        cctv_dto_list = []

        for index, row in df.iterrows():
            year_fixed = row["Tahun"].replace("\xa0", " ")
            cctv_dto_list.append(
                CctvDto(cctv_name=row["Nama"],
                        ip_address=row["IP"],
                        inventory_number=row["Inventaris"],
                        location=row["Lokasi"],
                        year=year_fixed,
                        merk=row["Merk"],
                        tipe=row["Tipe"],
                        note=row["Note"],
                        deactive=False)
            )
        return cctv_dto_list
