# Whitelist Updater

Автоматически скачивает белые списки из репозитория [igareck/vpn-configs-for-russia](https://github.com/igareck/vpn-configs-for-russia). Каждые 6 часов GitHub Actions обновляет файлы и коммитит результат в репозиторий.

## 🔗 Подписки

| Описание | Ссылка |
|---|---|
| 🏳️ Белый список CIDR (проверенный) | `https://raw.githubusercontent.com/Rageru01/igareck/main/configs/WHITE-CIDR-RU-checked.txt` |
| 🏳️ Белый список CIDR (полный) | `https://raw.githubusercontent.com/Rageru01/igareck/main/configs/WHITE-CIDR-RU-all.txt` |
| 🏳️ Белый список SNI | `https://raw.githubusercontent.com/Rageru01/igareck/main/configs/WHITE-SNI-RU-all.txt` |

## ⚙️ Как добавить в VPN-клиент

1. Скопируйте нужную ссылку из таблицы выше
2. Откройте настройки клиента (Karing, NekoBox, v2rayN, Shadowrocket, Sing-box)
3. Добавьте новую подписку и вставьте ссылку
4. Включите автообновление — список будет обновляться каждые 6 часов сам

## 📌 Источник данных

Белые списки берутся из репозитория [igareck/vpn-configs-for-russia](https://github.com/igareck/vpn-configs-for-russia) и сохраняются без проверки.

## 🔍 Как работает обновление

- Белые списки CIDR и SNI скачиваются из источника
- Файлы сохраняются в `configs/` и коммитятся в репозиторий
