require 'elasticsearch/model'

class Movie
  include Mongoid::Document
  include Elasticsearch::Model
  include Elasticsearch::Model::Callbacks
  
  field :name, type: String

  belongs_to :gender

  field :description, type: String
  field :rank, type: Integer

  before_create :check_values

  def check_values
    name ||= "Undefined"
    description ||= "Description was not provided"

  end

  def as_indexed_json(options={})
    as_json(only: [:name, :description])
  end

   mapping do
    indexes :name, type: :string, :analyzer => :english, :boost => 50
    indexes :description, type: :string, :analyzer => :english, :boost => 20
  end

  def self.search(q)
    __elasticsearch__.search( query: {
          multi_match: {
              fields:  [ "name", "description" ],
              query: q,
              fuzziness: 2,
              prefix_length: 2
              }
            },

        highlight: {
          fields: {
            description: {fragment_size: 100, number_of_fragments: 3}
          }
        }
      )
  end

  def self.ranking
    map = %Q{
            function() {
              emit(this.gender, this.rank);
            };
          } 

   reduce = %Q{
      function(key, ranks) {
        return Array.sum(ranks) / ranks.length;
      };
   }

   result = map_reduce(map, reduce).out(inline: true)
   result 
  end

end
