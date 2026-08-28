pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat '''
                    if exist venv rmdir /s /q venv
                    python -m venv venv
                    venv\\Scripts\\python.exe -m pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    if not exist reports mkdir reports
                    venv\\Scripts\\python.exe -m pytest tests/ -v --junitxml=reports/junit-report.xml
                '''
            }
        }
    }

    post {
        always {
            junit testResults: 'reports/junit-report.xml', allowEmptyResults: true
            echo 'Jenkins pipeline execution completed.'
        }
    }
}