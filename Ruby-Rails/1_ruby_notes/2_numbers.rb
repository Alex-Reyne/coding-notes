# Numbers
puts 1 + 2        # => 3
puts 10 / 4       # => 2
puts 10.0 / 4     # => 2.5
puts 10 / 4.0     # => 2.5
puts 10 / 4.to_f  # => 2.5
puts (10/4).to_f  # => 2.0

puts "-" * 20             # creates line of dashes
20.times { print "-" }    # creates line of dashes
puts
20.times { puts rand(10) } # generates random number between 0-9


# Simple calculator
puts "Simple calculator"
25.times { print "-" }
puts
puts "Enter the first number"
num_1 = gets.chomp
puts "Enter the second number"
num_2 = gets.chomp
puts "The first number multiplied by the second number is: #{num_1.to_f * num_2.to_f}"
puts "The first number divided by the second number is: #{num_1.to_f / num_2.to_f}"
puts "The first number subtracted from the second number is: #{num_2.to_f - num_1.to_f}"
puts "The first number added to the second number is: #{num_2.to_f + num_1.to_f}"
puts "The first number mod the second number is: #{num_1.to_f % num_2.to_f}"
