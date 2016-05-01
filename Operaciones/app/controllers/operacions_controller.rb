class OperationsController < ApplicationController
  def index
  end

  def new
    @operation = Operacion.new
    op1 = Random.new
    @operation.operando1 = op1.rand(1..99)
    op2 = Random.new
    @operation.operando2 = op2.rand(1..99)
    @operation.operador = [:*, :+, :-, :/].sample
    @operation.name = 'Rafa'
    @resultado = @operation.operando1.send(@operation.operador,@operation.operando2)
    @operation.save

    #redirect to @Operation
  end

  def create

  end
end
