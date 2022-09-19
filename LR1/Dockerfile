FROM python:3.8-slim-buster
RUN ["mkdir","/my_directory"]
COPY test.py  /my_directory
WORKDIR /my_directory
CMD ["python3", "test.py"]
