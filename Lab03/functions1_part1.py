# 1
def to_ounces(grams):
   print( grams / 28.3495231)


# 2
def to_centigrade(fahrenheit):
   print((5 / 9) * (fahrenheit - 32))


# 3
def solve(numheads, numlegs):
   rabbits = (numlegs - 2*numheads) / 2
   chickens = numheads - rabbits
   print(f"Chickens - {int(chickens)}, rabbits - {int(rabbits)}")


# 4
def filter_prime(numbers):
   prime_numbers = []
   for number in numbers:
      if number <= 1:
         continue
      if number == 2:
         prime_numbers.append(number)
         continue
      if number % 2 == 0:
         continue

      is_prime = True
      for i in range(3, int(number ** 0.5) + 1, 2):
         if number % i == 0:
            is_prime = False
            break

      if is_prime:
         prime_numbers.append(number)

   return prime_numbers


# 5
def permutations(string):
   sequence = [i for i in string]
   n = len(sequence)
   a = sequence[::]
   b = [i for i in range(n)]
   c = [0 for i in range(n + 1)]
   k = 1
   j = 1
   
   while True:
      yield ''.join(a)
      k = 1
      while c[k] == k:
         c[k] = 0
         k += 1
      if k == n:
         return
      c[k] += 1
      a[0], a[b[k]] = a[b[k]], a[0]
      j = 1
      k -= 1
      while j < k:
         b[j], b[k] = b[k], b[j]
         j += 1
         k -= 1
   

# 6
def reverse_sentence(sentence):
   sentence_list = sentence.split()
   
   r_sentence = ""
   for i in range(len(sentence_list) - 1, -1, -1):
      r_sentence += sentence_list[i]
      if i != 0:
         r_sentence += " "

   return r_sentence


# 7
def has_33(nums):
   for i in range(len(nums) - 1):
      if nums[i] == 3 and nums[i + 1] == 3:
         return True
   return False


# 8
def spy_game(nums):
   if 0 in nums and ((len(nums) - 1) - nums.index(0) >= 2):
      slice1 = nums.index(0) + 1
      if 0 in nums[slice1:] and ((len(nums[slice1:]) - 1) - nums[slice1:].index(0) >= 1):
         slice2 = nums[slice1:].index(0) + 1
         if 7 in nums[slice2:]:
            return True
   return False


# 9
def sphere_volume(radius):
   volume = (4/3) * 3.14 * (radius**3)
   print(volume)


# 10
def unique_elements(elements):
   u_elements = []
   for element in elements:
      if element not in u_elements:
         u_elements.append(element)
   return u_elements


# 11
def palindrome(phrase):
   r_phrase = ""
   for i in range(len(phrase) - 1, -1, -1):
      r_phrase += phrase[i]
   return phrase == r_phrase


# 12
def histogram(nums):
   for num in nums:
      print('*' * num)


# 13
import random

def guess_the_number():
   name = ""
   while name == "":
      name = input("Hello! What is your name?\n")

   to_guess = random.randint(1, 20)
   print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
   guess = int(input("Take a guess.\n"))
   tries = 1

   while guess != to_guess:
      tries += 1
      if guess > to_guess:
         print("\nYour guess is too high.")
      else:
         print("\nYour guess is too low.")
      guess = int(input("Take a guess.\n"))

   print(f"\nGood job, {name}! You guessed my number in {tries} guesses!")