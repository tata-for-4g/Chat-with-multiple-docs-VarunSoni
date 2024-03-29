css = '''
<style>
. chat-message {
padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex

.chat-message.user {
background-color: #2b313e

.chat-message.bot {
background-color: #475063

.chat-message .avatar {
width: 15%;

.chat-message .avatar img {
max-width: 78px;
max-height: 78px;
border-radius: 50%;
object-fit: cover;

. chat-message .message {
width: 85%;
padding: 0 1.5rem;
color: #fff;
'''
bot_template = '''
<div class="chat-message bot">
<div class="avatar">
</div>
<div class="message">{{$MSG}}</div>
</div>'''
# <img src="https://images.pexels.com/photos/289923/pexels-photo-289923.jpeg">
# <img src="https://images.pexels.com/photos/289923/pexels-photo-289923.jpeg">
# <img src="https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg" style="max-height: 78px; max-width: 78px; border-radius: 50%; |
# <img src="https://img.freepik.com/free-photo/bohemian-man-with-his-arms-crossed_1368-3542.jpg">
user_template = '''
<div class="chat-message user">
<div class="avatar">

</div>
<div class="message">{{$MSG}}</div>
</div>
'''