import cv2
import numpy as np
import streamlit as st

st.set_page_config(page_title="Comprehensive Bone Analytics", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 2rem; padding-bottom: 2rem;}
</style>
""", unsafe_allow_html=True)

def analyze_bone(image_bytes):
    img_array = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    equalized = cv2.equalizeHist(gray)
    
    kernel = np.array([[-1, -1, -1],
                       [-1,  9, -1],
                       [-1, -1, -1]])
    spatial_filtered = cv2.filter2D(equalized, -1, kernel)
    
    density_map = cv2.applyColorMap(spatial_filtered, cv2.COLORMAP_JET)
    
    blurred_for_edges = cv2.GaussianBlur(spatial_filtered, (5, 5), 0)
    
    laplacian = cv2.Laplacian(blurred_for_edges, cv2.CV_64F)
    laplacian_abs = cv2.convertScaleAbs(laplacian)
    
    _, strong_edges = cv2.threshold(laplacian_abs, 80, 255, cv2.THRESH_BINARY)
    
    edge_overlay = cv2.cvtColor(spatial_filtered, cv2.COLOR_GRAY2BGR)
    edge_overlay[strong_edges == 255] = [0, 255, 0] 
    
    total_pixels = strong_edges.size
    edge_pixels = np.count_nonzero(strong_edges)
    edge_density = (edge_pixels / total_pixels) * 100
    
    return img, equalized, spatial_filtered, density_map, edge_overlay, edge_density

st.title("Dual-View Structural Integrity Analytics")
st.markdown("Full Pipeline: Histogram Eq → Spatial Filter → Density Map → Laplacian Edges")

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Reference Image (Healthy Baseline)")
    upload_healthy = st.file_uploader("Upload Normal Radiograph", type=["png", "jpg", "jpeg"], key="healthy")

with col_b:
    st.subheader("Diagnostic Image (Test Subject)")
    upload_unhealthy = st.file_uploader("Upload Suspected Fracture", type=["png", "jpg", "jpeg"], key="unhealthy")

if upload_healthy and upload_unhealthy:
    with st.spinner("Executing mathematical spatial filtering pipeline..."):
        img1, eq1, spat1, dens1, edge1, score1 = analyze_bone(upload_healthy.read())
        img2, eq2, spat2, dens2, edge2, score2 = analyze_bone(upload_unhealthy.read())
        
        st.divider()
        st.markdown(f"### Mathematical Variance Detected: **{abs(score2 - score1):.2f}%** structural difference")
        
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Raw Radiographs", "Histogram Equalization", "Spatial Filtering", "Density Heatmaps", "Laplacian Edges"])
        
        with tab1:
            r1c1, r1c2 = st.columns(2)
            with r1c1: st.image(img1, caption="Baseline Raw", use_container_width=True, channels="BGR")
            with r1c2: st.image(img2, caption="Test Raw", use_container_width=True, channels="BGR")
            
        with tab2:
            r2c1, r2c2 = st.columns(2)
            with r2c1: st.image(eq1, caption="Baseline Histogram Equalization", use_container_width=True)
            with r2c2: st.image(eq2, caption="Test Histogram Equalization", use_container_width=True)

        with tab3:
            r3c1, r3c2 = st.columns(2)
            with r3c1: st.image(spat1, caption="Baseline Spatial Filtering", use_container_width=True)
            with r3c2: st.image(spat2, caption="Test Spatial Filtering", use_container_width=True)
            
        with tab4:
            r4c1, r4c2 = st.columns(2)
            with r4c1: st.image(dens1, caption="Baseline Density Map", use_container_width=True, channels="BGR")
            with r4c2: st.image(dens2, caption="Test Density Map", use_container_width=True, channels="BGR")
            
        with tab5:
            r5c1, r5c2 = st.columns(2)
            with r5c1: st.image(edge1, caption=f"Baseline Laplacian Edges (Score: {score1:.2f}%)", use_container_width=True, channels="BGR")
            with r5c2: st.image(edge2, caption=f"Test Laplacian Edges (Score: {score2:.2f}%)", use_container_width=True, channels="BGR")