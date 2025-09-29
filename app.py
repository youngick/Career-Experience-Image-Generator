import streamlit as st
import base64
import json
from io import BytesIO
from PIL import Image
from strands import Agent
from strands_tools import generate_image

# 다국어 텍스트 정의
TEXTS = {
    "ko": {
        "page_title": "직업 체험 이미지 생성기",
        "title": "🎨 직업 체험 이미지 생성기",
        "description": "성별과 원하는 직업을 선택하면 AI가 이미지를 생성해드립니다!",
        "settings": "설정",
        "language": "언어:",
        "gender_label": "성별을 선택하세요:",
        "job_label": "원하는 직업을 선택하세요:",
        "generate_btn": "이미지 생성하기",
        "selected_info": "선택한 정보",
        "gender": "성별:",
        "job": "직업:",
        "generating": "이미지를 생성하고 있습니다...",
        "generated_image": "생성된 이미지",
        "download_btn": "이미지 다운로드",
        "error": "이미지 생성 중 오류가 발생했습니다:",
        "info": "AWS 자격 증명과 Bedrock 서비스 접근 권한을 확인해주세요.",
        "usage": "💡 **사용법:** 왼쪽에서 성별과 직업을 선택한 후 '이미지 생성하기' 버튼을 클릭하세요!",
        "genders": ["남자", "여자"],
        "jobs": ["요리사", "경찰관", "소방관", "우주비행사", "학교 선생님", "의사", "간호사", "파일럿", "과학자", "예술가"]
    },
    "en": {
        "page_title": "Career Experience Image Generator",
        "title": "🎨 Career Experience Image Generator",
        "description": "Select gender and desired job, and AI will generate an image for you!",
        "settings": "Settings",
        "language": "Language:",
        "gender_label": "Select gender:",
        "job_label": "Select desired job:",
        "generate_btn": "Generate Image",
        "selected_info": "Selected Information",
        "gender": "Gender:",
        "job": "Job:",
        "generating": "Generating image...",
        "generated_image": "Generated Image",
        "download_btn": "Download Image",
        "error": "An error occurred while generating the image:",
        "info": "Please check your AWS credentials and Bedrock service access permissions.",
        "usage": "💡 **How to use:** Select gender and job on the left, then click 'Generate Image' button!",
        "genders": ["Male", "Female"],
        "jobs": ["Chef", "Police Officer", "Firefighter", "Astronaut", "Teacher", "Doctor", "Nurse", "Pilot", "Scientist", "Artist"]
    }
}

# Streamlit 페이지 설정
st.set_page_config(page_title="Career Experience Image Generator", page_icon="👨‍💼", layout="wide")

# 언어 선택 (세션 상태로 관리)
if 'language' not in st.session_state:
    st.session_state.language = 'ko'

# 상단에 언어 선택
col_lang1, col_lang2, col_lang3 = st.columns([1, 1, 8])
with col_lang1:
    if st.button("한국어", type="secondary" if st.session_state.language == 'en' else "primary"):
        st.session_state.language = 'ko'
        st.rerun()
with col_lang2:
    if st.button("English", type="secondary" if st.session_state.language == 'ko' else "primary"):
        st.session_state.language = 'en'
        st.rerun()

# 현재 언어 텍스트 가져오기
t = TEXTS[st.session_state.language]

st.title(t["title"])
st.write(t["description"])

# 사이드바에 입력 컨트롤
with st.sidebar:
    st.header(t["settings"])
    
    # 성별 선택
    gender = st.selectbox(
        t["gender_label"],
        t["genders"]
    )
    
    # 직업 선택
    job = st.selectbox(
        t["job_label"],
        t["jobs"]
    )
    
    # 이미지 생성 버튼
    generate_btn = st.button(t["generate_btn"], type="primary")

# 메인 영역
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader(t["selected_info"])
    st.write(f"**{t['gender']}** {gender}")
    st.write(f"**{t['job']}** {job}")

with col2:
    if generate_btn:
        with st.spinner(t["generating"]):
            try:
                # 프롬프트 생성 (언어별 매핑)
                if st.session_state.language == 'ko':
                    gender_eng = "man" if gender == "남자" else "woman"
                    job_mapping = {
                        "요리사": "chef", "경찰관": "police officer", "소방관": "firefighter",
                        "우주비행사": "astronaut", "학교 선생님": "teacher", "의사": "doctor",
                        "간호사": "nurse", "파일럿": "pilot", "과학자": "scientist", "예술가": "artist"
                    }
                    job_eng = job_mapping.get(job, job)
                else:
                    gender_eng = "man" if gender == "Male" else "woman"
                    job_eng = job.lower().replace(" ", " ")
                
                prompt = f"Professional portrait photograph of a korean {gender_eng} working as a {job_eng}, photorealistic, high resolution, studio lighting, sharp focus, detailed facial features, professional attire, natural skin texture, realistic hair, commercial photography style, 8K quality"
                
                # Strands Agent를 사용한 이미지 생성
                agent = Agent(tools=[generate_image])
                
                # stability.stable-image-core-v1:1 모델 사용
                # 현재 agent tool 에서 사용 가능한 이미지 생성 모델은 stability.sd3-5-large-v1:0, stability.stable-image-core-v1:1, stability.stable-image-ultra-v1:1
                # 위 모델들의 리전도 제한적이며 다음 링크에서 확인 https://docs.aws.amazon.com/ko_kr/bedrock/latest/userguide/model-lifecycle.html
                result = agent.tool.generate_image(
                    prompt=prompt,
                    region="us-west-2",
                    model="stability.stable-image-core-v1:1"
                )
                
                # 결과에서 이미지 데이터 추출
                image_bytes = None
                if result and result.get("status") == "success" and "content" in result:
                    # content에서 이미지 찾기
                    for content_item in result["content"]:
                        if isinstance(content_item, dict) and "image" in content_item:
                            if "source" in content_item["image"] and "bytes" in content_item["image"]["source"]:
                                image_bytes = content_item["image"]["source"]["bytes"]
                                break
                
                if not image_bytes:
                    raise Exception(f"No image data found in response. Result: {result}")
                
                # 이미지 표시
                image = Image.open(BytesIO(image_bytes))
                st.subheader(t["generated_image"])
                st.image(image, caption=f"{gender} {job}", width='stretch')
                
                # 다운로드 버튼
                st.download_button(
                    label=t["download_btn"],
                    data=image_bytes,
                    file_name=f"{gender}_{job}.png",
                    mime="image/png"
                )
                
            except Exception as e:
                st.error(f"{t['error']} {str(e)}")
                # 디버깅을 위한 상세 정보
                if hasattr(e, '__dict__'):
                    st.write("Error details:", e.__dict__)
                st.info(t["info"])

# 하단 정보
st.markdown("---")
st.markdown(t["usage"])
