path=$(dirname $0)
aws_dir=$path/../..

grep -Po '(?<=stack_name = ")[^"]*' $aws_dir/samconfig.toml
