puts "*" * 40
puts "Connecting to redis... "

if Rails.env == "production"
  uri = URI.parse(ENV["REDIS_URL"])
  $redis = Redis.new(:host => uri.host, :port => uri.port, :password => uri.password)
else
  $redis = Redis.new(:host => 'localhost', :port => 6379)
end
puts "*" * 40