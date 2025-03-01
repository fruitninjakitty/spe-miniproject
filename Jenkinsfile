pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/fruitninjakitty/spe-miniproject']])
            }
        }
        stage('Test') {
            steps {
                sh 'python3 test_calculator.py'
            }
        }
    }
