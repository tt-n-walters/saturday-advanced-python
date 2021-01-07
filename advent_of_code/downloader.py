import requests

token = "53616c7465645f5f11ce59e132dabb773e043ffc4dfb9e6e071573f400ecb805d2becc88bc0876989ebd3203fe3cf4a6"

def download(day_number):
    url = "https://adventofcode.com/2020/day/{}/input".format(day_number)
    print("Downloading day {} from {}".format(day_number, url))
    cookies = {
        "session": token
    }
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        return response.text
    else:
        print("Download error {}\n{}".format(response.status_code, response.text))
        exit()


if __name__ == "__main__":
    import sys
    day_number = sys.argv[1] if len(sys.argv) > 1 else exit("No day supplied!")
    inputs = download(day_number)
    filename = "day{}inputs".format(day_number)
    with open(filename, "w") as file:
        file.write(inputs)
