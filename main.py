from test import rectangle_test, ellipse_test, square_test, circle_test
from stats import rectangle_stats, ellipse_stats, square_stats, circle_stats

mode = int(input('To run walk simulation, enter 1. To generate average steps graph, enter 2: '))
shape = int(input('Choose shape: 1. rectangle, 2. ellipse, 3. square, 4. circle: '))

if mode == 1:
  num_walks = int(input('Enter number of walks to do (1-5) :  '))
  def one():
    rectangle_test(num_walks)
 
  def two():
    ellipse_test(num_walks)
 
  def three():
    square_test(num_walks)

  def four():
    circle_test(num_walks)
 
  switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
      }
  func = switcher.get(shape, "nothing")
  func()


if mode == 2:
  num_walks = int(input('Enter number of walks to do  :  '))
  def one():
    rectangle_stats(num_walks)
 
  def two():
    ellipse_stats(num_walks)
 
  def three():
    square_stats(num_walks)

  def four():
    circle_stats(num_walks)
 
  switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
      }
  func = switcher.get(shape, "nothing")
  func()