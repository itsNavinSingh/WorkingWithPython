def Data_List(a,b,c,d):
    Datas =[]
    for i in range(len(a)):
        Units = {}
        Units['Name'] = a[i]
        Units['Follower_Count'] = b[i]
        Units['Description'] = c[i]
        Units['Country'] = d[i]
        Datas.append(Units)
    return Datas

Name = 'Barak Obama, Elon Musk, Justin Bieber, Katy Perry, Rihana, Ronaldo, Taylor Swift, Donald Trump, Narendra Modi, Lady Gaga, Youtube, Ellen DeGenereres, Kim Kardashian, NASA, Selena Gomez, Twitter, CNN Breaking News, Justin Timberlake, Bill Gates, CNN, Neymar, Britney Spears, The Newyork Times, Demi Lovato, Shakira, LeBoron, Virat Kohli, PMO India, BBC Breaking News, Jimmy Fallon, Amitabh Bachchan, BTS, Miley Cyrus, Real Madrid CF, UEFA Champions League, Jennifer Lopez, Akshay Kumar, FC Barcelona, Salman Khan, ESPN, Bruno Mars, Oprah Winfrey, Shah Rukh Khan, BTS Bighit, Sports Centers, Niall Horan, NBA, Kylie Jenner, Drake, BBC World News'.split(', ')
Follower = [133.3, 125.2, 113.6, 108.7, 107.5, 106.9, 92.2, 87.7, 85.6, 85.2, 84.9, 77.9, 76.9, 74.3, 67.6, 66.4, 65.0, 64.0, 62.7, 61.2, 60.7, 59.5, 56.0, 54.7, 53.9, 53.2, 52.4, 52.2, 51.6, 51.4, 51.2, 48.1, 47.8, 46.7, 45.8, 45.7, 45.5, 45.2, 44.6, 43.6, 43.1, 43.0, 42.8, 42.2, 41.3, 41.1, 41.09, 40.3, 39.8, 39.0]
Description = '44th US President, Businessman, Musician, Musician, Musician, Football Player, Musician, 45th US President, Prime Minister of India, Musician, Musician, Video Sharing Platform, Comedian, Bussiness Women, Space Agency, Musician, Operator of Platform, News Channel, Musician, Bussinessman, News Channel, Footbal Player, Musician, Newspaper, Musician, Basketball Player, Cricket Player, Prime Minister Office of India, News Channel, Comedian, Actor, Musician, Actress, Football Club, Football League, Musician, Actor, Football Club, Actor, Sports Channel, Musician, Television Personality, Actor, Musician, Sports Channel, Musician, Basketball Leauge, Bussiness women, Rapper, News Channel'.split(', ')
Country = 'USA, USA, CANADA, USA, BARBADOS, PORTUGAL, USA, USA, INDIA, USA, USA, USA, USA, USA, USA, USA, USA, USA, USA, USA, BRAZIL, USA, USA, USA, COLOMBIA, USA, INDIA, INDIA, UK, USA, INDIA, SOUTH KOREA, USA, SPAIN, EUROPE, USA, CANADA, SPAIN, INDIA, USA, USA, USA, INDIA, SOUTH KOREA, USA, IRELAND, USA, USA, CANADA, UK'.split(', ')

List_Of_Datas = Data_List(Name, Follower, Description, Country)
