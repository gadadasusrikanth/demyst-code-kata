import csv
from os.path import abspath, exists
import json
import codecs

class fixedwidth_parser():

    def __init__(self, spec_file, fixed_file, csv_file):
        self.spec = spec_file
        self.fixed_width_file = fixed_file
        self.output_csv_file = csv_file

    def validations(self):
        print("Starting validations for the spec file and fixedwidth file")
        if self.spec is None:
            print('Spec file must be specified')
            
        else:
            if not exists(abspath(self.spec)):
                print(f"The spec file {self.spec} does not exist")
            
        
        with open(abspath(self.spec), 'r') as file:
            data = file.read()
        
        spec_data = json.loads(data)

        try:
            fields = spec_data["ColumnNames"]
            if len(fields) == 0:
                print("Spec file has no fields specified")
                
        except Exception as e:
            print("Error parsing spec file for field names")
            

        try:
            offsets = spec_data["Offsets"]
            if len(offsets) == 0:
                print("Spec file has no offsets defined")
                
        except Exception as e:
            print("Error parsing spec file for offsets")
        
        if len(fields) != len(offsets):
            print("Provided spec is not matching the number of columns to offsets")

        try:
            fixedwidthencoding = spec_data["FixedWidthEncoding"]
            if not codecs.lookup(fixedwidthencoding):
                print(f"Provided encoding {fixedwidthencoding} is not valid")
                
        except Exception as e:
            print("Error in parsing FixedWidthEncoding")
            

        try:
            delimitedencoding = spec_data["DelimitedEncoding"]
            if not codecs.lookup(delimitedencoding):
                print(f"Provided encoding {delimitedencoding} is not valid")
                
        except Exception as e:
            print("Error in parsing DelimitedEncoding")

        print("All validations completed")
                       

    # Function to parse a fixed-width line into fields based on the offsets
    def parse_fixed_width_line(self, line, offsets):
        fields = []
        start = 0
        for offset in offsets:
            fields.append(line[start:start + int(offset)].strip())
            start += int(offset)
        return fields

    # Main function to convert fixed-width file to CSV
    def fixed_width_to_csv(self):
        print("Parsing and Converting the Fixedwidthfile to CSV")

        with open(abspath(self.spec), 'r') as file:
            data = file.read()
        
        spec_data = json.loads(data)
        # print(spec_data)
        with open(self.fixed_width_file, 'r', encoding=spec_data["FixedWidthEncoding"]) as fw_file, \
            open(self.output_csv_file, 'w', encoding=spec_data["DelimitedEncoding"]) as csv_file:

            csv_writer = csv.writer(csv_file)

            # If the fixed-width file includes a header, read the first line as a header
            if spec_data["IncludeHeader"] == "True":
                header = fw_file.readline().strip()  # Read and discard the header in the fixed-width file

                # Write the column names from the spec to the CSV
                csv_writer.writerow(spec_data["ColumnNames"])

            # Process each line of the fixed-width file and write to CSV
            for line in fw_file:
                parsed_line = self.parse_fixed_width_line(line.strip(), spec_data["Offsets"])
                csv_writer.writerow(parsed_line)

        return self.output_csv_file