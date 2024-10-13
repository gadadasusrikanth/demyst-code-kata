docker run \
--mount type=bind,source="$(pwd)"/data,target=/staging_data \
--name problem2-csv-anonymiser  fixedwidth-parser:latest \
python src/process_data_and_anonymise_problem2.py \
--input_file '/staging_data/problem2_input_csv_file.csv' --output_file '/staging_data/output_problem2_anonymized_data'
