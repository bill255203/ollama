from translate import Translator

# Define the text to translate
to_translate = (
    "凡有僧道住持之宗教上建築物，不論用何名稱，均為寺廟。 "
    "寺廟及其財產法物，除法律別有規定外，依本條例監督之。 "
    "前項法物，謂於宗教上、歷史上、美術上、有關係之佛像、神像、禮器、樂器、法器、經典、雕刻、繪畫、及其他向由寺廟保存之一切古物。 "
    "寺廟屬於左列各款之一者，不適用本條例之規定： "
    "一、由政府機關管理者。 "
    "二、由地方公共團體管理者。 "
    "三、由私人建立並管理者。 "
    "荒廢之寺廟，由地方自治團體管理之。 "
    "寺廟財產及法物，應向該管地方官署呈請登記。 "
    "寺廟財產及法物為寺廟所有，由住持管理之。 "
    "寺廟有管理權之僧道，不論用何名稱，認為住持。但非中華民國人民，不得為住持。 "
    "住持於宣揚教義修持戒律，及其他正當開支外，不得動用寺廟財產之收入。 "
    "寺廟之不動產及法物，非經所屬教會之決議，並呈請該管官署許可，不得處分或變更。 "
    "寺廟收支款項及所興辦事業，住持應於每半年終報告該管官署，並公告之。 "
    "寺廟應按其財產情形，興辦公益或慈善事業。 "
    "違反本條例第五條、第六條或第十條之規定者，該管官署得革除其住持之職，違反第七條、第八條之規定者，得逐出寺廟或送法院究辦。 "
    "本條例於西藏、西康、蒙古、青海之寺廟不適用之。 "
    "本條例自公布日施行。 "
    "政府為船舶航行之安全，設置各種航路標識。 "
    "前項標識為燈塔、燈船、浮樁、標桿及霧號。 "
 
)

# Create a Translator instance
translator = Translator(to_lang="en", from_lang="zh-TW")

# Translate the text
translation = translator.translate(to_translate)

# Print the translation
print(translation)
