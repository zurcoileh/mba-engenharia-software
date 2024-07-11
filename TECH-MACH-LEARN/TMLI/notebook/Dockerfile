
FROM continuumio/miniconda3

WORKDIR /app
RUN /opt/conda/bin/conda install jupyter -y 
RUN pip install pandas
EXPOSE 8888

ENTRYPOINT ["jupyter", "notebook","--allow-root","--ip=0.0.0.0","--port=8888","--no-browser"]


