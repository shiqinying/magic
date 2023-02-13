import streamlit as st

import streamlit as st


import openai
from loguru import logger
openai.api_key = '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'


def get_completion(question):
    for i in range(5):
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
            continue
    return '哎呀，走神了'
    

st.write("# 全天下最爱你的老公👋")
st.write("## 无所不能的老公👋👋👋")
st.write("### 最不抠的老公👋👋👋👋")
input_text = st.text_input('陈可爱:')

if input_text:
    st.write('老公思考中。。。。。。')
    result = get_completion(question=input_text)
    st.text('老公说：')
    st.success(result)
    st.balloons()

if __name__ == '__main__':
    # get_completion(question='学习中医有用吗？')
    pass


