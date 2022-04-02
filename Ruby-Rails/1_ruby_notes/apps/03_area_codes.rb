# Area codes


dial_book = {
  "toronto" => "416",
  "mississauga" => "905",
  "vancouver" => "604",
  "calgary" => "403",
  "montreal" => "514"
}

# Get city names from the hash
def get_city_names(somehash)
  somehash.keys
end

# Get area code based on given hash and key
def get_area_code(somehash, key)
  somehash[key]
end

# Execution flow
loop do
  puts "Do you want to lookup an area code based on a city name? (Y/N)"
  answer = gets.chomp.downcase
  break if answer != "y"

  puts "Which city do you want the area code for?"
  puts get_city_names(dial_book)
  puts "Enter your selection"
  city = gets.chomp

  if dial_book.include?(city)
    puts "The area code for #{city} is #{get_area_code(dial_book, city)}"
  else
    puts "You entered a city name not in the dictionary"
  end
end






