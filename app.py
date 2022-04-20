import streamlit as st
import altair as alt
import pandas as pd
import numpy as np



def main():

    df = load_data_random()
    df2 = load_data_scrape()
    page = st.sidebar.selectbox("mi a rák ez?", ["Rákok, a bevezetés","kicsirák","nagyrák", "szöveges rák"])

    if page == "Rákok, a bevezetés":
        st.header("Rákok!")
        st.write("nézd meg a rákismertetőt: https://phatslug.github.io/")

    elif page == "kicsirák":
        st.header("óriási, de apró rákok")
        st.write("itt vagyunk a rákoknál, nem mész át a nagyrákra?")
        st.write(df)

    elif page == "nagyrák":
        st.title("ezek a rákok igen nagyok")
        x_axis = st.selectbox("mi legyen az x rákon?", df.columns, index=1)
        y_axis = st.selectbox("mi legyen az y rákon?", df.columns, index=2)

        visual(df, x_axis, y_axis)
    elif page == "szöveges rák":
        st.title("ezek most itt szöveg rák")
        st.write("tiz random rák cikk az indexről, március hóból")
        st.write(df2)
@st.cache
def load_data_random():
    df = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
    return df

@st.cache
def load_data_scrape():
    df2 = pd.read_parquet("napi_tiz.parquet")
    return df2

def visual(df, x_axis, y_axis):
    graph = alt.Chart(df).mark_circle().encode(x = x_axis,y = y_axis, color = "c").interactive()
    st.write(graph)

if __name__ == "__main__":
    main()