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
        stage('Checkout') {
        steps {
            checkout scm
        }
    }
    stage('Initialize'){
           def dockerHome = tool 'my_docker'
           env.PATH = "${dockerHome}/bin:${env.PATH}"
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
