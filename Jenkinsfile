/*
 * Jenkins File
 * python 3.9 기준 빌드이므로 docker image 는 python 3.9 로 설정
 * Jenkins 빌드 기준 설정 필요
 * Stage 는 파라미터에 python 파일 실행하는 스크립트로 작성
 */

pipeline{
  stages{
    //dockerbuild
    stage('Bulid Docker'){
      agent any
      steps{
        echo 'Bulid Docker'
        script{
          dockerImage=docker.build("${imagename}:${version}",
          "--no-cache .")
        }
      }post{
        failure{
          error 'This pipeline stops here...'
        }
      }
    }
    //dockerDeploy
    stage('Deploy Docker'){
      agent any
      steps{
        echo 'Deploy Docker '
        sh 'tag=${version} docker-compose -f ./docker/docker-compose.yml up -d'
      }post{
        failure{
          error 'This pipeline stops here...'
        }
      }
    }
    //docker push
    stage('Push Docker'){
      agent any
      steps{
        echo 'Push Docker'
        script{
          docker.withRegistry('',
          registryCredential){
            dockerImage.push(version)//ex)"1.0"
          }
        }
      }post{
        failure{
          error 'This pipeline stops here...'
        }
      }
    }
  }
}
