import os
import yadisk


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        yd = yadisk.YaDisk(token=self.token)
        yd.upload(file_path, os.path.basename(file_path))
        return f"File {file_path} uploaded"


def get_ya_token():
    with open("..\\token.txt") as f:
        return f.readline()


if __name__ == '__main__':
    path_to_file = "test_file.txt"
    token_str = get_ya_token()

    uploader = YaUploader(token_str)
    print(uploader.upload(path_to_file))