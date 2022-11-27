/*
 * Jenkins File
 * agent 는 any 로 되어 있으나, docker 를 이용하여 빌드 환경이 구성 가능합니다.
 * Push Request 에 대한 설정은 GitHub Pull Request Builder 를 이용하여 구성을 하였습니다.
 * Git repository 에 webhook 으로 http://{jenkins_url}/ghprbhook 설정을 하였습니다.
 * pipeline 의 Stage 에 python 파일 실행하는 Script 로 작성하였고,
 * python Script 에 사용되는 Argument 는 github pull reqeust builder 의 parameter 를 이용하여 생성하였습니다.
 * accounts 의 경우, parameter 에 입력을 받도록 하였습니다.
 * python script 실행 전, PyGithub Library 를 설치 후, 실행하도록 작성하였습니다.
 * Refspec setting : +refs/pull/${ghprbPullId}/*:refs/remotes/origin/pr/${ghprbPullId}/*
 * Branch Specifier setting : ${ghprbActualCommit}
 */

pipeline{
    agent any
    parameters {
        text(
            name: 'SKIP_ACCOUNT',
            defaultValue: '''bot1
bot2 ''',
            description: 'account info'
        )
    }
    stages {
        //Excute Script
        stage('Execute Script') {
            environment {
                GITHUB_ACCESS_TOKEN = credentials("${env.ghprbCredentialsId}")
            }
            steps{
                echo 'Execute Script'
                script {
                    def skip_accounts = params.SKIP_ACCOUNT.replace("\n", " ")
                    sh """
                        pip3 install PyGithub
                        python3 3-1.py --access-token ${env.GITHUB_ACCESS_TOKEN} --repo-name ${env.ghprbGhRepository} --accounts ${skip_accounts} --pr-num ${env.ghprbPullId}
                       """
                }
            }
        }
    }
}
