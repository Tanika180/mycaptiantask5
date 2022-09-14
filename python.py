def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
A=most_frequent('Mississippi')
def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
print(A)
print("\nSort (descending) the said dictionary elements by value:")
print(sort_dict_by_value(A, True))
