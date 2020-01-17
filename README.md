### VIVALDI TELEGRAM BOT ###

### Что оно делает ###

После старта джанги и выкатки миграций, нужно заполнить группы в админке, это будут входные данные для парсинга.

Сам парсер , разбирает либо поле description группы, либо страницу на которой висит общая афиша.
На ней он ищет строки формата [id1123123|Концерт залупы конской], берет из нее slug группы ивента и строит список.
Дальше по готовому списку, добывается нужная инфа и записывается в бд.

### Запуск проекта ###

В корне репозитория сбилдить образ с джангой docker build -f .docker/Dockerfile -t vivaldi:test .

Запросить ключь для api на vkhost.github.io

Прописать его в .docker/docker-compose.yml

Запустить проект: docker-compose -f .docker/docker-compose.yml up -d

в контейнере с джангой добавить в админку пользователя: python /app/src/manage.py createsupeuser

### Запуск парсера ###

Заполнить в админке группы вк нужной инфой.
В контейнере с джанго запустить python /app/src/manage.py vk_parser
