#!/usr/bin/env python3
import sys, shutil, os
from jinja2 import Template, Environment, FileSystemLoader


# variables
aplication = sys.argv[1]
label_app = sys.argv[2]
origen = 'templates/template-deployment.yaml'
destino = aplication + "-deployment.yaml"

# Configuracion y reemplazo de valores
env = Environment(loader=FileSystemLoader('')) # carpeta de template vacia
template = env.get_template(origen) # template
output_from_parsed_template = template.render(
    app_name=aplication,
    app_label=label_app
)

# Print contenido modificado
print(output_from_parsed_template)
if not os.path.exists(destino):
    with open(destino, 'w'): pass

# volcado de contenido
f = open(destino,'w')
print(output_from_parsed_template, file=f)

