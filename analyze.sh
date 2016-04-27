#!/bin/bash

#empty database
mysql --user=homestead --password=secret icc -e "DROP DATABASE icc" 
mysql --user=homestead --password=secret -e "CREATE DATABASE icc" 
mysql --user=homestead --password=secret icc < schema

echo "Running parser..."
python parser.py
echo "Creating architectural models..."
python architectural_model.py

echo "Done"

