class Operacion < ActiveRecord::Base
   enum op:[:add, :div, :mul, :sub]
   field :operando1, type: Integer
   field :operando2, type: Integer
   field :name, type: String
   field :tiempo, type: String
end
