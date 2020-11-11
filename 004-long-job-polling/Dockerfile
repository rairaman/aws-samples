FROM lambci/lambda:build-python3.8
WORKDIR /var/task/

COPY src/requirements.txt /var/task/
RUN pip install -r requirements.txt

COPY src /var/task/src/
copy tests /var/task/tests/
