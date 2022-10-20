pipeline {
  agent {
    kubernetes {
      //cloud 'kubernetes'
      yaml """
kind: Pod
metadata:
  name: kaniko
spec:
  containers:
  - name: jhooq-pod-with-pvc
    image: rahulwagh17/kubernetes:jhooq-k8s-springboot
    imagePullPolicy: Always
"""
    }
  }
  stages {
      stage('build') {
          steps {
              echo "Hello World!"
          }
      }
  }
}
