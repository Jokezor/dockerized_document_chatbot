FROM python:3.10-buster

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements

RUN pip install -r /requirements/base.txt

COPY ./compose/pdf_to_text/convert /convert
RUN sed -i 's/\r//' /convert
RUN chmod +x /convert

# Create app directory
WORKDIR /app

