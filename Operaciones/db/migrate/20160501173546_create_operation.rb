class CreateOperation < ActiveRecord::Base
  def change
    create_table :operations do |t|
      t.string :time
      t.string :name
      t.integer :operation1
      t.integer :answer
      t.integer :operation2
      t.string :operator
    end
  end
end
