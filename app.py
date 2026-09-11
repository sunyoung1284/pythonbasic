import sys
# 1. 변수 선언 및 기본 정보
project_name = "My First Work Log"
version = 1.0
# 2. 콘솔 안내 메시지 출력
print("=" * 40)
print(f"프로젝트 이름: {project_name} (v{version})")
print(f"현재 실행 중인 Python 버전: {sys.version.split()[0]}")
print("=" * 40)
# 3. 간단한 계산 로직
daily_tasks = 4
completed_tasks = 3
progress = (completed_tasks / daily_tasks) * 100
print(f"오늘 처리한 업무 진척도: {progress:.1f}%")