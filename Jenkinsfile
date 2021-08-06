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
                    cd ..
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
        stage('deploy to kubernetes'){
            steps {
                script {
                    sh '''
                    curl -o aws-iam-authenticator https://amazon-eks.s3-us-west-2.amazonaws.com/1.21.2/2021-07-05/bin/linux/amd64/aws-iam-authenticator
                    chmod +x ./aws-iam-authenticator
                    mkdir -p $HOME/bin && cp ./aws-iam-authenticator $HOME/bin/aws-iam-authenticator && export PATH=$PATH:$HOME/bin
                    kubectl --kubeconfig terraform-eks-sample-deployment/kubeconfig_pipeline-eks-cluster apply -f kubernetes-sample
                    '''
                }
            }
        }
    }
}
