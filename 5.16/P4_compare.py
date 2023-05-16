from elice_utils import EliceUtils
import numpy as np
import pandas as pd

elice_utils = EliceUtils()

def remove_items(series1, series2):
    #series임을 유지하면서 numpy isin 쓰는 풀이
    membership = np.isin(series1, series2)
    only_in_s1 = series1[~membership]
    print(only_in_s1)
    
    #series임을 유지하면서 pandas series isin 쓰는 풀이
    only_in_s1 = series1[~series1.isin(series2)]
    print(only_in_s1)

    return only_in_s1
def main():
    series1 = pd.Series([1, 2, 3, 4, 5])
    series2 = pd.Series([4, 5, 6, 7, 8])

    print('Series 1 after removing items in series 2:', remove_items(series1, series2))


if __name__ == "__main__":
    main()