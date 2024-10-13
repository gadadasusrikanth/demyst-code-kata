docker run \
--mount type=bind,source="$(pwd)"/data,target=/staging_data \
--name problem1-fixedwidth-parser  fixedwidth-parser:latest \
python src/parse_fixed_width_file.py \
--spec_file '/staging_data/spec.json' --fixed_file '/staging_data/fixedwidth_data.txt' --csv_file '/staging_data/output_csv_parsed_problem1.csv'
