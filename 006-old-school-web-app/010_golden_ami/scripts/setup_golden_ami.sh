#!/bin/bash

# Sleep for a little bit to allow EC2 to initialise
sleep 15

# Apply all updates
yum -y update

# Do more things here to customize AMI!!