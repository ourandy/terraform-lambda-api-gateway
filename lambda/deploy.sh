#!/bin/bash

cd venv/Lib/site-packages 
zip -r ../../../lambda-deployment.zip .
cd ../../../
zip -g lambda-deployment.zip lambda_function.py