FROM bentoml/model-server:0.11.0-py312
MAINTAINER ersilia

RUN pip install lazyqsar[descriptors]==2.2.0
RUN lazyqsar-setup


WORKDIR /repo
COPY . /repo
