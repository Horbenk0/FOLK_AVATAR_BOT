import telebot
import os
from PIL import Image
#



# !لِيَتَقَدَّسِ اسْمُكَ
#
# !لِيَأْتِ مَلَكُوتُكَ
#
# !لِتَكُنْ مَشِيئَتُكَ عَلَى الأَرْضِ كَمَا هِيَ السَّمَاءِ فِي
#
# !خُبْزَنَا كَفَافَنَا أَعْطِنَا الْيَوْمَ
#
# ،وَاغْفِرْ لَنَا ذُنُوبَنَا !كَمَا نَغْفِرُ نَحْنُ لِلْمُذْنِبِينَ إِلَيْنَا
#
# ،وَلاَ تُدْخِلْنَا فِي تَجْرِبَةٍ ،لَكِنْ نَجِّنَا مِنَ الشِّرِّيرِ
#
# .لأَنَّ لَكَ
#
# الْمُلْكَ
#
# وَالْقُوَّةَ
#
# وَالْمَجْدَ إِلَى الأَبَدِ


def scale_and_overlay_images(input_folder, ramka_folk_folder, ramka_volk_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    input_images = sorted(os.listdir(input_folder))
    ramka_folk_images = sorted(os.listdir(ramka_folk_folder))[:3]
    ramka_volk_images = sorted(os.listdir(ramka_volk_folder))[:3]

    def resize_and_crop(image, size):
        image_width, image_height = image.size
        target_width, target_height = size

        scale = max(target_width / image_width, target_height / image_height)
        new_width = int(image_width * scale)
        new_height = int(image_height * scale)

        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

        left = (new_width - target_width) / 2
        top = (new_height - target_height) / 2
        right = (new_width + target_width) / 2
        bottom = (new_height + target_height) / 2

        return image.crop((left, top, right, bottom))

    for i in range(3):
        input_image_file = input_images[i]
        input_image = Image.open(os.path.join(input_folder, input_image_file)).convert('RGB')
        input_image = resize_and_crop(input_image, (1000, 1000))

        ramka_folk_image_file = ramka_folk_images[i]
        ramka_folk_image = Image.open(os.path.join(ramka_folk_folder, ramka_folk_image_file)).convert('RGBA')
        ramka_folk_image = ramka_folk_image.resize((1000, 1000), Image.Resampling.LANCZOS)
        combined_image = Image.alpha_composite(input_image.convert('RGBA'), ramka_folk_image)
        combined_image = combined_image.convert('RGB')
        combined_image.save(os.path.join(output_folder, f'{i+1}_folk.jpg'))

        ramka_volk_image_file = ramka_volk_images[i]
        ramka_volk_image = Image.open(os.path.join(ramka_volk_folder, ramka_volk_image_file)).convert('RGBA')
        ramka_volk_image = ramka_volk_image.resize((1000, 1000), Image.Resampling.LANCZOS)
        combined_image = Image.alpha_composite(input_image.convert('RGBA'), ramka_volk_image)
        combined_image = combined_image.convert('RGB')
        combined_image.save(os.path.join(output_folder, f'{i+4}_volk.jpg'))

def delete_folder_contents(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            delete_folder_contents(file_path)
            os.rmdir(file_path)


# باسم الآب والابن والروح القدس. آمين.
#
# المجد لك يا إلهنا المجد لك.
#
# أيها الملك السماوي، المعزي، روح الحق، الموجود في كل مكان والمالئ الكل، كنز الصالحات وواهب الحياة، هلم واسكن فينا. طهرنا من كل دنس وخلص أيها الرب الصالح نفوسنا.
#
# قدوس الله قدوس القدير قدوس الذي لا يموت ارحمنا .
#
# المجد للآب والابن والروح القدس الآن وكل أوان وإلى دهر الداهرين. آمين.
#
# أيها الثالوث الأقدس، ارحمنا. يا رب اغفر خطايانا. يا سيد اغفر ذنوبنا. أيها القدوس، افتقد واشفي أمراضنا، من أجل اسمك.
#
# يا رب ارحم. يا رب ارحم. يا رب ارحم.
#
# المجد للآب والابن والروح القدس الآن وكل أوان وإلى دهر الداهرين. آمين.

TOKEN = '7466186236:AAHcWeiq8_ASkxbvYfaa41raGgGzHrH_7f0'
bot = telebot.TeleBot(TOKEN)

INPUT_PHOTO_FOLDER = 'input_photo'
OUTPUT_PHOTO_FOLDER = 'output_photo'
os.makedirs(INPUT_PHOTO_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_PHOTO_FOLDER, exist_ok=True)

photo_count = 0


# मेरे अल्लाह! आप मेरे भगवान हैं. आपके अलावा कोई भी देवता पूजा के योग्य नहीं है। आपने मुझे बनाया. मैं आपका गुलाम हूं.
# और मैं आपकी आज्ञाकारिता और निष्ठा की शपथ को निभाने की अपनी पूरी क्षमता से कोशिश करता हूं। मैंने जो गलतियाँ और पाप किए हैं,
# उनकी बुराई से सुरक्षा के लिए मैं आपका सहारा लेता हूँ। मैं आपके द्वारा दिए गए सभी आशीर्वादों के लिए आपको धन्यवाद देता हूं,
# और आपसे मेरे पापों को क्षमा करने के लिए प्रार्थना करता हूं। मुझे क्षमा कर, क्योंकि तेरे सिवा कोई नहीं जो पापों को क्षमा कर सके

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    global photo_count
    if photo_count < 3:
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        photo_path = os.path.join(INPUT_PHOTO_FOLDER, f'photo_{photo_count + 1}.jpg')

        with open(photo_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        photo_count += 1
        bot.reply_to(message, f'Фото {photo_count} получено!')

        if photo_count == 3:
            photo_count = 0

            bot.reply_to(message, 'Все три фото получены, начинаю обработку...')
            scale_and_overlay_images(INPUT_PHOTO_FOLDER, 'ramka_folk', 'ramka_volk', OUTPUT_PHOTO_FOLDER)

            for photo_file in os.listdir(OUTPUT_PHOTO_FOLDER):
                photo_path = os.path.join(OUTPUT_PHOTO_FOLDER, photo_file)
                with open(photo_path, 'rb') as photo:
                    bot.send_document(message.chat.id, photo)

            delete_folder_contents(INPUT_PHOTO_FOLDER)
            delete_folder_contents(OUTPUT_PHOTO_FOLDER)
            bot.reply_to(message, 'Обработка завершена, изображения отправлены и удалены!')
    else:
        bot.reply_to(message, 'Только 3 фото можно отправить.')

bot.polling()

# अबू मूसा (अल्लाह उस पर प्रसन्न हो सकता है!) ने बताया: "अल्लाह के दूत ने मेरी ओर रुख किया:" क्या मुझे तुम्हें स्वर्ग के खजाने में से एक तक ले जाना चाहिए?
#
# मैंने उत्तर दिया: "हाँ, हे अल्लाह के दूत!" जिस पर आप (सल्लल्लाहु अलैहि व सल्लम) ने कहाः
#
# "दोहराएं: "ला हवाला वा ला कुव्वाता इल्ला बिल्लाह" (ताकत और शक्ति केवल अल्लाह की है)।