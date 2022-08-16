from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import random
updater = Updater(token='5631753023:AAHqOqbCtyZsxSQ_QNqNv985E343Oox50bs', use_context=True)
dispatcher = updater.dispatcher

def func1():
    global flower3, flower4, new_dict
    club, spade, dimond, heart = [], [], [], []

    index = [int(i) for i in range(1, 14)]
    for i in range(1, 11):
        club += [''.join([f'♣{i}'])]
    club = club + ['♣J', '♣Q', '♣K']
    club_rank = dict(zip(club, index))
    for i in range(1, 11):
        spade += [''.join([f'♠{i}'])]
    spade = spade + ['♠J', '♠Q', '♠K']
    spade_rank = dict(zip(spade, index))
    for i in range(1, 11):
        dimond += [''.join([f'♦{i}'])]
    dimond = dimond + ['♦J', '♦Q', '♦K']
    dimond_rank = dict(zip(dimond, index))
    for i in range(1, 11):
        heart += [''.join([f'❤{i}'])]
    heart = heart + ['❤J', '❤Q', '❤K']
    heart_rank = dict(zip(heart, index))
    flower1 = dict(club_rank, **spade_rank)
    flower2 = dict(dimond_rank, **heart_rank)
    flower3 = dict(flower1, **flower2)
    flower4 = dict(flower1, **flower2)
    #print(flower3, flower4)
    return flower3, flower4

def func2():
    global li0, li1, li2, li3, li4, li5, li6, li7, li8, li9, li10, li11, li12, li13, flower3, flower4, new_dict, \
        li0_rep, li1_rep, li2_rep, li3_rep, li4_rep, li5_rep, li6_rep, li7_rep, li8_rep, li9_rep, li10_rep, li11_rep
    # 印出初始排
    li0, li1, li2, li3, li4, li5, li6, li7, li8, li9, li10, li11, li12, li13 = [], [], [], [], [], [], [], [], [], [], \
                                                                               [], [], [], []
    li0_rep, li1_rep, li2_rep, li3_rep, li4_rep, li5_rep, li6_rep, li7_rep, li8_rep, li9_rep, li10_rep, li11_rep = [], \
                                                                            [], [], [], [], [], [], [], [], [], [], []
    global flower3, flower4, new_dict

    new_dict = flower3
    # 找到flower 中的key直
    li0, li0_rep = ['♣(0):'], ['♣(0):']
    li1, li1_rep = ['♦(1):'], ['♦(1):']
    li2, li2_rep = ['❤(2):'], ['❤(2):']
    li3, li3_rep = ['♠(3):'], ['♠(3):']
    li4, li4_rep = ['🂠(4):'], ['🂠(4):']
    li5 = ['row(5)'] + random.sample(list(new_dict.keys()), 1)
    li5_rep = li5[0:2]
    [new_dict.pop(key) for key in li5[1:]]
    li6 = ['row(6)'] + random.sample(list(new_dict.keys()), 2)
    li6_rep = li6[0:2] + ['*'] * 1
    [new_dict.pop(key) for key in li6[1:]]

    li7 = ['row(7)'] + random.sample(list(new_dict.keys()), 3)
    li7_rep = li7[0:2] + ['*'] * 2
    [new_dict.pop(key) for key in li7[1:]]

    li8 = ['row(8)'] + random.sample(list(new_dict.keys()), 4)
    li8_rep = li8[0:2] + ['*'] * 3
    [new_dict.pop(key) for key in li8[1:]]

    li9 = ['row(9)'] + random.sample(list(new_dict.keys()), 5)
    li9_rep = li9[0:2] + ['*'] * 4
    [new_dict.pop(key) for key in li9[1:]]

    li10 = ['row(10)'] + random.sample(list(new_dict.keys()), 6)
    li10_rep = li10[0:2] + ['*'] * 5
    [new_dict.pop(key) for key in li10[1:]]

    li11 = ['row(11)'] + random.sample(list(new_dict.keys()), 7)
    li11_rep = li11[0:2] + ['*'] * 6
    [new_dict.pop(key) for key in li11[1:]]

    li12 = [li0_rep, li1_rep, li2_rep, li3_rep, li4_rep, li5_rep, li6_rep, li7_rep, li8_rep, li9_rep, li10_rep,
            li11_rep]
    li13 = [li0, li1, li2, li3, li4, li5, li6, li7, li8, li9, li10, li11]

def init(update, context): #開始執行初始化
    func1()
    func2()
    for i in range(12):
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'{li12[i]}\n')

def Move(update, context):
    global li0, li1, li2, li3, li4, li5, li6, li7, li8, li9, li10, li11, li12, li13, flower3, flower4, new_dict
    pos = update.message.text
    pos_temp = pos.split(',')
    pos1, pos2, end = int(pos_temp[0]), int(pos_temp[1]), int(pos_temp[2])
    # 輸入move(pos1, pos2, end)值
    extract = []
    extract_actul = []
    loc = 0
    # 做起使字串的擷取，如果i到'*'時，取前面的部分，用loc當計數器，得知取的位置
    for i in li12[pos1]:
        if i == '*':
            extract = li12[pos1][(pos2+1):loc]
            extract_actul = li13[pos1][(pos2+1):loc]
            break
        else:   #當後面已無'*'時就是直接取全部
            if loc == (len(li12[pos1]) - 1):
                extract = li12[pos1][(pos2+1):loc+1]
                extract_actul = li13[pos1][(pos2 + 1):loc+1]
                break
            else:
                loc = loc + 1
                continue

    # 將extract做放置
    accept = 0
    if len(li12[end]) == 1:   #end 沒有排空的
        li12[end] += extract
        li13[end] += extract_actul
        accept = 1
    elif len(li12[end]) != 1:   #end有牌要做比較
        pos1_value = flower4[extract[-1]]  #擷取排堆中的最後一張
        end_value = flower4[li12[end][1]]  #要放置的第一張，也就是row的後面一個
        if (end_value-pos1_value) == 1:
            li12[end][1:1] = extract
            li13[end][1:1] = extract_actul
            accept = 1
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text='cannot place')

    # 將移走的排加一張 ，且把pos1的extract去掉
    if accept == 1 and '*' in li12[pos1]: #成功移走且起始排堆有*
        [li12[pos1].pop(1) for i in range(len(extract))]
        [li13[pos1].pop(1) for i in range(len(extract_actul))]
        li12[pos1].insert(1, li13[pos1][pos2+1])
        li12[pos1].remove('*')
    elif accept == 1 and '*' not in li12[pos1]: #成功移走且起始排堆沒有*
        [li12[pos1].pop(1) for i in range(len(extract))]
        [li13[pos1].pop(1) for i in range(len(extract_actul))]

    for i in range(12):
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'{li12[i]}\n')

    # 如果全部完成
    if len(li12[0]) == 14 and len(li12[1]) == 14 and len(li12[2]) == 14 and len(li12[3]) == 14:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Congratulation you are the King of the world')

def Pause(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='PAUSE', reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton('Retry??', callback_data='r')],
            [InlineKeyboardButton('Continue', callback_data='c')],
            [InlineKeyboardButton('Deal', callback_data='b')]
        ]))

def func(update, context):
    global li0, li1, li2, li3, li4, li5, li6, li7, li8, li9, li10, li11, li12, li13, flower3, flower4, new_dict, li4_rep
    if update.callback_query.data == 'r':
        func1()
        func2()
        for i in range(12):
            context.bot.send_message(chat_id=update.effective_chat.id, text=f'{li12[i]}\n')
    elif update.callback_query.data == 'c':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Continue to the game')
    elif update.callback_query.data == 'b':
        new_card = random.sample(list(flower3.keys()), 1)
        if new_card == None:
            context.bot.send_message(chat_id=update.effective_chat.id, text='No card')
        else:
            li4_rep += new_card
            li4 += new_card
            flower3.pop(new_card[0])
            for i in range(12):
                context.bot.send_message(chat_id=update.effective_chat.id, text=f'{li12[i]}\n')

dispatcher.add_handler(CallbackQueryHandler(func))

start_handler = CommandHandler('start', init)
dispatcher.add_handler(start_handler)

pause_handler = CommandHandler('pause', Pause)
dispatcher.add_handler(pause_handler)

move_handler = MessageHandler(Filters.text, Move)
dispatcher.add_handler(move_handler)

updater.start_polling()