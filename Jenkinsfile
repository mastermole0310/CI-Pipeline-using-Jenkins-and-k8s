pipeline {
  agent {
    kubernetes {
      //cloud 'kubernetes'
      yaml """
apiVersion: v1
kind: Pod
metadata:
  name: kaniko
spec:
  containers:
  - name: kaniko
    image: gcr.io/kaniko-project/executor:latest
    args:
    - "--context=git://github.com/mastermole0310/CI-Pipeline-using-Jenkins-and-k8s"
    - "--destination=mastermole/flask:1.0"
    volumeMounts:
      - name: dockerfile-storage
        mountPath: /workspace
  restartPolicy: Never
  volumes:
    - name: dockerfile-storage
      persistentVolumeClaim:
        claimName: m2
"""
    }
  }
  stages { 
        stage('Checkout external proj') {
        steps {
            checkout scm 
           }
       }
   }
}
