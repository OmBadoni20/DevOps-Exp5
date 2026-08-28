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
                    npm install
                '''
            }
        }

        stage('Setup Python') {
            steps {
                bat '''
                    if exist venv rmdir /s /q venv
                    python -m venv venv
                    venv\\Scripts\\python.exe -m pip install --upgrade pip
                    venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Start React App') {
            steps {
                bat '''
                    cd react-app
                    start "" /B cmd /c "npm start > react.log 2>&1"
                    ping 127.0.0.1 -n 16 > nul
                '''
            }
        }

        stage('Run Selenium Tests') {
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