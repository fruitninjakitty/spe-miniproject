pipeline {
    agent any
    
    triggers {
        githubPush()
    }

    environment {
        DOCKER_IMAGE_NAME = 'spe-miniproject'
    }

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
                sh 'docker build -t ${DOCKER_IMAGE_NAME} .'
            }
        }
        stage('Push Docker Images') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: "DockerHub", passwordVariable: "dockerpass", usernameVariable: "dockerhubuser")]) {
                        sh "docker login -u ${env.dockerhubuser} -p ${env.dockerpass}"
                        echo 'login successful'
                        sh "docker tag ${DOCKER_IMAGE_NAME} ${env.dockerhubuser}/${DOCKER_IMAGE_NAME}:latest"
                        sh "docker push ${env.dockerhubuser}/${DOCKER_IMAGE_NAME}:latest"
                    }
                }
            }
        }
        stage('Run Ansible Playbook') {
            steps {
                script {
                    ansiblePlaybook(playbook: 'deploy.yml', inventory: 'inventory')
                }
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executed successfully!'
            emailext (
                subject: "SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'</p>
                <p>Check console output at <a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a></p>""",
                to: 'maximus200214@gmail.com',
                from: 'maximus200214@gmail.com',
                replyTo: 'maximus200214@gmail.com',
                mimeType: 'text/html',
                attachLog: true,
                compressLog: true
            )
        }
        failure {
            echo 'Pipeline execution failed!'
            emailext (
                subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'</p>
                <p>Check console output at <a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a></p>""",
                to: 'maximus200214@gmail.com',
                from: 'maximus200214@gmail.com',
                replyTo: 'maximus200214@gmail.com',
                mimeType: 'text/html',
                attachLog: true,
                compressLog: true
            )
        }
    }
}
