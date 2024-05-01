import pandas as pd

from src.utils import save_train_data, save_valid_data, save_test_data


def prepare_data(path2data: str):
    seeds_data = pd.read_csv(path2data)

    length = len(seeds_data)
    split_coef_train = 0.8
    split_coef_test = 0.1
    split_coef_validation = 0.1
    assert 1.0 == sum([split_coef_train, split_coef_test, split_coef_validation])

    train_data = seeds_data.loc[:int(length * split_coef_train)]
    test_data = seeds_data.loc[:int(length * split_coef_test)]
    validation_data = seeds_data.loc[:int(length * split_coef_validation)]

    save_train_data(train_data)
    save_test_data(test_data)
    save_valid_data(validation_data)


if __name__ == "__main":
    prepare_data("../data/seeds.csv")
