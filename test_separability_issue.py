#!/usr/bin/env python

"""Test script to reproduce the separability matrix issue"""

# Let me create a minimal version to understand the problem first
import numpy as np

def mock_separability_matrix(model):
    """Mock implementation to understand the problem"""
    if hasattr(model, '_separability'):
        return model._separability
    else:
        # Default case - identity matrix
        return np.eye(model.n_outputs, model.n_inputs, dtype=bool)

class MockModel:
    def __init__(self, n_inputs, n_outputs, separable=True):
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.separable = separable
        if separable and n_inputs == n_outputs:
            self._separability = np.eye(n_outputs, n_inputs, dtype=bool)
        else:
            self._separability = np.ones((n_outputs, n_inputs), dtype=bool)

class CompoundModel:
    def __init__(self, left, right, op):
        self.left = left
        self.right = right
        self.op = op
        
        if op == '&':  # parallel combination
            self.n_inputs = left.n_inputs + right.n_inputs
            self.n_outputs = left.n_outputs + right.n_outputs
        elif op == '|':  # series combination
            self.n_inputs = right.n_inputs
            self.n_outputs = left.n_outputs
            
    def __and__(self, other):
        return CompoundModel(self, other, '&')
        
    def __or__(self, other):
        return CompoundModel(self, other, '|')

# Mock Linear1D
class Linear1D(MockModel):
    def __init__(self, slope):
        super().__init__(1, 1, separable=True)
        self.slope = slope
        
    def __and__(self, other):
        return CompoundModel(self, other, '&')
        
    def __or__(self, other):
        return CompoundModel(self, other, '|')

# Mock Pix2Sky_TAN
class Pix2Sky_TAN(MockModel):
    def __init__(self):
        super().__init__(2, 2, separable=False)
        
    def __and__(self, other):
        return CompoundModel(self, other, '&')
        
    def __or__(self, other):
        return CompoundModel(self, other, '|')

# Test the issue
if __name__ == "__main__":
    print("Testing separability matrix issue...")
    
    # Case 1: Simple compound model
    cm = Linear1D(10) & Linear1D(5)
    print(f"cm: Linear1D(10) & Linear1D(5)")
    print(f"n_inputs: {cm.n_inputs}, n_outputs: {cm.n_outputs}")
    
    # Case 2: More complex compound model
    complex_model = Pix2Sky_TAN() & Linear1D(10) & Linear1D(5)
    print(f"\ncomplex_model: Pix2Sky_TAN() & Linear1D(10) & Linear1D(5)")
    print(f"n_inputs: {complex_model.n_inputs}, n_outputs: {complex_model.n_outputs}")
    
    # Case 3: Nested compound model (the problematic case)
    nested_model = Pix2Sky_TAN() & cm
    print(f"\nnested_model: Pix2Sky_TAN() & cm")
    print(f"n_inputs: {nested_model.n_inputs}, n_outputs: {nested_model.n_outputs}")
    
    print("\nThe issue is in the nested case where 'cm' is already a CompoundModel")