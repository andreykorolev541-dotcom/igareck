# VPN Config Checker

Автоматически проверяет работоспособность VLESS-конфигураций и скачивает белые списки. Каждые 6 часов GitHub Actions запускает проверку — нерабочие конфиги отсеиваются, результат коммитится в репозиторий.

## 🔗 Подписки

| Описание | Ссылка |
|---|---|
| ✅ Рабочие VLESS (base64-подписка) | `https://raw.githubusercontent.com/Rageru01/igareck/main/configs/working_sub.txt` |
| ✅ Рабочие VLESS (plain text) | `https://raw.githubusercontent.com/Rageru01/igareck/main/configs/working.txt` |
| 🏳️ Белый список CIDR (проверенный) | `https://raw.githubusercontent.com/Rageru01/igareck/main/configs/WHITE-CIDR-RU-checked.txt` |
| 🏳️ Белый список CIDR (полный) | `https://raw.githubusercontent.com/Rageru01/igareck/main/configs/WHITE-CIDR-RU-all.txt` |
| 🏳️ Белый список SNI | `https://raw.githubusercontent.com/Rageru01/igareck/main/configs/WHITE-SNI-RU-all.txt` |

## ⚙️ Как добавить в VPN-клиент

1. Скопируйте нужную ссылку из таблицы выше
2. Откройте настройки клиента (Karing, NekoBox, v2rayN, Shadowrocket, Sing-box)
3. Добавьте новую подписку и вставьте ссылку
4. Включите автообновление — список будет обновляться каждые 6 часов сам

## 📌 Источник данных

Конфигурации берутся из репозитория [igareck/vpn-configs-for-russia](https://github.com/igareck/vpn-configs-for-russia), проходят проверку TCP/TLS-соединения и только рабочие попадают в итоговый список.

## 🔍 Как работает проверка

- Скачиваются VLESS-конфиги из источника
- Каждый конфиг проверяется реальным подключением (TCP + TLS, до 50 потоков)
- Нерабочие отсеиваются
- Результат сохраняется в `configs/` и коммитится в репозиторий
- Белые списки CIDR и SNI скачиваются без проверки и обновляются синхронно

## 📊 Статистика последнего запуска

Доступна в [`configs/stats.json`](configs/stats.json)
