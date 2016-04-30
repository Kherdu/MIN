class OperacionesController < ApplicationController
  def new
    @operation = Operacion.new
    op1 = Random.new
    @Operation.operando1 = op1.rand(1..99)
    op2 = Random.new
    @Operation.operando2 = op2.rand(1..99)
    @Operation.operador = [:*, :+, :-, :/].sample
    @Operation.name = 'Rafa'
    resultado = @Operation.operando1.send(@Operation.operador,@Operation.operando2)

    redirect_to '/contesta'
  end

  def answer


  end
end
