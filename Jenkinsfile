pipeline {
    agent any
    triggers {
        cron('H * * * *')
    }   
    environment {
    registry = "mastermole/flask"
    registryCredential = 'dockerhub'
    dockerImage = ''
    }
    stages { 
        stage('Checkout external proj') {
        steps {
            checkout scm 
        }
    }
    stage('Initialize') {
        steps {
            script {
                def dockerHome = tool 'my_docker'
                env.PATH = "${dockerHome}/bin:${env.PATH}"
            }
        }
    }
    
    stage('Run docker deamon') { 
            steps { 
                sh "groupadd docker"
                sh "usermod -aG docker jenkins"
            } 
        }
        
        stage('Building our image') { 
            steps { 
                script { 
                    dockerImage = docker.build registry + ":$BUILD_NUMBER" 
                }
            } 
        }
        stage('Deploy our image') { 
            steps { 
                script { 
                    docker.withRegistry( '', registryCredential ) { 
                        dockerImage.push() 
                    }
                } 
            }
        }
    }    
}
