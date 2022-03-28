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

# Methods
# last evaluated expression in a method is automatically returned
def multiply(num_1, num_2)
  num_1.to_f * num_2.to_f
end
puts multiply(2, 5) # => 10
