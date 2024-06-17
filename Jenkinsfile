pipeline {
//     agent any
    agent {
        docker {
            image 'python:3.9'
        }
    }
    stages {
        stage('ci') {
            steps {
                sh 'git checkout dev'
                sh 'git pull'
//                 sh 'docker build . -t kirrog76/infr_big_data'
//                 sh 'docker login -u $docker_hub_us -p $docker_hub_pw'
//                 sh 'docker push kirrog76/infr_big_data'
//                 sh "pip install virtualenv"
//                 sh "virtualenv venv"
//                 sh 'python -m pip install --no-cache-dir -r requirements.txt'
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh "python -m pip install virtualenv"
                    sh "python -m virtualenv venv"
                    sh "python -m pip install -r requirements.txt "

                }
            }
        }
        stage('cd') {
            steps {
//                 sh 'docker login -u $docker_hub_us -p $docker_hub_pw'
//                 sh 'docker pull kirrog76/infr_big_data'
//                 sh 'docker run kirrog76/infr_big_data sh -c "python -m main; python -m unittest tests.tests"'
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python -m main'
                    sh 'python -m unittest tests.tests'
                }

            }
        }
    }
}