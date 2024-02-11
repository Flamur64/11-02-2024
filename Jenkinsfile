pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Flamur64/11-02-2024.git'
            }
        }
        stage('Setup') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'source venv/bin/activate && python -m unittest discover tests'
            }
        }
        stage('Deployment') {
            when {
                expression {
                    currentBuild.result == 'SUCCESS'
                }
            }
        }
    }
}
