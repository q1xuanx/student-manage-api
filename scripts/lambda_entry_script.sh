if [ -z "${AWS_LAMBDA_RUNTIME_API}" ]; then
  exec /usr/local/bin/aws-lambda-rie /usr/bin/python3 -m awslambdaric $@
else
  exec /usr/bin/python3 -m awslambdaric $@
fi