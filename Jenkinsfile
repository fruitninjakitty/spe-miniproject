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
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t spe-miniproject .'
            }
        }
        stage('Push Docker Images') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "DockerHub", passwordVariable: "dockerpass", usernameVariable: "dockerhubuser")]) {
                        sh "docker login -u ${env.dockerhubuser} -p ${env.dockerpass}"
                        echo 'login successful'
                        sh "docker tag spe-miniproject ${env.dockerhubuser}/spe-miniproject:latest"
                        sh "docker push ${env.dockerhubuser}/spe-miniproject:latest"
                    }
                }
            }
        }
    }
}
