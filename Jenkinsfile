pipeline {
    agent {
        docker { image 'python:3.9' }
    }
    stages {
        stage('ci') {
            steps {
                sh 'git checkout dev'
                sh 'git pull'

//                 sh 'docker build . -t kirrog76/infr_big_data'
//                 sh 'docker login -u $docker_hub_us -p $docker_hub_pw'
//                 sh 'docker push kirrog76/infr_big_data'
            }
        }
        stage('cd') {
            steps {
//                 sh 'docker login -u $docker_hub_us -p $docker_hub_pw'
//                 sh 'docker pull kirrog76/infr_big_data'
//                 sh 'docker run kirrog76/infr_big_data sh -c &quot;python -m src.preprocess ; python -m src.train ; python -m'
                sh 'python -m unittest tests.tests'
            }
        }
    }
}