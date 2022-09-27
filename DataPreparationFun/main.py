import numpy as np

def get_column(table, header, col_name):
    col = []
    col_index = header.index(col_name)
    for row in table:
        col.append(row[col_index])

    return col

def get_frequencies(table, header, col_name):
    col = get_column(table, header, col_name)
    col.sort() # inplace sort

    values = [] # 75, 76, 77
    counts = [] # 2, 1, 1
    for value in col:
        if value not in values:
            # first time seeing this value
            values.append(value)
            counts.append(1)
        else:
            # seen this value before
            counts[-1] += 1 # ok because the list is in sorted order
    return values, counts

def main():
    header = ["CarName", "ModelYear", "MSRP"]
    msrp_table = [["ford pinto", 75, 2769],
              ["toyota corolla", 75, 2711],
              ["ford pinto", 76, 3025],
              ["toyota corolla", 77, 2789]]
    msrps = get_column(msrp_table, header, "MSRP")
    print(msrps)

    # more on attributes
    # 1. what is the attributes type?
    # e.g. how is it stored
    # int, float, str, list, ...
    # 2. what is the attribute's semantic type?
    # e.g. what does it mean/represent?
    # domain knowledge!!
    # 3. what is the attribute's measurement scale?
    # categorical vs continuous (numeric)
    # nominal: categorical with no inherent ordering
    # ex: zip codes, eye color, names, etc.
    # ordinal: categorical with an inherent ordering
    # ex: T shirt sizes (..., S, M, L, ...)
    # letter grades (A, A-, B+, ...)
    # ratio-scaled: continuous where 0 means absence
    # ex: 0lbs means an absence of weight
    # 0 degrees K means an absence of temperature
    # interval: continuous where 0 does not mean absence
    # ex: 0 degrees F does not mean an absence of temperature

    # noisy vs invalid
    # noisy: valid on the scale but recorded incorrectly
    # an 18 year old that accidentally enter in 81 years old
    # invalid: are not valid on the scale
    # ex: enters "bob" for an age

    # missing values
    # 2 main ways to deal
    # 1. discard them
    # we never want to throw away data
    # usually only do this when your dataset is large
    # and the missing values are small (rare)
    # 2. fill them
    # a few techniques
    # 2.A. categorical attribute: majority voting system (e.g. 
    # most frequent value)
    # 2.B. continuous attribute: central tendency measure (
    # e.g. mean, medians, modes, etc.)
    # later... more "intelligent" filling with looking
    # at similar subsets of the data (kNN algorithm)

    # warm up task
    modelyear_values, modelyear_counts = get_frequencies(msrp_table, header, "ModelYear")
    print(modelyear_values, modelyear_counts)

    # summary stats
    # central tendency measures
    # arithmetic mean
    msrp_mean = sum(msrps) / len(msrps)
    print("mean:", msrp_mean)
    # note the mean is influenced by outliers
    # often prefer the median (middle number in a sorted list)
    # or the mode (most frequelty occurring value(s))
    # mid value (AKA mid range)
    msrp_mid = (min(msrps) + max(msrps)) / 2
    print("mid:", msrp_mid)

    # data dispersion
    # variance: measures the spread of data from the "middle"
    # low variance: the data is close to the mean
    # variance is the average of the squared mean deviations
    squared_mean_deviations = [(msrp - msrp_mean) ** 2 for msrp in msrps]
    variance = sum(squared_mean_deviations) / len(squared_mean_deviations)
    # stdev is the square root of variance
    stdev = np.sqrt(variance)
    print("stdev:", stdev)
    # lets compare our stdev calculation with numpy's std()
    # assert stdev == np.std(msrps)
    # best practice when comparing floats is to use
    # np.isclose() for scalars or np.allclose() for lists
    assert np.isclose(stdev, np.std(msrps))
    # more on stdev
    # empirical rule for normal distributions (bell shaped curves)
    # 68% of the data is within  mean +/- 1 std
    # 95% of the data is within mean +/- 2 std
    # 99.7% of the data is within mean +/- 3 std

    # quantiles
    # paritition (sorted) data into roughly equal sized groups
    # 2-quantiles: 1 cutoff point that makes 2 groups (median)
    # quartiles: 3 cutoff points that make 4 groups
    # percentiles: 99 cutoff points that makes 100 groups
    # more on percentiles later...

if __name__ == "__main__":
    main()