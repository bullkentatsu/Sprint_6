from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators

FAQ_DATA = [
    (MainPageLocators.QUESTION_0, MainPageLocators.ANSWER_0,
     "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (MainPageLocators.QUESTION_1, MainPageLocators.ANSWER_1,
     "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    (MainPageLocators.QUESTION_2, MainPageLocators.ANSWER_2,
     "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    (MainPageLocators.QUESTION_3, MainPageLocators.ANSWER_3,
     "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    (MainPageLocators.QUESTION_4, MainPageLocators.ANSWER_4,
     "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
    (MainPageLocators.QUESTION_5, MainPageLocators.ANSWER_5,
     "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    (MainPageLocators.QUESTION_6, MainPageLocators.ANSWER_6,
     "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
    (MainPageLocators.QUESTION_7, MainPageLocators.ANSWER_7,
     "Да, обязательно. Всем самокатов! И Москве, и Московской области."),
]

ORDER_DATA_TOP = {
    "name": "Егор",
    "surname": "Робкий",
    "address": "Москва, Москворечье 8",
    "metro": "Кантемировская",
    "phone": "+79774442211",
    "date": "10.10.2025",
    "color_locator": OrderPageLocators.COLOR_BLACK,
    "comment": "Привезите к подъезду",
}

ORDER_DATA_BOTTOM = {
    "name": "Ульяна",
    "surname": "Серьезная",
    "address": "Москва, Москворечье 8",
    "metro": "Каширская",
    "phone": "+79653339010",
    "date": "11.10.2025",
    "color_locator": OrderPageLocators.COLOR_GREY,
    "comment": "Позвоните за час",
}
