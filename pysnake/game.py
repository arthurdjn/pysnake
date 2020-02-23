# -*- coding: utf-8 -*-
# Created on Sun Feb 16 12:48:18 2020
# @author: arthurd


import numpy as np
import random as rd

from pysnake.enum import Item
from pysnake.grid import Cell, Grid
from pysnake.snake import Snake


class Game:
    
    def __init__(self, shape, seed=True):
        
        # Fix random numbers, use for debug mode
        self.seed = seed
        if seed:
            rd.seed(1968)
        
        self.shape = shape
        self.grid = Grid(shape)
        # Add borders to the grid
        self.grid.add_wall_borders()
        self.snakes = [Snake(self)]
        self.apples = []
        self.add_apple()
        
        # Update snake's vision, because we just added some apples.
        for snake in self.snakes:
            snake.update_full_vision()
            
        
    def add_snake(self, snake=None):
        if snake is None:
            snake = Snake(self)
        self.snakes.append(snake)
    
            
    def generate_apple(self):
        """
        Generate and add an apple cell in the grid.

        Returns
        -------
        Cell
            Generated apple cell.
        """
                
        height, width = self.shape
        available_coord = []
        
        # Check the available cells
        for i in range(height):
            for j in range(width):
                cell = self.grid[i, j]
                # If the cell is empty, add it to the available cells list
                if cell.is_empty():
                    available_coord.append(cell.coord)
                    
        # Choose a position among all
        coord = rd.choices(available_coord)[0]
        apple = Cell(coord, Item.APPLE)
                
        return apple
    
    
    def add_apple(self):
        apple = self.generate_apple()
        self.apples.append(apple)
        # Update the grid
        self.grid.set_cell(apple)
        

    def restart(self):
        # Kill the snakes
        for snake in self.snakes:
            snake.kill()
        self.snakes = []
        # Add a new snake
        self.add_snake()
        
        # Delete all apples
        for apple in self.apples:
            self.grid.set_empty(apple.coord)
        self.apples = []
        # Add a new apple
        self.add_apple()
        
        # Update the snake's vision, in case the apple is visible
        for snake in self.snakes:
            snake.update_full_vision()















        
        