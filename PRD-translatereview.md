# PRD - translateReview

- Date: 2026-01-20
- Owner: 86lyh
- Status: Draft
- Scope: BE

## 1. Problem / Opportunity
- 호텔 상세 페이지의 제휴사 리뷰를 자동 번역해야 함

## 2. Goals
- AI 번역으로 정확도 향상
- 신속한 번역 처리
- 제휴사 리뷰만 대상으로 안정적으로 처리

## 3. Non-goals
- 호텔 상세의 제휴사 리뷰가 아닌 콘텐츠는 대상 아님

## 4. Users / Personas
- 직접 사용자

## 5. Scope
- In scope:
  - AIController에서 시작하는 번역 흐름
- Out of scope:
  - 호텔 상세의 제휴사 리뷰 외 콘텐츠

## 6. Requirements
### 6.1 Functional
- 번역 트리거 제공

### 6.2 Non-functional
- 번역 속도 성능이 좋아야 함

## 7. User Stories / Use Cases
- 사용자가 호텔 상세 페이지에 진입하면 익스피디아, 호텔스닷컴 등의 제휴사 리뷰가 빠르게 번역되어 보여야 함

## 8. Success Metrics
- 번역 응답 지연 10초 내외

## 9. Risks / Assumptions
- LLM 번역 엔드포인트 노출로 인한 오남용 방지 필요

## 10. Milestones
- 개발
- 테스트
- QA
- 배포

## 11. Open Questions
- TBD

## 12. References
- TBD


<!-- BE_SECTION_START -->
## BE Section

### Domain Model
- TBD

### API Endpoints
- TBD

### Data Store / Schema
- TBD

### Auth / AuthZ
- TBD

### Async / Jobs
- TBD

### Observability
- TBD

### Scaling / Performance
- TBD

### Security
- TBD

### Migration / Backfill
- TBD

### BE Testing
- TBD
<!-- BE_SECTION_END -->
