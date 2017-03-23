from flask import request, abort, render_template, flash
import telegram

from . import main
from .forms import WebhookUrlForm
from .. import bot


@main.route('/hook', methods=['POST'])
def webhook_handler():
    if request.method == 'POST':
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        chat_id = update.message.chat.id
        text = update.message.text.encode('utf-8')

        bot.send_message(chat_id=chat_id, text=text)
        return 'ok'
    return abort(400)


@main.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    form = WebhookUrlForm()
    form.webhook_url.data = bot.getWebhookInfo()['url']
    if form.validate_on_submit():
        status = bot.setWebhook(form.webhook_url.data)
        if status:
            flash('Webhook setup successed')
        else:
            flash('Webhook setup failed')
    return render_template('webhookurl.html', form=form)
