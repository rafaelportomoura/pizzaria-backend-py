path=$(dirname $0)
aws_dir=$path/../..

grep -Po '(?<=region = ")[^"]*' $aws_dir/samconfig.toml
