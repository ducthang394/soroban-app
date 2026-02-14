import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Báo cáo kinh doanh", layout="wide")

st.title("📊 Báo cáo kết quả kinh doanh")

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=[
        "Ngày", "Doanh thu", "Chi phí", "Lợi nhuận", "Ghi chú"
    ])

st.subheader("➕ Nhập dữ liệu")

col1, col2, col3 = st.columns(3)

with col1:
    ngay = st.date_input("Ngày", date.today())

with col2:
    doanh_thu = st.number_input("Doanh thu", 0)

with col3:
    chi_phi = st.number_input("Chi phí", 0)

ghi_chu = st.text_input("Ghi chú")

if st.button("Lưu"):
    loi_nhuan = doanh_thu - chi_phi
    new_row = pd.DataFrame([{
        "Ngày": ngay,
        "Doanh thu": doanh_thu,
        "Chi phí": chi_phi,
        "Lợi nhuận": loi_nhuan,
        "Ghi chú": ghi_chu
    }])

    st.session_state.data = pd.concat([st.session_state.data, new_row], ignore_index=True)
    st.success("Đã lưu!")

st.subheader("📋 Dữ liệu")

st.dataframe(st.session_state.data, use_container_width=True)

if not st.session_state.data.empty:

    tong_doanh_thu = st.session_state.data["Doanh thu"].sum()
    tong_chi_phi = st.session_state.data["Chi phí"].sum()
    tong_loi_nhuan = st.session_state.data["Lợi nhuận"].sum()

    col1, col2, col3 = st.columns(3)

    col1.metric("Tổng doanh thu", f"{tong_doanh_thu:,}")
    col2.metric("Tổng chi phí", f"{tong_chi_phi:,}")
    col3.metric("Tổng lợi nhuận", f"{tong_loi_nhuan:,}")

    csv = st.session_state.data.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Tải Excel",
        csv,
        "baocao.csv",
        "text/csv"i
    )
