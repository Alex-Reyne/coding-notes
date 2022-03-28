# Conditionals - if/else
condition_1 = false
condition_2 = false
if condition_1 && condition_2
  puts "All conditions evaluated to true"
elsif condition_1 || condition_2
  puts "1 condition evaluated to true"
else
  puts "All conditions evaluated to false"
end

# Conditionals Branching
name = "Evgeny"
if name == "John"
  puts "Welcome, John"
elsif name == "Mike"
  puts "Welcome, Mike"
else
  puts "Welcome, User"
end
