# ДАННЫЕ:
BUTTONS_MAIN = ["О книге", "О дизайнере", "Презентация книги", "Скачать электронную версию", "Купить оригинал"]
BUTTONS_BOOK = ["Для кого эта книга?", "Сравнение разворотов", "Навигация по книге", "Поиск по достопримечательностям"]
BUTTONS_NAVIGATION = ["О местности", "Самые красивые виды", "Исторические личности"]
BUTTONS_CITIES = {"Ада-Бояна": ["", "https://tonkosti.ru/%D0%90%D0%B4%D0%B0-%D0%91%D0%BE%D1%8F%D0%BD%D0%B0",
                                "https://montegora.ru/ada-bayana-chernogoriya.html"],
                  "Бар": ["124-131", "https://tonkosti.ru/%D0%91%D0%B0%D1%80",
                          "https://montenegro-trip.ru/gorod-bar-v-chernogorii/"],
                  "Бечичи": ["", "https://tonkosti.ru/%D0%91%D0%B5%D1%87%D0%B8%D1%87%D0%B8",
                             "https://montenegro-trip.ru/kurort-bechichi-v-chernogorii/"],
                  "Будва": ["62-77", "https://tonkosti.ru/%D0%91%D1%83%D0%B4%D0%B2%D0%B0",
                            "https://montenegro-trip.ru/kurortnyj-gorod-budva-v-chernogorii/",
                            "https://montegora.ru/gde-luchshe-ostanovitsya-v-budve.html"],
                  "Герцег-Нови": ["",
                                  "https://tonkosti.ru/%D0%93%D0%B5%D1%80%D1%86%D0%B5%D0%B3-%D0%9D%D0%BE%D0%B2%D0%B8",
                                  "https://montenegro-trip.ru/gorod-gerceg-novi-v-chernogorii/",
                                  "https://montegora.ru/onlajn-putevoditel-po-xerceg-novi.html"],
                  "Жабляк": ["", "https://tonkosti.ru/%D0%96%D0%B0%D0%B1%D0%BB%D1%8F%D0%BA",
                             "https://montenegro-trip.ru/zhabljak-gornolyzhnyj-kurort-chernogorii/",
                             "https://montegora.ru/zhablyak.html"],
                  "Игало": ["", "https://tonkosti.ru/%D0%98%D0%B3%D0%B0%D0%BB%D0%BE",
                            "https://montenegro-trip.ru/kurort-igalo-v-chernogorii/"],
                  "Колашин": ["", "https://tonkosti.ru/%D0%9A%D0%BE%D0%BB%D0%B0%D1%88%D0%B8%D0%BD",
                              "https://montenegro-trip.ru/kolashin-gornolyzhnyj-kurort-chernogorii/",
                              "https://montegora.ru/most-dzhurdzhevicha.html"],
                  "Котор": ["44-61", "https://tonkosti.ru/%D0%9A%D0%BE%D1%82%D0%BE%D1%80",
                            "https://montenegro-trip.ru/gorod-kotor-v-chernogorii/",
                            "https://montegora.ru/kotor-chernogoriya.html"],
                  "Пераст": ["28-43", "https://tonkosti.ru/%D0%9F%D0%B5%D1%80%D0%B0%D1%81%D1%82",
                             "https://montenegro-trip.ru/gorod-perast-v-chernogorii/",
                             "https://montegora.ru/perast-chernogoriya.html "],
                  "Петровац": ["В книге не упоминается, но очень советую посетить",
                               "https://tonkosti.ru/%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%B2%D0%B0%D1%86",
                               "https://montenegro-trip.ru/kurort-petrovac-v-chernogorii/",
                               "https://montegora.ru/?s=%D0%BF%D0%B5%D1%82%D1%80%D0%BE%D0%B2%D0%B0%D1%86"],
                  "Подгорица": ["88-103", "https://tonkosti.ru/%D0%9F%D0%BE%D0%B4%D0%B3%D0%BE%D1%80%D0%B8%D1%86%D0%B0",
                                "https://montenegro-trip.ru/podgorica-stolica-chernogorii/",
                                "https://montegora.ru/podgorica-dostoprimechatelnosti.html"],
                  "Пржно": ["", "https://montenegro-trip.ru/kurortnyj-poselok-przhno-v-chernogorii/",
                            "https://montenegro-trip.ru/kurortnyj-poselok-przhno-v-chernogorii/",
                            "https://montegora.ru/przhno.html"],
                  "Рафаиловичи": ["", "https://tonkosti.ru/%D0%A0%D0%B0%D1%84%D0%B0%D0%B8%D0%BB%D0%BE%D0%B2%D0%B8%D1%87%D0%B8",
                                  "https://montenegro-trip.ru/kurort-rafailovichi-v-chernogorii/",
                                  "https://montegora.ru/plyazhi-budvy.html"],
                  "Рисан": ["упоминается на стр. 13", "https://tonkosti.ru/%D0%A0%D0%B8%D1%81%D0%B0%D0%BD",
                            "https://montegora.ru/risan-chernogoriya.html"],
                  "Святой Стефан": ["78-85", "https://tonkosti.ru/%D0%A1%D0%B2%D1%8F%D1%82%D0%BE%D0%B9_%D0%A1%D1%82%D0%B5%D1%84%D0%B0%D0%BD",
                                    "https://montenegro-trip.ru/svjatoj-stefan-v-chernogorii/",
                                    "https://montegora.ru/plyazh-galiya.html"],
                  "Скадарское озеро": ["114-123", "https://tonkosti.ru/%D0%A1%D0%BA%D0%B0%D0%B4%D0%B0%D1%80%D1%81%D0%BA%D0%BE%D0%B5_%D0%BE%D0%B7%D0%B5%D1%80%D0%BE",
                                       "https://montegora.ru/virpazar.html"],
                  "Сутоморе": ["", "https://tonkosti.ru/%D0%A1%D1%83%D1%82%D0%BE%D0%BC%D0%BE%D1%80%D0%B5",
                               "https://montenegro-trip.ru/kurortnyj-gorod-sutomore-v-chernogorii/",
                               "https://montegora.ru/sutomore-chernogoriya.html"],
                  "Тиват": ["упоминается на стр. 13", "https://tonkosti.ru/%D0%A2%D0%B8%D0%B2%D0%B0%D1%82",
                            "https://montenegro-trip.ru/tivat-v-chernogorii/",
                            "https://montegora.ru/tivat-dostoprimechatelnosti.html"],
                  "Ульцинь": ["", "https://tonkosti.ru/%D0%A3%D0%BB%D1%8C%D1%86%D0%B8%D0%BD%D1%8C",
                              "https://montenegro-trip.ru/kurortnyj-gorod-ulcin-v-chernogorii/",
                              "https://montegora.ru/ulcin-chernogoriya.html"],
                  "Цетинье": ["104-111", "https://tonkosti.ru/%D0%A6%D0%B5%D1%82%D0%B8%D0%BD%D1%8C%D0%B5",
                              "https://montenegro-trip.ru/cetine-v-chernogorii-jekskursii-dostoprimechatelnosti/"]}  # items[номера_страниц, ссылки_на_статьи...]
SHORT_INFO = "Эта книга для тех, кто интересуется балканскими народами, их культурой и историей. " \
             "Важно понимать, что это не путеводитель в его привычном облике."
NAVIGATION_INFO = ["Информацию о местности вы найдёте в следующих главах:\nII - IV",
                   "Самые красивые виды страны вы найдёте на следующих страницах:\n"
                   "16, 42, 54, 70, 82, 96, 100, 109, 116-121, 130",
                   "Информацию об исторических личностях вы найдёте на следующих страницах:\n"
                   "13, 18, 23, 32-36, 92-93"]
