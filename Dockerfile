
FROM python:3.10.5-slim-bullseye

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y git wget tar unzip


RUN wget --no-check-certificate https://github.com/mariadb-corporation/mariadb-connector-c/archive/refs/heads/3.2.zip
RUN unzip 3.2.zip
RUN apt-get install cmake -y
RUN apt-get install -y ca-certificates gcc libc-dev libffi-dev  build-essential \
    && apt-get install --only-upgrade openssl \
    && apt-get install --only-upgrade libssl-dev \
    && update-ca-certificates

RUN apt-get install -y libmariadb3 libmariadb-dev 
RUN mkdir build && cd build
RUN cmake ../mariadb-connector-c-3.2/ 
#-DCMAKE_INSTALL_PREFIX=/usr
RUN make
RUN make install
# Switch to the directory where our project will be stored
WORKDIR /project
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy our project to the build container
COPY . .
RUN chmod +x run.sh

# Create an unprivileged user and switch to it so the process does not have access to root
RUN useradd -U --no-create-home --shell /usr/sbin/nologin --uid 1000 notroot
USER notroot:notroot

ENTRYPOINT [ "/project/run.sh" ]
