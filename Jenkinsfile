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
    args:
    - "--context=git://https://github.com/mastermole0310/CI-Pipeline-using-Jenkins-and-k8s.git"
    - "--destination=mastermole/flask:1.0"
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
