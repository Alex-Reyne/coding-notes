puts "What is your first name?"
first_name = gets.chomp
puts "What is your last name?"
last_name = gets.chomp
full_name = "#{first_name} #{last_name}"
puts "Your full name is #{full_name}"
puts "Your name reversed is #{full_name.reverse}"
puts "Your name has #{full_name.length - 1} characters in it"

puts "Thank you, you said your first name is #{first_name}"

puts "Enter a number to multiply by 2"
input = gets.chomp
puts input * 2 # will repeat number as str
puts input.to_i * 2

