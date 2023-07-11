path=$(dirname $0)
utils=$path/utils
user="ec2-user"

dns=$(sh $utils/describe_stack.sh InstanceDns)

ssh -i $path/../keys/id_rsa $user@$dns
