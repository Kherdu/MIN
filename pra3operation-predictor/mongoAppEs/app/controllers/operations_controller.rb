class OperationsController < ApplicationController

  def index
    @name = "Yo"
  end

  def new
    @operation = Operation.create_random
    print @operation.op1
  end

  def answer
    @operation = Operation.find(params[:id])

    if @operation.op1 + @operation.op2 == params[:respuesta].to_i
      @operation.t1 = Time.new
      @operation.save
    else
      render :new
    end

  end

end
