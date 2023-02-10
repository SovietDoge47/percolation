# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press Ctrl+F8 to toggle the breakpoint.
import numpy as np
import random


def main():
    matrix_dimension = get_inputs()  # Get user input for dimensions
    the_matrix = create_empty_matrix(matrix_dimension)  # Create a matrix of dim*dim size that is full of zeroes
    print(the_matrix)
    random

class Matrix:
    def __init__(self):
        self.dim = self.get_dim()
        self.p = self.get_p()

    def get_dim(self):
        """
        This function asks the user to input a size for the matrix and will not stop until an integer >1 is entered
        :parameter:
            None
        :return:
            size (int): The user's input for the size dimensions of the matrix (this program only allows matrices that
                        are square, having the same number of rows as columns)
        """
        while True:
            size = input('Enter the size of the matrix as a positive integer that is greater than 1: ')
            try:
                size = int(size)  # check if the input is an integer or not
            except ValueError:
                print('ERROR: not an int')
                continue
            if size > 1:  # check if the input is greater than 1
                return int(size)  # If both tests are passed, return size as an integer
            else:
                print("ERROR: not greater than 1")

    def get_p(self):
        """
        This function asks the user to input a size for the matrix and will not stop until an integer >1 is entered
        :parameter:
            None
        :return:
            size (int): The user's input for the size dimensions of the matrix (this program only allows matrices that
                        are square, having the same number of rows as columns)
        """
        while True:
            size = input('Enter the size of the matrix as a positive integer that is greater than 1: ')
            try:
                size = int(size)  # check if the input is an integer or not
            except ValueError:
                print('ERROR: not an int')
                continue
            if size > 1:  # check if the input is greater than 1
                return int(size)  # If both tests are passed, return size as an integer
            else:
                print("ERROR: not greater than 1")

def create_empty_matrix(dim):
    """
    This function creates a matrix of size (dim*dim) that is populated with zeroes
    :param:
        dim (int): The dimension of the matrix. The matrix is square, so the width and height will both be equal to dim
    :return:
        a_matrix:
    """
    matrix = np.zeros((dim, dim))
    return matrix


def fill_matrix(p):
    """

    :param p:
    :return:
    """
    print("howdy")


if __name__ == '__main__':
    main()
