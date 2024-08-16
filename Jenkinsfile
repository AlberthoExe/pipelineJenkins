pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                git branch: 'main', url: 'https://github.com/AlberthoExe/pipelineJenkins.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'pip install -r requirements.txt || true'
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