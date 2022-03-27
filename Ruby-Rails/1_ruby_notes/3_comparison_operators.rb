# Comparison operators

puts 10 == 10         # => true
puts 10 == 9          # => false
puts 10 == "10"       # => false
puts 10 == "10".to_i  # => true
puts 10 == "10".to_f  # => true
puts 10 === 10.0      # => true
puts 10.eql?(10.0)    # => false .eql compares types
puts 10 != 9          # => true

