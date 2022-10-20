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
    image: "gcr.io/kaniko-project/executor:latest"
    imagePullPolicy: Always
    "stdin": true,
    "stdinOnce": true,
    "args": [
      "--dockerfile=https://github.com/mastermole0310/CI-Pipeline-using-Jenkins-and-k8s.git/Dockerfile",
      "--context=git://github.com/mastermole0310/CI-Pipeline-using-Jenkins-and-k8s.git#refs/heads/main,
      "--destination=gcr.io/my-repo/my-image"
"""
    }
  }
}
