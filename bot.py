keyboard = {
    "inline_keyboard": [
        [
            {"text": "➕ New Account", "callback_data": "new_account"},
            {"text": "💼 My accounts", "callback_data": "my_accounts"}
        ],
        [
            {"text": "💰 Balance", "callback_data": "balance"},
            {"text": "👥 My referrals", "callback_data": "referrals"}
        ],
        [
            {"text": "🏆 Rank", "callback_data": "rank"},
            {"text": "❓ Help", "callback_data": "help"}
        ],
        [
            {"text": "🎲 DICE Game", "callback_data": "dice_game"}
        ]
    ]
}

bot.sendMessage(
    "Choose an option:",
    reply_markup=keyboard
)
