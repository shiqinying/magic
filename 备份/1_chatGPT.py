import streamlit as st


import openai
from loguru import logger
openai.api_key = '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'


def get_completion(question):
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
    except Exception as e:
        print(e)
        return e
    result = response['choices'][0]['text']
    logger.success(result)
    return result


st.title('无所不能的老公')
input_text = st.text_input('陈可爱:')

if input_text:
    result = get_completion(question=input_text)
    st.text('老公：')
    st.success(result)
    st.balloons()


if __name__ == '__main__':
    # get_completion(question='学习中医有用吗？')
    pass


