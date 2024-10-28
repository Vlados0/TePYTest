import logging
from pages.main_page import MainPage
from pages.contacts_page import ContactsPage

logging.basicConfig(level=logging.INFO)

def test_contact_region(driver):
    main_page = MainPage(driver)
    contacts_page = ContactsPage(driver)

    logging.info("Открываем главную страницу и переходим в раздел Контакты")
    main_page.open()
    main_page.go_contacts_page()

    logging.info("Проверка региона")
    actual_region = contacts_page.get_region_text()
    logging.info(f"Текущий регион: {actual_region}")
    assert actual_region == "Ярославская обл.", "Регион определен неверно"

    logging.info("Проверяем наличие партнеров на первой странице")
    initial_partners = contacts_page.get_partners()
    assert len(initial_partners) > 1, "Список партнеров на первой странице пуст."

    logging.info("Нажимаем на выбор региона и выбираем Камчатский край")
    contacts_page.select_region()

    logging.info("Проверка URL после смены региона")
    current_url = contacts_page.get_current_url()
    assert "41-kamchatskij-kraj" in current_url, f"URL не изменился на новый регион: {current_url}"

    logging.info("Проверка кнопки региона 'Камчатский край'")
    assert contacts_page.get_region_text() == "Камчатский край", "Регион не обновлен на 'Камчатский край'."

    logging.info("Проверка названия страницы")
    assert contacts_page.get_page_title() == "СБИС Контакты — Камчатский край", "Название страницы не соответствует."

    logging.info("Проверяем список партнеров после смены региона")
    new_partners = contacts_page.get_partners()
    assert len(new_partners) > 1, "Список партнеров пуст на новой странице."

    logging.info("Сравнение списков партнёров с предыдущей страницы и новой")
    assert initial_partners != new_partners, "Элементы партнеров не отличаются от предыдущей страницы."