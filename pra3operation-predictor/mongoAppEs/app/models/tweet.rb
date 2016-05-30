class Tweet
  include Mongoid::Document
  field :text, type: String
  field :hashtag, type: String

  after_create :cache_hashtag


  def cache_hashtag
    $redis.lpush(hashtag, text)
  end
end
