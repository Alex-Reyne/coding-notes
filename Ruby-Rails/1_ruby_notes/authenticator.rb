# Password Authenticator App
# Will use: Hash, Array, Branching, Loops

users = [
  { username: "john", password: "password1"}, 
  { username: "jack", password: "password2"}, 
  { username: "jill", password: "password3"}, 
]

puts "Welcome to the authenticator"
puts "-" * 20
puts
puts "This program will take input from the user and compare password"
puts "If password is correct, you will get back the user object"

def auth_user(username, password, list_of_users)
  list_of_users.each do |user_record|
    if (user_record[:username] == username) && (user_record[:password] == password)
      return user_record
      break
    end
  end
  "Credentials were not correct" # last line is implicitly returned
end

attempts = 1
while attempts < 4
  print "Username: "
  username = gets.chomp
  print "Password: "
  password = gets.chomp

  authentication = auth_user(username, password, users)
  puts authentication

  puts "Press n to quit or any other key to continue:"
  input = gets.chomp.downcase
  break if input == "n"
  attempts += 1
end

puts "You have exceeded the number of attempts" if attempts == 4
