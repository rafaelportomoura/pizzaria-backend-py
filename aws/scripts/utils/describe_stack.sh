path=$(dirname $0)

stack_name=$(sh $path/stack_name.sh)
region=$(sh $path/region.sh)

output_key=$1

value="$(aws cloudformation describe-stacks --region $region --stack-name $stack_name --query "Stacks[0].Outputs[?OutputKey=='$output_key'].OutputValue" --output text)"

echo $value
