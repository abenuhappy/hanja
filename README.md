# 한자 학습 게임 (Hanja Learning Game)

초등, 중등, 고등학생을 위한 필수 한자 학습 웹 애플리케이션입니다.

## 🚀 배포 방법 (GitHub + Vercel)

모바일 브라우저에서 실행하기 위해 GitHub와 Vercel을 사용하여 배포하는 단계입니다.

### 1단계: GitHub에 코드 올리기
1.  GitHub에서 새로운 저장소(Repository)를 생성합니다.
2.  터미널에서 다음 명령어를 실행하여 코드를 업로드합니다:
    ```bash
    git init
    git add .
    git commit -m "Initial commit: Hanja learning game"
    git branch -M main
    git remote add origin https://github.com/사용자아이디/저장소이름.git
    git push -u origin main
    ```

### 2단계: Vercel에 연결하기
1.  [Vercel](https://vercel.com/)에 로그인합니다 (GitHub 계정 사용 권장).
2.  **Add New...** > **Project**를 클릭합니다.
3.  방금 생성한 GitHub 저장소를 선택하고 **Import**를 누릅니다.
4.  **Deploy** 버튼을 누르면 배포가 완료됩니다!
5.  제공되는 URL을 통해 모바일에서 접속할 수 있습니다.

## 🛠️ 주요 기능
- 중학교(900자) / 고등학교(900자) 과정 선택
- 발음 및 뜻 풀이 퀴즈 (Type A/B)
- 실시간 피드백 및 취약 한자 복습 기능
- 모바일 우선 반응형 디자인
