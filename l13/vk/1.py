import vk_api

def predict_user_age(user_id):
    # Авторизация
    vk_session = vk_api.VkApi(token='vk1.a.fXetEGfstRY0Hp139l7VN0kXaAdlLkctCaxT0zygjZVajn7bT06qvzw9RoPvKtR8kM6_V6UE2EwNaQTTJXFgjA7Dz2NgeQ84YuRSBBGPUBI10PVphvKBF81pfMe5rNTFq7R-pK8G5UUzaDlKM7fVuYA-JS9c1NDHAUB2RDh46PSwPl5Jq8F6LqmDOBjYAstGj-pWZsuLPDWrJkUR7r7CyA')

    vk = vk_session.get_api()
    
    # Получаем информацию о друзьях пользователя
    friends = vk.friends.get(user_id=user_id, fields='bdate')
    
    ages = []
    for friend in friends['items']:
        if 'bdate' in friend:
            bdate = friend['bdate'].split('.')
            if len(bdate) == 3:
                age = 2024 - int(bdate[2])
                ages.append(age)
    
    if len(ages) > 0:
        predicted_age = sum(ages) // len(ages)
        return predicted_age
    else:
        return "Недостаточно данных для прогнозирования возраста"

# Пример использования
user_id = '91096618'
predicted_age = predict_user_age(user_id)
print(f"Прогнозируемый возраст пользователя: {predicted_age}")