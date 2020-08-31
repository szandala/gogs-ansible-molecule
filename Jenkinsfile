pipeline {
  agent any
  stages {
    stage('One') {
      agent any
      environment {
        IS_DEMO = 'true'
      }
      steps {
        echo 'Hello'
        validateDeclarativePipeline 'Jenkinsfile'
        sh 'echo "working" > file.txt'
        archiveArtifacts(artifacts: '*.txt', followSymlinks: true, onlyIfSuccessful: true)
      }
    }

    stage('Two') {
      parallel {
        stage('Two') {
          steps {
            echo 'hi'
          }
        }

        stage('Twoparallel') {
          steps {
            echo 'Two parallel'
          }
        }

        stage('Twoparallel2') {
          steps {
            sleep 10
          }
        }

      }
    }

    stage('Complete') {
      steps {
        echo 'Done'
      }
    }

  }
}