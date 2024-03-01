import requests
import sys

# 커맨드 라인 인자로 파일 경로 받기
if len(sys.argv) > 1:
    file_path = sys.argv[1]  # 첫 번째 인자로 파일 경로 지정
    print(f"파일 경로: {file_path}")
else:
    print("파일 경로를 인자로 제공해주세요.")
    sys.exit()

def get_gofile_server():
    print("GoFile 서버 정보를 가져오는 중...")
    try:
        response = requests.get('https://api.gofile.io/getServer')
        data = response.json()
        if data['status'] == 'ok':
            print(f"서버 정보 받기 성공: {data['data']['server']}")
            return data['data']['server']
        else:
            print("서버 정보를 가져오는데 실패했습니다.")
            return None
    except requests.RequestException as e:
        print(f"서버 정보 요청 중 오류 발생: {e}")
        return None

def upload_file_to_gofile(file_path, server):
    print(f"{server} 서버로 파일 업로드를 시도합니다.")
    url = f'https://{server}.gofile.io/uploadFile'
    try:
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(url, files=files)
            data = response.json()
            if data['status'] == 'ok':
                # 파일 업로드 성공 시 다운로드 페이지 URL만 출력
                print("파일 업로드 성공, 다운로드 링크:", data['data']['downloadPage'])
            else:
                print("파일 업로드 실패")
    except requests.RequestException as e:
        print(f"파일 업로드 중 오류 발생: {e}")

server = get_gofile_server()
if server:
    upload_file_to_gofile(file_path, server)
else:
    print("유효한 서버 정보를 받지 못했습니다.")
