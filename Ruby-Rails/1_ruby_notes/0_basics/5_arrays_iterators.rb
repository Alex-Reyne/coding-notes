# Arrays
puts "-" * 20, "Arrays"
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print a       # => [1, 2, 3, 4, 5, 6, 7, 8, 9]
puts
p a           # => [1, 2, 3, 4, 5, 6, 7, 8, 9] \n
puts a        # outputs each element on new line
p a.first     # => 1
p a.last      # => 9
a.append(10)  # adds item to end
p a           # => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.unshift(0)  # adds item to start
p a           # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
puts

# Range
puts "-" * 20, "Range"
p x = 1..10       # => 1..10
p x.class         # => Range
p x.to_a          # to array => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p x.to_a.shuffle  # method chain to shuffle => [9, 7, 10, 2, 6, 3, 1, 5, 4, 8]
p x.to_a.reverse  # => [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
p x               # x range is unmutated => 1..10
puts

# ! will modify object it's called on
puts "-" * 20, "Bang methods"
p y = (11..20).to_a # => [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
p y.reverse         # => [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
p y                 # y left unmutated => [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
p y.reverse!        # ! mutates caller => [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
p y                 # => [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
puts

# Range with letters
puts "-" * 20, "Range with letters"
p alpha = "a".."z"  # => "a".."z"
p alpha.to_a        # => ["a", "b", "c", ... "z"]
p alpha.to_a.length # => 26
puts

# Other Array Methods
puts "-" * 20, "Other Array Methods"
a = [1, 2, 3]
a.unshift('item')
a.append('item')
p a       # => ["item", 1, 2, 3, "item"]
p a.uniq  # only contain unique items => ["item", 1, 2, 3]
p a       # caller unmutated => ["item", 1, 2, 3, "item"]
p a.uniq!
p a                   # caller mutated => ["item", 1, 2, 3]

p a.include?("item")  # => true
p a.include?(100)     # => false
p a.push("new item")  # => ["item", 1, 2, 3, "new item"]
b = a.pop
p a                   # => ["item", 1, 2, 3]
p b                   # => "new item"

p a_join = a.join("-")  # => "item-1-2-3"
p a_join.split("-")     # => ["item", "1", "2", "3"]
puts

# Iteration
puts "-" * 20, "Iteration"
p arr = ("a".."c").to_a # => ["a", "b", "c"]
# Conventional for loop
for i in arr
  print i + " "
end
puts
# Ruby approach
arr.each do |i|
  print i + " "
end
puts
# Further simplified
arr.each {|i| print i + " "}
puts
arr.each {|i| print i.capitalize + " "}
puts

# Select method
p z = (1..10).to_a.shuffle
p z.select {|number| number.odd?} # selects only odd numbers

