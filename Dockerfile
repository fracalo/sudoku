ARG PYTHON_VERSION=3.13
FROM python:${PYTHON_VERSION}-slim AS builder
WORKDIR /tmp

RUN apt-get update && pip install --upgrade pip

# need to recreate locally with poetry export
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


FROM gcr.io/distroless/python3-debian12:nonroot
ARG PYTHON_VERSION=3.13

COPY --from=builder /usr/local/lib/python${PYTHON_VERSION}/site-packages /usr/local/lib/python${PYTHON_VERSION}/site-packages

COPY . /app
WORKDIR /app

ENV PYTHONPATH=/usr/local/lib/python${PYTHON_VERSION}/site-packages

#CMD ["main.py"]
CMD ["standalone.py"]
