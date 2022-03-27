# Arrays
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print a   # => [1, 2, 3, 4, 5, 6, 7, 8, 9]
puts
p a       # => [1, 2, 3, 4, 5, 6, 7, 8, 9] \n
puts a    # outputs each element on new line
p a.last  # => 9

# Range
p x = 1..10       # => 1..10
p x.class         # => Range
p x.to_a          # to array => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p x.to_a.shuffle  # method chain to shuffle => [9, 7, 10, 2, 6, 3, 1, 5, 4, 8]
p x.to_a.reverse  # => [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
p x               # x range is unmutated => 1..10

# ! will modify object it's called on
p y = (11..20).to_a # => [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
p y.reverse         # => [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
p y                 # y left unmutated => [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
p y.reverse!        # ! mutates caller => [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
p y                 # => [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

