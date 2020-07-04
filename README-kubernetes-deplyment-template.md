# pipeline_kubernetes_python 


Debug: 

```
python3 -mpdb deployment_dinamic.py arg1 arg2 arg3
```

Run:

```
python deployment_dinamic.py "app_web_ideas_extraordinarias" "web_ideas" "v:3.0" "nginx:1.15.4" "nginx" "80" "dev"
```
Run model:

```
python deployment_dinamic.py app_name app_label app_version docker_image docker_name environment

```
internal variables: 

```
sys.argv[1] sys.argv[2] sys.argv[3]
```

