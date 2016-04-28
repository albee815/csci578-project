#!/bin/bash

#empty database
mysql --user=root --password=123 icc -e "DROP DATABASE icc" 
mysql --user=root --password=123 -e "CREATE DATABASE icc" 
mysql --user=root --password=123 icc < schema

#run scripts
echo "Running parser..."
python parser.py
echo "Finding links"
python links.py
echo "Creating architectural models..."
python architectural_model.py

echo "Done"