
script_dir=$(dirname "$0")

python3 -m venv venv
. ./venv/bin/activate
pip install -r ${script_dir}/requirements.txt
python3 ${script_dir}/transmission_util/check_for_duplicates.py "$@"
