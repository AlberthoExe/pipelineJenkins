pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                git 'https://github.com/AlberthoExe/pipelineJenkins.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Ejecutar pruebas unitarias') {
            steps {
                sh 'python -m unittest discover'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}