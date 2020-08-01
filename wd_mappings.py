import re

parser = re.compile(r"/wiki/(Q\d+).*index=(\d+)")

def get_wd_abs_mappings():
    with open("Matches_WD_ABS.csv") as f:
        mappings = [parser.search(l).groups() for  l in f.readlines() if parser.search(l)]
    return mappings


if __name__=="__main__":
    print(get_wd_abs_mappings())
