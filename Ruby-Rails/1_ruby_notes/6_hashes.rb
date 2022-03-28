# Hashes a.k.a. dictionary
p string_hash = {'a' => 1, 'b' => 2, 'c' => 3}
p string_hash['a']    # => 1
p string_hash.keys    # => ["a", "b", "c"]
p string_hash.values  # => [1, 2, 3]
string_hash.each do |key, value|
  puts "The key is #{key} and the value is #{value}"
end
puts

# Hash w/ symbols
p symbol_hash = {a: 1, b: 2, c: 3}
p symbol_hash[:a] # => 1
symbol_hash[:d] = 4
p symbol_hash     # => {:a=>1, :b=>2, :c=>3, :d=>4}
symbol_hash[:a] = 'new val'
p symbol_hash     # => {:a=>"new val", :b=>2, :c=>3, :d=>4}
symbol_hash.each {|key, value| puts "The key is #{key} and the value is #{value}"}
p symbol_hash.select {|k, v| v.is_a?(String) } # => {:a=>"new val"}
p symbol_hash.each {|k, v| symbol_hash.delete(k) if v.is_a?(String)} # => {:b=>2, :c=>3, :d=>4}
