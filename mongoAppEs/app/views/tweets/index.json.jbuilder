json.array!(@tweets) do |tweet|
  json.extract! tweet, :id, :text, :hashtag
  json.url tweet_url(tweet, format: :json)
end
