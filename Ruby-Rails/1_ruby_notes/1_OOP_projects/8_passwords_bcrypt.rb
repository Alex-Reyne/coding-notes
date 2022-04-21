# Password hashing with bcrypt

require 'bcrypt'

my_password_1 = BCrypt::Password.create("my password")
my_password_2 = BCrypt::Password.create("my password")
# all hash versions are different
puts my_password_1 # => $2a$12$OsQ4CuejQNXvuSGN6YbONuqqw4gOr5Tyj7IIWuD8HDpVl3mLiBPvC
puts my_password_2 # => $2a$12$jmEYMulGzF9ETZGlxP4wY.1uzKX3jcGrlpiP0i723mUtDzSxFDJpe
puts my_password_1 == "my password" # => true
puts my_password_1 == my_password_2 # => false

# Set new password to my_password_1 hash, will equal original string
my_new_password = BCrypt::Password.new("$2a$12$OsQ4CuejQNXvuSGN6YbONuqqw4gOr5Tyj7IIWuD8HDpVl3mLiBPvC")
puts my_new_password == "my password"     # => true
puts my_new_password == "not my password" # => false


# CRUD Functions for hash

users = [
      { username: "john", password: "password1" },
      { username: "jane", password: "password2" },
      { username: "jack", password: "password3" },
]

def create_hash_digest(password)
  BCrypt::Password.create(password)
end

def verify_hash_digest(password)
  BCrypt::Password.new(password)
end

# convert password str to hash_digest
def create_secure_users(list_of_users)
  list_of_users.each do |user_record|
    user_record[:password] = create_hash_digest(user_record[:password])
  end
  list_of_users # implicit return
end

puts create_secure_users(users)

new_password = create_hash_digest("password1")
puts new_password == "password1" # => true
puts new_password == "password2" # => false

