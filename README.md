# Diplom_3
Проект написан в рамках дипломного задания по тестированию UI

[Документация API](https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89)

### Установка зависимостей

pip install -r requirements.txt

### Запуск тестов и генерация отчета в Allure

запуск на chrome: pytest tests --browser=chrome --alluredir=allure_results


запуск на firefox: pytest tests --browser=firefox --alluredir=allure_results