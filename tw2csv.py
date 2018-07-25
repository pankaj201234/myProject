#tw2csv.py
def tw2csv(twdata,csvfile_out):
    import csv
    import functools
    allkey = functools.reduce(lambda x, y: x.union(y.keys()), twdata, set())
    with open(csvfile_out,'wt') as output_file:
        dict_writer=csv.DictWriter(output_file,allkey)
        dict_writer.writeheader()
        dict_writer.writerows(twdata)
