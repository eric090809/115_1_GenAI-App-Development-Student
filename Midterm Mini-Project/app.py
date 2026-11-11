
import os
import streamlit as st
from openai import OpenAI
from pydantic import BaseModel, ConfigDict
from typing import List

st.set_page_config(
    page_title="AI 大學生作業整理助手",
    page_icon="📚"
)

class HomeworkResult(BaseModel):
    model_config = ConfigDict(extra="forbid")
    title: str
    requirements: List[str]
    deadline: str
    reminders: List[str]
    todo_list: List[str]

st.title("📚 AI 大學生作業與考試重點整理助手")
st.write("貼上老師的公告，AI 幫你整理重要資訊。")

use_api = st.checkbox("啟用 OpenAI API", value=False)

with st.form("homework_form"):
    content = st.text_area(
        "請貼上作業或考試公告",
        height=220,
        max_chars=6001
    )
    submitted = st.form_submit_button("開始整理")

if "record" not in st.session_state:
    st.session_state.record = None
if "error" not in st.session_state:
    st.session_state.error = ""

if submitted:
    st.session_state.record = None
    st.session_state.error = ""

    if not content.strip():
        st.session_state.error = "請先輸入公告內容。"
    elif len(content) > 6000:
        st.session_state.error = "輸入不可超過 6000 字元。"
    elif not use_api:
        st.session_state.error = "請先勾選啟用 OpenAI API。"
    else:
        try:
            api_key = ""
            if "OPENAI_API_KEY" in st.secrets:
                api_key = st.secrets["OPENAI_API_KEY"]
            else:
                api_key = os.getenv("OPENAI_API_KEY", "")

            if not api_key:
                st.session_state.error = "尚未設定 API 金鑰。"
            else:
                model = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")
                if "OPENAI_MODEL" in st.secrets:
                    model = st.secrets["OPENAI_MODEL"]

                client = OpenAI(
                    api_key=api_key,
                    timeout=60.0,
                    max_retries=0
                )

                response = client.responses.parse(
                    model=model,
                    instructions=(
                        "你是大學生作業公告整理助手。"
                        "只能根據使用者提供的原文整理資訊，"
                        "不得編造日期、要求或其他事實。"
                        "缺少的文字資訊填寫「未提及」，"
                        "缺少的清單資訊使用空清單。"
                        "所有欄位使用繁體中文。"
                    ),
                    input=content,
                    text_format=HomeworkResult
                )

                if response.status != "completed":
                    raise ValueError("模型回應未完成。")

                result = response.output_parsed
                if result is None:
                    raise ValueError("模型沒有回傳有效的結構化結果。")

                data = result.model_dump()
                st.session_state.record = {
                    "input": content,
                    "data": data,
                    "model": model
                }

        except Exception as e:
            st.session_state.error = (
                f"處理失敗：{type(e).__name__}。"
                "請檢查設定或稍後再試。"
            )

if st.session_state.error:
    st.error(st.session_state.error)

if st.session_state.record:
    record = st.session_state.record
    data = record["data"]

    st.success("整理完成！")
    st.subheader("📌 作業名稱")
    st.write(data["title"])

    st.subheader("📝 作業要求")
    for item in data["requirements"]:
        st.write("- " + item)

    st.subheader("📅 繳交期限")
    st.write(data["deadline"])

    st.subheader("⚠️ 重要提醒")
    for item in data["reminders"]:
        st.write("- " + item)

    st.subheader("✅ 待完成事項")
    for item in data["todo_list"]:
        st.write("- " + item)

    with st.expander("查看原始輸入"):
        st.write(record["input"])
