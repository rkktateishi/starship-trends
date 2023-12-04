def total_average(starship_dict, films):
    total_avg = {
        "id": "Total Average",
        "data": []
    }
    for film in films:
        starships_in_film = []
        total_ships = 0
        total_cost = 0
        for ship_url in film["starships"]:
            starships_in_film.append(starship_dict[ship_url])
            if starship_dict[ship_url]["cost_in_credits"] != "unknown" and "station" not in starship_dict[ship_url]["starship_class"]:
                total_ships += 1
                total_cost += int(float(starship_dict[ship_url]["cost_in_credits"]))
        film["starships"] = starships_in_film
        total_avg["data"].append({
            "x": film["title"],
            "y": (total_cost / total_ships) / 1000000 # in millions of credits
        })

    return total_avg

def costs_by_film(starship_dict, films):
    data = []
    count = 0
    for film in films:
        count += 1
        for ship_url in film["starships"]:
            if starship_dict[ship_url]["cost_in_credits"] != "unknown" and "station" not in starship_dict[ship_url]["starship_class"]:
                data.append({
                    "group": film["title"],
                    "mu": count,
                    "sd": 1,
                    "n": 20,
                    "value": int(float(starship_dict[ship_url]["cost_in_credits"])) / 1000000
                })
    return data

def average_by_starship_class(starship_dict, films):
    starship_classes = {}
    for film in films:
        for ship_url in film["starships"]:
            # Ignore ships with unknown costs and extreme outliers (Death Star)
            if starship_dict[ship_url]["cost_in_credits"] != "unknown" and "station" not in starship_dict[ship_url]["starship_class"]:
                starship_class = {}
                try:
                    starship_class = starship_classes[starship_dict[ship_url]["starship_class"]]
                except KeyError:
                    starship_class = {
                        "id": starship_dict[ship_url]["starship_class"],
                        "data": {}
                    }
                class_by_film = {}
                try:
                    class_by_film = starship_class["data"][film["title"]]
                except KeyError:
                    class_by_film = {
                        "total_ships": 0,
                        "total_cost": 0,
                        "y": 0,
                        "x": film["title"]
                    }
                class_by_film["total_ships"] += 1
                class_by_film["total_cost"] += int(float(starship_dict[ship_url]["cost_in_credits"]))
                class_by_film["y"] = class_by_film["total_cost"] / class_by_film["total_ships"] / 1000000
                starship_class["data"][film["title"]] = class_by_film
                starship_classes[starship_dict[ship_url]["starship_class"]] = starship_class

    for starship_class, value in starship_classes.items():
        data = [v for k, v in value["data"].items()]
        value["data"] = data

    return [v for k, v in starship_classes.items()]

