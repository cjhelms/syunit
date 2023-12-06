FROM python:bookworm
WORKDIR $HOME/prj
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./test test/
COPY ./syunit syunit/
CMD [ "pytest", "./test/test.py" ]
