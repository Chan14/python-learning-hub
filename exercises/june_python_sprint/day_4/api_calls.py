import requests


def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        joke_data = response.json()
        # print(joke_data)
        print(dir(response))
        # print("Joke:", joke_data["value"])
    else:
        print(f"Oops, got error code: {response.status_code}")


def get_valid_categories() -> list:
    url = "https://api.chucknorris.io/jokes/categories"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch categories: {response.status_code}")
    return []


def get_joke_by_category(category: str):
    categories = get_valid_categories()
    if category not in categories:
        print(f"Category {category} not found. Valid categories are: {categories}")
        return

    url = "https://api.chucknorris.io/jokes/random"
    params = {"category": category}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        joke = response.json()["value"]
        print(f"Joke from category '{category}' : {joke}")
    else:
        print(f"Failed to get joke: Status code : {response.status_code}")


# Example usage:
get_joke_by_category("dev")
get_joke_by_category("unknown")

# get_chuck_norris_joke()
# print(get_valid_categories())
