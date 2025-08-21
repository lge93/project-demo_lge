# Instalación

```bash
conda create -n project-demo python=3.12.11
conda activate project-demo

pip install -r requirements.txt
```

# Data

```bash
mkdir data
cd data
wget https://raw.githubusercontent.com/lab-pep-itba/Clase-3---Clasificadores-Bayesianos/refs/heads/master/data/alturas-pesos-mils-train.csv
```

# Build docker

```bash
docker build -t project-demo .

docker run \
  --name "project-demo" \
  -it \
  project-demo /bin/bash

docker run \
  --name "project-demo" \
  -p 8501:8501 \
  project-demo

docker ps
docker rm project-demo
```




   --env-file=.env \
   --add-host=host.docker.internal:host-gateway \
   -d \
   -p "$PORT":8501 \
  
   -v /home/julian/gnina/drugs:/databases \