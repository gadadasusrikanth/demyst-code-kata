import csv
from faker import Faker

# Initialize Faker to generate fake data
fake = Faker()

# Generate sample CSV data
def generate_csv(file_name, num_rows):
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(num_rows):
            writer.writerow({
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'address': fake.address().replace("\n", ", "),
                'date_of_birth': fake.date_of_birth().strftime("%Y-%m-%d")
            })

    print(f"CSV file '{file_name}' generated with {num_rows} rows.")

# Generate a sample CSV file
csv_file_name = 'data/problem2_csv_file.csv'
generate_csv(csv_file_name, num_rows=100)