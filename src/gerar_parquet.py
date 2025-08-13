import pandas as pd
import numpy as np
from faker import Faker

# Inicializa gerador de dados falsos
fake = Faker()
Faker.seed(42)

# Gera 3000 registros
n = 3000
data = {
    "id": range(1, n + 1),
    "name": [fake.first_name() for _ in range(n)],
    "age": np.random.randint(18, 70, size=n),
    "signup_date": [fake.date_between(start_date="-5y", end_date="today") for _ in range(n)],
    "is_active": np.random.choice([True, False], size=n),
    "score": np.round(np.random.uniform(0, 100, size=n), 2),
    "country": [fake.country() for _ in range(n)],
}

df = pd.DataFrame(data)

# Salva como Parquet
df.to_parquet("data/raw/sample_data.parquet", index=False)

print("Arquivo Parquet gerado com sucesso!")