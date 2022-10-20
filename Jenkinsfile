pipeline {
  agent {
    kubernetes {
      //cloud 'kubernetes'
      yaml """
kind: Pod
metadata:
  name: kaniko
spec:
  volumes:
  - name: shared-data
    emptyDir: {}
  containers:
  - name: kaniko
    image: gcr.io/kaniko-project/executor:latest
    imagePullPolicy: Always
    command:
    - /busybox/cat
    tty: true
    volumeMounts:
    - name: shared-data
      mountPath: /shared-data
"""
    }
  }
  stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/mastermole0310/CI-Pipeline-using-Jenkins-and-k8s.git'
            }
         }
     }
}
