json.array!(@tuits) do |tuit|
  json.extract! tuit, :id, :text, :hashtag
  json.url tuit_url(tuit, format: :json)
end
