import csv

def get_data_csv(file_path):
    with open(file_path) as f:
        reader = csv.reader(f)
        data = [row for row in reader]
    return data


if __name__ == "__main__":
    open_path = "./result_data/result.csv"
    print(get_data_csv(open_path))