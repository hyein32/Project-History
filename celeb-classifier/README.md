# 사진(연예인) 분류 머신러닝 서비스

수원대학교 데이터과학부 신혜인

사진을 올리면 AI가 얼굴을 분석해 **조유리 · 최예나 · 김채원** 세 명 중 누구와 가장 닮았는지 알려주는 웹 서비스입니다.

## 주요 기능
- 사진 업로드: 클릭하거나 드래그해서 이미지를 올립니다.
- 닮은꼴 분석: 가장 높은 확률의 인물과 소개를 보여줍니다.
- 확률 막대 그래프: 세 인물 각각의 닮은 정도(%)를 한눈에 비교합니다.
- 다시 시도: 버튼 하나로 다른 사진을 다시 분석합니다.
- 반응형 디자인: 모바일 화면에서도 볼 수 있습니다.

## 사용한 기술
- [Teachable Machine](https://teachablemachine.withgoogle.com/) 이미지 분류 모델 (입력 크기 224×224, 클래스 3개)
- TensorFlow.js, `@teachablemachine/image`
- HTML / CSS / JavaScript, Bootstrap 4, jQuery

모든 분석은 브라우저 안에서 이루어지며 사진은 서버로 전송되지 않습니다.

## 폴더 구조
```
index.html            # 화면과 분류 로직
mltest_files/
├─ model.json         # 모델 구조
├─ weights.bin        # 모델 가중치
├─ metadata.json      # 클래스 이름 등 메타데이터
├─ style.css          # 디자인
└─ ...                # 라이브러리(tf.min.js 등), 이미지
```

## 실행 방법
모델 파일을 불러오기 때문에 `index.html`을 바로 열지 말고 간단한 웹 서버로 실행해야 합니다.

```bash
python3 -m http.server 6000 --bind 0.0.0.0
```

브라우저에서 `http://localhost:6000/`으로 접속합니다.

## 참고
- 제작 도움: 조코딩 유튜브 채널
- 업로드 영역 스타일: Aaron Vanston의 CodePen (MIT License)
- 분류 결과는 재미를 위한 것이며 실제 닮은 정도를 보장하지 않습니다.
