import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np

# 그림 크기 설정
fig, ax = plt.subplots(1, 1, figsize=(14, 10))
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# 색상 정의
aws_orange = '#FF9900'
streamlit_red = '#FF4B4B'
stability_blue = '#4A90E2'
strands_green = '#00C851'

# 제목
ax.text(7, 9.5, 'Career Experience Image Generator Architecture', 
        fontsize=18, fontweight='bold', ha='center')

# 1. 사용자 인터페이스 (Streamlit)
streamlit_box = FancyBboxPatch((1, 7), 3, 1.5, 
                               boxstyle="round,pad=0.1", 
                               facecolor=streamlit_red, 
                               edgecolor='black', 
                               alpha=0.8)
ax.add_patch(streamlit_box)
ax.text(2.5, 7.75, 'Streamlit UI', fontsize=12, fontweight='bold', 
        ha='center', va='center', color='white')
ax.text(2.5, 7.4, '• Multi-language (KR/EN)', fontsize=9, ha='center', va='center', color='white')
ax.text(2.5, 7.1, '• Gender/Job Selection', fontsize=9, ha='center', va='center', color='white')

# 2. Strands Agent
strands_box = FancyBboxPatch((6, 7), 3, 1.5, 
                             boxstyle="round,pad=0.1", 
                             facecolor=strands_green, 
                             edgecolor='black', 
                             alpha=0.8)
ax.add_patch(strands_box)
ax.text(7.5, 7.75, 'Strands Agent', fontsize=12, fontweight='bold', 
        ha='center', va='center', color='white')
ax.text(7.5, 7.4, '• AI Agent Framework', fontsize=9, ha='center', va='center', color='white')
ax.text(7.5, 7.1, '• generate_image Tool', fontsize=9, ha='center', va='center', color='white')

# 3. AWS Bedrock
aws_box = FancyBboxPatch((10.5, 7), 3, 1.5, 
                         boxstyle="round,pad=0.1", 
                         facecolor=aws_orange, 
                         edgecolor='black', 
                         alpha=0.8)
ax.add_patch(aws_box)
ax.text(12, 7.75, 'AWS Bedrock', fontsize=12, fontweight='bold', 
        ha='center', va='center', color='white')
ax.text(12, 7.4, '• Managed AI Service', fontsize=9, ha='center', va='center', color='white')
ax.text(12, 7.1, '• Model Hosting', fontsize=9, ha='center', va='center', color='white')

# 4. Stability AI 모델
stability_box = FancyBboxPatch((6, 4.5), 3, 1.5, 
                               boxstyle="round,pad=0.1", 
                               facecolor=stability_blue, 
                               edgecolor='black', 
                               alpha=0.8)
ax.add_patch(stability_box)
ax.text(7.5, 5.25, 'Stability AI', fontsize=12, fontweight='bold', 
        ha='center', va='center', color='white')
ax.text(7.5, 4.9, 'stable-image-core-v1:1', fontsize=10, ha='center', va='center', color='white')
ax.text(7.5, 4.6, '• Image Generation Model', fontsize=9, ha='center', va='center', color='white')

# 5. 데이터 플로우 화살표
# Streamlit -> Strands Agent
ax.annotate('', xy=(6, 7.75), xytext=(4, 7.75),
            arrowprops=dict(arrowstyle='->', lw=2, color='black'))
ax.text(5, 8, 'User Input', fontsize=9, ha='center', va='bottom')

# Strands Agent -> AWS Bedrock
ax.annotate('', xy=(10.5, 7.75), xytext=(9, 7.75),
            arrowprops=dict(arrowstyle='->', lw=2, color='black'))
ax.text(9.75, 8, 'API Call', fontsize=9, ha='center', va='bottom')

# AWS Bedrock -> Stability AI
ax.annotate('', xy=(7.5, 6.5), xytext=(12, 7),
            arrowprops=dict(arrowstyle='->', lw=2, color='black'))
ax.text(10, 6.5, 'Model Invoke', fontsize=9, ha='center', va='bottom')

# Stability AI -> Strands Agent (응답)
ax.annotate('', xy=(7.5, 6.5), xytext=(7.5, 6),
            arrowprops=dict(arrowstyle='->', lw=2, color='green'))
ax.text(8.5, 6.25, 'Image Generated', fontsize=9, ha='left', va='center', color='green')

# Strands Agent -> Streamlit (응답)
ax.annotate('', xy=(4, 7.25), xytext=(6, 7.25),
            arrowprops=dict(arrowstyle='->', lw=2, color='green'))
ax.text(5, 6.9, 'Image Response', fontsize=9, ha='center', va='top', color='green')

# 6. 기술 스택 정보
tech_box = FancyBboxPatch((1, 2), 12, 1.5, 
                          boxstyle="round,pad=0.1", 
                          facecolor='lightgray', 
                          edgecolor='black', 
                          alpha=0.3)
ax.add_patch(tech_box)
ax.text(7, 3.2, 'Technology Stack', fontsize=14, fontweight='bold', ha='center')
ax.text(3, 2.7, '• Frontend: Streamlit (Python)', fontsize=10, ha='left')
ax.text(3, 2.4, '• AI Agent: Strands Agent Framework', fontsize=10, ha='left')
ax.text(8, 2.7, '• Cloud: AWS Bedrock', fontsize=10, ha='left')
ax.text(8, 2.4, '• AI Model: Stability AI Image Generation', fontsize=10, ha='left')

# 7. 워크플로우 설명
workflow_box = FancyBboxPatch((1, 0.2), 12, 1.3, 
                              boxstyle="round,pad=0.1", 
                              facecolor='lightyellow', 
                              edgecolor='black', 
                              alpha=0.5)
ax.add_patch(workflow_box)
ax.text(7, 1.2, 'Workflow', fontsize=14, fontweight='bold', ha='center')
ax.text(1.5, 0.8, '1. User selects gender and job', fontsize=10, ha='left')
ax.text(1.5, 0.5, '2. Strands Agent generates prompt', fontsize=10, ha='left')
ax.text(7.5, 0.8, '3. Call Stability AI model via AWS Bedrock', fontsize=10, ha='left')
ax.text(7.5, 0.5, '4. Display generated image and provide download', fontsize=10, ha='left')

# 로고/아이콘 표시 (텍스트로 대체)
ax.text(2.5, 6.7, 'STREAMLIT', fontsize=8, ha='center', va='center', 
        color='white', fontweight='bold', style='italic')
ax.text(7.5, 6.7, 'STRANDS', fontsize=8, ha='center', va='center', 
        color='white', fontweight='bold', style='italic')
ax.text(12, 6.7, 'AWS', fontsize=8, ha='center', va='center', 
        color='white', fontweight='bold', style='italic')
ax.text(7.5, 4.3, 'STABILITY AI', fontsize=8, ha='center', va='center', 
        color='white', fontweight='bold', style='italic')

plt.tight_layout()
plt.savefig('/home/ubuntu/environment/agent-test/architecture_diagram.png', 
            dpi=300, bbox_inches='tight', facecolor='white')
plt.close()

print("Architecture diagram saved as 'architecture_diagram.png'")
