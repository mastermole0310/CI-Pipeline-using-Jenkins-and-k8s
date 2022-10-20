pipeline {
  agent {
      kubernetes {
      cloud 'kubernetes'
      label 'mastermole/flask'
      defaultContainer 'jenkins-jnlp'
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
    - mountPath: "/root/.m2"
      name: m2
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
    environment {
    registry = "mastermole/httpd_pipeline"
    registryCredential = 'dockerhub'
    dockerImage = ''
    }   
       stages { 
        stage('Checkout external proj') {
        steps {
        agent { label 'dockerfile' }
            checkout scm 
            }
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

