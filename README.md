# Storyboarder PRD Skills

Storyboarder는 일관된 구조의 PRD를 생성/로드하는 Codex 스킬 세트입니다. FE/BE 범위 선택을 지원하며 `PRD-<project>.md` 파일을 현재 프로젝트 경로에 저장합니다.

## 기능
- FE/BE 범위 선택 기반 PRD 인터뷰
- 역할별 섹션을 포함한 일관된 PRD 템플릿
- PRD 로더로 완성도 검증 및 누락 섹션 안내
- 문서(pptx/pdf/xlsx/md)에서 내용 추출 후 PRD 자동 채움
- 프로젝트 로컬 스킬을 글로벌 Codex 스킬로 동기화 가능

## 시작하기

1) 스킬을 글로벌 Codex 스킬로 동기화

```bash
rsync -a ./skills/ ~/.codex/skills/
```

2) PRD 인터뷰 시작

```text
$prd-author
```

3) 문서 기반으로 PRD 채우기 (선택)

```bash
./skills/prd-author/scripts/extract_doc_text.py <file1> <file2> --out extracted.txt
```

4) 기존 PRD 로드

```text
$prd-loader
```

5) 템플릿에서 PRD 파일 직접 생성 (옵션)

```bash
./skills/prd-author/scripts/init_prd.py --project <name> --role fe|be|both --outdir . --owner <owner>
```

## PRD 예시

```text
$prd-author
# 범위: BE
# 프로젝트명: translateReview
# 소유자: 86lyh

결과 파일: PRD-translatereview.md
```

## FAQ

Q. PRD 파일명 규칙은?
- `PRD-<project>.md` 형식이며 `<project>`는 소문자 슬러그로 저장됩니다.

Q. PRD가 이미 있을 때는?
- `prd-author`는 덮어쓰기 전에 확인합니다. `prd-loader`는 PRD를 읽고 누락 섹션을 알려줍니다.

Q. FE/BE 범위를 나중에 바꿀 수 있나요?
- 네. 필요 시 범위를 다시 선택해 해당 섹션을 추가/보완하면 됩니다.

Q. 문서 추출이 실패하면?
- `pdfplumber`, `PyPDF2`, `python-pptx`, `openpyxl` 중 필요한 라이브러리가 없을 수 있습니다. 설치 후 재시도하거나, 핵심 내용을 복사해 PRD 인터뷰에 입력하면 됩니다.

## TODO
- 실제 PRD에서 BE 섹션 상세(도메인 모델, API, 데이터 스토어, 인증, 비동기, 관측성, 스케일링, 보안, 마이그레이션, 테스트) 채우기
- 지연 외 성공 지표(정확도/품질 기준) 정의
- 스코프 in/out 및 사용자 페르소나 구체화
