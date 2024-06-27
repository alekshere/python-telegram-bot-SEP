import datetime

from telegram import Update, Poll, PollOption, CallbackQuery, User, Message, Chat
from telegram.ext import ExtBot


class TestExtBot:
    def test_insert_callback_data_bot_should_process_callback_query(self):
        bot = ExtBot(token="23")

        update = Update(
            update_id=23,
            callback_query=CallbackQuery(
                id="23",
                from_user=User(
                    id=23,
                    is_bot=True,
                    first_name="test"
                ),
                data="23",
                chat_instance=""
            )
        )
        bot.insert_callback_data(update)

        assert bot.get_branch_coverage()["101"] is True
        assert bot.get_branch_coverage()["102"] is False

    def test_insert_callback_data_bot_should_process_callback_effective(self):
        bot = ExtBot(token="23")

        chat = Chat(1, "private")
        effective_message = Message(message_id=1, date=None, chat=chat)
        update = Update(
            update_id=23,
            callback_query=None,
            message=effective_message
        )
        bot.insert_callback_data(update)

        assert bot.get_branch_coverage()["101"] is False
        assert bot.get_branch_coverage()["102"] is True
