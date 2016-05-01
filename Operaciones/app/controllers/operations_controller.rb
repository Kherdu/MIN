class OperationsController < ApplicationController
  def index
  end

  def new
    op1 = Random.new
    @operando1 = op1.rand(1..99)
    op2 = Random.new
    @operando2 = op2.rand(1..99)
    @operador = [:*, :+, :-, :/].sample
    @name = 'Rafa'
    @texto = nil
  end

  def create
    answer = params[:answer].to_i
    operando1 = params[:operando1].to_i
    operador = params[:operador].to_sym
    operando2 = params[:operando2].to_i
    resultado = operando1.send(operador,operando2)
    if resultado==answer
      op = Operation.new
      op.operation1 = operando1
      op.operation2 = operando2
      op.operator = operador
      op.answer = answer
      #raise "YA ESTA INSERTADO"
      op.save!
    end
  end
end

private
def operation_params
  return params.require(:operation).permit(:answer, :operando1, :operando2, :operador)
end 
