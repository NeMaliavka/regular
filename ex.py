import re

#p = re.compile(r"[a-z]|[а-я]", re.I) # нахождение букв английского или руского языка
#p = re.compile(r"[\w]") # Нахождение любых букв, цифр и символа нижнего подчеркивания
#p = re.compile(r"[\W]") # Нахождение всего, кроме букв, цифр и символа нижнего подчеркивания. Если нет никаких доп символов, ничего не найдет
#p = re.compile(r"^[a-z]+$", re.I) # re.I − игнорирование регистра
#p = re.compile(r"[\s]") # Нахождение любого пробельного символа, включая сам пробел (\t, \n, \r, \f, \v)
#p = re.compile(r"[\S]") # Нахождение любого значения, кроме пробельного символа, включая сам пробел (\t, \n, \r, \f, \v). Ничего не найдет, если строка состоит только из пробельных символов
#p = re.compile(r"[\d]") # Нахождение любой цифры
#p = re.compile(r"[\D]") # Нахождение всего, кроме любой цифры.Ничего не найдет, если строка состоит только из цифр
#print("Найдено" if p.search(text) else "Not found")

data = '23.07.2024'
p = re.compile(r"\d{2}.\d{2}.\d{4}")
#Даты в формате ДД.ММ.ГГГГ
# (и прочие куски, на них похожие, например, 98.76.5432)
print(data if p.search(data) else 'Not found')
print(' --*-- ' * 5)
www = 'https://habr.com/ru/articles/349860/'
p2 = re.compile(r"\b\w{5}\b")
#Слова в точности из трёх букв
# \b означает границу слова  (с одной стороны буква, а с другой — нет)
# \w — любая буква, {5} — ровно пять раз
print(www if p2.search(www) else 'Not found')
print(' --*-- ' * 5)
num = '+1234-12'
p3 = re.compile(r'[-+]?\d+')
# Целое число, например, 7, +17, -42, 0013 (возможны ведущие нули)
# [-+]? — либо -, либо +, либо пусто, \d+ — последовательность из 1 или более цифр
print(num if p3.search(num) else 'Not found')
print(' --*-- ' * 5)

regex = r"Вронск[а-я]+"

test_str = ("Вронский пошел за кондуктором в вагон и при входе в отделение остановился, чтобы дать дорогу выходившей даме. С привычным тактом светского человека, по одному взгляду на внешность этой дамы, Вронский определил ее принадлежность к высшему свету. Он извинился и пошел было в вагон, но почувствовал необходимость еще раз взглянуть на нее — не потому, что она была очень красива, не по тому изяществу и скромной грации, которые видны были во всей ее фигуре, но потому, что в выражении миловидного лица, когда она прошла мимо его, было что-то особенно ласковое и нежное. Когда он оглянулся, она тоже повернула голову. Блестящие, казавшиеся темными от густых ресниц, серые глаза дружелюбно, внимательно остановились на его лице, как будто она признавала его, и тотчас же перенеслись на подходившую толпу, как бы ища кого-то. В этом коротком взгляде Вронский успел заметить сдержанную оживленность, которая играла в ее лице и порхала между блестящими глазами и чуть заметной улыбкой, изгибавшею ее румяные губы. Как будто избыток чего-то так переполнял ее существо, что мимо ее воли выражался то в блеске взгляда, то в улыбке. Она потушила умышленно свет в глазах, но он светился против ее воли в чуть заметной улыбке.\n\n"
	"Вронский вошел в вагон. Мать его, сухая старушка с черными глазами и букольками, щурилась, вглядываясь в сына, и слегка улыбалась тонкими губами. Поднявшись с диванчика и передав горничной мешочек, она подала маленькую сухую руку сыну и, подняв его голову от руки, поцеловала его в лицо.\n\n"
	"— Получил телеграмму? Здоров? Слава богу.\n\n"
	"— Хорошо доехали? — сказал сын, садясь подле нее и невольно прислушиваясь к женскому голосу из-за двери. Он знал, что это был голос той дамы, которая встретилась ему при входе.\n\n"
	"— Я все-таки с вами не согласна, — говорил голос дамы.\n\n"
	"— Петербургский взгляд, сударыня.\n\n"
	"— Не петербургский, а просто женский, — отвечала она.\n\n"
	"— Ну-с, позвольте поцеловать вашу ручку.\n\n"
	"— До свиданья, Иван Петрович. Да посмотрите, не тут ли брат, и пошлите его ко мне, — сказала дама у самой двери и снова вошла в отделение.\n\n"
	"— Что ж, нашли брата? — сказала Вронская, обращаясь к даме.\n\n"
	"Вронский вспомнил теперь, что это была Каренина.\n\n"
	"— Ваш брат здесь, — сказал он, вставая. — Извините меня, я не узнал вас, да и наше знакомство было так коротко, — сказал Вронский, кланяясь, — что вы, верно, не помните меня.\n\n"
	"— О, нет, — сказала она, — я бы узнала вас, потому что мы с вашею матушкой, кажется, всю дорогу говорили только о вас, — сказала она, позволяя, наконец, просившемуся наружу оживлению выразиться в улыбке. — А брата моего все-таки нет.\n\n"
	"— Позови же его, Алеша, — сказала старая графиня.\n\n"
	"Вронский вышел на платформу и крикнул:\n\n"
	"— Облонский! Здесь!\n\n"
	"Но Каренина не дождалась брата, а, увидав его, решительным легким шагом вышла из вагона. И, как только брат подошел к ней, она движением, поразившим Вронского своею решительностью и грацией, обхватила брата левою рукой за шею, быстро притянула к себе и крепко поцеловала. Вронский, не спуская глаз, смотрел на нее и, сам не зная чему, улыбался. Но вспомнив, что мать ждала его, он опять вошел в вагон.\n\n"
	"— Не правда ли, очень мила? — сказала графиня про Каренину. — Ее муж со мною посадил, и я очень рада была. Всю дорогу мы с ней проговорили. Ну, а ты, говорят… vous filez le parfait amour. Tant mieux, mon cher, tant mieux[1].\n\n"
	"— Я не знаю, на что вы намекаете, maman, — отвечал сын холодно. — Что ж, maman, идем.\n\n"
	"Каренина опять вошла в вагон, чтобы проститься с графиней.\n\n"
	"— Ну вот, вы, графиня, встретили сына, а я брата, — весело сказала она. — И все истории мои истощились; дальше нечего было бы рассказывать.\n\n"
	"— Ну нет, милая, — сказала графиня, взяв ее за руку, — я бы с вами объехала вокруг света и не соскучилась бы. Вы одна из тех милых женщин, с которыми и поговорить и помолчать приятно. А о сыне вашем, пожалуйста, не думайте: нельзя же никогда не разлучаться.\n\n"
	"Каренина стояла неподвижно, держась чрезвычайно прямо, и глаза ее улыбались.\n\n"
	"— У Анны Аркадьевны, — сказала графиня, объясняя сыну, — есть сынок восьми лет, кажется, и она никогда с ним не разлучалась и все мучается, что оставила его.\n\n"
	"— Да, мы все время с графиней говорили, я о своем, она о своем сыне, — сказала Каренина, и опять улыбка осветила ее лицо, улыбка ласковая, относившаяся к нему.\n\n"
	"— Вероятно, это вам очень наскучило, — сказал он, сейчас, на лету, подхватывая этот мяч кокетства, который она бросила ему. Но она, видимо, не хотела продолжать разговора в этом тоне и обратилась к старой графине:\n\n"
	"— Очень благодарю вас. Я и не видала, как провела вчерашний день. До свиданья, графиня.\n\n"
	"— Прощайте, мой дружок, — отвечала графиня. — Дайте поцеловать ваше хорошенькое личико. Я просто, по-старушечьи, прямо говорю, что полюбила вас.\n\n"
	"Как ни казенна была эта фраза, Каренина, видимо, от души поверила и порадовалась этому. Она покраснела, слегка нагнулась, подставила свое лицо губам графини, опять выпрямилась и с тою же улыбкой, волновавшеюся между губами и глазами, подала руку Вронскому. Он пожал маленькую ему поданную руку и, как чему-то особенному, обрадовался тому энергическому пожатию, с которым она крепко и смело тряхнула его руку. Она вышла быстрою походкой, так странно легко носившею ее довольно полное тело.\n\n"
	"— Очень мила, — сказала старушка.\n\n"
	"То же самое думал ее сын. Он провожал ее глазами до тех пор, пока не скрылась ее грациозная фигура, и улыбка остановилась на его лице. В окно он видел; как она подошла к брату, положила ему руку на руку и что-то оживленно начала говорить ему, очевидно о чем-то не имеющем ничего общего с ним, с Вронским, и ему это показалось досадным.\n\n"
	"— Ну что, maman, вы совершенно здоровы? — повторил он, обращаясь к матери.\n\n"
	"— Все хорошо, прекрасно. Alexandre очень был мил. И Marie очень хороша стала. Она очень интересна.\n\n"
	"И опять начала рассказывать о том, что более всего интересовало ее, о крестинах внука, для которых она ездила в Петербург, и про особенную милость государя к старшему сыну.\n\n"
	"— Вот и Лаврентий, — сказал Вронский, глядя в окно, — теперь пойдемте, если угодно.\n\n"
	"Старый дворецкий, ехавший с графиней, явился в вагон доложить, что все готово, и графиня поднялась, чтоб идти.\n\n"
	"— Пойдемте, теперь мало народа, — сказал Вронский.\n\n"
	"Девушка взяла мешок и собачку, дворецкий и артельщик другие мешки. Вронский взял под руку мать; но когда они уже выходили из вагона, вдруг несколько человек с испуганными лицами пробежали мимо. Пробежал и начальник станции в своей необыкновенного цвета фуражке. Очевидно, что-то случилось необыкновенное. Народ от поезда бежал назад.\n\n"
	"— Что?.. Что?.. Где?.. Бросился!.. задавило!.. — слышалось между проходившими.\n\n"
	"Степан Аркадьич с сестрой под руку, тоже с испуганными лицами, вернулись и остановились, избегая народ, у входа в вагон.\n\n"
	"Дамы вошли в вагон, а Вронский со Степаном Аркадьичем пошли за народом узнавать подробности несчастия.\n\n"
	"Сторож, был ли он пьян или слишком закутан от сильного мороза, не слыхал отодвигаемого задом поезда, и его раздавили.\n\n"
	"Еще прежде чем вернулись Вронский и Облонский, дамы узнали эти подробности от дворецкого.\n\n"
	"Облонский и Вронский оба видели обезображенный труп. Облонский, видимо, страдал. Он морщился и, казалось, готов был плакать.\n\n"
	"— Ах, какой ужас! Ах, Анна, если бы ты видела! Ах, какой ужас! — приговаривал он.\n\n"
	"Вронский молчал, и красивое лицо его было серьезно, но совершенно спокойно.\n\n"
	"— Ах, если бы вы видели, графиня, — говорил Степан Аркадьич. — И жена его тут… Ужасно видеть ее… Она бросилась на тело. Говорят, он один кормил огромное семейство. Вот ужас!\n\n"
	"— Нельзя ли что-нибудь сделать для нее? — взволнованным шепотом сказала Каренина.\n\n"
	"Вронский взглянул на нее и тотчас же вышел из вагона.\n\n"
	"— Я сейчас приду, maman, — прибавил он, обертываясь в дверях.\n\n"
	"Когда он возвратился через несколько минут, Степан Аркадьич уже разговаривал с графиней о новой певице, а графиня нетерпеливо оглядывалась на дверь, ожидая сына.\n\n"
	"— Теперь пойдемте, — сказал Вронский, входя.\n\n"
	"Они вместе вышли. Вронский шел впереди с матерью. Сзади шла Каренина с братом. У выхода к Вронскому подошел догнавший его начальник станции.\n\n"
	"— Вы передали моему помощнику двести рублей. Потрудитесь обозначить, кому вы назначаете их?\n\n"
	"— Вдове, — сказал Вронский, пожимая плечами, — Я не понимаю, о чем спрашивать.\n\n"
	"— Вы дали? — крикнул сзади Облонский и, прижав руку сестры, прибавил: — Очень мило, очень мило! Не правда ли, славный малый? Мое почтение, графиня.\n\n"
	"И он с сестрой остановились, отыскивая ее девушку.\n\n"
	"Когда они вышли, карета Вронских уже отъехала. Выходившие люди все еще переговаривались о том, что случилось.\n\n"
	"— Вот смерть-то ужасная! — сказал какой-то господин, проходя мимо. — Говорят, на два куска.\n\n"
	"— Я думаю, напротив, самая легкая, мгновенная, — заметил другой.\n\n"
	"— Как это не примут мер, — говорил третий.\n\n"
	"Каренина села в карету, и Степан Аркадьич с удивлением увидал, что губы ее дрожат и она с трудом удерживает слезы.\n\n"
	"— Что с тобой, Анна? — спросил он, когда они отъехали несколько сот сажен.\n\n"
	"— Дурное предзнаменование, — сказала она.\n\n"
	"— Какие пустяки! — сказал Степан Аркадьич. — Ты приехала, это главное. Ты не можешь представить себе, как я надеюсь на тебя.\n\n"
	"— А ты давно знаешь Вронского? — спросила она.\n\n"
	"— Да. Ты знаешь, мы надеемся, что он женится на Кити.\n\n"
	"— Да? — тихо сказала Анна. — Ну, теперь давай говорить о тебе, — прибавила она, встряхивая головой, как будто хотела физически отогнать что-то лишнее и мешавшее ей. — Давай говорить о твоих делах. Я получила твое письмо и вот приехала.\n\n"
	"— Да, вся надежда на тебя, — сказал Степан Аркадьич.\n\n"
	"— Ну, расскажи мне все.\n\n"
	"И Степан Аркадьич стал рассказывать.\n\n"
	"Подъехав к дому, Облонский высадил сестру, вздохнул, пожал ее руку и отправился в присутствие.")

matches = re.finditer(regex, test_str)
# for ind, match in enumerate(matches):
#     print(f"Найдено совпадение: {match.group()}")

print(' --*-- ' * 5)
# для поиска адреса электронной почты. Любого адреса электронной почты, если быть точным
f_mail = 'opendata@nalog.ru\nOlga.Lukina@minfin.ru\n\n1248@minfin.ru\ndhskhgkhs\nIvan.Laguntcov@minfin.ru\nOLukina@minfin.ru'
for_found_email = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
result = re.finditer(for_found_email, f_mail)
for ind, match in enumerate(result):
    print(f"Найдено совпадение: {match.group()}")

#  Очень похожее регулярное выражение (замените первый \b на ^ , а последний на $ )
# может использоваться программистом для проверки того, правильно ли пользователь ввел адрес электронной почты в формат
