# 🌟 Challenge 9: Zip & Unzip Coordinates
# Let’s play with tuples and zip() magic.

# 🧩 Challenge:
# Write two functions:


def zip_coords(x_coords: list[int], y_coords: list[int]) -> list[tuple[int, int]]:
    """
    Takes two lists of coordinates and returns a list of (x, y) tuples.
    """
    count = min(len(x_coords), len(y_coords))
    return [(x_coords[i], y_coords[i]) for i in range(count)]


def zip_coords_improved_using_zip(
    x_coords: list[int], y_coords: list[int]
) -> list[tuple[int, int]]:
    """
    Takes two lists of coordinates and returns a list of (x, y) tuples.
    """
    return list(zip(x_coords, y_coords))


def unzip_coords(coords: list[tuple[int, int]]) -> tuple[list[int], list[int]]:
    """
    Takes a list of (x, y) tuples and returns two lists: x_coords and y_coords.
    """
    x_coords = []
    y_coords = []
    for x, y in coords:
        x_coords.append(x)
        y_coords.append(y)
    return x_coords, y_coords


def unzip_coords_polished(coords: list[tuple[int, int]]) -> tuple[list[int], list[int]]:
    """
    Takes a list of (x, y) tuples and returns two lists: x_coords and y_coords.
    """
    return tuple(map(list, zip(*coords)))


x = [1, 2, 3, 4, 5, 6]
y = [10, 20, 30]

print(zip_coords(x, y))
print(zip_coords_improved_using_zip(x, y))

zipped = [(1, 10), (2, 20), (3, 30)]
print(zipped)
print(*zipped)
print(tuple(map(list, zip(*zipped))))
print(unzip_coords(zipped))
print(unzip_coords_polished(zipped))

coords = [(10, 20), (30, 40), (50, 60)]
print("Original:", coords)

unzipped = zip(*coords)
print("After zip(*coords):", list(unzipped))  # [(10, 30, 50), (20, 40, 60)]

unzipped = zip(*coords)
x_coords, y_coords = [list(t) for t in unzipped]
list_result = list(x_coords), list(y_coords)
