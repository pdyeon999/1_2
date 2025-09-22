### SKN19-mini-5Team
EDA / ML mini project 5Team

# 도쿄 숙소값 예측 프로젝트

### 🙋 팀 소개
| 이름    | 김범섭 |  박도연  |  이상혁  |  이승원   |
| ------- | -------|----------|----------|---------- |
| git |        | pdyeon999 |          |          |



### 2. 프로젝트 개요
- 프로젝트 명: 도쿄 여행객들을 위한 숙소값 예측
- 프로젝트 소개: 에어비앤비에서 제공하는 도쿄 숙소 리스트를 기반으로 숙소 조건과 가격의 관계를 분석함
- 프로젝트 목표: 숙소 조건과 가격의 유의미한 관계를 포착하고, 나아가 조건별 숙소값을 예측


- 에어비앤비에서 제공하는 데이터셋 분석으로 예약 가능 여부와 상관없이 숙소의 조건에 따른 가격 예측 가능


### 3. 기술 스택
| 분야 |	기술 |
|------|---------|
|언어 |  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 3.12 |
|개발 환경|	Jupyter Notebook| 
|데이터 처리|	Pandas, NumPy|
|시각화|	Matplotlib (pyplot), Seaborn|
|버전 관리|<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white"> |

### 4. WBS


### 📑 데이터셋
- 파일명: `tokyo_listings.csv.gz`
- 주요 칼럼: 숙소별 room type, 침실 개수, 1박당 가격 등
- 데이터 출처: [Airbnb](https://insideairbnb.com/)


### 6. EDA
**0. 프로젝트 방향 선정**
    - 숙소값에 큰 영향을 미치는 날짜별 가격 데이터를 조회
    - 성수기에 따른 추가 가격은 에어비앤비 측에서 미제공
    -

**1. 데이터 로드**
```
df = pd.read_csv('./data/listings.csv.gz', compression='gzip')
```
**2. 데이터 구조 및 기초 통계 확인**
    - 데이터의 구조를 파악하기 위해 컬럼 정보와 데이터 타입을 확인한다.
    - 데이터의 기본 통계 정보를 출력하여 각 변수의 분포와 특성을 살펴본다.
    - df.head(), df.tail(), df.info(), df.describe() 등의 함수를 사용한다.

    
**3. 결측치 및 이상치 탐색**
    - 결측치(NaN) 값이 존재하는지 확인하고, 이를 처리하는 방법을 결정한다.
    - 데이터에 존재하는 이상치(Outlier)를 탐지하고, 이를 어떻게 처리할지 결정한다.
    - df.isnull().sum(), df.boxplot() 등의 함수를 활용한다.
    
**4. 데이터 시각화를 통한 탐색**
    - 데이터를 시각화하여 변수 간의 관계, 분포 등을 파악한다.
    - 히스토그램, 박스플롯, 상관관계 행렬 등 다양한 그래프를 통해 데이터의 특성을 시각적으로 확인한다.
    - sns.countplot(), sns.heatmap() 등의 함수를 사용한다.
    
**5. 데이터 정제 및 전처리**
