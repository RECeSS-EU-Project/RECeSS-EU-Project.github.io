# coding:utf-8

## Import models
import benchscofi
from benchscofi.SimpleBinaryClassifier import SimpleBinaryClassifier
from benchscofi.SimplePULearning import SimplePULearning

## Import dataset utils
import stanscofi
from stanscofi.datasets import generate_dummy_dataset, Dataset

## Import training utils
from stanscofi.training_testing import random_simple_split

random_seed = 12345 ## for reproducibility

## create the synthetic dataset
npositive, nnegative, nfeatures, mean, std = 200, 100, 6, 0.5, 0.25
data_args = generate_dummy_dataset(npositive, nnegative, nfeatures, mean, std, random_state=random_seed)
dataset = Dataset(**data_args)

## split the data into training and testing sets
(train_folds, test_folds), _ = random_simple_split(dataset, 20/100, random_state=random_seed)

params = {
	"layers_dims": [4, 16, 32, 16], ## four layers
	"steps_per_epoch":10, ## 10 steps per epoch
	"epochs":10, ## 10 epoch
	"PI": 0.33, ## the value of pi (in the PU loss)
	"random_state": random_seed,
	"preprocessing_str":"meanimputation_standardize", "subset":None, 
}

for model in [SimplePULearning(params=params), SimpleBinaryClassifier(params=params)]:
	## training
	train_dataset = dataset.subset(train_folds)
	model.fit(train_dataset)
	## prediction on testing set
	test_dataset = dataset.subset(test_folds)
	scores = model.predict_proba(test_dataset)
	predictions = model.predict(scores, threshold=0.5)
	## visualize results
	test_dataset.visualize(predictions=predictions)