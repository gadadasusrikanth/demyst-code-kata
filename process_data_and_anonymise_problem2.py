import csv
import hashlib
import multiprocessing
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input_file", required=True)

def anonymize_chunk(chunk, chunk_index):
    #Anonymizes a given chunk of rows and writes it to a separate CSV file

    filename = f"data/output_problem2_anonymized_data_{chunk_index}.csv"
    print(f"writing csv file {filename}")

    with open(filename, 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(['first_name', 'last_name', 'address', 'date_of_birth'])

        for row in chunk:
            first_name, last_name, address, date_of_birth = row

            # Hash firstname, last name and address 
            first_name = hashlib.sha256(first_name.encode()).hexdigest()
            last_name = hashlib.sha256(last_name.encode()).hexdigest()
            address = hashlib.sha256(address.encode()).hexdigest()

            writer.writerow([first_name, last_name, address, date_of_birth])

def anonymize_data_parallel(filename, chunk_size, num_processes):
    # Anonymizes personal information in a large CSV file using multiprocessing and threading
    print(f"Start: Anonymizes the input file {filename}")
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header = next(reader) # ignore header
        
        print("Creating chunks and submitting them to multiple threads for parallel porocessing")
        
        with multiprocessing.Pool(num_processes) as pool:
            # print(f"Initiated pool : {pool}")
            i=0
            while True:
                try:
                    chunk = [next(reader) for _ in range(chunk_size)]
                    if not chunk:
                        break
                    i += 1
                    # print(i)
                    pool.apply(anonymize_chunk, args=(chunk, i))
                    # print(chunk)
                except Exception as e:
                    break

            # Wait for all tasks to finish
            pool.close()
            pool.join()

if __name__ == "__main__":

    # file_name = "data/problem2_input_csv_file.csv" 
    args = parser.parse_args()
    input_file = args.input_file

    # file_size_bytes = os.path.getsize(file_name)
    # file_size_mb = file_size_bytes / (1024 ** 2)  # Convert to megabytes
    # print("File size:", file_size_mb, "MB")

    #chunk size will be changed based on input csv file size
    anonymize_data_parallel(filename=input_file, chunk_size=100, num_processes=4)