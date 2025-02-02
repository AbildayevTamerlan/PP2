# List of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


# 1
import random

def not_bad1(movie):
   return movie["imdb"] > 5.5

m_index = random.randrange(len(movies))
print(not_bad1(movies[m_index]))
print(not_bad1(movies[0]))
print("\n")


# 2
def not_bad2(movies):
   not_bad_m = []
   for movie in movies:
      if movie["imdb"] > 5.5:
         not_bad_m.append(movie)
   return not_bad_m

print(not_bad2(movies))
print("\n")

# 3
def by_category(category):
   category_m = []
   for movie in movies:
      if movie["category"] == category:
         category_m.append(movie)
   return category_m

print(by_category("Thriller"), "\n")
print(by_category("Action"), "\n")
print(by_category("Adventure"), "\n")
print(by_category("Drama"), "\n")
print(by_category("Romance"), "\n")
print(by_category("War"), "\n")
print(by_category("Crime"), "\n")
print(by_category("Comedy"), "\n")
print(by_category("Suspense"), "\n\n")


# 4
def average(movies):
   score = 0
   for movie in movies:
      score += movie["imdb"]
   print(score / len(movies))

average(movies)
print("\n")


# 5
def average_by_category(category):
   score = 0
   count = 0
   for movie in movies:
      if movie["category"] == category:
         score += movie["imdb"]
         count += 1
   print(category, ": ", score / count)

average_by_category("Thriller")
average_by_category("Action")
average_by_category("Adventure")
average_by_category("Drama")
average_by_category("Romance")
average_by_category("War")
average_by_category("Crime")
average_by_category("Comedy")
average_by_category("Suspense")