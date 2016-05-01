class OperationsController < ApplicationController
  def index
  end

  def new

  end

  def create
    @Operation = Operacion.new
    op1 = Random.new
    @Operation.operando1 = op1.rand(1..99)
    op2 = Random.new
    @Operation.operando2 = op2.rand(1..99)
    @Operation.operador = [:*, :+, :-, :/].sample
    @Operation.name = 'Rafa'
    @resultado = @Operation.operando1.send(@Operation.operador,@Operation.operando2)
    @Operation.save

    redirect to @Operation
  end
end
