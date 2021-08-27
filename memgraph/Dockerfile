FROM memgraph:1.6.1-community

USER root

# Install the required pip libraries
RUN python3 -m pip install -U pip setuptools wheel && \
    python3 -m pip install -U simplejson requests pandas

USER memgraph
