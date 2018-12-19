# Extend the offical Rasa Core SDK image
FROM rasa/rasa_core_sdk:latest

# Add a custom system library (e.g. git)
RUN apt-get update && \
    apt-get install -y git

# Add a custom python library (e.g. mysql)
RUN apt-get install -y python-mysql.connector

# Add a custom python library (e.g. mysql)
RUN apt-get install -y python3-mysql.connector

# Add a custom python library (e.g. jupyter)
RUN pip install --no-cache-dir \
    jupyter
