편행 서버의 Ai 학습을 위한 레포지토리 (ReadME 수정 필요)

- 각 데이터 Set : 500EA
- Train data : 400EA, Validate Data : 100EA

### 분류 기준

-> beverage : 음료수류 (우유, 탄산음료, 이온음료, 페트류, 술)
-> dailyneccersity : 생필품 (휴지, 물티슈, 칫솔, 치약, 왁스, 섬유유연제, 세제)
-> iceCream : 아이스크림 (바, 콘, 컵)
-> instanceFood : 즉석제품 (라면, 컵라면, 컵밥, 즉석밥, 냉동식품류)

-> Foods : 식품 (스팸, 리챔, 소세지, 안주류)
-> Snack : 과자

### 모델 성능

- [Test Phase] Loss: 0.5482 Acc: 91.2222% Time: 20.1917s

### 개선 예정

- 정확도가 아주 높은편이 아님, 클래스를 세분화 하여 모델의 정확도를 높히는 편이 좋을것으로 분석
