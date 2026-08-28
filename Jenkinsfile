pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Node Dependencies') {
            steps {
                bat '''
                    cd react-app
                    npm ci
                '''
            }
        }

        stage('Setup Python') {
            steps {
                bat '''
                    if exist venv rmdir /s /q venv
                    python -m venv venv
                    venv\\Scripts\\python.exe -m pip install --upgrade pip
                    venv\\Scripts\\python.exe -m pip install selenium pytest
                '''
            }
        }

        stage('Start React App') {
            steps {
                bat '''
                    cd react-app
                    start /B cmd /c "npm start > react.log 2>&1"
                    timeout /t 15 /nobreak
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat '''
                    venv\\Scripts\\python.exe -m pytest tests/ -v
                '''
            }
        }
    }

    post {
        always {
            echo 'Jenkins pipeline execution completed.'
        }

        success {
            echo 'React Selenium tests passed successfully.'
        }

        failure {
            echo 'React Selenium tests failed.'
        }
    }
}