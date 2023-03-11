import requests


def get_json_by_url(url):
    base_url = "https://akabab.github.io/superhero-api/api"
    res = requests.get(base_url + "/" + url)
    jsn = res.json()
    return jsn


def get_hero_id(heroes, hero_name):
    rows = list([row for row in heroes if row["name"] == hero_name])
    if len(rows) == 1:
        return rows[0]["id"]
    return None


def get_hero_stats(hero):
    ps = hero["powerstats"]["intelligence"]
    return int(ps)


def get_super_hero():
    all_heroes = get_json_by_url("all.json")

    hulkId = get_hero_id(all_heroes, "Hulk")
    camId = get_hero_id(all_heroes, "Captain America")
    thanosId = get_hero_id(all_heroes, "Thanos")

    hulkIq = get_hero_stats(get_json_by_url(f"id/{hulkId}.json"))
    camIq = get_hero_stats(get_json_by_url(f"id/{camId}.json"))
    thanosIq = get_hero_stats(get_json_by_url(f"id/{thanosId}.json"))

    if hulkIq > camIq and hulkIq > thanosIq:
        return "Hulk"
    elif camIq > hulkIq and camIq > thanosIq:
        return "Captain America"
    else:
        return "Thanos"


if __name__ == '__main__':
    print(get_super_hero())