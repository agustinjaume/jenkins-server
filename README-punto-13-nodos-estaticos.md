# Curso de JENKINS 

## 13_ Nodos
 
### Nodos Estáticos 

En este video veremos:
Conceptos de Jenkins server y estructura de nodos y cual nos conviene utilizar o se adapta mejor a nuestros objetivos.
Como agregar y administrar nodos estáticos a nuestro Jenkins server.

Aprenderemos como seleccionar los nodos ya sea por formulario o por código.


Escenario con nodos estáticos:
Ventajas : 
- Todos los componentes se desplegaran en nodos que estarán siempre dando servicio, por lo tanto en el mejor de los casos es inmediata la gestión.
Desventajas :
- consumo eléctrico debido a servidores. refrigeración
- Escalado manual
- Administración y dependencia de soporte en mayor grado que opciones dinámicas de nodos.

![Texto alternativo](imagenes/diapositivas-13-nodos-13-nodos-estaticos.png)  

Escenario con nodos dinámicos:

Ventajas : 
- Ahorro de costes, unificación de gastos de refrigeración, mantenimiento de hardware
- Escalado por demanda
- 
Desventajas :
- Delay de despliegue


![Texto alternativo](imagenes/diapositivas-13-nodos-13-nodos-dinamicos.png)  

Cotejando ambos escenarios podemos hablar el siguiente cuadro de ejes:


![Texto alternativo](imagenes/diapositivas-13-nodos-13-1a-TEORIA.png)


### Agregaremos 2 nodos estaticos 
Componentes necesarios

### Codigo con el que trabajaremos.

```
pipeline {
    agent any
    // agent { label '$NODO' }
    parameters { 
      choice(name: 'Entornos', choices: ['dev', 'pre', 'pro'], description: 'Seleccione el entorno a utilizar')
      choice(name: 'Nodo', choices: ['ubuntu19', 'windows','python.27','Alpine'], description: 'Seleccione el entorno a utilizar')
    }
    environment {
     NODO="${ Nodo }" 
    }

    stages {
        stage('Build') {
            agent { label "$NODO" }
            steps {
                echo 'Building..'
                sh '''
                '''
            }
        }
    }

    post {
        success {
            echo 'This will run only if successful'
        }
    }
}

```

-




