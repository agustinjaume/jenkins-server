#!groovy

node {
      for (i=0; i<2; i++) { 
           stage "Stage #"+i
           print 'Hello, world !'
           if (i==0)
           {

            step { withCredentials([[
            $class: 'AmazonWebServicesCredentialsBinding', 
            credentialsId: 'aws-jenkins-server', 
            accessKeyVariable: 'AWS_ACCESS_KEY_ID', 
            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
            ]]) 
            {
            aws --version 
            aws s3 ls
            } 
            }  // fin step

           }
           else {
               build 'Declarative pipeline'
               echo 'Running on Stage #1'
           }
      }
}