from surprise import KNNBasic
from surprise import Dataset
from surprise.model_selection import cross_validate

# Load the movielens-100k dataset (download it if needed),
data = Dataset.load_builtin('ml-100k')

# We'll use the famous SVD algorithm.
algo = KNNBasic()

# Run 4-fold cross-validation and print results.
cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=4, verbose=True)

