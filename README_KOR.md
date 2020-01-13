# 사용법

이 프로젝트를 클론 하신 뒤, 프로젝트의 경로를 숙지하도록 하세요.
이후 "GPU_CHANGER" 라는 파일을 생성하고 (혹은 원하는것 아무거나 괜찮습니다.), 그리고 다음의 명령어를 실행하여 권한을 주도록 하세요.

```bash
chmod u+x GPU_CHANGER
```

그리고서는 GPU_CHANGER에 다음과 같이 적어주세요.

```bash
#!/usr/bin/env bash
python3 {이곳에 해당 파이썬 스크립트의 경로를 적어주세요} &;
```

그리고는, "시스템 환결설정" -> "사용자 & 그룹" -> "로그인 항목", '+' 버튼을 클릭하시고, 생성한 "GPU_CHANGER"를 선택해서 추가해주세요.

수고하셨습니다!