# kubedraw

Requirements:

1) Install required packages

apt-get update && apt-get install graphviz python3 python3-pip python3-venv git
mkdir /opt/kubedraw-venv
python3 -m venv /opt/kubedraw-venv
cd /opt/
git clone https://github.com/genseb13011/kubedraw.git
cd kubedraw
git checkout develop
source /opt/kubedraw-venv/bin/activate
pip3 install -r requirements.txt


2) generate read serviceaccount