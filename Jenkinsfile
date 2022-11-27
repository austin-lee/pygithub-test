/*
 * Jenkins File
 * python 3.9 기준 빌드이므로 docker image 는 python 3.9 로 설정
 * Jenkins 빌드 기준 설정 필요 (GitHub Pull Request Builder)
 * Stage 는 파라미터에 python 파일 실행하는 스크립트로 작성
 */

pipeline{
    agent any
    stages {
        //Excute Script
        stage('Execute Script') {
            steps{
                echo 'Execute Script'
                script {
                  sh """
                    python3.9 /Users/austin.lee/Develop/line_test/python_project/python_ci.py --access-token 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 --repo-name austin-lee/pygithub-test --accounts bot1 bot2 --pr-num 6
                  """
                }
                post {
                    failure {
                      error 'This pipeline stops here...'
                    }
                }
            }
        }
    }
}
