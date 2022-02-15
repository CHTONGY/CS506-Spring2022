import csv
import csv
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    # raise NotImplementedError()
    with open(csv_file_path) as f:
        reader = csv.reader(f, quoting = csv.QUOTE_NONNUMERIC)
        data = list(reader)
    
    return data
