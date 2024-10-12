import argparse
from common.fixedwidth_parser import fixedwidth_parser

parser = argparse.ArgumentParser()
parser.add_argument("--spec_file", required=True)
parser.add_argument("--fixed_file",required=True)
parser.add_argument("--csv_file", required=True)

def parse_fixedwidth_file(spec_file, fixed_file, csv_file):

    fixed_parser = fixedwidth_parser(spec_file, fixed_file, csv_file)

    # print(fixed_parser)
    print("Validate the input arguments and spec contents")
    fixed_parser.validations()

    # Call the function to convert the fixed-width file to CSV
    csv_file = fixed_parser.fixed_width_to_csv()

    # print(csv_file)

    print(f"CSV file generated: {csv_file} successfully from fixedwidth file")

if __name__ == "__main__":
    # Passing the required arguments
    args = parser.parse_args()
    spec_file = args.spec_file
    fixed_file = args.fixed_file
    csv_file = args.csv_file

    # print(f"{spec_file}, {fixed_file}, {csv_file}")

    # Parse the input Fixedwidth file and convert it to csv file
    parse_fixedwidth_file(spec_file, fixed_file, csv_file)
