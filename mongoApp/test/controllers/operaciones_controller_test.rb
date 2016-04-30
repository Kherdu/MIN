require 'test_helper'

class OperacionesControllerTest < ActionController::TestCase
  test "should get genera" do
    get :genera
    assert_response :success
  end

  test "should get guarda" do
    get :guarda
    assert_response :success
  end

end
