# A simple recursive implemention of the powerset function.

def set_of_sets(s):
    if len(s) == 1:
        return [s]
    else:
        first_s = s[0]
        rest_s = s[1:]
        subsets1 = set_of_sets(rest_s)
        subsets2 = [[first_s] + subset for subset in subsets1]
        return [[first_s]] + subsets1 + subsets2


