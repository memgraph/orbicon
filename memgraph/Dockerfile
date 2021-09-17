FROM memgraph:1.6.1-community

USER root

RUN apt-get update && \
    apt-get --yes install curl git cmake g++ clang python3-dev && \
    cd /usr/local/bin && \
    ln -s /usr/bin/python3 python && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install the required pip libraries
RUN python3 -m pip install -U pip setuptools wheel && \
    python3 -m pip install -U simplejson requests pandas networkx==2.5 python-Levenshtein==0.12.1 gensim==4.0.0 scikit-learn==0.24.2

COPY github_token.txt /github_token.txt
COPY twitter_token.txt /twitter_token.txt

USER memgraph
