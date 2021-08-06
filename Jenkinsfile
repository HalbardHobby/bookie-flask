pipeline {
    agent { label 'master'}
    environment {
        REGISTRY = "halbard/bookie-flask"
        DOCKERHUB_CREDENTIALS = 'halbard-dockerhub'
    }
    stages {
        stage('check infraestructure') {
            steps {
                script {
                    sh '''
                    cd terraform-eks-sample-deployment
                    terraform init
                    terraform apply --auto-approve
                    '''
                }
            }
        }
        stage('build image') {
            steps {
                script {
                	def dockerImage = docker.build REGISTRY
                    docker.withRegistry( '', DOCKERHUB_CREDENTIALS ) { 
                        sh 'docker push $REGISTRY:latest'
                    }
                }
            }
        }
        stage('clean up image') {
            steps {
                script {
                    sh 'docker rmi $REGISTRY'
                }
            }
        }
    }
}
