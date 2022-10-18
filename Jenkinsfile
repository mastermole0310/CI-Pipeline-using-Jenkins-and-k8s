pipeline {
  agent any
  environment {
    registry = "mastermole/httpd_pipeline"
    registryCredential = 'dockerhub'
    dockerImage = ''
    }
  stages { 
        stage('Checkout external proj') {
        steps {
            checkout scm 
        }
    }
    
  stage('Create pod') {
      steps {
  agent {
    kubernetes {
      label 'mastermole/flask'
      defaultContainer 'jnlp'
      yaml """
apiVersion: v1
kind: Pod
metadata:
labels:
  component: ci
spec:
  # Use service account that can deploy to all namespaces
  serviceAccountName: default
  containers:
  - name: maven
    image: maven:latest
    command:
    - cat
    tty: true
    volumeMounts:
      - mountPath: /var/run/docker.sock
        name: default
  - name: docker
    image: docker:latest
    command:
    - cat
    tty: true
    volumeMounts:
    - mountPath: /var/run/docker.sock
      name: docker-sock
  volumes:
    - name: docker-sock
      hostPath:
        path: /var/run/docker.sock
    - name: default
      persistentVolumeClaim:
        claimName: default
"""
}
   }
       } 
          }
    
    stage('Build') {
      steps {
        container('maven') {
          sh """
                        mvn package -DskipTests
                                                """
        }
      }
    
        stage('Building our image') {
            steps { 
              container('docker') {
                sh "docker build . --tag mastermole/flask:$BUILD_NUMBER"
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
