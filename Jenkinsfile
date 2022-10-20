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
  - name: kaniko
    image: gcr.io/kaniko-project/executor:debug
    imagePullPolicy: Always
    command:
    - /busybox/cat
    tty: true
    volumeMounts:
      - name: jenkins-docker-cfg
        mountPath: /kaniko/.docker
  volumes:
  - name: jenkins-docker-cfg
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
