class OperacionesController < ApplicationController
  def genera
    operando1 = Random.new
    operando1.rand(1..99)
    operando2 = Random.new
    operando2.rand(1..99)
    print operando1
    print operando2
    operador = [:*, :+, :-, :/].sample

  end

  def guarda


  end
end
