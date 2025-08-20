import streamlit as st

# Sidebar
st.sidebar.markdown("Clicked Page 1")
st.sidebar.markdown("Side Menu")
st.sidebar.button("Click")
st.sidebar.radio("성별", ["여자", "남자"])

# Page
st.title("Page 1")
st.markdown("Mark Down")
st.header("Header")
st.subheader("Sub Header")
st.caption("Caption")
st.code("""
def func():
    print("OK!")
def func2():
    print("OK@")
""", language="python")

st.code("""
#include <stdio.h>

int main() {
    printf("혜주");

    return 0;
}
""", language="c")