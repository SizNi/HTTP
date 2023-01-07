# SELECT * FROM users WHERE name = "John" ORDER BY last_name DESC LIMIT 10
users = User.objects.filter(  # WHERE
    first_name='John',
).order_by(  # ORDER BY
    '-last_name'
)[:10]  # LIMIT

for user in users:
    print(user.last_name)

User.objects.filter(
    id__in=[45, 101, 512],      # равно одному из значений списка (входит В список)
    first_name__iexact='John',  # равно без учёта регистра
    age__range=(18, 21),        # входит в диапазон 18..21
    middle_name__isnull=True,   # необязательное поле не заполнено
    last_name__icontains='ibn'  # содержит подстроку без учёта регистра
)