import numpy as np

def batch_set_random_seed(seed):
    np.random.seed(seed)

def batch_generator(all_data, batch_size, shuffle=True):
    """
    :param all_data: list [dataset0, dataset1, dataset2,... ,datasetN]
    :param batch_size: 
    :param shuffle: 
    :return: list [batch0, batch1, batch2,... ,batchN]
    """
    #TODO: check if all dataset0 in all_data is numpy.narray
    data_size = all_data[0].shape[0]
    
    if shuffle:
        p = np.random.permutation(data_size)
        #all_data = [d[p] for d in all_data]
    batch_count = 0
    while batch_count* batch_size + batch_size <= data_size:
        #if all dataset is consumed, reshuffle the dataset    
        start = batch_count * batch_size
        end = start + batch_size
        batch_count += 1
        if shuffle:
            yield [d[p[start: end]] for d in all_data]
        else:
            yield [d[start: end] for d in all_data]