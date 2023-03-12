import os
import requests


class YaUploader:
    def __init__(self, token: str):
        self.Token = token
        self.Url = "https://cloud-api.yandex.net/v1/disk/resources1"
        self.Headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.Token}'}

    def upload(self, file_path: str):
        res = requests.get(self.Url, headers=self.Headers)
        if res.status_code != 400:
            return f"Error: {res.text}"

        res = requests.get(f'{self.Url}/upload?path={os.path.basename(file_path)}&overwrite=True', headers=self.Headers).json()
        if 'href' not in res.keys():
            return f"Error: {res['error']}"
        else:
            with open(file_path, 'rb') as f:
                requests.put(res['href'], files={'file': f})
        return f"File {file_path} uploaded"


def get_ya_token():
    with open("..\\token.txt") as f:
        return f.readline()


if __name__ == '__main__':
    path_to_file = "test_file.txt"
    token_str = get_ya_token()

    uploader = YaUploader(token_str)
    print(uploader.upload(path_to_file))