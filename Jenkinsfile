pipeline {
  agent any
  environment {
    registry = "mastermole/httpd_pipeline"
    registryCredential = 'dockerhub'
    dockerImage = ''
    }
  stages { 
    stage('Create pod') {
      steps {
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
      }
    }
  }
}
  
