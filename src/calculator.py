def divide(a, b):
"""Retourne la division de a par b. Lance une exception"""
""" si elle detecte une erreur."""
 if b == 0:
  raise ValueError("Division par zero est impossible")
return a /b