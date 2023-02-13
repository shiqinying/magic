# !/usr/bin/env python
# coding=utf-8
# pip3 install -r requirements.txt  -i https://pypi.douban.com/simple/
# 导出 requirements.txt  pip install pipreqs ; cd current porject ; pipreqs
#streamlit run home.py
#https://shiqinying-magicai-home-r1gu35.streamlit.app/
#https://platform.openai.com/account/usage
import time
import streamlit as st


import openai
from loguru import logger
openai.api_key = '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'


def get_completion(question):
    for i in range(3):
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"{question}\n",
                temperature=0.9,
                max_tokens=2048,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=None
            )
            result = response['choices'][0]['text']
            logger.success(result)
            return result
        except Exception as e:
            time.sleep(i)
            continue
    return '哎呀，走神了'
    

st.write("# 全天下最爱你的老公👋")
st.write("## 无所不能的老公👋👋")
st.write("### 最聪明的老公👋👋👋")
st.write("#### 最不抠的老公👋👋👋👋")
input_text = st.text_input('陈可爱:')
buttern = st.button('🚀🚀🚀老公快告诉我🚀🚀🚀')

if input_text and buttern:
    st.write('老公思考中。。。。。。')
    result = get_completion(question=input_text)
    st.text('老公说：')
    st.success(result)
    st.balloons()

if __name__ == '__main__':
    # get_completion(question='学习中医有用吗？')
    pass


