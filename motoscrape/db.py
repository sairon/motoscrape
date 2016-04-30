import glob
import json


ads_db = {}


def load_data():
    try:
        for file_ in glob.glob("scrapes/*.json"):
            with open(file_, "r") as f:
                data = json.load(f, "utf-8")
                for item in data:
                    ads_db[item['permalink']] = ads_db
    except IOError:
        pass

load_data()
