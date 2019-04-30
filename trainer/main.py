from csv_to_output import printMovies
import numpy as np
import sys
from model import generate_recommendations

client_id = int(sys.argv[1])
already_rated = [2, 2, 2]
k = 5
user_map = np.load("user.npy")
item_map = np.load("item.npy")
row_factor = np.load("row.npy")
col_factor = np.load("col.npy")
user_idx = np.searchsorted(user_map, client_id)
user_rated = [np.searchsorted(item_map, i) for i in already_rated]

recommendations = generate_recommendations(user_idx, user_rated, row_factor, col_factor, k)

printMovies(recommendations)
