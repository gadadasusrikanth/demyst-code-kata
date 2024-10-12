import random
from faker import Faker
import json
import io


def read_spec_file(spec_file_path):
    
    with open(spec_file_path, 'r') as specfile:
        data = specfile.read()

    # parse spec file content
    spec_data = json.loads(data)

    return spec_data

def generate_random_data(spec_offsets):
    # Generate random data
    faker = Faker()
    data = []
    row_width = 0
    for _ in range(100):
        row = []
        for offset in spec_offsets:
            if offset > 5:
                row.append(faker.word())
            else:
                row.append(str(random.randint(1, 1000)))
        row_width += offset
        data.append(row)
    
    return data, row_width

def generate_fixed_width_file(spec, spec_offsets, data):
    # Generates a fixed-width text file based on the given spec and data

    file_content = io.StringIO()

    # Create the header row
    if spec["IncludeHeader"]:
        header_row = "".join(field.ljust(offset) for field, offset in zip(spec["ColumnNames"], spec_offsets))
        file_content.write(header_row + "\n")

    # Create data based on spec
    for row in data:
        row_generated = "".join(str(value).ljust(offset) for value, offset in zip(row, spec_offsets))
        file_content.write(row_generated + "\n")

    # Get the file content as a byte string and encode using spec
    file_content.seek(0)
    file_bytes = file_content.read().encode(spec["FixedWidthEncoding"]) #it encodes using windows-1252 encoding

    # Write the file content to a file
    with open("data/fixedwidth_data.txt", "wb") as f:
        f.write(file_bytes)


if __name__ == "__main__":

    spec_file_path = 'data/spec.json'

    # Read spec file
    spec_data = read_spec_file(spec_file_path)

    spec_data_offsets = [int(offset) for offset in spec_data["Offsets"]]

    # Generate random data rows
    data, row_width = generate_random_data(spec_data_offsets)

    # Generate the fixed-width file
    file_bytes = generate_fixed_width_file(spec_data, spec_data_offsets, data)

