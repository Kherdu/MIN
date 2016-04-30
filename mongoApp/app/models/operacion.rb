#valdrá?
# operador suma, resta, multiplicación y division entera
# los operandos son 2 numeros enteros entre 1 y 99
# nombre de la persona que hace la Operacion
# tiempo que ha tardado en la operacion
class Operacion
  include Mongoid::Number
  field :op, type: [:add, :div, :mul, :sub]
  field :operando1, type: Integer
  field :operando2, type: Integer
  field :name, type: String
  field :tiempo, type: String
end
