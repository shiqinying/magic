
import os,sys
import streamlit as st

import pandas as pd


CURRENT_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

df_万城万充_base = pd.read_excel(os.path.join('result_data','万城万充_base.xlsx'))
df_万城万充_terminal = pd.read_excel(os.path.join('result_data','万城万充_terminal.xlsx'))
df_云快充_base= pd.read_excel(os.path.join('result_data','云快充_base.xlsx'))
df_云快充_terminal = pd.read_excel(os.path.join('result_data','云快充_terminal.xlsx'))
df_充电圈_base = pd.read_excel(os.path.join('result_data','充电圈_base.xlsx'))
df_充电圈_terminal = pd.read_excel(os.path.join('result_data','充电圈_terminal.xlsx'))
df_小桔充电_base = pd.read_excel(os.path.join('result_data','小桔充电_base.xlsx'))
df_小桔充电_terminal = pd.read_excel(os.path.join('result_data','小桔充电_terminal.xlsx'))
df_星星充电_base = pd.read_excel(os.path.join('result_data','星星充电_base.xlsx'))
df_星星充电_terminal = pd.read_excel(os.path.join('result_data','星星充电_terminal.xlsx'))
df_汇充电_base = pd.read_excel(os.path.join('result_data','汇充电_base.xlsx'))
df_汇充电_terminal = pd.read_excel(os.path.join('result_data','汇充电_terminal.xlsx'))
df_象前充_base = pd.read_excel(os.path.join('result_data','象前充_base.xlsx'))
df_象前充_terminal = pd.read_excel(os.path.join('result_data','象前充_terminal.xlsx'))


st.title('df_万城万充_base')
df_万城万充_base
st.title('df_万城万充_terminal')
df_万城万充_terminal
st.title('df_云快充_base')
df_云快充_base
st.title('df_云快充_terminal')
df_云快充_terminal
st.title('df_充电圈_base')
df_充电圈_base
st.title('df_充电圈_terminal')
df_充电圈_terminal
st.title('df_小桔充电_base')
df_小桔充电_base
st.title('df_小桔充电_terminal')
df_小桔充电_terminal
st.title('df_星星充电_base')
df_星星充电_base
st.title('df_星星充电_terminal')
df_星星充电_terminal
st.title('df_汇充电_base')
df_汇充电_base
st.title('df_汇充电_terminal')
df_汇充电_terminal
st.title('df_象前充_base')
df_象前充_base
st.title('df_象前充_terminal')
df_象前充_terminal

