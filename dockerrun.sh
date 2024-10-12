docker run \
--mount type=bind,source="$(pwd)"/data,target=/data \
--name problem1-fixedwidth-parser  fixedwidth-parser:latest \
python parse_fixed_width_file.py \
--spec_file 'data/spec.json' --fixed_file 'data/fixedwidth_data.txt' --csv_file 'data/output_csv_parsed_problem1.csv'
