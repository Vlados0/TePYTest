import logging
from pages.main_page import MainPage
from pages.contacts_page import ContactsPage
from pages.tensor_page import TensorPage

logging.basicConfig(level=logging.INFO)

def test_tensor_info(driver):
    main_page = MainPage(driver)
    contacts_page = ContactsPage(driver)
    tensor_page = TensorPage(driver)

    logging.info("Открываем главную страницу и переходим в раздел Контакты")
    main_page.open()
    main_page.go_contacts_page()

    logging.info("На странице контактов ищем и кликаем на баннер Тензор")
    contacts_page.click_tensor_banner()
    assert "tensor.ru" in driver.current_url, "Не удалось перейти на сайт Тензора"

    logging.info("Проверяем наличие блока 'Сила в людях'")
    assert tensor_page.verify_block(), "Блок 'Сила в людях' не найден"

    logging.info("Переходим в раздел 'Подробнее' и проверяем, что открылась страница 'О компании'")
    tensor_page.more_info()
    assert tensor_page.verify_page_opened(), "Страница 'О компании' не открылась"

    logging.info("Проверяем, что все фотографии имеют одинаковый размер")
    assert tensor_page.images_size(), "Фотографии имеют разные размеры"