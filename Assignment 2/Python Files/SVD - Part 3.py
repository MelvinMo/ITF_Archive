from surprise import SVD
from surprise import Dataset
from surprise.model_selection import train_test_split

# Load the movielens-100k dataset (download it if needed),
data = Dataset.load_builtin('ml-100k')

# sample random trainset and testset
# test set is made of 25% of the ratings.
trainset, testset = train_test_split(data, test_size=.25)

# We'll use the famous SVD algorithm.
algo = SVD()

# Train the algorithm on the trainset and the testset
algo.fit(trainset)

#predict ratings by directly calling the predict() method
# raw user id (as in the ratings file). They are **strings**!
# raw item id (as in the ratings file). They are **strings**!
#The full dataset contains 100000 ratings by 943 users on 1682 items.
testset = trainset.build_anti_testset()
predictions = algo.test(testset)
for uid in predictions:
    for iid in predictions:
        pred = algo.predict(str(uid), str(iid), r_ui=4, verbose=True)