FROM python:3.10

ADD src ./src
ADD text_files ./text_files 

WORKDIR src

RUN pip install -r requiremens.txt 

CMD ["python", "main.py"]