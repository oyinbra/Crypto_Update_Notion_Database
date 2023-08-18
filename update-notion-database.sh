#!/bin/bash

echo "Running Top 100"
python -u ./index.py
echo "DONE"

echo "Running Top 200"
sed -i 's/top0100/top0200/' index.py
python -u ./index.py
echo "DONE"

echo "Running Top 300"
sed -i 's/top0200/top0300/' index.py
python -u ./index.py
echo "DONE"

echo "Running Top 400"
sed -i 's/top0300/top0400/' index.py
python -u ./index.py
echo "DONE"

echo "Running Top 500"
sed -i 's/top0400/top0500/' index.py
python -u ./index.py
echo "DONE"

echo "Running Top 600"
sed -i 's/top0500/top0600/' index.py
python -u ./index.py
echo "DONE"

echo "Running Top 700"
sed -i 's/top0600/top0700/' index.py
python -u ./index.py
echo "DONE"

echo "Running Top 800"
sed -i 's/top0700/top0800/' index.py
python -u ./index.py
echo "DONE"

echo "Running Top 900"
sed -i 's/top0800/top0900/' index.py
python -u ./index.py
echo "DONE"

echo "Running Top 1000"
sed -i 's/top0900/top1000/' index.py
python -u ./index.py
echo "DONE"

echo "Running Top 1100"
sed -i 's/top1000/top1100/' index.py
python -u ./index.py
echo "DONE"

echo "Running Top 1200"
sed -i 's/top1100/top1200/' index.py
python -u ./index.py
echo "DONE"

echo "Running Top 1300"
sed -i 's/top1200/top1300/' index.py
python -u ./index.py
echo "DONE"

echo "Running Top 1400"
sed -i 's/top1300/top1400/' index.py
python -u ./index.py
echo "DONE"

echo "Running Top 1500"
sed -i 's/top1400/top1500/' index.py
python -u ./index.py
echo "DONE"

echo "Running Top 1600"
sed -i 's/top1500/top1600/' index.py
python -u ./index.py
echo "DONE"

echo "Running Top 1700"
sed -i 's/top1600/top1700/' index.py
python -u ./index.py
echo "DONE"

echo "Running Top 1800"
sed -i 's/top1700/top1800/' index.py
python -u ./index.py
echo "DONE"

echo "Running Top 1900"
sed -i 's/top1800/top1900/' index.py
python -u ./index.py
echo "DONE"

echo "Running Top 2000"
sed -i 's/top1900/top2000/' index.py
python -u ./index.py
echo "DONE"

echo "Return back to Top 100"
sed -i 's/top2000/top0100/' index.py
echo "DONE"
