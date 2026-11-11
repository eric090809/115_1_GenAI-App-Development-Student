# AI 大學生作業與考試重點整理助手

## 一、專題介紹
本專題使用 Python、Streamlit 與 OpenAI API，開發一個協助大學生整理作業及考試公告的 AI 工具。

### 目標使用者
需要整理課堂公告、作業要求及考試資訊的大學生。

### 解決的問題
老師的公告有時內容較長，學生可能忽略重要要求或繳交期限。本工具將公告轉換成容易閱讀的結構化資訊。

## 二、主要功能
1. 貼上老師的作業或考試公告。
2. 點擊「開始整理」。
3. 使用 OpenAI API 分析公告內容。
4. 顯示五個整理結果：
   - 作業名稱
   - 作業要求
   - 繳交期限
   - 重要提醒
   - 待完成事項

## 三、使用技術
- Python
- Streamlit
- OpenAI API
- Pydantic Structured Outputs

選擇 Pydantic 的原因是可以定義明確的資料欄位及型別，並檢查模型回應是否符合預期格式。

## 四、安裝與啟動
安裝套件：

`pip install -r requirements.txt`

啟動程式：

`streamlit run app.py`

使用前須設定 `OPENAI_API_KEY`。本機可透過環境變數設定，雲端使用 Streamlit Secrets。

## 五、輸入與輸出
輸入為老師的公告文字，最多 6000 字元。

輸出包含：
- `title`：公告或作業名稱
- `requirements`：作業要求清單
- `deadline`：繳交期限
- `reminders`：重要提醒清單
- `todo_list`：待完成事項清單

未提供的資訊不得自行編造。

## 六、測試與驗收
目前狀態：尚未完成實際測試。

待驗證項目：
- 空白輸入檢查
- 超過 6000 字元檢查
- API 預設關閉
- 正常公告整理
- 資訊不足公告整理
- API 金鑰缺失處理
- Streamlit Cloud 部署與實際 API 測試

測試結果將於實際操作後補充，不以模擬結果代替真實測試。

## 七、雲端部署
Streamlit App 網址：待部署

部署分支：main

Main file path：`Midterm Mini-Project/app.py`

雲端驗收日期：未測

雲端 API 成功紀錄：未測

## 八、成本與限制
每次有效提交最多呼叫一次 OpenAI API，不自動重試。

使用模型預設為 `gpt-5.4-mini`，實際可用性與模型名稱須於測試時確認。

AI 可能誤解公告內容，因此使用者仍須對照原文檢查結果。

## 九、AI 協助說明
本專題使用 ChatGPT 協助規劃題目、撰寫初版程式及 README。

程式修改、測試結果、雲端部署與個人驗收紀錄須依實際完成情況補充。
