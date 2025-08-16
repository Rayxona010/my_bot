import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config1 import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Assalomu alaykum\nNa gap?")


@dp.message(F.text == "Assalomu alaykum")
async def cmd_na_gap(message: Message):
    await message.reply("Valeykum Assalom!")


@dp.message(Command("salom"))  # /salom
async def cmd_salom(message: Message):
    await message.reply("Salom! Qanday yordam bera olaman?")


@dp.message(Command("yahshimisan"))  # /yahshimisan
async def cmd_yahshimisan(message: Message):
    await message.reply("Men sun'iy intellektman, o'zimni juda yaxshi his qilyapman!")


@dp.message(Command("yordam"))  # /yordam
async def cmd_yordam(message: Message):
    await message.reply("Albatta! Men sizga yordam bera olaman.")


@dp.message(Command("yordam"))
async def cmd_yordam(message: Message):
    await message.reply("Albatta! Men sizga yordam bera olaman.")


@dp.message(Command("malumot"))
async def cmd_malumot(message: Message):
    await message.reply("Men sizga kerakli ma'lumotlarni topishga yordam beraman.")


@dp.message(Command("boshlash"))
async def cmd_boshlash(message: Message):
    await message.reply("Xush kelibsiz! /yordam buyrug'ini yozing.")


@dp.message(Command("hazil"))
async def cmd_hazil(message: Message):
    await message.reply("Nega kompyuter kechikib keldi? Chunki u qattiq diskda edi!")


@dp.message(Command("vaqt"))
async def cmd_vaqt(message: Message):
    await message.reply("Kechirasiz, lekin vaqtni bilmayman.")


@dp.message(Command("sana"))
async def cmd_sana(message: Message):
    await message.reply("Bugun yaxshi kun bo'lishi aniq!")


@dp.message(Command("xayr"))
async def cmd_xayr(message: Message):
    await message.reply("Xayr! Yaxshi kunlar tilayman!")


@dp.message(Command("rahmat"))
async def cmd_rahmat(message: Message):
    await message.reply("Arzimaydi!")


@dp.message(Command("til"))
async def cmd_til(message: Message):
    await message.reply("Men o'zbek va ingliz tillarini tushunaman.")


@dp.message(Command("yaratuvchi"))
async def cmd_yaratuvchi(message: Message):
    await message.reply("Meni dasturchilar guruhi yaratgan.")


@dp.message(Command("versiya"))
async def cmd_versiya(message: Message):
    await message.reply("Siz botning 1.0 versiyasidan foydalanmoqdasiz.")


@dp.message(Command("qollabquvvatlash"))
async def cmd_qollabquvvatlash(message: Message):
    await message.reply("Qo'llab-quvvatlash uchun rasmiy saytga murojaat qiling.")


@dp.message(Command("qayta"))
async def cmd_qayta(message: Message):
    await message.reply("Sozlamalar qayta tiklandi.")


@dp.message(Command("yangilik"))
async def cmd_yangilik(message: Message):
    await message.reply("Yangiliklar uchun sevimli saytlaringizni tekshiring.")


@dp.message(Command("ibora"))
async def cmd_ibora(message: Message):
    await message.reply(
        "“Harakatni boshlashning eng yaxshi yo‘li — gapirishni bas qilish.”"
    )


@dp.message(Command("motivatsiya"))
async def cmd_motivatsiya(message: Message):
    await message.reply("Davom eting! Siz buni uddalaysiz.")


@dp.message(Command("salomlashish"))
async def cmd_salomlashish(message: Message):
    await message.reply("Assalomu alaykum, foydalanuvchi!")


@dp.message(Command("fakt"))
async def cmd_fakt(message: Message):
    await message.reply("Asalarilar hech qachon asalni buzmaydi.")


@dp.message(Command("ism"))
async def cmd_ism(message: Message):
    await message.reply("Meni ChatBot deb atashingiz mumkin.")


@dp.message(Command("botmisan"))
async def cmd_botmisan(message: Message):
    await message.reply("Ha, men botman. 🤖")


@dp.message(Command("ai"))
async def cmd_ai(message: Message):
    await message.reply("Men sun'iy intellekt asosida ishlayman.")


@dp.message(Command("menyu"))
async def cmd_menyu(message: Message):
    await message.reply("Mana buyruqlar menyusi.")


@dp.message(Command("qahva"))
async def cmd_qahva(message: Message):
    await message.reply("Men icholmasam ham, qahvani yaxshi ko‘raman.")


@dp.message(Command("uxla"))
async def cmd_uxla(message: Message):
    await message.reply("Botlar uxlamaydi, faqat bekor turadi.")


@dp.message(Command("qo'shiq"))
async def cmd_qushiq(message: Message):
    await message.reply("La la la~ 🎶")


@dp.message(Command("raqis"))
async def cmd_raqis(message: Message):
    await message.reply("men botman")


@dp.message(Command("kul"))
async def cmd_kul(message: Message):
    await message.reply("Haha 😄")


@dp.message(Command("xafa"))
async def cmd_xafa(message: Message):
    await message.reply("Xafa bo‘lmang! Men siz bilanman.")


@dp.message(Command("jahlim chiqdi"))
async def cmd_jahlimchiqdi(message: Message):
    await message.reply("Tinching, hammamizda shunaqa kunlar bo'ladi.")


@dp.message(Command("xursandman"))
async def cmd_xursandman(message: Message):
    await message.reply("Zo'r! Quvonchingizga quvonaman!")


@dp.message(Command("zerikdim"))
async def cmd_zerikdim(message: Message):
    await message.reply("Keling, biror foydali narsa o‘rganamiz.")


@dp.message(Command("ovqat"))
async def cmd_ovqat(message: Message):
    await message.reply("Men faqat raqamli taomlarni yeyman 😄")


@dp.message(Command("ob-havo"))
async def cmd_obhavo(message: Message):
    await message.reply("Afsuski, ob-havo ma'lumotim yo'q.")


@dp.message(Command("sevimlimavzu"))
async def cmd_sevimlimavzu(message: Message):
    await message.reply("Sun’iy intellekt, albatta!")


@dp.message(Command("sher"))
async def cmd_sher(message: Message):
    await message.reply("Hayot gulshan, uni gul etmoq kerak.")


@dp.message(Command("she'rayt"))
async def cmd_sherayt(message: Message):
    await message.reply("Yashaydi yurakda umid, mehr ila.")


@dp.message(Command("kitob"))
async def cmd_kitob(message: Message):
    await message.reply("Kitob – bilim manbai.")


@dp.message(Command("qiziqarli fakt"))
async def cmd_qiziqarlifakt(message: Message):
    await message.reply("Odam tanasidagi tomirlar uzunligi 100 ming km dan oshadi!")


@dp.message(Command("telefon"))
async def cmd_telefon(message: Message):
    await message.reply("Telefoningiz quvvatini tekshiring 😉")


@dp.message(Command("dasturlash"))
async def cmd_dasturlash(message: Message):
    await message.reply("Python – boshlovchilar uchun eng yaxshi til.")


@dp.message(Command("sinf"))
async def cmd_sinf(message: Message):
    await message.reply("Darsga kechikmang 😄")


@dp.message(Command("ustoz"))
async def cmd_ustoz(message: Message):
    await message.reply("Ustoz – hayot yo‘lini ko‘rsatuvchi.")


@dp.message(Command("talaba"))
async def cmd_talaba(message: Message):
    await message.reply("Talabalik – oltin davr!")


@dp.message(Command("imtihon"))
async def cmd_imtihon(message: Message):
    await message.reply("Omad tilayman imtihonlarda!")


@dp.message(Command("tanaffus"))
async def cmd_tanaffus(message: Message):
    await message.reply("Dam olish ham muhim!")


@dp.message(Command("suv ich"))
async def cmd_suvich(message: Message):
    await message.reply("Suv ichishni unutmang!")


@dp.message(Command("uyqu"))
async def cmd_uyqu(message: Message):
    await message.reply("Yaxshi uxlash sog‘liq uchun foydali.")


@dp.message(Command("xotira"))
async def cmd_xotira(message: Message):
    await message.reply("Bot sifatida xotiram juda kuchli!")


@dp.message(Command("tezkorjavob"))
async def cmd_tezkorjavob(message: Message):
    await message.reply("Ha, men doimo tayyorman!")


@dp.message(Command("shirinlik"))
async def cmd_shirinlik(message: Message):
    await message.reply("Shokoladni yaxshi ko‘raman 🍫")


@dp.message(Command("yangiliklar"))
async def cmd_yangiliklar(message: Message):
    await message.reply("Bugungi yangiliklar uchun internetni tekshiring.")


@dp.message(Command("til o‘rganish"))
async def cmd_tilorganish(message: Message):
    await message.reply("Yangi til o‘rganish – ajoyib g‘oya!")


@dp.message(Command("tarix"))
async def cmd_tarix(message: Message):
    await message.reply("Tarixdan saboq olish kerak.")


@dp.message(Command("geografiya"))
async def cmd_geografiya(message: Message):
    await message.reply("Dunyo xaritasi qiziq!")


@dp.message(Command("biologiya"))
async def cmd_biologiya(message: Message):
    await message.reply("Organizmlar hayoti juda murakkab.")


@dp.message(Command("fizika"))
async def cmd_fizika(message: Message):
    await message.reply("Fizika — tabiat qonunlarini o‘rganadi.")


@dp.message(Command("matematika"))
async def cmd_matematika(message: Message):
    await message.reply("Matematika – mantiqning tili.")


@dp.message(Command("savol"))
async def cmd_savol(message: Message):
    await message.reply("Ha, albatta! Savolingizni yozing.")


@dp.message(Command("vazifa"))
async def cmd_vazifa(message: Message):
    await message.reply("Bugungi vazifangizni bajardingizmi?")


@dp.message(Command("tanishuv"))
async def cmd_tanishuv(message: Message):
    await message.reply("Botman, siz bilan tanishganimdan xursandman!")


@dp.message(Command("sinfda ko'plab do'stlarim bor men ularni yomon ko'raman!"))
async def cmd_sinfdagi(message: Message):
    await message.reply("Sinfdagi do‘stlaringiz bilan yaxshi munosabatda bo‘ling.")


@dp.message(Command("oy"))
async def cmd_oy(message: Message):
    await message.reply("Oydagi odam – fantastika emas, tarix!")


@dp.message(Command("quyosh"))
async def cmd_quyosh(message: Message):
    await message.reply("Quyosh bizga hayot beradi.")


@dp.message(Command("olam"))
async def cmd_olam(message: Message):
    await message.reply("Olam sirlariga qiziqasizmi?")


@dp.message(Command("kompyuter"))
async def cmd_kompyuter(message: Message):
    await message.reply("Kompyuter – zamonaviy vosita.")


@dp.message(Command("internet"))
async def cmd_internet(message: Message):
    await message.reply("Internet – bilim ombori.")


@dp.message(Command("wifi"))
async def cmd_wifi(message: Message):
    await message.reply("WiFi signali yaxshi ishlayaptimi?")


@dp.message(Command("qiziq"))
async def cmd_qiziq(message: Message):
    await message.reply("Ha, bu juda qiziqarli mavzu!")


@dp.message(Command("rasm"))
async def cmd_rasm(message: Message):
    await message.reply("Tasavvurdagi rasmni chiza olmayman, lekin tasvirlay olaman.")


@dp.message(Command("video"))
async def cmd_video(message: Message):
    await message.reply("Hozircha video ko‘rsata olmayman.")


@dp.message(Command("muzika"))
async def cmd_muzika(message: Message):
    await message.reply("Musiqa ruhingizni ko‘taradi!")


@dp.message(Command("poema"))
async def cmd_poema(message: Message):
    await message.reply("Hayot bir she’r, har kuni bir misra.")


@dp.message(Command("ismlar"))
async def cmd_ismlar(message: Message):
    await message.reply("Ismlar dunyosi keng va go‘zal.")


@dp.message(Command("havo"))
async def cmd_havo(message: Message):
    await message.reply("Toza havo — sog‘liq garovi.")


@dp.message(Command("sport"))
async def cmd_sport(message: Message):
    await message.reply("Harakat — salomatlik kaliti.")


@dp.message(Command("futbol"))
async def cmd_futbol(message: Message):
    await message.reply("Futbolchilar kabi jamoaviy ishlang!")


@dp.message(Command("basketbol"))
async def cmd_basketbol(message: Message):
    await message.reply("Basketbol – tezlik va aniqlik o‘yini.")


@dp.message(Command("shaxmat"))
async def cmd_shaxmat(message: Message):
    await message.reply("Shaxmat aqlni o‘tkirlaydi.")


@dp.message(Command("damolish"))
async def cmd_damolish(message: Message):
    await message.reply("Dam olishga vaqt ajrating.")


@dp.message(Command("motivatsiya ber"))
async def cmd_motiv(message: Message):
    await message.reply("Bugun – yangiliklar kuni!")


@dp.message(Command("maqsad"))
async def cmd_maqsad(message: Message):
    await message.reply("Maqsadingiz yo‘lingizni belgilaydi.")


@dp.message(Command("yo‘l"))
async def cmd_yol(message: Message):
    await message.reply("Yo‘ldan adashmaslik uchun maqsadingiz bo‘lsin.")


@dp.message(Command("kelajak"))
async def cmd_kelajak(message: Message):
    await message.reply("Kelajak — sizning qo‘lingizda.")


@dp.message(Command("muammo"))
async def cmd_muammo(message: Message):
    await message.reply("Har bir muammo – yangi imkoniyat.")


@dp.message(Command("javob"))
async def cmd_javob(message: Message):
    await message.reply("Mana sizga javob ")


@dp.message(Command("savolber"))
async def cmd_savolber(message: Message):
    await message.reply("Marhamat, savolingizni yozing!")


@dp.message(Command("ulash"))
async def cmd_ulash(message: Message):
    await message.reply("Bu xabarni do‘stlaringiz bilan ulashing.")


@dp.message(Command("bosqich"))
async def cmd_bosqich(message: Message):
    await message.reply("Hayot bir necha bosqichlardan iborat.")


@dp.message(Command("natija"))
async def cmd_natija(message: Message):
    await message.reply("Harakat bo‘lsa – natija bo‘ladi.")


@dp.message(Command("sabr"))
async def cmd_sabr(message: Message):
    await message.reply("Sabr – yutuq kaliti.")


@dp.message(Command("qaleysan"))
async def cmd_sabr(message: Message):
    await message.reply("Men yaxshiman o'zingiz aleysiz!")


@dp.message(Command("Hayrli tong"))
async def cmd_sabr(message: Message):
    await message.reply("Hayrli tong sizga ham😊")


@dp.message(Command("Hayrli kun"))
async def cmd_sabr(message: Message):
    await message.reply("Hayrli kun sizga ham😉")


@dp.message(Command("Hayrli tun"))
async def cmd_sabr(message: Message):
    await message.reply("Hayrli tun sizga ham😉")


@dp.message(Command("Ahvolingiz qalay"))
async def cmd_sabr(message: Message):
    await message.reply("Men botman va ahvolim yaxshi, o'zizqalaysiz?")


@dp.message(F.photo)
async def photo(message: Message):
    await message.answer(f"Foto ID si: {message.photo[-1].file_id}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nGoodbye")
