require 'test_helper'

class TuitsControllerTest < ActionController::TestCase
  setup do
    @tuit = tuits(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:tuits)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create tuit" do
    assert_difference('Tuit.count') do
      post :create, tuit: { hashtag: @tuit.hashtag, text: @tuit.text }
    end

    assert_redirected_to tuit_path(assigns(:tuit))
  end

  test "should show tuit" do
    get :show, id: @tuit
    assert_response :success
  end

  test "should get edit" do
    get :edit, id: @tuit
    assert_response :success
  end

  test "should update tuit" do
    patch :update, id: @tuit, tuit: { hashtag: @tuit.hashtag, text: @tuit.text }
    assert_redirected_to tuit_path(assigns(:tuit))
  end

  test "should destroy tuit" do
    assert_difference('Tuit.count', -1) do
      delete :destroy, id: @tuit
    end

    assert_redirected_to tuits_path
  end
end
