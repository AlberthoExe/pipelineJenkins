pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                git branch: 'main', url: 'https://github.com/AlberthoExe/pipelineJenkins.git'
            }
        }

        

        //stage('Configurar entorno virtual e instalar dependencias') {
        //    steps {
         //       sh '''
          //      python3 -m venv venv
            //    . venv/bin/activate
             //   pip install -r requirements.txt
            //    '''
           // }
       // }

        stage('Ejecutar pruebas unitarias') {
            steps {
                sh 'python3 -m unittest discover'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}