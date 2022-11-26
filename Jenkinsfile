/*
 *  
 */

pipeline{
  stages{
    //dockerbuildstage('Bulid Docker'){
      agentanysteps{
        echo'Bulid Docker'script{
          dockerImage=docker.build("${imagename}:${version}",
          "--no-cache .")
        }
      }post{
        failure{
          error'This pipeline stops here...'
        }
      }
    }//dockerDeploystage('Deploy Docker'){
      agentanysteps{
        echo'Deploy Docker 'sh'tag=${version} docker-compose -f ./docker/docker-compose.yml up -d'
      }post{
        failure{
          error'This pipeline stops here...'
        }
      }
    }//dockerpushstage('Push Docker'){
      agentanysteps{
        echo'Push Docker'script{
          docker.withRegistry('',
          registryCredential){
            dockerImage.push(version)//ex)"1.0"
          }
        }
      }post{
        failure{
          error'This pipeline stops here...'
        }
      }
    }
  }
}
