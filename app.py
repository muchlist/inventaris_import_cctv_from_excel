import os
import time

import setting
from utils.excel_reader import ExcelExtractor
from utils.postman import Postman


def main_program():
    path_file = os.path.join('static', setting.file_name)

    reader = ExcelExtractor(path_file)
    cctv_list = reader.get_cctv_dto()

    postman = Postman()
    token_response = postman.get_token(setting.user_name, setting.password)
    postman.set_token(token_response)

    list_response = []

    for cctv in cctv_list:
        response = postman.post_cctv(cctv)
        list_response.append(response)
        time.sleep(0.3)

    file_response_path = os.path.join("static", "response.txt")
    file_response_text = open(file_response_path, "w")
    for response in list_response:
        file_response_text.writelines(f'{response}\n')
        print(response)
    file_response_text.close()


if __name__ == '__main__':
    main_program()
