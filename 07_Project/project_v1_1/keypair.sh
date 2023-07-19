#!/bin/bash

aws ec2 create-key-pair --key-name <key-pair-name> --query 'KeyMaterial' --output text > private-key.pem
