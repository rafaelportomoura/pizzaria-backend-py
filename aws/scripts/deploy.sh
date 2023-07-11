path=$(dirname $0)
aws_dir=$path/..
utils=$aws_dir/scripts/utils
keys=$aws_dir/keys
document=$aws_dir/data/document.json

# =========================================== PARAMETERS ===========================================

subnetid=subnet-0ac968a83e408e276
vpcid=vpc-0ad20d3ad8630dfd4

# =========================================== FUNCTIONS ============================================

readFile() {
  sh $utils/read_file.sh "$1"
}

describeStack() {
  sh $utils/describe_stack.sh "$1"
}
# =========================================== SCRIPT ===============================================

echo "🖥️ EC2"

if [ ! -d "$keys" ]; then
  echo "Criando diretório de chaves..."
  mkdir $keys
fi

if [ ! -f "$keys/id_rsa" ] || [ ! -f "$keys/id_rsa.pub" ]; then
  echo "Gerando chave ssh.."
  ssh-keygen -t rsa -b 4096 -C "pizzaria@dcc.ufla" -f "$keys/id_rsa" -P ""
fi

ip=$(curl --silent ifconfig.me)
publicKey=$(readFile $keys/id_rsa.pub)

echo "🚀 iniciando deploy..."
cd $aws_dir
sam build

sam validate --lint

sam deploy --no-fail-on-empty-changeset \
  --parameter-overrides \
  "Ip=$ip" \
  "PublicKey='$publicKey'" \
  "SubnetId=$subnetid" \
  "VpcId=$vpcid"

dns=$(describeStack InstanceDns)

echo "🌍 DNS: http://$dns"
