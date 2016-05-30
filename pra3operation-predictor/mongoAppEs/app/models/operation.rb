require 'net/http'

class Operation
  include Mongoid::Document

  field :op, type: String
  field :op1, type: Integer
  field :op2, type: Integer
  field :t0, type: Time
  field :t1, type: Time
  field :estimation, type: String

  def total_time
    t1 - t0
  end

  def estimate
    uri = URI('http://localhost:5000/predict')
    params= {:op1 => op1.to_f, :op => op, :op2 => op2.to_f }
    uri.query = URI.encode_www_form(params)
    estimation = Net::HTTP.get_response(uri)
  end

  def self.create_random
    @operation = Operation.new
    @operation.op1 = rand(99)
    @operation.op2 = rand(99)
    @operation.op = ['+'].sample#,'-','*','/'].sample
    @operation.estimate
    @operation.t0 = Time.new
    @operation.save
    @operation
  end
end
