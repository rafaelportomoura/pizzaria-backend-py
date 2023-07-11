path=$(dirname $0)
utils=$path/utils

# =========================================== FUNCTIONS ============================================
describeStack() {
  sh $utils/describe_stack.sh "$1"
}
# =========================================== SCRIPT ===============================================
instance_id=$(describeStack InstanceID)

aws ssm get-command-invocation \
  --command-id "$1" \
  --instance-id "$instance_id"
