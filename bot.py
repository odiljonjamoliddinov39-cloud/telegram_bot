import os
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
    ConversationHandler,
)

TOKEN = "8613797909:AAHH-XTD0f1PtGHrxY-NpOuT37NZdecSsh4"
ADMIN_USERNAME = "@jiaru_jamshid"

NAME, UNIVERSITY, PHONE, EMAIL = range(4)

os.makedirs("uploads", exist_ok=True)

menu_ru = ReplyKeyboardMarkup(
    [
        ["О Компании", "Условия конкурса"],
        ["Принять участие"],
        ["Заполнить анкету"],
        ["Загрузить файл (или ссылку disk.yandex)"],
        ["Задать вопрос"],
    ],
    resize_keyboard=True,
)

menu_uz = ReplyKeyboardMarkup(
    [
        ["Kompaniya haqida", "Tanlov shartlari"],
        ["Ishtirok etish"],
        ["Anketani to'ldirish"],
        ["Fayl yuklash (yoki disk.yandex havolasi)"],
        ["Savol berish"],
    ],
    resize_keyboard=True,
)

lang_menu = ReplyKeyboardMarkup(
    [["RUS", "O'ZB"]],
    resize_keyboard=True,
)


# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Выберите язык / Tilni tanlang",
        reply_markup=lang_menu,
    )


# LANGUAGE
async def language(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if text == "RUS":
        context.user_data["lang"] = "ru"

        await update.message.reply_text(
            "Открытый конкурс дизайна интерьера от компании ZIMO \nТашкент 2026",
            reply_markup=menu_ru
        )

    elif text == "O'ZB":
        context.user_data["lang"] = "uz"

        await update.message.reply_text(
            "Interyer dizayn ochiq tanlovi ZIMO kompaniyasidan \nToshkent 2026",
            reply_markup=menu_uz
        )


# ---------- КНОПКИ ----------
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    lang = context.user_data.get("lang")

    if text in ["О Компании", "Kompaniya haqida"]:

        if lang == "ru":

            await update.message.reply_text(
                """Вот уже более 10 лет компания ZIMO успешно работает в сфере строительства, реализуя проекты различной сложности и масштаба. За это время мы зарекомендовали себя как надёжного партнёра, способного воплотить в жизнь самые амбициозные архитектурные решения.
       Среди наших крупных объектов:
Таможенный склад OOO Stock Group (г. Ташкент, Полевая – Аэропорт)
Бизнес-центр Muqimiy Plaza (г. Ташкент, ул. Мукимий, Piramit)
И многие другие проекты, которые сегодня служат примером качественного строительства и грамотного проектирования.
      На протяжении многих лет основной деятельностью компании было строительство административных и коммерческих зданий, но, учитывая потребность рынка и растущий спрос на качественный ремонт жилых помещений, мы открыли новое направление — ремонт квартир под ключ.
       Теперь ZIMO объединяет в себе опыт крупного строительства и практичные решения для частных клиентов. Мы адаптировали лучшие технологии, стандарты и методы контроля качества, чтобы создать удобный, понятный и комфортный сервис ремонта.
                """)

        else:
            await update.message.reply_text(
                """ZIMO kompaniyasi 10 yildan ortiq vaqt davomida qurilish sohasida muvaffaqiyatli faoliyat yuritib kelmoqda. 
        Shu vaqt ichida biz turli murakkablik va hajmdagi loyihalarni amalga oshirib, ishonchli hamkor sifatida o'zimizni namoyon qildik.
        Yirik loyihalarimizdan ba'zilari:
        Toshkent shahridagi Stock Group bojxona ombori
        Muqimiy Plaza biznes markazi
        Ko‘p yillar davomida kompaniya asosan ma'muriy va tijorat binolari qurilishi bilan shug‘ullangan. 
        Bozordagi ehtiyoj va sifatli kvartira ta’miriga bo‘lgan talabni inobatga olib, biz yangi yo‘nalish — kvartiralarni "kalit topshirish" asosida ta’mirlash xizmatini yo‘lga qo‘ydik.
        Endi ZIMO yirik qurilish tajribasi va xususiy mijozlar uchun qulay yechimlarni birlashtiradi."""
            )



    elif text in ["Условия конкурса", "Tanlov shartlari"]:
        if lang == "ru":
            await update.message.reply_text(
                """Цель конкурса:
Разработка правильного дизайн-проекта с 3D визуализацией нескольких квартир под сдачу в аренду с акцентом на:
•	Реализуемость проекта
•	Экономическую целесообразность
•	Продуманную планировку
•	Современную эстетику
•	Рациональное хранение
 Исходные данные:
•	Тип объекта: квартира
•	Площади: ___ м²,___ м²,___ м²,___ м²,___ м²,___ м²,___ м²,___ м².
•	Формат: под аренду
•	Основные материалы: бамбуковые панели, декоративная штукатурка, натяжной потолок
•	Бюджет реализации: средний сегмент
•	Стены квартиры по периметру – кирпичные
•	Межэтажные перекрытия – монолит
Участник обязан предоставить:
1.	Планировочное решение
2.	Визуализации помещений (3-4 фото каждого помещения)
3.	Чертежи (план мебели, свет, мокрые зоны)
4.	Краткое описание концепции (с обоснованием выбора материалов)
5.	Обмерный план
6.	План перегородок
7.	План пола и потолка
8.	План электрики и сантехники
9.	Развертки стен
10.	Спецификацию материалов
11.	Ведомость освещения и мебели
       ВАЖНО! Без полного комплекта проект не рассматривается/Формат сдачи: PDF / DWG(до 20мб)
           Требования:
•	Реалистичный свет
•	Реальные материалы (без фантастики)
•	Соответствие бюджету
•	Возможность повторить в реальности 
    Требования к участникам
•	Студенты 2–5 курса или дизайнеры архитекторы
•	Владение:
•	AutoCAD / ArchiCAD
•	3ds Max / SketchUp(желательно)
•	Базовое понимание стройки
•	Соблюдение сроков
•	Готовность к корректировкам
Проект должен:
•	Быть типовым
•	Быть из доступных материалов
•	Быть реалистичным а не «инстаграмным» 
•	Быть универсальным по стилю (нейтральный современный интерьер)
•	Использовать износостойкие материалы
•	Быть легко обслуживаемым и ремонтопригодным
•	Иметь светлую цветовую базу
•	Использоваться Бамбуковые панели (в качестве акцента)
•	Декоративная штукатурка (моющаяся)
•	Натяжной потолок (простой, без сложных многоуровневых форм)
           Запрещается:
•	Сложные гипсокартонные потолки
•	Эксклюзивные дорогие материалы
•	Нереализуемые дизайнерские решения
          Призы конкурса:
1.	Денежное вознаграждение за 1, 2 и 3 место
2.	Профессиональное признание и сертификат компании ZIMO
3.	Возможность получить предложение о работе в нашей компании
Этапы конкурса:
ПЕРВЫЙ ЭТАП: Онлайн-отбор финалистов
ВТОРОЙ ЭТАП: Офлайн-защита лучших проектов

Начало конкурса: ____
Окончание конкурса: ____
Дата объявления победителей: ____
""")


        else:
            await update.message.reply_text(
                """Tanlov maqsadi:
Bir nechta kvartiralarni ijaraga berish uchun 3D vizualizatsiyaga ega to‘g‘ri dizayn-loyiha ishlab chiqish. Loyiha quyidagi jihatlarga e’tibor qaratgan bo‘lishi kerak:

• Loyihaning amalda bajarilishi mumkinligi
• Iqtisodiy maqsadga muvofiqligi
• Puxta o‘ylangan rejalashtirish
• Zamonaviy estetika
• Ratsional saqlash tizimi

Boshlang‘ich ma’lumotlar:

• Obyekt turi: kvartira
• Maydoni: ___ m², ___ m², ___ m², ___ m², ___ m², ___ m², ___ m², ___ m²
• Format: ijaraga berish uchun
• Asosiy materiallar: bambuk panellar, dekorativ suvoq, tortma (natyažnoy) shift
• Amalga oshirish byudjeti: o‘rta segment
• Kvartira devorlari: g‘isht
• Qavatlar oralig‘i yopmasi: monolit

Ishtirokchi quyidagilarni taqdim etishi shart:

Rejalashtirish yechimi

Xonalar vizualizatsiyasi (har bir xona uchun 3–4 ta rasm)

Chizmalar (mebel rejasi, yoritish, nam zonalar)

Konsepsiyaning qisqa tavsifi (materiallar tanlovining asoslanishi bilan)

O‘lchov rejasi

Bo‘linma devorlar rejasi

Pol va shift rejasi

Elektr va santexnika rejasi

Devorlar razvertkasi

Materiallar spetsifikatsiyasi

Yoritish va mebel vedomosti

MUHIM!
To‘liq loyiha to‘plamisiz ishlar ko‘rib chiqilmaydi.
Topshirish formati: PDF / DWG (20 MB gacha)

Talablar:

• Realistik yoritish
• Haqiqiy materiallar (fantastik elementlarsiz)
• Byudjetga moslik
• Amalda qayta amalga oshirish imkoniyati

Ishtirokchilarga qo‘yiladigan talablar:

• 2–5 kurs talabalari yoki dizayner / arxitektorlar
• Quyidagi dasturlarni bilish:
• AutoCAD / ArchiCAD
• 3ds Max / SketchUp (maqsadga muvofiq)
• Qurilish jarayonlari haqida asosiy tushuncha
• Muddatlarga rioya qilish
• Tuzatishlar kiritishga tayyor bo‘lish

Loyiha quyidagilarga mos bo‘lishi kerak:

• Tipik loyiha bo‘lishi
• Mavjud va qulay materiallardan foydalanish
• Realistik bo‘lishi (faqat “Instagram uslubi” emas)
• Universal uslub (neytral zamonaviy interyer)
• Eskirishga chidamli materiallar ishlatilishi
• Oson xizmat ko‘rsatish va ta’mirlash imkoniyati
• Yorug‘ ranglar asosida bo‘lishi
• Bambuk panellar aksent sifatida ishlatilishi
• Dekorativ suvoq (yuviladigan)
• Tortma shift (oddiy, murakkab ko‘p darajali shakllarsiz)

Ta’qiqlanadi:

• Murakkab gipsokarton shiftlar
• Qimmat eksklyuziv materiallar
• Amalda bajarib bo‘lmaydigan dizayn yechimlari

Tanlov sovrinlari:

1-, 2- va 3-o‘rin uchun pul mukofoti

ZIMO kompaniyasining sertifikati va professional e’tirof

Kompaniyada ish taklifini olish imkoniyati

Tanlov bosqichlari:

1-bosqich: Finalchilarni onlayn saralash
2-bosqich: Eng yaxshi loyihalarni oflayn himoya qilish

Tanlov boshlanishi: ____
Tanlov yakuni: ____
G‘oliblar e’lon qilinadigan sana: ____"""
)



    elif text in ["Принять участие", "Ishtirok etish"]:
        if lang == "ru":
            await update.message.reply_text(

                """ВНИМАНИЕ!
    Нажимая на кнопку «Принять участие», вы соглашаетесь на следующие условия:
    Компания ZIMO оставляет за собой право на следующее:
    1. Все работы переходят в собственность компании ZIMO
    2. Видео и фотосъемка процесса конкурса и участников (контент для соцсетей)
    """       )


        else:
            await update.message.reply_text(
                """DIQQAT!
    “Ishtirok etish” tugmasini bosish orqali siz quyidagi shartlarga rozilik bildirasiz:
    1. Barcha ishlar ZIMO kompaniyasi mulkiga o'tadi
    2. Tanlov jarayonida foto va video tasvirga olish mumkin(ijtimoiy tarmoqlar uchun kontent)
    """ )



    elif text in ["Задать вопрос", "Savol berish"]:
        if lang == "ru":
            await update.message.reply_text(
                "Напишите ваш вопрос организатору: @jiaru_jamshid" )


        else:
            await update.message.reply_text(
                "Savolingizni tashkilotchiga yozing: @jiaru_jamshid")



    elif text in ["Загрузить файл (или ссылку disk.yandex)", "Fayl yuklash (yoki disk.yandex havolasi)"]:
        if lang == "ru":
            await update.message.reply_text(
                "Отправьте PDF/DWG файл проекта или ссылку."
            )


        else:
            await update.message.reply_text(
                "Loyiha PDF/DWG faylini yoki disk.yandex havolasini yuboring."
            )


# ---------- НАЧАЛО АНКЕТЫ ----------
async def form_start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    lang = context.user_data.get("lang")

    if lang == "ru":

        await update.message.reply_text(
            "Введите ФИО:",
            reply_markup=ReplyKeyboardRemove()
        )

    else:

        await update.message.reply_text(
            "F.I.O ni kiriting:",
            reply_markup=ReplyKeyboardRemove()
        )

    return NAME


# NAME
async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["name"] = update.message.text

    lang = context.user_data.get("lang")

    if lang == "ru":
        await update.message.reply_text("Университет / курс или место работы:")
    else:
        await update.message.reply_text("Universitet / kurs yoki ish joyi:")

    return UNIVERSITY


# UNIVERSITY
async def get_university(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["university"] = update.message.text

    lang = context.user_data.get("lang")

    if lang == "ru":
        await update.message.reply_text("Телефон:")
    else:
        await update.message.reply_text("Telefon raqami:")

    return PHONE


# PHONE
async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["phone"] = update.message.text

    lang = context.user_data.get("lang")

    if lang == "ru":
        await update.message.reply_text("Email:")
    else:
        await update.message.reply_text("Email:")

    return EMAIL


# EMAIL
async def get_email(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["email"] = update.message.text

    lang = context.user_data.get("lang")

    if lang == "ru":

        await update.message.reply_text(
            "Спасибо! Ваша работа принята.Результаты конкурса будут объявлены __ числа.",
            reply_markup=menu_ru
        )

    else:

        await update.message.reply_text(
            "Rahmat! Sizning ishingiz qabul qilindi. Tanlov natijalari __ sanada e'lon qilinadi.",
            reply_markup=menu_uz
        )

    return ConversationHandler.END


# ---------- ФАЙЛЫ ----------
async def file_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    lang = context.user_data.get("lang")

    if update.message.document:

        filename = update.message.document.file_name

        if not filename.lower().endswith((".pdf", ".dwg")):

            if lang == "ru":
                await update.message.reply_text(
                    "Можно отправлять только PDF/DWG файлы или загрузить ссылку disk.yandex"
                )
            else:
                await update.message.reply_text(
                    "Faqat PDF/DWG fayllarni yuborish mumkin yoki disk.yandex havolasini yuboring"
                )
            return

        file = await update.message.document.get_file()

        path = f"uploads/{filename}"

        await file.download_to_drive(path)

        if lang == "ru":
            await update.message.reply_text("Файл получен ✅")
        else:
            await update.message.reply_text("Fayl qabul qilindi ✅")

    elif "http" in update.message.text:

        if lang == "ru":
            await update.message.reply_text("Ссылка получена ✅")
        else:
            await update.message.reply_text("Havola qabul qilindi ✅")


# ---------- APP ----------
app = ApplicationBuilder().token(TOKEN).build()

form_handler = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex("Заполнить анкету|Anketani to'ldirish"), form_start)],
    states={
        NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
        UNIVERSITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_university)],
        PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
        EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_email)],
    },
    fallbacks=[],
)

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Regex("RUS|O'ZB"), language))
app.add_handler(form_handler)
app.add_handler(MessageHandler(filters.Document.ALL, file_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, buttons))

print("Бот работает 🚀")

app.run_polling()