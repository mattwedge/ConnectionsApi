#!/usr/bin/env bash
set -x
awslocal s3 mb s3://droppoint-labels-dev
awslocal s3 mb s3://droppoint-public-media-dev
set +x
