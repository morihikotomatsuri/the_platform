#!/usr/local/bin bash
# main.sh

echo ""
echo "Humanity-Evolution Experiment"
echo "Does the humanity evolve in limited food amount situation?"
echo "executed by `whoami`"

cd /Users/toma/GitHub/the_platform
source venv/bin/activate
cd 01_src
python main.py
deactivate