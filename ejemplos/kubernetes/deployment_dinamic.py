#!/usr/bin/env python3
import sys, shutil, os
from jinja2 import Template, Environment, FileSystemLoader
from kubernetes import client, config, watch
# variables

app_name= sys.argv[1]
app_label= sys.argv[2]
app_version= sys.argv[3]
docker_image= sys.argv[4]
docker_name= sys.argv[5]
port= sys.argv[6]
environment= sys.argv[7]
app_replicas= sys.argv[8]

from_app = 'templates/template-deployment.yaml'
from_namespace = 'templates/template-namespace.yaml'
to_app = app_name + "-deployment.yaml"
to_namespace = app_name + "-namespace.yaml"

def template_app(app_name,app_label,app_version,docker_image,docker_name,port,environment,app_replicas):
# Configuracion y reemplazo de valores
    env = Environment(loader=FileSystemLoader('')) # carpeta de template vacia
    template = env.get_template(from_app) # template
    output_from_parsed_template = template.render(
        app_name=app_name,
        app_label=app_label,
        port=port,
        docker_image=docker_image,
        docker_name=docker_name,
        app_replicas=app_replicas
    )

# Print contenido modificado
    print(output_from_parsed_template)
    if not os.path.exists(to_app):
        with open(to_app, 'w'): pass

# Volcado de contenido
    f = open(to_app,'w')
    print(output_from_parsed_template, file=f)


# TEMPLATE NAMESPACES
def template_namespace(app_name,app_label,app_version,docker_image,environment):

# Configuracion y reemplazo de valores
    env = Environment(loader=FileSystemLoader('')) # carpeta de template vacia
    template = env.get_template(from_namespace) # template
    output_from_parsed_template = template.render(
        app_name=app_name,
        app_label=app_label,
        app_version=app_version,
        docker_image=docker_image,
        environment=environment
    )

# Print contenido modificado
    print(output_from_parsed_template)
    if not os.path.exists(to_namespace):
        with open(to_namespace, 'w'): pass

# Volcado de contenido
    f = open(to_namespace,'w')
    print(output_from_parsed_template, file=f)

    

#Creando to_app = app_name + "-deployment.yaml"
#Creando app_name + "-namespace.yaml"
template_app(app_name,app_label,app_version,docker_image,docker_name,port,environment,app_replicas)
template_namespace(app_name,app_label,app_version,docker_image,environment)

def check(app_name):
    config.load_kube_config()
    v1 = client.CoreV1Api()
    count = 10
    w = watch.Watch()
    for event in w.stream(v1.list_namespace, timeout_seconds=5):
        print( event['object'].metadata.name)
        if event['object'].metadata.name == app_name:
            print("el namespaces existe")
            result = "ok"
            break 
        else:
            print("no existe")
            result = "ko"
        count -= 1
        if not count:
            w.stop()
    print("Finished namespace stream.")
    return result

result = check(app_name)
print(result)
