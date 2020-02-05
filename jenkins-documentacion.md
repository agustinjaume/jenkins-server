
# Fuente de de Jenkins: 
    https://hub.docker.com/r/jenkins/jenkins/
# Codigo de Jenkins: 
    https://github.com/jenkinsci/docker

# Mejoras a realizar en la imagen

RUN apt-get update && apt-get upgrade -y && apt-get install -y git curl && curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash && apt-get install -y git-lfs && git lfs install && rm -rf /var/lib/apt/lists/*
RUN apt-get update
RUN apt-get install -y  python3
RUN apt-get install -y  python-pip python3-pip
RUN apt-get install -y virtualenv
RUN pip install  cryptography==2.7
RUN pip3 install  cryptography==2.7
RUN apt-get install -y software-properties-common
RUN apt-get install -y awscli
RUN pip3 install ansible==2.5.0
RUN pip3 install hvac
RUN pip3 install boto
RUN echo "root:root" | chpasswd



# Creacion de la imagen con las modificaciones 

docker build -t "jenkins:v3" .

# Desplegar un contenedor con Jenkins server con la imagen previamente desplegada

docker run -d -v jenkins_home:/var/jenkins_home -p 8080:8080 -p 50000:50000 jenkins:v3

# Accedemos al contenedor 
docker exec -it c088 /bin/bash

# Cambiamos de usuario para mejoras sobre 
su root  --> root

# apt install 


