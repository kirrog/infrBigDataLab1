pipeline {
    agent any
    tools {
        python 'python'
        docker 'docker'
        git 'git'
    }
    stages {
        stage('ci') {
            steps {
                git 'checkout dev'
                git 'pull'
                docker 'build . -t kirrog76/infr_big_data'
                docker 'login -u $docker_hub_us -p $docker_hub_pw'
                docker 'push kirrog76/infr_big_data'
            }
        }
        stage('cd') {
            steps {
                docker 'login -u $docker_hub_us -p $docker_hub_pw'
                docker 'pull kirrog76/infr_big_data'
                docker 'run kirrog76/infr_big_data sh -c &quot;python -m src.preprocess ; python -m src.train ; python -m'
                python '-m unittest tests.tests'
            }
        }
    }
}