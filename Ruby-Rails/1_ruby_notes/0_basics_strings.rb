# Basics
print "Hello World"   # outputs str to console, no new line
print "Hello World\n" # adds new line
puts "Hello World"    # outputs str to console, returns nil, new line
p "Hello World"       # outputs and returns arg value

greeting = "Greeting variable"
puts greeting

def say_hello(name)
  puts "inside method"
  puts name
end
say_hello "Hello John"


# Strings
## String concatenation
first_name = "John"
last_name = "Doe"
puts first_name + " " + last_name # => John Doe
## String interpolation
full_name = "#{first_name} #{last_name}" # only works w/ double quotes
puts full_name # => John Doe

## String methods
puts full_name.class      # => String
puts full_name.length     # => 8
puts full_name.reverse    # => eoD nhoJ
puts full_name.capitalize # => John doe
puts full_name.empty?     # => false
puts "".empty?            # => true
puts "".nil?              # => false

sentence = "Welcome to the jungle"
puts sentence                             # => Welcome to the jungle
puts sentence.sub("the jungle", "utopia") # => Welcome to utopia

## Method chaining
puts 10             # => 10
puts 10.class       # => Integer
puts 10.to_s        # => "10"
puts 10.to_s.class  # => String


# Variable assignment
road_sign = "broadview"
new_road_sign = road_sign
puts new_road_sign # => broadview
road_sign = "granville" # re-assigning var
puts road_sign # => granville
puts new_road_sign # => broadview
# new_road_sign still points to original value location

