FROM dizcza/docker-hashcat:cuda

RUN apt-get update && \
    apt-get install -y bzip2 python3-distutils nginx supervisor

RUN wget --no-check-certificate https://bootstrap.pypa.io/pip/3.6/get-pip.py -O /tmp/get-pip.py && \
    python3 /tmp/get-pip.py

RUN apt-get install ocl-icd-libopencl1 opencl-headers clinfo

COPY requirements.txt /root/app/requirements.txt
RUN pip3 install -r /root/app/requirements.txt

COPY . /root/app

EXPOSE 8081

CMD [ "python3", "/root/app/server.py"  ]
