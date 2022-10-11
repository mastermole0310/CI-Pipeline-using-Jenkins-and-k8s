pipeline {
    agent {
        kubernetes {
            label 'kaniko'
            yaml """
apiVersion: v1
kind: Pod
metadata:
  labels:
    jenkins: worker
spec:
  containers:
  - name: kaniko
    image: gcr.io/kaniko-project/executor:debug
    command: ["/busybox/cat"]
    tty: true
    volumeMounts:
      - name: dockercred
        mountPath: /root/.docker/
  volumes:
  - name: dockercred
    secret:
      secretName: dockercred
"""
    }
  }
  
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
                    
        stage('Building our image') { 
            steps { 
               container('kaniko') {
                    sh './build-go-bin.sh'
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
