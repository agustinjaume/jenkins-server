#!groovy

node {
      for (i=0; i<2; i++) { 
           stage "Stage #"+i
           print 'Hello, world !'
           if (i==0)
           {
            withCredentials([[
            $class: 'AmazonWebServicesCredentialsBinding', 
            credentialsId: 'aws-jenkins-server', 
            accessKeyVariable: 'AWS_ACCESS_KEY_ID', 
            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
            ]]) 
            sh 'aws --version' 
            sh 'aws s3 ls'
           }
           else {
               build 'Declarative pipeline'
               echo 'Running on Stage #1'
           }
      }
}