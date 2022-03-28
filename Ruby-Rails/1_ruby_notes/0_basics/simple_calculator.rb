# Simple calculator

# Methods
def multiply(num_1, num_2)
  num_1.to_f * num_2.to_f
end
def divide(num_1, num_2)
  num_1.to_f / num_2.to_f
end
def subtract(num_1, num_2)
  num_1.to_f - num_2.to_f
end
def add(num_1, num_2)
  num_1.to_f + num_2.to_f
end
def mod(num_1, num_2)
  num_1.to_f % num_2.to_f
end

# User prompt
puts "Simple calculator"
25.times { print "-" }
puts
puts "What do you want to do? 1) multiply 2) divide 3) subtract 4) find remainder"
prompt = gets.chomp
puts "Enter first number"
num_1 = gets.chomp
puts "Enter second number"
num_2 = gets.chomp

# Conditional Branching
if prompt == "1"
  puts "You have chosen to multiply #{num_1} with #{num_2}"
  result = multiply(num_1, num_2)
elsif prompt == "2"
  puts "You have chosen to divide"
  result = divide(num_1, num_2)
elsif prompt == "3"
  puts "You have chosen to subtract"
  result = subtract(num_1, num_2)
elsif prompt == '4'
  puts "You have chosen to find the remainder"
  result = mod(num_1, num_2)
else
  puts "You have made an invalid choice"
end

puts result
