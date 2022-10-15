pipeline {
  options {
    ansiColor('xterm')
  }
    agent {
      kubernetes {
        yamlFile 'builder.yaml'
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
                    
       stage('Kaniko Build & Push Image') {
      steps {
        container('kaniko') {
          script {
            sh '''
            /kaniko/executor --dockerfile `pwd`/Dockerfile \
                             --context `pwd` \
                             --destination=mastermole/flask:${BUILD_NUMBER}
            '''
          }
        }
      }
    }
    
    }    
}
