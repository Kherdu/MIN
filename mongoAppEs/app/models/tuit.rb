class Tuit
  include Mongoid::Document
  field :text, type: String
  field :hashtag, type: String

  after_create :cache_hashtag
  before_destroy :uncache_hashtag

  def cache_hashtag
    $redis.lpush(hashtag, text)
  end

  def uncache_hashtag
    $redis.lrem(hashtag, 0, text)
  end
end
