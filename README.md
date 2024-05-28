# Видеомейкер

Видеомейкер - это сервер, предназнаенный для создания видео в формате mp4 с бегущей строкой. Длина видео составляет 3 секунды.



# Содержание

- [Технологии](#технологии)
- [Требования](#требования)
- [Развертывание приложения](#деплой)
- [Использование](#использование)
- [Команда](#команда)

# Технологии

<a name="технологии"></a>

- BE
  - Python
  - Django
  - DRF
  - OpenCV
  - Pillow
  - Ruff
- Docker
- Docker Compose
- PostgreSQL

# Требования

<a name="требования"></a>

Сервер обрабатывает текст как на английском, так и на русском языке.
Размер текста, который используется для бегущей строки не должен превышать 50 символов. В зависимости от от количества символов изменятеся размер шрифта.

# Развертывание приложения

<a name="деплой"></a>

Для развертывания приложения в проекте используется Docker Compose. Проект состоит из двух контейнеров: db(postgres), app(python).
Для полного запуска проекта в root директории используйте команду:

```bash
docker compose up -d
```

# Использование
<a name="использование"></a>

Для того, чтобы загрузить видео с бегущей строкой, в адресной строке введите:
[http://localhost:8000/api/createvide?text=Здесь будет ваш текст](http://localhost:8000/api/createvideo?text=%D0%97%D0%B4%D0%B5%D1%81%D1%8C%20%D0%B1%D1%83%D0%B4%D0%B5%D1%82%20%D0%B2%D0%B0%D1%88%20%D1%82%D0%B5%D0%BA%D1%81%D1%82)



# Команда проекта

<a name="команда"></a>
[Sokolova Polina — Python developer](https://github.com/Pololoshka)
