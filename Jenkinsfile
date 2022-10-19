pipeline {
  agent any
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
    
  stage('Create pod') {
      steps {
  agent {
      kubernetes {
      cloud 'kubernetes'
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
        agent {
      kubernetes {
      cloud 'kubernetes'
      label 'mastermole/flask'
        container('maven') {
          sh """
                        mvn package -DskipTests
                                                """
        }
      }
    } 
      }
    }
    stage('Test') {
      steps {
        agent {
      kubernetes {
      cloud 'kubernetes'
      label 'mastermole/flask'
        container('maven') {
          sh """
             mvn test
          """
        }
      }
    }
      }
    }
        stage('Building our image') {
            steps { 
              agent {
      kubernetes {
      cloud 'kubernetes'
      label 'mastermole/flask'
              container('docker') {
                sh "docker build . --tag mastermole/flask:$BUILD_NUMBER"
                sh "docker push mastermole/flask:$BUILD_NUMBER"
            } 
        }
        }
            }
        }
    
        stage('Initialize') {
        steps {
            script {
                def dockerHome = tool 'mydocker'
                env.PATH = "${dockerHome}/bin:${env.PATH}"
            }
        }
    }
    
        stage('Deploy our image') { 
            steps { 
             agent { label 'dockerfile' }
                script { 
                  docker.withTool(mydocker){
                    docker.withRegistry( '', registryCredential ) { 
                        dockerImage.push()
                      }
                    }
                } 
            }
        }
    } 
}
