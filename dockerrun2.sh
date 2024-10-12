docker run \
--mount type=bind,source="$(pwd)"/data,target=/data \
--name problem2-csv-anonymiser  fixedwidth-parser:latest \
python process_data_and_anonymise_problem2.py \
--input_file 'data/problem2_input_csv_file.csv'
