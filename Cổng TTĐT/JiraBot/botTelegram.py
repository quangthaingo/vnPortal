import telegram
from jira import JIRA

# Thông tin xác thực Jira
JIRA_URL = "https://cntt.vnpt.vn/secure/Dashboard.jspa"
JIRA_USERNAME = "thainq.cmu"
JIRA_API_TOKEN = "OA7lMcaXZ7mm8SttIOYgWV5rJnbt7HzbrJF"

# Khởi tạo kết nối với Jira
jira = JIRA(server=JIRA_URL, basic_auth=(JIRA_USERNAME, JIRA_API_TOKEN))

# Khởi tạo bot Telegram
TELEGRAM_TOKEN = "6598262237:AAHvrfk3DMfCrZlz8TxM41NfK9hqKweuG9s"
bot = telegram.Bot(token=TELEGRAM_TOKEN)

def handle_message(update, context):
    # Xử lý tin nhắn từ người dùng
    message = update.message.text
    # Xử lý logic của bạn ở đây (ví dụ: tìm task trong Jira và chuyển trạng thái)
    # Để chuyển trạng thái task, bạn cần sử dụng API của Jira

    # Ví dụ: Chuyển task với key là "YOUR_JIRA_ISSUE_KEY" vào trạng thái mới
    issue_key = "YOUR_JIRA_ISSUE_KEY"
    new_status = "YOUR_NEW_STATUS"
    jira.transition_issue(issue_key, new_status)

    # Gửi phản hồi cho người dùng
    update.message.reply_text("Task đã được chuyển sang trạng thái mới!")

def main():
    updater = telegram.Updater(token=TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(telegram.MessageHandler(telegram.Filters.text, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
