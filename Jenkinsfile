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
        
    stage('123') {
            steps { 
                sh "docker exec -it -u root jenkins /bin/bash"
                sh "sudo usermod -aG docker jenkins"
            } 
        }
        
        stage('Building our image') {
            steps { 
                sh "docker build . --tag mastermole/flask:$BUILD_NUMBER"
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
