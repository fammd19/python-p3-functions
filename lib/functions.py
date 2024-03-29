#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

#function greet(name) {
#  console.log(`Hello, ${name}!`);
#}

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

#function greetWithDefault(name = "programmer") {
#  console.log(`Hello, ${name}!`);
#}


def add(num1, num2):
    return num1 + num2

# function add(num1, num2) {
#  return num1 + num2;
#}
   

def halve(number):
    return number/2

#function halve(number) {
#  if (typeof number !== "number") return null;
#
#  return number / 2;
#}
