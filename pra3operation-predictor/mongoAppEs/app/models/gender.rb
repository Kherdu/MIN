class Gender
  include Mongoid::Document
  field :name, type: String
  has_many :movies
end
