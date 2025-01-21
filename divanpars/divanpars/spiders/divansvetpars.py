import scrapy  # Импортируем библиотеку Scrapy для создания пауков


# Определяем класс паука (Spider), наследуем его от scrapy.Spider
class DivansvetparsSpider(scrapy.Spider):
    # Имя паука, используется для запуска паука через команду Scrapy
    name = "divansvetpars"
    # Ограничиваем домены, чтобы паук не переходил на внешние сайты
    allowed_domains = ["divan.ru"]
    # Начальная точка для сканирования
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        """
        Основной метод парсинга, обрабатывает ответ с каждой страницы.

        :param response: Объект ответа от Scrapy, содержащий HTML-код страницы.
        """
        # Находим элементы на странице с помощью CSS-селекторов
        fixtures = response.css("div.LlPhw")  # Находим блоки товаров по указанному классу
        for fixture in fixtures:
            # Извлекаем информацию о товаре и возвращаем её в виде словаря
            yield {
                "name": fixture.css("div.lsooF span::text").get(),  # Название товара
                "price": fixture.css("div.lsooF span::text").get(),  # Цена товара
                "url": "https://www.divan.ru" + fixture.css("a::attr(href)").get(),  # Полный URL товара
            }

