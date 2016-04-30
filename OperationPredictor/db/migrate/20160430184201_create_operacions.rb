class CreateOperacions < ActiveRecord::Migration
  def change
    create_table :operacions do |t|
      t.string :name
      t.integer :operando1
      t.string :op
      t.integer :operando2
      t.string :tiempo
      t.timestamps null: false
    end
  end
end
