# WEB SCRAPPER

get information about car

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) t

```bash
pip install -r requirements.txt
```

## Usage


```bash
docker-compose up -d
```

aplication will run on localhost:5000

## REQUEST (GET)

```bash
/get-car-info?brand={BRAND}z&city={CITY}&type={CARTYPE}
```

## RESPONSE

```bash
[
{
  title: "Mercedes-Benz E 230",
  price: "950000",
  params: "1989 г., Б/у купе, 2.3 л, бензин, КПП автомат",
  picture: "https://photos-kl.kcdn.kz/webp/27/271afdba-4ff0-4894-a3f0-0fbb1c58bd9d/1-160x120.jpg"
  },
  {
  title: "Mercedes-Benz S 320",
  price: "3650000",
  params: "1998 г., Б/у седан, 3.2 л, бензин, КПП автомат, белый, металлик, литые диски, тонировка, люк, ветровики, хрустальная о...",
  picture: "https://photos-kl.kcdn.kz/webp/4e/4eeba79b-839c-4647-ab13-4976e64b5be5/1-160x120.jpg"
  },
  {
]
```
