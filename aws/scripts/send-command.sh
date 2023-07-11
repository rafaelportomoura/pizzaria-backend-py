path=$(dirname $0)
utils=$path/utils
user="ec2-user"
dotenv_dir="$path/../.."

# =========================================== FUNCTIONS ============================================

readFile() {
  sh $utils/read_file.sh "$1"
}

describeStack() {
  sh $utils/describe_stack.sh "$1"
}

# =========================================== SCRIPT ===============================================

database_env=$(readFile $dotenv_dir/.env)
rabbit_env=$(readFile $dotenv_dir/rabbit.env)
instance_id=$(describeStack InstanceID)
document_name=$(describeStack SsmDocument)

aws ssm send-command \
  --instance-ids "$instance_id" \
  --document-name "$document_name" \
  --parameters "DatabaseDotEnv='$database_env',\
  RabbitDotEnv='$rabbit_env'"
