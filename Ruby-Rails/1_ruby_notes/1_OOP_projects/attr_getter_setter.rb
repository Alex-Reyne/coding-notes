class Student

  # allows both set/get
  attr_accessor :first_name, :last_name, :email, :username
  # allows only get
  # attr_reader :username

  # instance variables
  @first_name
  @last_name
  @email
  @username
  @password

  def initialize(firstname, lastname, username, email, password)
    @first_name = firstname
    @last_name = lastname
    @username = username
    @email = email
    @password = password
  end

  def set_username
    @username =  "john_username"
  end

  # # setter notation
  # def first_name=(name)
  #   @first_name = name
  # end
  # # getter
  # def first_name
  #   @first_name
  # end


  # classes have this method by default:
  def to_s
    "First name: #{@first_name}"
  end
end

john = Student.new  # create new object
# Set instance variables
john.first_name = "John"
john.last_name = "Doe"
john.email = "john@example.com"
john.set_username
# Get instance variables
puts john.first_name
puts john.last_name
puts john.email
puts john.username


# class User
#   attr_accessor :name, :email
#   def initialize(name, email)
#     @name = name
#     @email = email
#   end
#   def run
#     puts "Hey I'm running"
#   end
#   def self.identify_yourself
#     puts "Hey I am a class method"
#   end
# end
# user = User.new("john", "john@example.com")
# user.run
# User.identify_yourself # to run this class method you don't need an instance of user 


