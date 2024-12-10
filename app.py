import streamlit as st
import home
import seiren
import seizou

# タイトルを表示
st.set_page_config(page_title="素材計算アプリ", layout="wide")

sideber, main = st.columns([1, 3])

# サイドバーのメニュー
with sideber:
    menu = st.radio("メニュー", ("ホーム", "精錬素材計算", "製造素材計算"))

# メニューに応じてページを切り替える

with main:
    if menu == "ホーム":
        home.app()  # home.py の app 関数を呼び出し
    elif menu == "精錬素材計算":
        seiren.app()  # seiren.py の app 関数を呼び出し
    elif menu == "製造素材計算":
        seizou.app()  # seizou.py の app 関数を呼び出し
